# Simulation Engine - Version 2 (V2)

## Overview
The main purpose of V2, beyond extending V1, is to tackle the question of:
> "Can we move beyond binary knowledge by modeling uncertainty, recall, and inference to better replicate to better replicate real contestant decision-making?"

---

## Goals

### 1. Knowledge vs Recall vs Confidence
The goal is to separate:
- knowing something
- recalling it under pressure
- being willing to guess it

This allows the simluation to distinguish between what a player knows, what they can access under pressure,and what they are willing to act on.

This is essential for modeling realistic decision-making.

### 2. Uncertain / Plausible Guesses
Key mindset to introduce:
- "I think this might be on the list"

This critical for comebacks, mid-risk decisions, and realism.

### 3. Real Answer Objects
Replace `1-100` with structured answers, such as:
- name
- value
- obscurity
- category tags

This allows for the system to test against real categories instead of a fixed range of 1-100

### 4. Category Types
Introduce different testing categories:
- WAR-heavy
- Old-era
- Modern players
- Awards-based
- Niche categories

This is important as testing against only one category / difficulty can result in overtuning and skewed general results.

### 5. Board Inference
Players will be able to:
- Update beliefs based on real answers
- Estimate cutoff depth
- Adjust risk dynamically

This adds a different layer of uncertainty to how the system decides guesses per contestant.

### 6. Improved Solo Logic
As this was one of the main short comings of V1, in V2, the solo player will:
- use confidence-weighted gusses
- plan comebacks based on deficit
- take calculated risks beyond known answers

The aim is to further reduce the `solo started behind but lost rate`, which remains extremely high at ~75% after V1.

---

## Design Evolution
The above mentioned goals were drawn upon after evaluating the limitations of V1. The most important improvements involve:
- full answer modeling
- inference systems
- uncertainty modeling
- improved solo logic

However, implementing all of these at once would make the system difficult to debug, validate and interpret.

As a result, V2 was broken into incremental milestones.

---

## Milestones and Core Components 

V2 was developed incrementally through a series of milestones, each targeting a specific limitation of V1 while maintaining system stability and intrepretability.

### Milestone 1 - Non-Binary Knowledge System
**Status:** Completed

#### Purpose
To replace the "known vs unknown" system from V1 with a richer representation of player knowledge.

#### Core Changes
- Transitioned from `Set[int]` &rarr; `Dict[int, AnswerState]`
- Introduced `AnswerState` dataclass:
    - knowledge
    - recall
    - confidence
- Added bridge logic to allow existing engine components to continue functioning

#### Key Outcome
- Established foundation for probabilistic reasoning
- Enbabled separation of:
    - what a player knows
    - what the can recall
    - what they are willing to act on

#### Notes
- This milestone prioritized **system stability over realism**
- Most testing focused on ensurinv the engine still ran correctly
- Output metrics were not yet meaningful

### Milestone 2 - Probabilistic Guess Generation
**Status:** Completed

#### Purpose
To move from deterministic guessing to probabilistic decision-making based on answer states.

#### Core Changes
- Reworked guess selection:
    - from binary eligibility to weighted candidate selection
- Introduced:
    - plausible guesses
    - uncertain guesses
    - blind risk behavior
- Added noise and variance:
    - recall noise
    - confidence noise
- Reworked:
    - `choose_guess_for_mode()`
    - `handle_guess()`

#### Key Outcome
- Mid-game behavior became more realistic
- Players could:
    - take calculated risks
    - make plausible but uncertain guesses

#### Notes
- Introduced significant instability:
    - high variance
    - inflated scores
    - extreme solo failure rates
- Revealed need for **system-level corrections (not just better guessing)**

### Milestone 3 - Solo / Endgame Rework
**Status:** Completed

#### Purpose
To address unrealistic endgame behavior, particularly the extreme high solo failure rate

#### Core Changes
- Reworked:
    - `decide_last_player_mode()`
    - `choose_last_player_guess()`
- Introduced dynamic solo modes:
    - chip-away
    - exact-win
    - comeback
    - desperation
- Added:
    - deficit-aware logic
    - strike-aware behavior
    - candidate-based decision paths

#### Key Outcome
- Significant reduction in:
    - solo starting deficits
    - solo failure rates
- Increased:
    - solo turns available
    - comeback viability

#### Key Insight
> The main driver of poor solo performance was not endgame logic, but the distribution of game states leading into it.

#### Notes
- Required upstream changes:
    - safer early play
    - improved risk pacing
- Marked a shift from:
    - fixing isolated logic &rarr; improving full system dynamics

