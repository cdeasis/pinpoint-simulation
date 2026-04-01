from __future__ import annotations

import random
import statistics
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Set

#==============================
# CONFIG / DATA MODELS
#==============================

@dataclass
class Category:
    """
    Represents a category type
    Later can be expanded to have things like:
    - old_time_heavy
    - active_players
    - WAR
    - awards
    - niche
    """
    name: str
    difficulty: float = 1.0 # >1 harder, <1 easier
    tags: Set[str] = field(default_factory=set)

@dataclass
class PlayerProfile:
    """
    Base player characteristics.
    Knowledge_by_bucket:
        Probability player knows an answer in each point bucket
        HIgher point values are more obscure / harder in this model
    style:
        'balanced', 'volatile', 'risky_then_safe', 'conservative'
    """
    name: str
    knowledge_by_bucket: Dict[str, float]
    style: str

    # category weakness, ex: {'war': 0.75}
    # means multiply knowledge by 0.75 in categories tagged 'war'
    category_modifiers: Dict[str, float] = field(default_factory=dict)

    # tendency to sometimes make a guess they do NOT actually know
    blind_risk_base: float = 0.0

    # social/content behavior
    content_bias: float = 0.0 # likes making entertaining choices
    pressure_sensitivity: float = 0.0 # reacts to jokes / score pressure

    # for players at snake ends who get two quick picks
    alternate_safe_risky_on_double: bool = False

@dataclass
class PlayerState:
    name: str
    score: int = 0
    strikes: int = 0
    alive: bool = True

    # answers this player genuinely knows for this game
    known_answers: Set[int] = field(default_factory=set)

    # track recent pick styles for snake-end rhythm
    double_pick_toggle: str = "risky" # alternates risky/safe when applicable

    # recent guess history
    correct_guesses: int = 0
    wrong_guesses: int = 0

@dataclass
class GuessResult:
    player: str
    guess: Optional[int]
    was_correct: bool
    points_awarded: int
    strike_given: bool
    style_used: str # 'safe', 'risky', 'blind_risk', etc.

@dataclass
class SimulationResult:
    scores: Dict[str, int]
    strikes: Dict[str, int]
    winner_names: List[str]
    history: List[GuessResult]
    elimination_order: List[str]
    solo_player_name: Optional[str]
    solo_started_behind: bool

#==============================
# HELPERS
#==============================

def point_bucket(points: int) -> str:
    """
    Bucket point values by difficulty / obscurity

    In this model:
    - higher points are harder / more obscure
    - lower points are safer / more famous
    """
    if 90 <= points <= 100:
        return"90_100"
    if 70 <= points <= 89:
        return "70_89"
    if 40 <= points <= 69:
        return "40_69"
    return "1_39"

def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))

def choose_from_top(values: List[int], n: int, rng: random.Random) -> Optional[int]:
    if not values:
        return None
    return rng.choice(values[: min(n, len(values))])

def choose_from_bottom(values: List[int], n: int, rng: random.Random) -> Optional[int]:
    if not values:
        return None
    return rng.choice(values[-min(n, len(values)) :])

#==============================
# KNOWLEDGE GENERATION
#==============================

def build_known_answers(
        profile: PlayerProfile,
        category: Category,
        rng: random.Random,
) -> Set[int]:
    """
    For a given simulated game / category, determine which answers this player actually knows.
    """
    known = set()

    for points in range(1, 101):
        bucket = point_bucket(points)
        p = profile.knowledge_by_bucket[bucket]

        # category difficulty: harder category reduces knowledge
        p /= category.difficulty

        # apply tag-based category modifiers
        for tag in category.tags:
            if tag in profile.category_modifiers:
                p *= profile.category_modifiers[tag]

        p = clamp(p, 0.0, 1.0)

        if rng.random() < p:
            known.add(points)

    return known
    
#==============================
# TURN ORDER
#==============================

def snake_round_order(player_names: List[str]) -> List[str]:
    """
    Returns one full snake cycle
    Example for [A, B, C]:
    [A, B, C, C, B, A]
    """
    return player_names + list(reversed(player_names))

def alternating_order(player_names: List[str]) -> List[str]:
    """
    Simpler alternating order for 2 players if desired:
    [A, B]
    """
    return player_names[:]

