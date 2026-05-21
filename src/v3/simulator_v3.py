from __future__ import annotations

import random
import statistics
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set

#==============================
# CONFIG / DATA MODELS
#==============================
# These dataclasses define the core objects used by the simulator
# They do not perform logic by themselves; they simply hold structural data

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

    difficulty:
        A global category difficulty multiplier
        Higher difficulty means fewer answers are known on average

    tags:
        Optional labels that can interact with contestant weaknesses 
    """
    name: str
    difficulty: float = 1.0 # >1 harder, <1 easier
    tags: Set[str] = field(default_factory=set)
    precision_difficulty: float = 1.0 # how much precision matters for category

@dataclass
class PlayerProfile:
    """
    Permanent player base profile / identity / tendencies

    knowledge_by_bucket:
        Probability a player knows answers in each point-value bucket
        In this version of the model, higher model values are treated as more obscure / harder to know

    style:
        High-level playstyle used by the generic mode-selection logic

    category_modifiers:
        Optional per-tag knowledge penalites or bonsuses
        Example: { 'war': 0.78 } means this player knows WAR categories worse

    blind_risk_base:
        Baseline chance to intentionally guess something they do NOT know

    content_bias:
        How much the player is influenced by the "make the show entertaining" dynamic

    pressure_sensitivity:
        How strongly the player reacts to score pressure and table flow

    alternate_safe_risky_on_double:
        Used for end-of-snake contestants who often alternate risky/safe on their back-to-back style turns
    """
    name: str
    knowledge_by_bucket: Dict[str, float]
    style: str
    category_modifiers: Dict[str, float] = field(default_factory=dict)
    blind_risk_base: float = 0.0
    content_bias: float = 0.0
    pressure_sensitivity: float = 0.0
    alternate_safe_risky_on_double: bool = False

@dataclass
class AnswerState:
    """
    add comment here later, something about how this introduces a more dynamic, non binary knowledge system compared to V1
    """
    knowledge: float
    recall: float
    confidence: float

@dataclass
class PlayerState:
    """
    Temporary per-game state for a player

    This changes throughout a simulation
    """
    name: str
    score: int = 0
    strikes: int = 0
    alive: bool = True

    # new knowledge system
    answer_states: Dict[int, AnswerState] = field(default_factory=dict)

    # Used for end-of-snake alternating risky/safe behavior
    double_pick_toggle: str = "risky" # alternates risky/safe when applicable

    # Simple tracking counters
    correct_guesses: int = 0
    wrong_guesses: int = 0

    # new v3 inference variables

    # m1 + m2
    depth_read: float = 0.0 # how deep/generous the board feels
    precision_read: float = 0.0 # how tight/compressed the board feels
    cutoff_estimate: float = 50.0 # rough midpoint startiing assumption
    cutoff_uncertainty: float = 1.0 #very uncertain, shrinks overtime

    # m3
    local_density_read: float = 0.0 # how many viable answers seem to exist near the cutoff (open vs sparse board)
    surprise_read: float = 0.0 # how often outcomes contradict expectations (generous vs harsh surprises)
    near_cutoff_hits: float = 0.0 # recent count of correct answers near estimated cutoff
    near_cutoff_misses: float = 0.0 # recent count of misses near estimated cutoff

    # can keep this for now, unused but will come in later
    table_trust: float = 0.0 # positive: table reactions are somewhat useful, negative: table reactions have been misleading

@dataclass
class GuessResult:
    """
    One logged guess event.

    This lets you inspect game history later if desired
    """
    player: str
    guess: Optional[int]
    was_correct: bool
    points_awarded: int
    strike_given: bool
    style_used: str # 'safe', 'risky', 'blind_risk', etc.

@dataclass
class SimulationResult:
    """
    End-of-game output returned by one simulation

    Includes the normal summary plus solo/endgame tracking fields.
    """
    scores: Dict[str, int]
    strikes: Dict[str, int]
    winner_names: List[str]
    history: List[GuessResult]
    elimination_order: List[str]
    solo_player_name: Optional[str]
    solo_started_behind: bool
    solo_start_deficit: Optional[int] = None
    solo_turns_taken: int = 0
    solo_had_winning_answer_at_start: bool = False
    avg_final_board_read: float = 0.0
    avg_abs_final_board_read: float = 0.0
    strong_harsh_board_rate: float = 0.0
    strong_generous_board_rate: float = 0.0
    avg_final_cutoff_estimate: float = 0.0 # avg end of game belief about where the board line is
    avg_final_cutoff_uncertainty: float = 0.0 # avg end of game uncertainty
    low_uncertainty_rate: float = 0.0 # how often players finiish pretty confident (ex: uncertainty <= 0.25)
    high_cutoff_rate: float = 0.0 # how often players finish thinking the board line is high (ex: estimate >= 70)
    avg_final_safe_floor: float = 0.0 # average of players' final "safe floor" (cutoff estimate - uncertainty margin)
    avg_final_local_density_read: float = 0.0 # average of players' final local density read
    avg_final_surprise_read: float = 0.0 # average of players' final surprise read
    avg_final_near_cutoff_hits: float = 0.0 # average of players' final near-cutoff hit count
    avg_final_near_cutoff_misses: float = 0.0 # average of players' final near-cutoff miss count
    mode_counts: Dict[str, int] = field(default_factory=dict)
    double_window_mode_counts: Dict[str, int] = field(default_factory=dict)
    context_counts: Dict[str, int] = field(default_factory=dict)
    context_action_counts: Dict[str, int] = field(default_factory=dict)

#==============================
# HELPERS
#==============================

def point_bucket(points: int) -> str:
    """
    Map a point value to a difficulty bucket.

    In this model:
    - 90_100: hardest / most obscure
    - 70_89: medium-hard
    - 40_69: medium
    - 1_39: easiest / safest
    """
    if 90 <= points <= 100:
        return"90_100"
    if 70 <= points <= 89:
        return "70_89"
    if 40 <= points <= 69:
        return "40_69"
    return "1_39"

def clamp(x: float, lo: float, hi: float) -> float:
    """
    Clamp a numeric value into a bounded range.
    """
    return max(lo, min(hi, x))

def get_board_signal(state: PlayerState) -> float:
    """
    Temporary bridge for V3 M1

    Combines multiple board inference components into a single signal so existing V2 logic can continue working
    """
    return (0.6 * state.depth_read - 0.4 * state.precision_read)

# m4 helper
def get_board_context(state: PlayerState) -> Dict[str, bool]:
    """
    Lightweight M4 board context helper

    Converts numeric inference signals into strategic labels.
    Used by mode selection and safe-floor logic
    """
    board_signal = get_board_signal(state)

    dense = state.local_density_read >= 0.10
    generous = state.surprise_read >= 0.18
    
    return {
        "dense": dense,
        "generous": generous,
        "open": dense or generous,
        "tight": state.precision_read >= 0.12 or board_signal  <= -0.12,
        "uncertain": state.cutoff_uncertainty >= 0.50,
        "confident": state.cutoff_uncertainty <= 0.30,
        "high_cutoff": state.cutoff_estimate >= 70.0,
        "low_cutoff": state.cutoff_estimate <= 45.0,
    }


def choose_from_top(values: List[int], n: int, rng: random.Random) -> Optional[int]:
    """
    Randomly choose from the top N values of an already-sorted list.

    Used to model "aim high" behavior.
    """
    if not values:
        return None
    return rng.choice(values[: min(n, len(values))])

def choose_from_bottom(values: List[int], n: int, rng: random.Random) -> Optional[int]:
    """
    Randomly choose from the bottom N values of an already-sorted list

    Use to model "play safer / lower-value" behavior.
    """
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
    Build the set of answers a player knows for this simulated game.

    This is one of the biggest "environment" levers in the model.
    Higher category difficulty lowers the proability that answers are known.
    """
    known = set()

    for points in range(1, 101):
        bucket = point_bucket(points)
        p = profile.knowledge_by_bucket[bucket]

        # Harder category: fewer known answers
        p /= category.difficulty

        # Apply category-tag-specific modifiers if relevant
        for tag in category.tags:
            if tag in profile.category_modifiers:
                p *= profile.category_modifiers[tag]

        # Keep probability valid
        p = clamp(p, 0.0, 1.0)

        # Sample whether this answer is known
        if rng.random() < p:
            known.add(points)

    return known