### Milestone 4 - Board Inference
**Status:** Completed

#### Purpose
To introduce adaptive behavior based on revealed board information and table dynamics

#### Core Changes
- Introduced `board_read` system:
    - tracks percieved board difficulty
- Updated based on:
    - surprising results
    - strikes on plausible answers
    - density of safe answers
- Applied to: 
    - risk thresholds
    - guess selection behavior
- Added light table effects:
    - reduced trust in reactions
    - increased caution after surprises

#### Key Outcome
- Players no longer act purely on static profiles
- Behavior adapts dynamically to:
    - board state
    - revealed information

#### Notes
- Inference is intentionally lightweight
- Serves as foundation for future expansion

---

## Implementation Details
This section outlines the core systems introduced in V2 and how they interact to produce simulation behavior.

### Answer Representation
The binary knowledge system from V1 is replaced with a structured per-answer state:
- `AnswerState`:
    - `knowledge`: likelihood the player knows the answer
    - `recall`: likelihood they can retrieve it
    - `confidence`: likelihood they are willing to guess

These values are sampled and updated per simulation, allowing for probabilistic behavior.

### Guess Generation System
Guess selection is now based on weighted cnadidate evaluation rather than binary filtering.

Key components:
- Candidate scoring is based on:
    - recall
    - confidence
    - contextual modifiers (pressure, mode)
- Separate handling for:
    - safe guesses
    - risky guesses
    - blind guesses

Noise is introduced via:
- recall inference
- confidence variance

This produces:
- plausible uncertainty
- non-deterministic outcomes

### Guess Resolution
Guess outcomes are determined probabilistically:
- Success depends on:
    - recall
    - confidence
    - contextual modifiers
- Incorrect guesses result in:
    - strikes
    - removal from board

This replaces deterministic correctness with **probabilistic execution**

### Mode Selection System
Players select behavior modes based on:
- score deficit
- strike count
- board size
- inferred difficulty

Modes include:
- safe
- balanced
- risky
- desperation

These modes influence:
- candidate selection 
- threshold adjustments

### Solo / Endgame System
The solo system introduces structured decision-making for the final player:
- Modes:
    - chip-away
    - exact-win
    - comeback
    - desperation
- Decisions are based on
    - deficit size
    - remaining strikes
    - available candidates

Additional tracking includes:
- solo start deficit
- solo turns taken
- winning answer availability

### Board Inference System
Players maintain a lightweight belief about board difficulty:
- `board_read` variable, which is updated based on:
    - surprising strikes
    - strike patterns
    - safe answer density

Effects:
- modifies risk tolerance
- influences guess selection

### Variance and Noise
To simulate human inconsistency:
- recall noise
- confidence noise
- stochastic candidate selection

This ensures:
- non-deterministic outcomes
- variablity across simulations

### Validation Framework
V2 introduces a multi-category validation suite:
- Multiple category types
- Varying difficulty levels
- Aggregate performance tracking

Metrics tracked include:
- win rates
- score distributions
- solo performance
- deficit distributions

This ensures:
- generalization across categories
- detection of tuning bias

---

## Validation Strategy
To avoid overfitting to a single category, V2 introduces a multi-category validation suite. This includes:
- varying category difficulty
- category-specific modifiers
- cross-simulation comparison

The purpose of this was to ensure generalization, validate behavioral consistency and to detect tuning bias.

---

## Results
V2 introduces significant changes to the simulation engine, making direct comparision with V1 non-trivial. However, several key trends emerge when evaulating preformance acorss milestones and the multi-category validation suite.

### Evolution Across Milestones

#### V2M2 - Probabalistic Guessing
Early results after introducing probabilistic guess generation showed the following:
- Improved realism in mid-game decision making
- More varied outomes due to non-binary knowledge

However, there are key metrics that also shifted:
- **High volatility (stdev)**
- **Extreme solo failure rates (~90%)**
- Inflated scoring and unstable distributions

This stage demonstrated that introducing uncertainty alone is insufficient without controlling game state dynamics.

#### V2M3 - Solo / Endgame Rework
After addressing both solo logic ***and upstream game issues***, results improved significantly:
- **Reduced solo starting deficits**
- **Increased solo turns available**
- **Higher probability of having winning answers available**

The largest drop in specific metrics were:
- `solo started behind but lost rate`
- `last survivor but lost rate`

All of this confirms that the endgame logic is strongly dependent on earlier game dynamics, not just solo decision logic.

#### V2M4 - Board Inference
Introducing lightweight board inference further refined behavior:
- Players adjusted risk based on perceived board difficulty
- Simulation exhibits:
    - category-dependent behavior shifts
    - adaptive (non-static) decision making