#==============================
# STRATEGY LOGIC
#==============================

def compute_social_pressure(
        player_state: PlayerState,
        all_states: Dict[str, PlayerState],
        recent_history: List[GuessResult],
        profile: PlayerProfile,
) -> float:
    """
    Very lightweight model of joking / content / pressure

    Positive pressure => more likely to do something risky/entertaining
    Negative pressure => more conservative
    """
    pressure = 0.0

    # If player is doing badly relative to others, may press
    scores = [s.score for s in all_states.values()]
    avg_score = sum(scores) / len(scores)
    score_gap = avg_score - player_state.score
    pressure += 0.0025 * score_gap

    # If a player already has 2 strikes, naturally become conservative
    if player_state.strikes == 2:
        pressure -= 0.45
    elif player_state.strikes == 1:
        pressure -= 0.10

    # Recent table vibe
    last_few = recent_history[-4:]
    if last_few:
        risky_count = sum(1 for h in last_few if h.style_used in {"risky", "blind_risk"})
        safe_count = sum(1 for h in last_few if h.style_used == "safe")

        # If everyone is being safe/boring, entertaining players may push risk
        if safe_count >= 3:
            pressure += 0.20 * profile.content_bias
        
        # If recent table is very aggressive, player may either match it or back off
        if risky_count >= 3:
            pressure += 0.10 * profile.content_bias
    
    # Amplify by player sensitivity
    pressure *= (1.0 + profile.pressure_sensitivity)

    return pressure

def decide_pick_mode(
        player_state: PlayerState,
        profile: PlayerProfile,
        all_states: Dict[str, PlayerState],
        recent_history: List[GuessResult],
        is_part_of_double_pick_window: bool,
) -> str:
    """
    Decide whether this turn is 'safe', 'risky', or 'blind_risk'

    This is intentionally heuristic and easy to tweak
    """

    pressure = compute_social_pressure(player_state, all_states, recent_history, profile)

    # End players alternating risky/safe on two quick picks
    if (
        profile.alternate_safe_risky_on_double
        and is_part_of_double_pick_window
        and player_state.strikes <= 1
    ):
        mode = player_state.double_pick_toggle
        player_state.double_pick_toggle = "safe" if mode == "risky" else "risky"
        return mode
    
    # Strong conservative behavior at 2 strikes
    if player_state.strikes >= 2:
        return "safe"
    
    # Base style
    if profile.style == "balanced":
        base_risk = 0.30
    elif profile.style == "volatile":
        base_risk = 0.50
    elif profile.style == "risky_then_safe":
        base_risk = 0.65 if player_state.strikes == 0 else 0.35
    else:
        base_risk = 0.35

    risk_score = base_risk + pressure

    # Small blind-risk chance
    blind_risk_chance = profile.blind_risk_base + max(0.0, pressure) * 0.25
    blind_risk_chance = clamp(blind_risk_chance, 0.0, 0.50)

    # blind risk only when not already in danger
    if player_state.strikes <= 1 and random.random() < blind_risk_chance:
        return "blind_risk"
    
    return "risky" if risk_score >= 0.5 else "safe"

def choose_guess_for_mode(
        mode: str,
        available_known: Set[int],
        available_unknown: Set[int],
        rng: random.Random,
) -> Optional[int]:
    """
    Choose a specific point value to guess.
    Higher points = more obscure / higher reward
    Lower points = safer / famous
    """
    known_sorted_desc = sorted(available_known, reverse=True)
    known_sorted_asc = sorted(available_known)

    if mode == "safe":
        # choose from safer, lower-value known answers
        return choose_from_bottom(known_sorted_desc, n=6, rng=rng) if known_sorted_desc else None
    if mode == "risky":
        # choose from higher-value known answers
        return choose_from_top(known_sorted_desc, n=6, rng=rng) if known_sorted_desc else None
    
    if mode == "blind_risk":
        # intentionally guess a high-value answer the player may not know
        unknown_sorted_desc = sorted(available_unknown, reverse=True)
        return choose_from_top(unknown_sorted_desc, n=12, rng=rng) if unknown_sorted_desc else None
    
    return None

#==============================
# GAME ENGINE
#==============================