def build_answer_states(
        profile: PlayerProfile,
        category: Category,
        rng: random.Random,
) -> Dict[int, AnswerState]:
    """
    Build per-answer mental state for a player for this game

    Intead of binary known/unknown, each player gets:
    - knowledge: how well the player knows it in general
    - recall: likelihood of recalling it in the moment
    - confidence: willingness to actually guess it
    """
    answer_states = {}

    for points in range(1, 101):
        # Step 1: Base knowledge (same as V1, but continuous)
        bucket = point_bucket(points)
        knowledge = profile.knowledge_by_bucket[bucket]

        # Apply category difficulty (harder -> less knowledge)
        knowledge /= category.difficulty

        # Apply category-specific modifiers
        for tag in category.tags:
            if tag in profile.category_modifiers:
                knowledge *= profile.category_modifiers[tag]

        # Clamp to valid probablity range
        knowledge = clamp(knowledge, 0.0, 1.0)

        # Step 2: Recall (noisy function of knowledge)
        # Idea: even if you know something, you might not recall it
        recall = knowledge * rng.uniform(0.75, 1.05)

        # Add a little randomness so low-knowledge answers sometimes surface
        recall += rng.uniform(-0.05, 0.05)

        recall = clamp(recall, 0.0, 1.0)

        # Step 3: Confidence (willingness to guess)
        # Blend knowledge + recall, then add slight noise
        confidence = (0.6 * knowledge + 0.4 * recall)

        confidence += rng.uniform(-0.05, 0.05)

        confidence = clamp(confidence, 0.0, 1.0)

        # Store
        answer_states[points] = AnswerState(
            knowledge=knowledge,
            recall=recall,
            confidence=confidence,
        )

    return answer_states

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
    Compute a lightweight pressure score.

    The idea is to capture a few social / momentum dynamics:
    - trailing players may press
    - players with 2 strikes become conservative
    - a very safe table can push content-seeking players toward risk
    - a very aggressive table can also shift behavior slightly
    """
    pressure = 0.0

    # Falling behind can push a player toward more aggressive choices.
    scores = [s.score for s in all_states.values()]
    avg_score = sum(scores) / len(scores)
    score_gap = avg_score - player_state.score
    pressure += 0.0020 * score_gap

    # Strikes push players toward safer play.
    if player_state.strikes == 2:
        pressure -= 0.45
    elif player_state.strikes == 1:
        pressure -= 0.10

    # Look at the recent table mood.
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
    
    # More sensitive players react more strongly to the same situation
    pressure *= (1.0 + profile.pressure_sensitivity)

    return pressure

def decide_pick_mode(
        player_state: PlayerState,
        profile: PlayerProfile,
        all_states: Dict[str, PlayerState],
        recent_history: List[GuessResult],
        is_part_of_double_pick_window: bool,
        rng: random.Random,
) -> str:
    """
    Choose a generic pick mode for a normal turn.

    Return one of:
    - safe
    - risky
    - blind_risk

    This is the default decision function outside of the solo endgame.
    """
    pressure = compute_social_pressure(player_state, all_states, recent_history, profile)
    pressure += get_board_signal(player_state) * 0.15

    # m4 stuff, fix comment later
    ctx = get_board_context(player_state)

    if ctx["dense"] and player_state.strikes == 0:
        pressure += 0.06
    elif ctx["generous"] and player_state.strikes == 0:
        pressure += 0.02
    
    if ctx["tight"]:
        pressure -= 0.08
    
    if ctx["uncertain"]:
        pressure -= 0.04
    
    if player_state.strikes == 1 and ctx["tight"]:
        pressure -= 0.08

    # score aware lead/trail adjustment
    other_scores = [s.score for n, s in all_states.items() if n != player_state.name]
    leader_gap = player_state.score - max(other_scores) if other_scores else 0

    # if already aheady by a lot, lean safer
    if leader_gap >= 100:
        pressure -= 0.18
    elif leader_gap >= 50:
        pressure -= 0.10
    
    # if far behind, allow a bit more aggression
    if leader_gap <= -100:
        pressure += 0.08
    elif leader_gap <= -50:
        pressure += 0.04

    # Snake-end players can alternate risky/safe on their double-pick rhythm
    if (
        profile.alternate_safe_risky_on_double
        and is_part_of_double_pick_window
        and player_state.strikes <= 1
    ):
        ctx = get_board_context(player_state)
        
        other_scores = [s.score for n, s in all_states.items() if n != player_state.name]
        leader_gap = player_state.score - max(other_scores) if other_scores else 0

        # protect meaningful lead
        if leader_gap >= 75:
            return "safe"
        
        # if player already has a strike and the board is tight/uncertain, avoid forcing risk
        if player_state.strikes >= 1 and (ctx["tight"] or ctx["uncertain"]):
            return "safe"

        # if behind and board does not feel tight, allow aggression
        if player_state.strikes == 0 and leader_gap <= -75 and not ctx["tight"]:
            return "risky"
        
        # if board feels open and player is clean, allow the old risky/safe rhythm
        if player_state.strikes == 0 and (ctx["dense"] or (ctx["generous"] and not ctx["tight"])):
            mode = player_state.double_pick_toggle
            player_state.double_pick_toggle = "safe" if mode == "risky" else "risky"
            return mode
        
        return "safe"
    
    # At 2 strikes, generic play becomes conservative
    if player_state.strikes >= 2:
        return "safe"
    
    # Baseline style tendencies
    if profile.style == "balanced":
        base_risk = 0.30
    elif profile.style == "volatile":
        base_risk = 0.58
    elif profile.style == "risky_then_safe":
        base_risk = 0.60 if player_state.strikes == 0 else 0.25
    else:
        base_risk = 0.35

    risk_score = base_risk + pressure

    # Blind risk chance = willingness to just throw out a speculative guess
    blind_risk_chance = profile.blind_risk_base + max(0.0, pressure) * 0.05
    blind_risk_chance = clamp(blind_risk_chance, 0.0, 0.50)

    # Blind risk only when not already in danger
    if player_state.strikes <= 1 and rng.random() < blind_risk_chance:
        return "blind_risk"
    
    return "risky" if risk_score >= 0.5 else "safe"

def choose_guess_for_mode(
        mode: str,
        player_state: PlayerState,
        remaining_answers: Set[int],
        rng: random.Random,
) -> Optional[int]:
    """
    detailed comment here later
    """
    candidates = {
        answer: ans_state 
        for answer, ans_state in player_state.answer_states.items()
        if answer in remaining_answers
    }

    if not candidates:
        return None
    
    # selection
    
    # Safe: high recall + high confidence
    if mode == "safe":
        margin = 10 + 6 * player_state.cutoff_uncertainty # can consider doing a 10 + 6 as well, try 8 + 8 first, keep 10 + 10 for now, need to fix correct-answer update first
        safe_floor = player_state.cutoff_estimate - margin
        
        safe_pool = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.14 and ans.confidence >= 0.14 and answer >= safe_floor
        ]

        if not safe_pool:
            safe_pool = [
                answer for answer, ans in candidates.items()
                if ans.recall >= 0.14 and ans.confidence >= 0.14
            ]
        
        safe_pool.sort(reverse=True)
        k = rng.randint(3, 6)
        return choose_from_bottom(safe_pool, n=k, rng=rng) if safe_pool else None
    
    # Risky: still recalled, but can include lower-confidence answers / higher-value answers
    if mode == "risky":
        risky_pool = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.07 and ans.confidence >= 0.07
        ]
        risky_pool.sort(reverse=True)

        if not risky_pool:
            return None
        
        # mid-high slice instead of always the absolute top
        top_slice = risky_pool[:min(12, len(risky_pool))]
        if len(top_slice) > 4:
            return rng.choice(top_slice[2:8])
        return rng.choice(top_slice)
    
    # Blind risk: very low-confidence pool / basically speculative
    if mode == "blind_risk":
        blind_pool = [
            answer for answer, ans in candidates.items()
            if ans.confidence < 0.08
        ]
        blind_pool.sort(reverse=True)
        return choose_from_top(blind_pool, n=12, rng=rng) if blind_pool else None

    return None

#==============================
# GAME ENGINE
#==============================

class PinpointGameSimulator:
    """
    Simulates one full game of Pinpoint

    This class holds all game state for a single run
    """
    def __init__(
        self,
        profiles: List[PlayerProfile],
        category: Category,
        seed: Optional[int] = None,
        stop_when_last_player_clinches: bool = False,
        two_player_alternate: bool = True,
    ):
        # Local RNG for reproducibility
        self.rng = random.Random(seed)
        self.category = category
        self.stop_when_last_player_clinches = stop_when_last_player_clinches
        self.two_player_alternate = two_player_alternate

        # Preserve original seating / order
        self.player_order = [p.name for p in profiles]
        self.profiles = {p.name: p for p in profiles}

        # Build each player's per-game state, including known answers 
        self.states = {
            p.name: PlayerState(
                name=p.name,
                answer_states=build_answer_states(p, category, self.rng),
            )
            for p in profiles
        }

        # Remaining answers available on the board
        self.remaining_answers: Set[int] = set(range(1, 101))

        # Game log and elimination tracking
        self.history: List[GuessResult] = []
        self.elimination_order: List[str] = []

        # Solo/endgame tracking
        self.solo_player_name: Optional[str] = None
        self.solo_started_behind: bool = False
        self.solo_phase_recorded: bool = False

        # Milestone 3 solo metrics
        self.solo_start_deficit: Optional[int] = None
        self.solo_turns_taken: int = 0
        self.solo_had_winning_answer_at_start: bool = False

        # V3M4 metrics
        self.mode_counts = {
            "safe": 0,
            "risky": 0,
            "blind_risk": 0,
            "chip_away": 0,
            "exact_win": 0,
            "comeback": 0,
            "high_upside": 0,
            "desperation": 0,
            "victory_lap": 0,
        }

        self.double_window_mode_counts = {
            "safe": 0,
            "risky": 0,
            "blind_risk": 0,
        }

        self.context_counts = {
            "open": 0,
            "dense": 0,
            "generous": 0,
            "dense_and_generous": 0,
            "tight": 0,
            "uncertain": 0,
            "double_window": 0,
            "total_decisions": 0,
        }

        self.context_action_counts = {
            "risky_on_open": 0,
            "risky_on_dense": 0,
            "risky_on_generous": 0,
            "risky_on_dense_and_generous": 0,
            "safe_on_tight": 0,
            "risky_on_uncertain": 0,
            "safe_on_uncertain": 0,
            "risky_on_double_window": 0,
            "safe_on_double_window": 0,
        }
        
    def alive_players(self) -> List[str]:
        """REturn players still alive in seating order"""
        return [name for name in self.player_order if self.states[name].alive]

    def max_other_score(self, player_name: str) -> int:
        """Return the highest score among everyone except the named player"""
        others = [s.score for n, s in self.states.items() if n != player_name]
        return max(others) if others else 0
    
    def is_last_player_clinched(self, player_name: str) -> bool:
        """
        Check whether the solo player is already ahead of everyone else.

        This is used if you want a pure competitive stop condition.
        """
        return self.states[player_name].score > self.max_other_score(player_name)
    
    def decide_last_player_mode(self, player_name: str) -> str:
        """
        Decide how the solo player behaves once they are the only one left.

        V2 version (Milestone 3):
        - Uses deficit size
        - Uses current strikes
        - Uses wehther direct winning answers are available
        - Uses how many plausible answers remain
        """
        state = self.states[player_name]
        deficit = self.max_other_score(player_name) - state.score
        remaining_count = len(self.remaining_answers)

        # Build a quick view of currently plausible remaining answers
        candidates = {
            answer: ans
            for answer, ans in state.answer_states.items()
            if answer in self.remaining_answers
        }

        plausible_answers = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.08 and ans.confidence >= 0.08
        ]

        safe_answers = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.12 and ans.confidence >= 0.12
        ]

        winning_answers = [a for a in plausible_answers if a >= deficit]

        plausible_count = len(plausible_answers)
        safe_count = len(safe_answers)
        winning_count = len(winning_answers)

        # 1. Already ahead -> victory lap
        if deficit <= 0:
            return "victory_lap"
        
        # 2. If there are no plausible answers at all, this is desperation territory
        if plausible_count == 0:
            return "desperation"
        
        # board size awareness
        if remaining_count <= 5:
            if winning_count > 0:
                return "exact_win"
            if safe_count > 0 and deficit <= 100:
                return "chip_away"
            if plausible_count > 0 and deficit <= 150:
                return "comeback"
            return "desperation"
        
        # 3. With 2 strikes, survival matters a lot more
        if state.strikes == 2:
            # If a winning answer exists, try to end it now
            if winning_count > 0:
                return "exact_win"
            
            # Small deficit and some safe answers -> chip away
            if deficit <= 100 and safe_count > 0 and remaining_count > 1:
                return "chip_away"

            # Otherwise, forced into desperation / high upside
            return "desperation"
        
        # 4. At 0 or 1 strike, use deficit size + board size
        if deficit <= 75:
            if winning_count:
                return "exact_win"
            return "chip_away"
        
        if deficit <= 175:
            if winning_count > 0:
                return "exact_win"
            return "comeback"
        
        # Large deficit
        if winning_count > 0:
            return "high_upside"
        
        return "desperation"
    
    def choose_last_player_guess(self, player_name: str, mode: str) -> Optional[int]:
        """
        Choose a solo guess using richer candidate groups:
        - safe: high recall/confidence, lower volatility
        - winning: directly clears the deficit
        - comeback: strong answers that materially reduce the deficit
        - desperation: lower-confidence high-value guesses
        - victory lap: when already ahead
        """
        state = self.states[player_name]
        deficit = self.max_other_score(player_name) - state.score
        lead = state.score - self.max_other_score(player_name)

        candidates = {
            answer: ans
            for answer, ans in state.answer_states.items()
            if answer in self.remaining_answers and ans.recall >= 0.08
        }

        if not candidates:
            return None
        
        # Candidate groups
        safe_candidates = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.12 and ans.confidence >= 0.12
        ]

        plausible_candidates = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.08 and ans.confidence >= 0.08
        ]

        desperation_candidates = [
            answer for answer, ans in candidates.items()
            if ans.recall >= 0.04 and ans.confidence >= 0.04
        ]

        winning_candidates = [a for a in plausible_candidates if a >= deficit]

        # Answers that don't win immediately but make a meaningful dent
        comeback_candidates = [
            a for a in plausible_candidates
            if a < deficit and a >= max(1, int(0.5 * deficit))
        ]

        # Sort descending so higher point values come first
        safe_candidates.sort(reverse=True)
        plausible_candidates.sort(reverse=True)
        desperation_candidates.sort(reverse=True)
        winning_candidates.sort(reverse=True)
        comeback_candidates.sort(reverse=True)

        # Mode behaviors
        if mode == "victory_lap":
            # already ahead: choose from plausible high end answers for fun / upside, has lead-size awarness
            # prefer safer options first to preserve lead
            if lead < 75 and safe_candidates:
                return max(safe_candidates) # just keep living
            
            if lead > 150 and plausible_candidates:
                return self.rng.choice(plausible_candidates[:min(4, len(plausible_candidates))])
            
            if safe_candidates:
                return self.rng.choice(safe_candidates[:min(6, len(safe_candidates))])
            
            return None
        
        if mode == "chip_away":
            # on 2 strikes, be much stricter
            if state.strikes == 2:
                below_safe = [a for a in safe_candidates if a < deficit]
                if below_safe:
                    return max(below_safe)
                
                if winning_candidates:
                    return min(winning_candidates)
                
                return None
            
            # at 0 or 1 strike, normal chip-away behavior
            below_safe = [a for a in safe_candidates if a < deficit]
            if below_safe:
                return max(below_safe)
            
            if winning_candidates:
                return min(winning_candidates)
            
            below_plausible = [a for a in plausible_candidates if a < deficit]
            if below_plausible:
                return max(below_plausible)
            
            return None
        
        if mode == "exact_win":
            # prefer the smallest winner that clears the deficit
            if winning_candidates:
                return min(winning_candidates)
            
            # fallback: best comeback answer
            if comeback_candidates:
                return max(comeback_candidates)
            
            return None
        
        if mode == "comeback":
            # prefer answers that make a large dent but are still plausible
            if comeback_candidates:
                return self.rng.choice(comeback_candidates[:min(5, len(comeback_candidates))])
            
            if winning_candidates:
                return min(winning_candidates)
            
            return None
        
        if mode == "high_upside":
            # prefer the biggest plausible answer available
            if plausible_candidates:
                return max(plausible_candidates)
            
            return None

        if mode == "desperation":
            # accept lower-confidence options when boxed in
            if desperation_candidates:
                return self.rng.choice(desperation_candidates[:min(8, len(desperation_candidates))])
            
            return None
        
        return None
    
    
    def update_board_inference(self, guess_result: GuessResult) -> None:
        """
        Light V3 M1/M2 board inference update

        depth_read:
        - positive: board feels deeper / more generous
        - negative: board feels shallower / harsher

        precision_read:
        - positive: board feels tighter / less forgiving near the cutoff
        - negative: board feels looser / more forgiving

        cutoff_estimate:
        - approximate value the player believes is needed to safely make the board

        cutoff_uncertainty:
        - how unsure the player is about that estimate
        - starts high and decreases as more information is revealed

        This update remains heuristic-based:
        - revealed correct answers pull the cutoff estimate toward observed board values
        - strikes nudge the estimated cutoff upward
        - repeated safe hits / misses continue to share broad board perception
        """
        for state in self.states.values():
            if not state.alive:
                continue

            revealed_value = guess_result.points_awarded if guess_result.was_correct else guess_result.guess

            if revealed_value is None:
                continue

            NEAR_BAND = 12
            MID_BAND = 25 # reserved for broader near-cutoff / board-shape logic later

            # correct low-value answer suggests the board is deeper / harsher than player might have expected
            if guess_result.was_correct and guess_result.points_awarded <= 25:
                state.depth_read -= 0.04

            elif guess_result.was_correct and guess_result.points_awarded >= 70:
                state.depth_read += 0.02
            
            # strike suggests the board may be harsher than expected
            elif guess_result.strike_given and guess_result.guess is not None:
                state.depth_read -= 0.04
                state.precision_read += 0.02 # misses suggest tighter board
            
            # recent table mood can also lightly influence the read
            last_few = self.history[-4:]
            if last_few:
                safe_hits = sum(1 for h in last_few if h.was_correct and h.style_used in {"safe", "chip_away"})
                misses = sum(1 for h in last_few if h.strike_given)

                if safe_hits >= 3:
                    state.depth_read += 0.01
                if misses >= 3:
                    state.depth_read -= 0.03
                    state.precision_read += 0.01

            # cutoff estimation updates (selective updates)
            if guess_result.was_correct and guess_result.guess is not None:
                revealed_value = guess_result.points_awarded
                delta = revealed_value - state.cutoff_estimate

                # only treat answers near the current estimate as informative
                # new split, describe this later
                if revealed_value >= state.cutoff_estimate - 10:
                    # strong boundary-like clue
                    weight = 0.18 if delta >= 0 else 0.16
                    uncertainty_mult = 0.975
                
                elif revealed_value >= state.cutoff_estimate - 30:
                    # weaker informative clue
                    weight = 0.10 if delta >= 0 else 0.06
                    uncertainty_mult = 0.990

                else:
                    weight = 0.0
                    uncertainty_mult = 1.0
                
                if weight > 0:
                    state.cutoff_estimate = ((1 - weight) * state.cutoff_estimate + weight * revealed_value)
                    state.cutoff_uncertainty *= uncertainty_mult
         
            elif guess_result.strike_given and guess_result.guess is not None:
                # a miss suggests the true cutoff may be above this region
                if guess_result.guess >= state.cutoff_estimate - 10:
                    state.cutoff_estimate += 4.0
                    state.cutoff_uncertainty *= 0.990
                else:
                    # misses are informative too, but slightly less precise
                    state.cutoff_estimate += 1.0
                    state.cutoff_uncertainty *= 0.997

            # M3: board shape inference

            distance = revealed_value - state.cutoff_estimate
            abs_distance = abs(distance)

            # near-cutoff tracking
            if abs_distance <= NEAR_BAND:
                if guess_result.was_correct:
                    state.near_cutoff_hits += 1.0
                elif guess_result.strike_given:
                    state.near_cutoff_misses += 1.0
            elif abs_distance <= NEAR_BAND + 8:
                if guess_result.was_correct:
                    state.near_cutoff_hits += 0.5
                elif guess_result.strike_given:
                    state.near_cutoff_misses += 0.5

            # local density signal
            recent_total = state.near_cutoff_hits + state.near_cutoff_misses

            if recent_total >= 3:
                observed_hit_rate = state.near_cutoff_hits / recent_total
                expected_hit_rate = 0.75
                density_signal = observed_hit_rate - expected_hit_rate
                state.local_density_read += 0.05 * density_signal

            # surprise signal
            # case a: low value hit -> generous surprise
            if guess_result.was_correct and revealed_value < state.cutoff_estimate - 30:
                state.surprise_read += 0.025
            
            # case b: high miss -> harsh surprise
            elif guess_result.strike_given and revealed_value >= state.cutoff_estimate - 10:
                state.surprise_read -= 0.05

            # use surprise to adjust precision
            state.precision_read += -0.02 * state.surprise_read

            # decay
            state.local_density_read *= 0.94
            state.surprise_read *= 0.94

            state.near_cutoff_hits *= 0.9
            state.near_cutoff_misses *= 0.9

            # clamps
            state.depth_read = clamp(state.depth_read, -0.30, 0.30)
            state.precision_read = clamp(state.precision_read, -0.30, 0.30)
            state.cutoff_estimate = clamp(state.cutoff_estimate, 20.0, 80.0)
            state.cutoff_uncertainty = clamp(state.cutoff_uncertainty, 0.10, 1.0)
            state.local_density_read = clamp(state.local_density_read, -0.5, 0.5)
            state.surprise_read = clamp(state.surprise_read, -0.5, 0.5)

    def handle_guess(
            self,
            player_name: str,
            is_part_of_double_pick_window: bool,
            forced_mode: Optional[str] = None,
            forced_guess: Optional[int] = None,
    ) -> None:
        """
        also might be bridge for now, but if not detailed comment here later
        """
        state = self.states[player_name]
        profile = self.profiles[player_name]

        if not state.alive:
            return
        
        # Choose mode
        if forced_mode is not None:
            mode = forced_mode
        else: # might have to fix how it's called
            mode = decide_pick_mode(
                player_state=state,
                profile=profile,
                all_states=self.states,
                recent_history=self.history,
                is_part_of_double_pick_window=is_part_of_double_pick_window,
                rng=self.rng,
            )

        self.mode_counts[mode] = self.mode_counts.get(mode, 0) + 1

        if is_part_of_double_pick_window:
            self.double_window_mode_counts[mode] = self.double_window_mode_counts.get(mode, 0) + 1

        ctx = get_board_context(state)

        self.context_counts["total_decisions"] += 1

        if ctx["open"]:
            self.context_counts["open"] += 1
            if mode in {"risky", "blind_risk"}:
                self.context_action_counts["risky_on_open"] += 1

        if ctx["dense"]:
            self.context_counts["dense"] += 1
            if mode in {"risky", "blind_risk"}:
                self.context_action_counts["risky_on_dense"] += 1
        
        if ctx["generous"]:
            self.context_counts["generous"] += 1
            if mode in {"risky", "blind_risk"}:
                self.context_action_counts["risky_on_generous"] += 1
        
        if ctx["dense"] and ctx["generous"]:
            self.context_counts["dense_and_generous"] += 1
            if mode in {"risky", "blind_risk"}:
                self.context_action_counts["risky_on_dense_and_generous"] += 1
        
        if ctx["tight"]:
            self.context_counts["tight"] += 1
            if mode == "safe":
                self.context_action_counts["safe_on_tight"] += 1
        
        if ctx["uncertain"]:
            self.context_counts["uncertain"] += 1
            if mode == "risky":
                self.context_action_counts["risky_on_uncertain"] += 1
            if mode == "safe":
                self.context_action_counts["safe_on_uncertain"] += 1
        
        if is_part_of_double_pick_window:
            self.context_counts["double_window"] += 1
            if mode == "risky":
                self.context_action_counts["risky_on_double_window"] += 1
            if mode == "safe":
                self.context_action_counts["safe_on_double_window"] += 1
        
        # choose guess
        if forced_guess is not None:
            guess = forced_guess
        else: # might have to fix how it's called
            guess = choose_guess_for_mode(
                mode=mode,
                player_state=state,
                remaining_answers=self.remaining_answers,
                rng=self.rng,
            )
        
        was_correct = False
        points_awarded = 0
        strike_given = False

        # map solo modes onto existing resolution families
        resolution_mode = mode
        
        if mode == "chip_away":
            resolution_mode = "safe"
        elif mode in {"exact_win", "comeback", "high_upside", "victory_lap"}:
            resolution_mode = "risky"
        elif mode == "desperation":
            resolution_mode = "desperation"
        # resolve guesses

        if guess is not None and guess in self.remaining_answers:
            ans = state.answer_states[guess]

            if resolution_mode == "safe":
                was_correct = ans.recall >= 0.14 and ans.confidence >= 0.14
            elif resolution_mode == "risky":
                was_correct = ans.recall >= 0.08 and ans.confidence >= 0.08
            elif resolution_mode == "desperation":
                was_correct = ans.recall >= 0.03 and self.rng.random() < max(0.15, ans.confidence + 0.08)
            elif resolution_mode == "blind_risk":
                was_correct = self.rng.random() < max(0.03, ans.confidence)
            else:
                was_correct = False

        # apply result
        if was_correct:
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

        result = GuessResult(
            player=player_name,
            guess=guess,
            was_correct=was_correct,
            points_awarded=points_awarded,
            strike_given=strike_given,
            style_used=mode,
        )

        self.history.append(result)

        # M4: update each player's read of the board after the reveal
        self.update_board_inference(result)

    def run(self) -> SimulationResult:
        """
        Run one full game until everyone is out or the board is exhausted
        """
        while True:
            alive = self.alive_players()
            if len(alive) == 0:
                break

            # SOLO PHASE: one player left
            if len(alive) == 1:
                last_player = alive[0]

                # Record solo-state info only once, right when solo play begins
                if not self.solo_phase_recorded:
                    self.solo_player_name = last_player
                    self.solo_started_behind = (
                        self.states[last_player].score < self.max_other_score(last_player)
                    )

                    start_deficit = self.max_other_score(last_player) - self.states[last_player].score
                    self.solo_start_deficit = start_deficit

                    # check if plausible winning answer existed at solo start
                    state = self.states[last_player]
                    plausible_answers = [
                        answer for answer, ans in state.answer_states.items()
                        if answer in self.remaining_answers and ans.recall >= 0.08 and ans.confidence >= 0.08
                    ]
                    self.solo_had_winning_answer_at_start = any(a >= start_deficit for a in plausible_answers)

                    self.solo_phase_recorded = True

                # Optional pure-competitive stop
                if self.stop_when_last_player_clinches and self.is_last_player_clinched(last_player):
                    break

                self.solo_turns_taken = 0
                # Continue solo guesses until eliminated or optional clinch stop
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
                    self.solo_turns_taken += 1

                break

            # MULTI-PLAYER PHASE
            if len(alive) == 2 and self.two_player_alternate:
                cycle = alternating_order(alive)
            else:
                cycle = snake_round_order(alive)

            # Approximate which players are currently in the snake-end cycle
            ends = {alive[0], alive[-1]} if len(alive) >= 3 else set()

            for player_name in cycle:
                if not self.states[player_name].alive:
                    continue

                is_double_window = player_name in ends
                self.handle_guess(player_name, is_part_of_double_pick_window=is_double_window)

                # If someone got eliminated, rebuild the order next outer loop
                new_alive = self.alive_players()
                if len(new_alive) != len(alive):
                    break
            
            # If no answers left, end game
            if not self.remaining_answers:
                break
        
        # Final scoring / winner extraction
        scores = {name: state.score for name, state in self.states.items()}
        strikes = {name: state.strikes for name, state in self.states.items()}
        max_score = max(scores.values()) if scores else 0
        winner_names = [name for name, score in scores.items() if score == max_score]

        # compute board reads
        final_board_reads = [get_board_signal(state) for state in self.states.values()]

        avg_final_board_read = statistics.mean(final_board_reads) if final_board_reads else 0.0
        avg_abs_final_board_read = (statistics.mean(abs(x) for x in final_board_reads) if final_board_reads else 0.0)

        strong_harsh_board_rate = (sum(1 for x in final_board_reads if x <= -0.15) / len(final_board_reads) if final_board_reads else 0.0)
        strong_generous_board_rate = (sum(1 for x in final_board_reads if x >= 0.15) / len(final_board_reads) if final_board_reads else 0.0)

        # compute estimate and uncertainty metrics (m2)
        final_cutoff_estimates = [state.cutoff_estimate for state in self.states.values()]
        final_cutoff_uncertainties = [state.cutoff_uncertainty for state in self.states.values()]

        avg_final_cutoff_estimate = (statistics.mean(final_cutoff_estimates) if final_cutoff_estimates else 0.0)
        avg_final_cutoff_uncertainty = (statistics.mean(final_cutoff_uncertainties) if final_cutoff_uncertainties else 0.0)

        low_uncertainty_rate = (sum(1 for x in final_cutoff_uncertainties if x <= 0.25) / len(final_cutoff_uncertainties) if final_cutoff_uncertainties else 0.0)

        high_cutoff_rate = (sum(1 for x in final_cutoff_estimates if x >= 70.0) / len(final_cutoff_estimates) if final_cutoff_estimates else 0.0)

        final_safe_floors = [state.cutoff_estimate - (10 + 6 * state.cutoff_uncertainty) for state in self.states.values()]

        avg_final_safe_floor = (statistics.mean(final_safe_floors) if final_safe_floors else 0.0)

        # compute local density read metrics (m3)
        final_local_density_reads = [state.local_density_read for state in self.states.values()]
        final_surprise_reads = [state.surprise_read for state in self.states.values()]
        final_near_cutoff_hits = [state.near_cutoff_hits for state in self.states.values()]
        final_near_cutoff_misses = [state.near_cutoff_misses for state in self.states.values()]

        avg_final_local_density_read = (statistics.mean(final_local_density_reads) if final_local_density_reads else 0.0)
        avg_final_surprise_read = (statistics.mean(final_surprise_reads) if final_surprise_reads else 0.0)
        avg_final_near_cutoff_hits = (statistics.mean(final_near_cutoff_hits) if final_near_cutoff_hits else 0.0)
        avg_final_near_cutoff_misses = (statistics.mean(final_near_cutoff_misses) if final_near_cutoff_misses else 0.0)

        # m4 mode counts:
        mode_counts = self.mode_counts
        double_window_mode_counts = self.double_window_mode_counts
        context_counts = self.context_counts
        context_action_counts = self.context_action_counts

        return SimulationResult(
            scores=scores,
            strikes=strikes,
            winner_names=winner_names,
            history=self.history,
            elimination_order=self.elimination_order,
            solo_player_name=self.solo_player_name,
            solo_started_behind=self.solo_started_behind,
            solo_start_deficit=self.solo_start_deficit,
            solo_turns_taken=self.solo_turns_taken,
            solo_had_winning_answer_at_start=self.solo_had_winning_answer_at_start,
            avg_final_board_read=avg_final_board_read,
            avg_abs_final_board_read=avg_abs_final_board_read,
            strong_harsh_board_rate=strong_harsh_board_rate,
            strong_generous_board_rate=strong_generous_board_rate,
            avg_final_cutoff_estimate=avg_final_cutoff_estimate,
            avg_final_cutoff_uncertainty=avg_final_cutoff_uncertainty,
            low_uncertainty_rate=low_uncertainty_rate,
            high_cutoff_rate=high_cutoff_rate,
            avg_final_safe_floor=avg_final_safe_floor,
            avg_final_local_density_read=avg_final_local_density_read,
            avg_final_surprise_read=avg_final_surprise_read,
            avg_final_near_cutoff_hits=avg_final_near_cutoff_hits,
            avg_final_near_cutoff_misses=avg_final_near_cutoff_misses,
            mode_counts=mode_counts,
            double_window_mode_counts=double_window_mode_counts,
            context_counts=context_counts,
            context_action_counts=context_action_counts,
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
    """
    Run many independent simulations and summarize the results

    This is the Monte Carlo wrapper around the single-game engine
    """
    rng = random.Random(seed)

    # Aggregate tracking containers
    win_counts = {p.name: 0.0 for p in profiles}
    score_history = {p.name: [] for p in profiles}
    strike_history = {p.name: [] for p in profiles}
    elimination_first_counts = {p.name: 0 for p in profiles}
    last_survivor_but_lost = 0
    solo_started_behind_count = 0
    solo_started_behind_and_lost = 0
    solo_started_deficits = []
    solo_turn_counts = []
    solo_had_winning_answer_count = 0
    solo_deficit_bucket_counts = {
        "1-75": 0,
        "76-150": 0,
        "151-250": 0,
        "251_plus": 0,
    }
    avg_final_board_reads = []
    avg_abs_final_board_reads = []
    strong_harsh_board_rates = []
    strong_generous_board_rates = []
    avg_final_cutoff_estimates = []
    avg_final_cutoff_uncertainties = []
    low_uncertainty_rates = []
    high_cutoff_rates = []
    avg_final_safe_floors = []
    avg_final_local_density_reads = []
    avg_final_surprise_reads = []
    avg_final_near_cutoff_hits = []
    avg_final_near_cutoff_misses = []
    mode_counts = {mode: 0 for mode in [
        "safe", "risky", "blind_risk", "chip_away", "exact_win", "comeback", "high_upside", "desperation", "victory_lap"
    ]}
    double_window_mode_counts = {mode: 0 for mode in [
        "safe", "risky", "blind_risk"
    ]}
    context_counts = {
        "open": 0,
        "dense": 0,
        "generous": 0,
        "dense_and_generous": 0,
        "tight": 0,
        "uncertain": 0,
        "double_window": 0,
        "total_decisions": 0,
    }
    context_action_counts = {
        "risky_on_open": 0,
        "risky_on_dense": 0,
        "risky_on_generous": 0,
        "risky_on_dense_and_generous": 0,
        "safe_on_tight": 0,
        "risky_on_uncertain": 0,
        "safe_on_uncertain": 0,
        "risky_on_double_window": 0,
        "safe_on_double_window": 0,
    }

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

        # Track conditional solo
        if result.solo_player_name is not None and result.solo_started_behind:
            solo_started_behind_count += 1
            if result.solo_player_name not in result.winner_names:
                solo_started_behind_and_lost += 1

            if result.solo_start_deficit is not None:
                d = result.solo_start_deficit
                solo_started_deficits.append(d)

                if d <= 75:
                    solo_deficit_bucket_counts["1-75"] += 1
                elif d <= 150:
                    solo_deficit_bucket_counts["76-150"] += 1
                elif d <= 250:
                    solo_deficit_bucket_counts["151-250"] += 1
                else:
                    solo_deficit_bucket_counts["251_plus"] += 1

            solo_turn_counts.append(result.solo_turns_taken)

            if result.solo_had_winning_answer_at_start:
                solo_had_winning_answer_count += 1

        # Split ties evenly across winners
        for winner in result.winner_names:
            win_counts[winner] += 1.0 / len(result.winner_names)

        # Record raw score/strike distributions
        for name, score in result.scores.items():
            score_history[name].append(score)

        for name, strikes in result.strikes.items():
            strike_history[name].append(strikes)

        # Track first elimination        
        if result.elimination_order:
            elimination_first_counts[result.elimination_order[0]] += 1

        # Broad "last survivor still lost" metric
        if result.elimination_order and len(result.elimination_order) == len(profiles):
            # final eliminated is last survivor
            last_survivor= result.elimination_order[-1]
            if last_survivor not in result.winner_names:
                last_survivor_but_lost += 1

        # Board read metrics
        avg_final_board_reads.append(result.avg_final_board_read)
        avg_abs_final_board_reads.append(result.avg_abs_final_board_read)
        strong_harsh_board_rates.append(result.strong_harsh_board_rate)
        strong_generous_board_rates.append(result.strong_generous_board_rate)
        avg_final_cutoff_estimates.append(result.avg_final_cutoff_estimate)
        avg_final_cutoff_uncertainties.append(result.avg_final_cutoff_uncertainty)
        low_uncertainty_rates.append(result.low_uncertainty_rate)
        high_cutoff_rates.append(result.high_cutoff_rate)
        avg_final_safe_floors.append(result.avg_final_safe_floor)
        avg_final_local_density_reads.append(result.avg_final_local_density_read)
        avg_final_surprise_reads.append(result.avg_final_surprise_read)
        avg_final_near_cutoff_hits.append(result.avg_final_near_cutoff_hits)
        avg_final_near_cutoff_misses.append(result.avg_final_near_cutoff_misses)
        # Mode counts
        for mode, count in result.mode_counts.items():
            mode_counts[mode] = mode_counts.get(mode, 0) + count
        for mode, count in result.double_window_mode_counts.items():
            double_window_mode_counts[mode] = double_window_mode_counts.get(mode, 0) + count
        for key, count in result.context_counts.items():
            context_counts[key] = context_counts.get(key, 0) + count
        for key, count in result.context_action_counts.items():
            context_action_counts[key] = context_action_counts.get(key, 0) + count

    total_modes = sum(mode_counts.values())
    total_double_window_modes = sum(double_window_mode_counts.values())

    mode_rates = {
        mode: (count / total_modes if total_modes > 0 else 0.0) for mode, count in mode_counts.items()
    }

    double_window_mode_rates = {
        mode: (count / total_double_window_modes if total_double_window_modes > 0 else 0.0) for mode, count in double_window_mode_counts.items()
    }

    total_decisions = context_counts.get("total_decisions", 0)
    open_count = context_counts.get("open", 0)
    tight_count = context_counts.get("tight", 0)
    uncertain_count = context_counts.get("uncertain", 0)
    double_window_count = context_counts.get("double_window", 0)
    dense_count = context_counts.get("dense", 0)
    generous_count = context_counts.get("generous", 0)
    dense_and_generous_count = context_counts.get("dense_and_generous", 0)

    context_rates = {
        "open_context_rate": open_count / total_decisions if total_decisions > 0 else 0.0,
        "dense_context_rate": dense_count / total_decisions if total_decisions > 0 else 0.0,
        "generous_context_rate": generous_count / total_decisions if total_decisions > 0 else 0.0,
        "dense_and_generous_context_rate": dense_and_generous_count / total_decisions if total_decisions > 0 else 0.0,
        "tight_context_rate": tight_count / total_decisions if total_decisions > 0 else 0.0,
        "uncertain_context_rate": uncertain_count / total_decisions if total_decisions > 0 else 0.0,

        "double_window_context_rate": double_window_count / total_decisions if total_decisions > 0 else 0.0,
        "risky_on_open_rate": context_action_counts.get("risky_on_open", 0) / open_count if open_count > 0 else 0.0,
        "risky_on_dense_rate": context_action_counts.get("risky_on_dense", 0) / dense_count if dense_count > 0 else 0.0,
        "risky_on_generous_rate": context_action_counts.get("risky_on_generous", 0) / generous_count if generous_count > 0 else 0.0,
        "risky_on_dense_and_generous_rate": context_action_counts.get("risky_on_dense_and_generous", 0) / dense_and_generous_count if dense_and_generous_count > 0 else 0.0,

        "safe_on_tight_rate": context_action_counts.get("safe_on_tight", 0) / tight_count if tight_count > 0 else 0.0,
        "risky_on_uncertain_rate": context_action_counts.get("risky_on_uncertain", 0) / uncertain_count if uncertain_count > 0 else 0.0,
        "safe_on_uncertain_rate": context_action_counts.get("safe_on_uncertain", 0) / uncertain_count if uncertain_count > 0 else 0.0,
        "risky_on_double_window_rate": context_action_counts.get("risky_on_double_window", 0) / double_window_count if double_window_count > 0 else 0.0,
        "safe_on_double_window_rate": context_action_counts.get("safe_on_double_window", 0) / double_window_count if double_window_count > 0 else 0.0,
    }

    # Build the final summary object
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
        "solo_start_deficit_avg": statistics.mean(solo_started_deficits) if solo_started_deficits else 0.0,
        "solo_turns_avg": statistics.mean(solo_turn_counts) if solo_turn_counts else 0.0,
        "solo_had_winning_answer_rate": solo_had_winning_answer_count / n_sims,
        "solo_had_winning_answer_given_started_behind_rate": (solo_had_winning_answer_count / solo_started_behind_count if solo_started_behind_count > 0 else 0.0),
        "solo_deficit_bucket_rates": {
            bucket: (count / solo_started_behind_count if solo_started_behind_count > 0 else 0.0) for bucket, count in solo_deficit_bucket_counts.items()
        },
        "avg_final_board_read": statistics.mean(avg_final_board_reads) if avg_final_board_reads else 0.0,
        "avg_abs_final_board_read": statistics.mean(avg_abs_final_board_reads) if avg_abs_final_board_reads else 0.0,
        "strong_harsh_board_rate": statistics.mean(strong_harsh_board_rates) if strong_harsh_board_rates else 0.0,
        "strong_generous_board_rate": statistics.mean(strong_generous_board_rates) if strong_generous_board_rates else 0.0,
        "avg_final_cutoff_estimate": statistics.mean(avg_final_cutoff_estimates) if avg_final_cutoff_estimates else 0.0,
        "avg_final_cutoff_uncertainty": statistics.mean(avg_final_cutoff_uncertainties) if avg_final_cutoff_uncertainties else 0.0,
        "low_uncertainty_rate": statistics.mean(low_uncertainty_rates) if low_uncertainty_rates else 0.0,
        "high_cutoff_rate": statistics.mean(high_cutoff_rates) if high_cutoff_rates else 0.0,
        "avg_final_safe_floor": statistics.mean(avg_final_safe_floors) if avg_final_safe_floors else 0.0,
        "avg_final_local_density_read": statistics.mean(avg_final_local_density_reads) if avg_final_local_density_reads else 0.0,
        "avg_final_surprise_read": statistics.mean(avg_final_surprise_reads) if avg_final_surprise_reads else 0.0,
        "avg_final_near_cutoff_hits": statistics.mean(avg_final_near_cutoff_hits) if avg_final_near_cutoff_hits else 0.0,
        "avg_final_near_cutoff_misses": statistics.mean(avg_final_near_cutoff_misses) if avg_final_near_cutoff_misses else 0.0,
        "mode_counts": mode_counts,
        "mode_rates": mode_rates,
        "double_window_mode_counts": double_window_mode_counts,
        "double_window_mode_rates": double_window_mode_rates,
        "context_counts": context_counts,
        "context_action_counts": context_action_counts,
        "context_rates": context_rates,
    }

    return summary
    
#==============================
# EXAMPLE SETUP
#==============================

def main() -> None:
    """
    Example entry point

    Defines three contestant profiles, one category, runs the simulation, and prints summary statistics
    """
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

    def run_validation_suite(profiles: List[PlayerProfile]) -> None:
        """
        comment here later
        """
        categories = [
            Category(name="All-Time OPS+", difficulty=3.5, tags=set()),
            Category(name="All-Time bWAR", difficulty=4.2, tags={"war"}),
            Category(name="Home Runs since 2000", difficulty=2.5, tags={"modern"}),
            Category(name="Hits since 1900", difficulty=3.0, tags={"all_time"}),
            Category(name="Every MVP Winner", difficulty=5.0, tags={"awards"}),
        ]

        all_summaries = []
        
        # per category summaries
        for category in categories:
            print(f"\n=== Category: {category.name} ===")

            summary = simulate_many(
                profiles=profiles,
                category=category,
                n_sims=10000,
                seed=42,
                stop_when_last_player_clinches=False,
                two_player_alternate=True,
            )

            all_summaries.append((category, summary))
            
            
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
            print(f"Avg solo start deficit: {summary['solo_start_deficit_avg']:.1f}")
            print(f"Avg solo turns taken: {summary['solo_turns_avg']:.2f}")
            print(f"Solo had winning answer rate: {summary['solo_had_winning_answer_rate']:.3f}")
            print(f"Solo had winning answer given started behind rate: {summary['solo_had_winning_answer_given_started_behind_rate']:.3f}")
            bucket_rates = summary["solo_deficit_bucket_rates"]
            print(
                "Solo start deficit buckets: "
                f"1-75: {bucket_rates['1-75']:.3f}, "
                f"76-150: {bucket_rates['76-150']:.3f}, "
                f"151-250: {bucket_rates['151-250']:.3f}, "
                f"251+: {bucket_rates['251_plus']:.3f}"
            )
            print(f"Avg final board read: {summary['avg_final_board_read']:.3f}")
            print(f"Avg absolute final board read: {summary['avg_abs_final_board_read']:.3f}")
            print(f"Strong harsh board rate: {summary['strong_harsh_board_rate']:.3f}")
            print(f"Strong generous board rate: {summary['strong_generous_board_rate']:.3f}")
            print(f"Avg final cutoff estimate: {summary['avg_final_cutoff_estimate']:.2f}")
            print(f"Avg final cutoff uncertainty: {summary['avg_final_cutoff_uncertainty']:.3f}")
            print(f"Low uncertainty rate: {summary['low_uncertainty_rate']:.3f}")
            print(f"High cutoff rate: {summary['high_cutoff_rate']:.3f}")
            print(f"Avg final safe floor: {summary['avg_final_safe_floor']:.2f}")
            print(f"Avg final local density read: {summary['avg_final_local_density_read']:.3f}")
            print(f"Avg final surprise read: {summary['avg_final_surprise_read']:.3f}")
            print(f"Avg final near-cutoff hits: {summary['avg_final_near_cutoff_hits']:.2f}")
            print(f"Avg final near-cutoff misses: {summary['avg_final_near_cutoff_misses']:.2f}")

            mode_rates = summary["mode_rates"]
            double_window_mode_rates = summary["double_window_mode_rates"]
            
            print(
                "Mode rates: "
                f"safe={mode_rates.get('safe', 0.0):.3f}, "
                f"risky={mode_rates.get('risky', 0.0):.3f}, "
                f"blind_risk={mode_rates.get('blind_risk', 0.0):.3f}, "
                f"chip_away={mode_rates.get('chip_away', 0.0):.3f}, "
                f"exact_win={mode_rates.get('exact_win', 0.0):.3f}, "
                f"comeback={mode_rates.get('comeback', 0.0):.3f}, "
                f"high_upside={mode_rates.get('high_upside', 0.0):.3f}, "
                f"desperation={mode_rates.get('desperation', 0.0):.3f}, "
                f"victory_lap={mode_rates.get('victory_lap', 0.0):.3f}"
            )

            print(
                "Double window mode rates: "
                f"safe={double_window_mode_rates.get('safe', 0.0):.3f}, "
                f"risky={double_window_mode_rates.get('risky', 0.0):.3f}, "
                f"blind_risk={double_window_mode_rates.get('blind_risk', 0.0):.3f}"
            )

            context_rates = summary["context_rates"]

            print(
                "Context rates: "
                f"open={context_rates.get('open_context_rate', 0.0):.3f}, "
                f"dense={context_rates.get('dense_context_rate', 0.0):.3f}, "
                f"generous={context_rates.get('generous_context_rate', 0.0):.3f}, "
                f"dense_and_generous={context_rates.get('dense_and_generous_context_rate', 0.0):.3f}, "
                f"tight={context_rates.get('tight_context_rate', 0.0):.3f}, "
                f"uncertain={context_rates.get('uncertain_context_rate', 0.0):.3f}, "
            )

            print(
                "Context-action rates: "
                f"risky_on_open={context_rates.get('risky_on_open_rate', 0.0):.3f}, "
                f"risky_on_dense={context_rates.get('risky_on_dense_rate', 0.0):.3f}, "
                f"risky_on_generous={context_rates.get('risky_on_generous_rate', 0.0):.3f}, "
                f"risky_on_dense_and_generous={context_rates.get('risky_on_dense_and_generous_rate', 0.0):.3f}, "
                f"safe_on_tight={context_rates.get('safe_on_tight_rate', 0.0):.3f}, "
                f"risky_on_uncertain={context_rates.get('risky_on_uncertain_rate', 0.0):.3f}, "
                f"safe_on_uncertain={context_rates.get('safe_on_uncertain_rate', 0.0):.3f}, "
                f"risky_on_double_window={context_rates.get('risky_on_double_window_rate', 0.0):.3f}, "
                f"safe_on_double_window={context_rates.get('safe_on_double_window_rate', 0.0):.3f}"
            )

        
        # aggregate summary across categories
        print("\n === Aggregate Summary Across Validation Suite ===")
        
        for name in [p.name for p in profiles]:
            avg_win_rate = statistics.mean(s["win_rate"][name] for _, s in all_summaries)
            avg_score = statistics.mean(s["avg_score"][name] for _, s in all_summaries)
            avg_median_score = statistics.mean(s["median_score"][name] for _, s in all_summaries)
            avg_stdev = statistics.mean(s["stdev_score"][name] for _, s in all_summaries)
            avg_strikes = statistics.mean(s["avg_strikes"][name] for _, s in all_summaries)
            avg_first_out_rate = statistics.mean(s["first_eliminated_rate"][name] for _, s in all_summaries)

            print(
                f"{name}: "
                f"avg_win_rate={avg_win_rate:.3f}, "
                f"avg_score={avg_score:.1f}, "
                f"avg_median_score={avg_median_score:.1f}, "
                f"avg_stdev={avg_stdev:.1f}, "
                f"avg_strikes={avg_strikes:.2f}, "
                f"avg_first_out_rate={avg_first_out_rate:.3f}"
            )

        avg_last_survivor_lost = statistics.mean(s["last_survivor_but_lost_rate"] for _, s in all_summaries)
        avg_solo_started_behind = statistics.mean(s["solo_started_behind_rate"] for _, s in all_summaries)
        avg_solo_started_behind_and_lost = statistics.mean(s["solo_started_behind_and_lost_rate"] for _, s in all_summaries)
        avg_solo_start_deficit = statistics.mean(s["solo_start_deficit_avg"] for _, s in all_summaries)
        avg_solo_turns = statistics.mean(s["solo_turns_avg"] for _, s in all_summaries)
        avg_solo_had_winning_answer = statistics.mean(s["solo_had_winning_answer_rate"] for _, s in all_summaries)
        avg_solo_had_winning_answer_given_started_behind = statistics.mean(s["solo_had_winning_answer_given_started_behind_rate"] for _, s in all_summaries)
        avg_bucket_1_75 = statistics.mean(s["solo_deficit_bucket_rates"]["1-75"] for _, s in all_summaries)
        avg_bucket_76_150 = statistics.mean(s["solo_deficit_bucket_rates"]["76-150"] for _, s in all_summaries)
        avg_bucket_151_250 = statistics.mean(s["solo_deficit_bucket_rates"]["151-250"] for _, s in all_summaries)
        avg_bucket_251_plus = statistics.mean(s["solo_deficit_bucket_rates"]["251_plus"] for _, s in all_summaries)
        avg_final_board_read = statistics.mean(s["avg_final_board_read"] for _, s in all_summaries)
        avg_abs_final_board_read = statistics.mean(s["avg_abs_final_board_read"] for _, s in all_summaries)
        avg_strong_harsh_board_rate = statistics.mean(s["strong_harsh_board_rate"] for _, s in all_summaries)
        avg_strong_generous_board_rate = statistics.mean(s["strong_generous_board_rate"] for _, s in all_summaries)
        avg_final_cutoff_estimate = statistics.mean(s["avg_final_cutoff_estimate"] for _, s in all_summaries)
        avg_final_cutoff_uncertainty = statistics.mean(s["avg_final_cutoff_uncertainty"] for _, s in all_summaries)
        avg_low_uncertainty_rate = statistics.mean(s["low_uncertainty_rate"] for _, s in all_summaries)
        avg_high_cutoff_rate = statistics.mean(s["high_cutoff_rate"] for _, s in all_summaries)
        avg_safe_floor = statistics.mean(s["avg_final_safe_floor"] for _, s in all_summaries)
        avg_local_density_read = statistics.mean(s["avg_final_local_density_read"] for _, s in all_summaries)
        avg_surprise_read = statistics.mean(s["avg_final_surprise_read"] for _, s in all_summaries)
        avg_near_cutoff_hits = statistics.mean(s["avg_final_near_cutoff_hits"] for _, s in all_summaries)
        avg_near_cutoff_misses = statistics.mean(s["avg_final_near_cutoff_misses"] for _, s in all_summaries)

        aggregate_mode_counts = {mode: 0 for mode in [
            "safe", "risky", "blind_risk", "chip_away", "exact_win", "comeback", "high_upside", "desperation", "victory_lap"
        ]}

        aggregate_double_window_mode_counts = {mode: 0 for mode in [
            "safe", "risky", "blind_risk"
        ]}

        for _, s in all_summaries:
            for mode, count in s["mode_counts"].items():
                aggregate_mode_counts[mode] = aggregate_mode_counts.get(mode, 0) + count
            
            for mode, count in s["double_window_mode_counts"].items():
                aggregate_double_window_mode_counts[mode] = aggregate_double_window_mode_counts.get(mode, 0) + count

        total_aggregate_modes = sum(aggregate_mode_counts.values())
        total_aggregate_double_modes = sum(aggregate_double_window_mode_counts.values())

        aggregate_mode_rates = {
            mode: (count / total_aggregate_modes if total_aggregate_modes > 0 else 0.0) for mode, count in aggregate_mode_counts.items()
        }

        aggregate_double_window_mode_rates = {
            mode: (count / total_aggregate_double_modes if total_aggregate_double_modes > 0 else 0.0) for mode, count in aggregate_double_window_mode_counts.items()
        }

        aggregate_context_counts = {
            "open": 0,
            "dense": 0,
            "generous": 0,
            "dense_and_generous": 0,
            "tight": 0,
            "uncertain": 0,
            "double_window": 0,
            "total_decisions": 0,
        }

        aggregate_context_action_counts = {
            "risky_on_open": 0,
            "risky_on_dense": 0,
            "risky_on_generous": 0,
            "risky_on_dense_and_generous": 0,
            "safe_on_tight": 0,
            "risky_on_uncertain": 0,
            "safe_on_uncertain": 0,
            "risky_on_double_window": 0,
            "safe_on_double_window": 0,
        }

        for _, s in all_summaries:
            for key, count in s["context_counts"].items():
                aggregate_context_counts[key] = aggregate_context_counts.get(key, 0) + count
            for key, count in s["context_action_counts"].items():
                aggregate_context_action_counts[key] = aggregate_context_action_counts.get(key, 0) + count

        total_decisions = aggregate_context_counts.get("total_decisions", 0)
        open_count = aggregate_context_counts.get("open", 0)
        tight_count = aggregate_context_counts.get("tight", 0)
        uncertain_count = aggregate_context_counts.get("uncertain", 0)
        double_window_count = aggregate_context_counts.get("double_window", 0)
        dense_count = aggregate_context_counts.get("dense", 0)
        generous_count = aggregate_context_counts.get("generous", 0)
        dense_and_generous_count = aggregate_context_counts.get("dense_and_generous", 0)

        aggregate_context_rates = {
            "open_context_rate": open_count / total_decisions if total_decisions > 0 else 0.0,
            "dense_context_rate": dense_count / total_decisions if total_decisions > 0 else 0.0,
            "generous_context_rate": generous_count / total_decisions if total_decisions > 0 else 0.0,
            "dense_and_generous_context_rate": dense_and_generous_count / total_decisions if total_decisions > 0 else 0.0,
            "tight_context_rate": tight_count / total_decisions if total_decisions > 0 else 0.0,
            "uncertain_context_rate": uncertain_count / total_decisions if total_decisions > 0 else 0.0,
            "risky_on_open_rate": aggregate_context_action_counts.get("risky_on_open", 0) / open_count if open_count > 0 else 0.0,
            "risky_on_dense_rate": aggregate_context_action_counts.get("risky_on_dense", 0) / dense_count if dense_count > 0 else 0.0,
            "risky_on_generous_rate": aggregate_context_action_counts.get("risky_on_generous", 0) / generous_count if generous_count > 0 else 0.0,
            "risky_on_dense_and_generous_rate": aggregate_context_action_counts.get("risky_on_dense_and_generous", 0) / dense_and_generous_count if dense_and_generous_count > 0 else 0.0,
            "safe_on_tight_rate": aggregate_context_action_counts.get("safe_on_tight", 0) / tight_count if tight_count > 0 else 0.0,
            "risky_on_uncertain_rate": aggregate_context_action_counts.get("risky_on_uncertain", 0) / uncertain_count if uncertain_count > 0 else 0.0,
            "safe_on_uncertain_rate": aggregate_context_action_counts.get("safe_on_uncertain", 0) / uncertain_count if uncertain_count > 0 else 0.0,
            "risky_on_double_window_rate": aggregate_context_action_counts.get("risky_on_double_window", 0) / double_window_count if double_window_count > 0 else 0.0,
            "safe_on_double_window_rate": aggregate_context_action_counts.get("safe_on_double_window", 0) / double_window_count if double_window_count > 0 else 0.0,
        }

        print(f"Last survivor but lost rate: {avg_last_survivor_lost:.3f}")
        print(f"Solo started behind rate: {avg_solo_started_behind:.3f}")
        print(f"Solo started behind and lost rate: {avg_solo_started_behind_and_lost:.3f}")
        print(f"Avg solo start deficit: {avg_solo_start_deficit:.1f}")
        print(f"Avg solo turns taken: {avg_solo_turns:.2f}")
        print(f"Solo had winning answer rate: {avg_solo_had_winning_answer:.3f}")
        print(f"Solo had winning answer given started behind rate: {avg_solo_had_winning_answer_given_started_behind:.3f}")
        print(
            "Solo start deficit buckets: "
            f"1-75: {avg_bucket_1_75:.3f}, "
            f"76-150: {avg_bucket_76_150:.3f}, "
            f"151-250: {avg_bucket_151_250:.3f}, "
            f"251+: {avg_bucket_251_plus:.3f}"
        )
        print(f"Avg final board read: {avg_final_board_read:.3f}")
        print(f"Avg absolute final board read: {avg_abs_final_board_read:.3f}")
        print(f"Avg strong harsh board rate: {avg_strong_harsh_board_rate:.3f}")
        print(f"Avg strong generous board rate: {avg_strong_generous_board_rate:.3f}")
        print(f"Avg final cutoff estimate: {avg_final_cutoff_estimate:.2f}")
        print(f"Avg final cutoff uncertainty: {avg_final_cutoff_uncertainty:.3f}")
        print(f"Avg low uncertainty rate: {avg_low_uncertainty_rate:.3f}")
        print(f"Avg high cutoff rate: {avg_high_cutoff_rate:.3f}")
        print(f"Avg final safe floor: {avg_safe_floor:.2f}")
        print(f"Avg final local density read: {avg_local_density_read:.3f}")
        print(f"Avg final surprise read: {avg_surprise_read:.3f}")
        print(f"Avg final near-cutoff hits: {avg_near_cutoff_hits:.2f}")
        print(f"Avg final near-cutoff misses: {avg_near_cutoff_misses:.2f}")
        print(
            "Mode rates: "
            f"safe={aggregate_mode_rates.get('safe', 0.0):.3f}, "
            f"risky={aggregate_mode_rates.get('risky', 0.0):.3f}, "
            f"blind_risk={aggregate_mode_rates.get('blind_risk', 0.0):.3f}, "
            f"chip_away={aggregate_mode_rates.get('chip_away', 0.0):.3f}, "
            f"exact_win={aggregate_mode_rates.get('exact_win', 0.0):.3f}, "
            f"comeback={aggregate_mode_rates.get('comeback', 0.0):.3f}, "
            f"high_upside={aggregate_mode_rates.get('high_upside', 0.0):.3f}, "
            f"desperation={aggregate_mode_rates.get('desperation', 0.0):.3f}, "
            f"victory_lap={aggregate_mode_rates.get('victory_lap', 0.0):.3f}"
        )
        print(
            "Double window mode rates: "
            f"safe={aggregate_double_window_mode_rates.get('safe', 0.0):.3f}, "
            f"risky={aggregate_double_window_mode_rates.get('risky', 0.0):.3f}, "
            f"blind_risk={aggregate_double_window_mode_rates.get('blind_risk', 0.0):.3f}"
        )
        print(
            "Context rates: "
            f"open={aggregate_context_rates.get('open_context_rate', 0.0):.3f}, "
            f"dense={aggregate_context_rates.get('dense_context_rate', 0.0):.3f}, "
            f"generous={aggregate_context_rates.get('generous_context_rate', 0.0):.3f}, "
            f"dense_and_generous={aggregate_context_rates.get('dense_and_generous_context_rate', 0.0):.3f}, "
            f"tight={aggregate_context_rates.get('tight_context_rate', 0.0):.3f}, "
            f"uncertain={aggregate_context_rates.get('uncertain_context_rate', 0.0):.3f}, "
        )
        print(
            "Context-action rates: "
            f"risky_on_open={aggregate_context_rates.get('risky_on_open_rate', 0.0):.3f}, "
            f"risky_on_dense={aggregate_context_rates.get('risky_on_dense_rate', 0.0):.3f}, "
            f"risky_on_generous={aggregate_context_rates.get('risky_on_generous_rate', 0.0):.3f}, "
            f"risky_on_dense_and_generous={aggregate_context_rates.get('risky_on_dense_and_generous_rate', 0.0):.3f}, "
            f"safe_on_tight={aggregate_context_rates.get('safe_on_tight_rate', 0.0):.3f}, "
            f"risky_on_uncertain={aggregate_context_rates.get('risky_on_uncertain_rate', 0.0):.3f}, "
            f"safe_on_uncertain={aggregate_context_rates.get('safe_on_uncertain_rate', 0.0):.3f}, "
            f"risky_on_double_window={aggregate_context_rates.get('risky_on_double_window_rate', 0.0):.3f}, "
            f"safe_on_double_window={aggregate_context_rates.get('safe_on_double_window_rate', 0.0):.3f}"
        )

    run_validation_suite(profiles)

if __name__ == "__main__":
    main()