- Board-read metrics show:
    - moderate variability
    - no longer overwhelmingly biased towards "generous" boards

### Final Validation Suite Results (Aggregate)
Across all categories:
- Contestant 1 win rate: ~0.69-0.71
- Contestant 2 win rate: ~0.21-0.23
- Contestant 3 win rate: ~0.07-0.09

Solo Metrics:
- `Last survivor but lost rate`: ~0.09
- `Solo started behind but lost rate`: ~0.43-0.54
- `Avg solo start deficit`: ~90-120
- `Avg solo turns`: ~8-11
- `Winning answer availability (given behind)`: ~0.48

Deficit Distribution:
- Majority of solo states fall within **1-150 points**
- Extreme deficits (>250) are rare

### Key Observations
1. **Game states are significantly more realistic and stable**
    - smaller deficits
    - more comeback opportunities
    - longer endamge sequences
2. **Solo play is now viable**
    - no longer a near-certain loss state
    - outomce depends on both strategy and opportunity
3. **Category differences are preserved**
    - hard categories (e.g., WAR) remain punishing
    - easier categories allow more balanced outcomes
4. **Inference adds meaningful variation**
    - behavior adapts to revealed information
    - players no longer act purely on static profiles

### Raw Results

Full validation outputs and intermediate benchmark runs are available in: `docs/supplements/v2_raw_results.md`

---

## Limitations
While V2 represents a substantial improvement over V1, several limitations remain.

1. **Category Calibration Imbalance**

Contestants are overly favored in specific categories, while punished harshly in others:
- WAR-heavy categories heavily favor Contestant 1
- MVP-style categories heavily favor Contestant 2
- Some categories nearly eliminate weaker contestants

This suggests that category modifiers may be **over-amplifying strengths and weaknesses**, and further calibration is needed for consistent balance.

2. **Board Inference Simplicity**

The inference system is intentionally lightweight:
- no opponent modeling
- no memory of individual player tendencies 
- no explicit cutoff estimation

Thus, as a result:
- `board_read` is **directional, not precise**
- inference influences behavior but does not fully explain it

3. **No Structured Answer Objects (Yet)**

Despite being a stated goal:
- answers are still represented as point values (1-100)
- no real player/entity data
- no semantic relationship between answers

This, in turn, does limit realism of inference, category richness and interpretability.

4. **Lack of Multi-Turn Planning**

Players operate primarly on **single-turn decision logic**:
- no planning sequences (e.g., setup &rarr; finish)
- no optimal path selection over multiple turns.

This particuarly affects comeback efficiency and endgame optimization.

5. **Residual Variance and Distribution Spread**

Although improved from early V2:
- standard deviation remains higher than V1
- some categories still produce volatile outcomes

This is partly expected due to probabilistic modeling and increased system complexity.

6. **Behavioral Simplifications**

Player behavior is still simplified:
- no personality modeling (aggressive vs cautious)
- no fatigue, tilt, or psychological factors
- no opponent-specific trust or adaptation

---

## Conclusions
V2 represents major evolution of the simulation engine.

### From V1 to V2
V1 modeled:
- binary knowledge
- static behavior
- deterministic decision rules

V2 modeled:
- probabilistic knowledge representation
- uncertainty and confidence modeling
- adaptive behavior through inference
- improved endgame realism

### Key Achievements
- Succesesfully moved from **binary &rarr; probabilistic modeling**
- Reduced unrealistic solo failure rates
- Produced more **balanced and interpretable game states**
- Introduced a funcitonal board inference system
- Validated behavior across multiple category types

### Most Important Insight
The most significant finding from V2 was:
> Endgame outcomes cannot be fixed in isolation, rather they are driven by the distribution of game states created earlier in the simulation.

This shifted the focus from "fixing solo logic" to "improving the entire system's state evolution."

### Position of V2 in the Project
V2 establishes the foundation for:
- richer answer modeling
- deeper inference systems
- more realistic player behavior

It transforms the simulation from a rule-based model into a dynamic system capable of producing emergent gameplay patterns.

### Looking Ahead
Future versions (V3+) will focus on:
- structured answer objects (real players, stats, metadata)
- improved category modeling
- deeper inference (cuttoff estimation, opponent modeling)
- multi-turn planning and strategy

### Final Assessment

V2 is considered **complete and successful**:
- It achieves its core goals
- Introduces meaningful system complexity
- Remains interpretable and extensible

Remaing issues are no longer blockers, but **natural next steps for futher iteration.**