class PinpointGameSimulator:
    def __init__(
        self,
        profiles: List[PlayerProfile],
        category: Category,
        seed: Optional[int] = None,
        stop_when_last_player_clinches: bool = False,
        two_player_alternate: bool = True,
    ):
        self.rng = random.Random(seed)
        self.category = category
        self.stop_when_last_player_clinches = stop_when_last_player_clinches
        self.two_player_alternate = two_player_alternate

        self.player_order = [p.name for p in profiles]
        self.profiles = {p.name: p for p in profiles}
        self.states = {
            p.name: PlayerState(
                name=p.name,
                known_answers=build_known_answers(p, category, self.rng),
            )
            for p in profiles
        }

        self.remaining_answers: Set[int] = set(range(1, 101))
        self.history: List[GuessResult] = []
        self.elimination_order: List[str] = []
        self.solo_player_name: Optional[str] = None
        self.solo_started_behind: bool = False
        self.solo_phase_recorded: bool = False

    def alive_players(self) -> List[str]:
        return [name for name in self.player_order if self.states[name].alive]
    
    def max_other_score(self, player_name: str) -> int:
        others = [s.score for n, s in self.states.items() if n != player_name]
        return max(others) if others else 0
    
    def is_last_player_clinched(self, player_name: str) -> bool:
        """
        Simple clinch rule:
        If already ahead of all others and we choose to stop there.
        """
        return self.states[player_name].score > self.max_other_score(player_name)
    
    def decide_last_player_mode(self, player_name: str) -> str:
        state = self.states[player_name]
        deficit = self.max_other_score(player_name) - state.score

        # Already ahead: victory lap
        if deficit <= 0:
            # mostly test fun / risky names once clinched
            return "risky" if self.rng.random() < 0.85 else "safe"
        
        # Small deficit: chip away safely most of the time
        if deficit <= 100:
            if state.strikes == 2:
                return "safe"
            return "safe" if self.rng.random() < 0.8 else "risky"
        
        # Medium deficit: roughly 50/50 split
        if deficit <= 200:
            return "safe" if self.rng.random() < 0.5 else "risky"
        
        # Large deficit: need points fast
        return "risky"
    
    def choose_last_player_guess(self, player_name: str, mode: str) -> Optional[int]:
        state = self.states[player_name]
        known = sorted(state.known_answers & self.remaining_answers)

        if not known:
            return None
        
        deficit = self.max_other_score(player_name) - state.score

        # Already ahead: victory lap
        if deficit <= 0:
            high_known = sorted(known, reverse=True)
            return self.rng.choice(high_known[:min(6, len(high_known))])
        
        winning = [x for x in known if x >= deficit]
        below = [x for x in known if x < deficit]

        if mode == "safe":
            # if a known answer wins immediately, take smallest such answer
            if winning:
                return min(winning)
            
            # otherwise chip away with the biggest safe answer that doesn't clear it yet
            if below:
                return max(below)
            
            return min(known)
        
        if mode == "risky":
            # if a known answer wins immediately, usually just take it
            if winning:
                if self.rng.random() < 0.8:
                    return min(winning)
                return max(winning)

            # if no known answer wins immediately, push the highest known points available
            return max(known)
        
        # Fallback
        if winning:
            return min(winning)
        return max(below) if below else max(known)

    def handle_guess(self, player_name: str, is_part_of_double_pick_window: bool, forced_mode: Optional[str] = None, forced_guess: Optional[int] = None) -> None:
        state = self.states[player_name]
        profile = self.profiles[player_name]

        if not state.alive:
            return
        
        available_known = state.known_answers & self.remaining_answers
        available_unknown = self.remaining_answers - state.known_answers

        if forced_mode is not None:
            mode = forced_mode
        else:
            mode = decide_pick_mode(
                player_state=state,
                profile=profile,
                all_states=self.states,
                recent_history=self.history,
                is_part_of_double_pick_window=is_part_of_double_pick_window,
            )

        if forced_guess is not None:
            guess = forced_guess
        else:
            guess = choose_guess_for_mode(
                mode=mode,
                available_known=available_known,
                available_unknown=available_unknown,
                rng=self.rng,
            )

        was_correct = False
        points_awarded = 0
        strike_given = False
        
        if guess is not None and guess in self.remaining_answers and guess in state.known_answers:
            was_correct = True
            points_awarded = guess
            state.score += guess
            state.correct_guesses += 1
            self.remaining_answers.remove(guess)
        else:
            strike_given = True
            state.strikes += 1
            state.wrong_guesses += 1

        if state.strikes >= 3 and state.alive:
            state.alive = False
            self.elimination_order.append(player_name)

        self.history.append(
            GuessResult(
                player=player_name,
                guess=guess,
                was_correct=was_correct,
                points_awarded=points_awarded,
                strike_given=strike_given,
                style_used=mode,
            )
        )

    def run(self) -> SimulationResult:
        while True:
            alive = self.alive_players()
            if len(alive) == 0:
                break

            if len(alive) == 1:
                last_player = alive[0]

                if not self.solo_phase_recorded:
                    self.solo_player_name = last_player
                    self.solo_started_behind = (
                        self.states[last_player].score < self.max_other_score(last_player)
                    )
                    self.solo_phase_recorded = True

                # for pure competitive sim, stop here once they clinch
                if self.stop_when_last_player_clinches and self.is_last_player_clinched(last_player):
                    break

                while self.states[last_player].alive:
                    if self.stop_when_last_player_clinches and self.is_last_player_clinched(last_player):
                        break
                    
                    forced_mode = self.decide_last_player_mode(last_player)
                    forced_guess = self.choose_last_player_guess(last_player, forced_mode)

                    self.handle_guess(
                        last_player,
                        is_part_of_double_pick_window=False,
                        forced_mode=forced_mode,
                        forced_guess=forced_guess,
                    )

                break

            # Multi-player phase
            if len(alive) == 2 and self.two_player_alternate:
                cycle = alternating_order(alive)
            else:
                cycle = snake_round_order(alive)

            # Detect which players are in "double-pick window"
            # In a 3-player snake [A, B, C, C, B, A], A and C have adjacent pairs across cycles
            # Approximate this by marking the ends of the current alive ordering
            ends = {alive[0], alive[-1]} if len(alive) >= 3 else set()

            for player_name in cycle:
                if not self.states[player_name].alive:
                    continue

                is_double_window = player_name in ends
                self.handle_guess(player_name, is_part_of_double_pick_window=is_double_window)

                # if player count changed due to elimination, rebuild next cycle
                new_alive = self.alive_players()
                if len(new_alive) != len(alive):
                    break
            
            # if no answers left, end game
            if not self.remaining_answers:
                break
        
        scores = {name: state.score for name, state in self.states.items()}
        strikes = {name: state.strikes for name, state in self.states.items()}
        max_score = max(scores.values()) if scores else 0
        winner_names = [name for name, score in scores.items() if score == max_score]

        return SimulationResult(
            scores=scores,
            strikes=strikes,
            winner_names=winner_names,
            history=self.history,
            elimination_order=self.elimination_order,
            solo_player_name=self.solo_player_name,
            solo_started_behind=self.solo_started_behind,
        )
    
#=============================
# BATCH SIMULATION
#=============================

def simulate_many(
    profiles: List[PlayerProfile],
    category: Category,
    n_sims: int = 10000,
    seed: Optional[int] = None,
    stop_when_last_player_clinches: bool = False,
    two_player_alternate: bool = True,
) -> Dict[str, object]:
    rng = random.Random(seed)

    win_counts = {p.name: 0.0 for p in profiles}
    score_history = {p.name: [] for p in profiles}
    strike_history = {p.name: [] for p in profiles}
    elimination_first_counts = {p.name: 0 for p in profiles}
    last_survivor_but_lost = 0
    solo_started_behind_count = 0
    solo_started_behind_and_lost = 0

    for _ in range(n_sims):
        sim_seed = rng.randint(1, 10**9)
        
        game = PinpointGameSimulator(
            profiles=profiles,
            category=category,
            seed=sim_seed,
            stop_when_last_player_clinches=stop_when_last_player_clinches,
            two_player_alternate=two_player_alternate
        )

        result = game.run()

        if result.solo_player_name is not None and result.solo_started_behind:
            solo_started_behind_count += 1
            if result.solo_player_name not in result.winner_names:
                solo_started_behind_and_lost += 1

        # split ties evenly
        for winner in result.winner_names:
            win_counts[winner] += 1.0 / len(result.winner_names)

        for name, score in result.scores.items():
            score_history[name].append(score)

        for name, strikes in result.strikes.items():
            strike_history[name].append(strikes)
        
        if result.elimination_order:
            elimination_first_counts[result.elimination_order[0]] += 1

        # check if last surivor lost
        if result.elimination_order and len(result.elimination_order) == len(profiles):
            # final eliminated is last survivor
            last_survivor= result.elimination_order[-1]
            if last_survivor not in result.winner_names:
                last_survivor_but_lost += 1
            
    summary = {
        "win_rate": {name: win_counts[name] / n_sims for name in win_counts},
        "avg_score": {name: statistics.mean(vals) for name, vals in score_history.items()},
        "median_score": {name: statistics.median(vals) for name, vals in score_history.items()},
        "stdev_score": {
            name: statistics.pstdev(vals) if len(vals) > 1 else 0.0
            for name, vals in score_history.items()
        },
        "avg_strikes": {name: statistics.mean(vals) for name, vals in strike_history.items()},
        "first_eliminated_rate": {
            name: elimination_first_counts[name] / n_sims for name in elimination_first_counts
        },
        "last_survivor_but_lost_rate": last_survivor_but_lost / n_sims,
        "score_history": score_history,
        "solo_started_behind_rate": solo_started_behind_count / n_sims,
        "solo_started_behind_and_lost_rate": (
            solo_started_behind_and_lost / solo_started_behind_count
            if solo_started_behind_count > 0 else 0.0
        ),
    }

    return summary
    
#==============================
# EXAMPLE SETUP
#==============================

def main() -> None:
    contestant_1 = PlayerProfile(
        name="Contestant 1",
        knowledge_by_bucket={
            "1_39": 0.88,
            "40_69": 0.78,
            "70_89": 0.62,
            "90_100": 0.42,
        },
        style="balanced",
        category_modifiers={},
        blind_risk_base=0.02,
        content_bias=0.20,
        pressure_sensitivity=0.20,
        alternate_safe_risky_on_double=True,
    )

    contestant_2 = PlayerProfile(
        name="Contestant 2",
        knowledge_by_bucket={
            "1_39": 0.87,
            "40_69": 0.77,
            "70_89": 0.61,
            "90_100": 0.40,
        },
        style="volatile",
        category_modifiers={
            "war": 0.78,   # worse on WAR-type categories
        },
        blind_risk_base=0.05,
        content_bias=0.30,
        pressure_sensitivity=0.35,
        alternate_safe_risky_on_double=False,
    )

    contestant_3 = PlayerProfile(
        name="Contestant 3",
        knowledge_by_bucket={
            "1_39": 0.78,
            "40_69": 0.61,
            "70_89": 0.43,
            "90_100": 0.29,
        },
        style="risky_then_safe",
        category_modifiers={},
        blind_risk_base=0.10,
        content_bias=0.45,
        pressure_sensitivity=0.25,
        alternate_safe_risky_on_double=True,
    )

    profiles = [contestant_1, contestant_2, contestant_3]

    category = Category(
        name="All-Time OPS+",
        difficulty=3.5,
        tags=set(),
    )

    summary = simulate_many(
        profiles=profiles,
        category=category,
        n_sims=10000,
        seed=42,
        stop_when_last_player_clinches=False,
        two_player_alternate=True,
    )

    print("=== Summary ===")
    for name in [p.name for p in profiles]:
        print(
            f"{name}: "
            f"win_rate={summary['win_rate'][name]:.3f}, "
            f"avg_score={summary['avg_score'][name]:.1f}, "
            f"median_score={summary['median_score'][name]:.1f}, "
            f"stdev={summary['stdev_score'][name]:.1f}, "
            f"avg_strikes={summary['avg_strikes'][name]:.2f}, "
            f"first_out_rate={summary['first_eliminated_rate'][name]:.3f}"
        )

    print(f"Last survivor but lost rate: {summary['last_survivor_but_lost_rate']:.3f}")
    print(f"Solo started behind rate: {summary['solo_started_behind_rate']:.3f}")
    print(f"Solo started behind and lost rate: {summary['solo_started_behind_and_lost_rate']:.3f}")

if __name__ == "__main__":
    main()