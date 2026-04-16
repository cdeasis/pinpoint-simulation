# Simulation Engine - Version 3 (V3)

## Overview
The main purpose of V3 is to extend upon V2's rudimentary introduction of board inference. It addresses the question of:
> "Can we model how contestants interpret and adapt to the board in real time, rather than just react to internal knowledge?"

---

## Goals
The main goal of V3 is to transform inference from a simple directional signal into a strucutred, multi-dimensional system that drives player decision making. 

This can be achieved by introducing several new capabilities:

### 1. Understanding what the board looks like
Players should form an internal representation of what the board looks like, including:
- how deep the board feels (number of viable answers)
- how forgiving or punishing the board is
- how tightly packed anwers are near the cutoff

This allows the simulation to distinguish between categoreies that are:
- broad but forgiving
- broad but precision heavy
- narrow and restrictive

### 2. Estimating where the cutoff is
Players should estimate the approximate threshold required to make the board.

This estimate should
- update dynamically based on revealed answers
- adjust after surprising hits or misses
- include some level of uncertainty

This models real contestant thinking, such as "1000 might be the line" or "actually that might not be safe anymore".

#### 3. Adapting risk based on evolving informatioin
Player decisions should adapt based on:
- current board understanding
- strike count
- score position
- remaining board size

Risk is no longer static, but evovles throughout the game.

### 4. Behaving like a human under uncertainty and pressure
Players should behave less like optimal agents but more liek real contestants by:
- showing hesitation under pressure
- favoring familiar or "comfortable" answers
- reacting to percieved board difficulty
- adjusting behavior based on game flow

This introduces realisitic inefficiencies and variability.

---

## Design Evolution
As with V2, the systems introduced in V3 are developed incrementally to preserve stability, interpretability, and debuggability.

Rather than introducing a fully complex inference system at once, V3 is broken into sequential phases:

### Phase 1 (Core System):
1. Milestone 1 - Multi-dimensional inference
2. Milestone 2 - Cutoff Estimation

These systems form the foundation for all higher-level behavior.

### Phase 2 (behavior realism):
3. Milestone 3 - Precision Modeling
4. Milestone 4 - Contextual strategy

These improve how players respond to different board types and game states.

### Phase 3 (Human realism):
5. Milestone 5 - Bias + identity

This introduces human tendencies and non-optimal behavior patterns.

### Phsae 4 (finalization):
6. Milestone 6 - Calibration

This ensures that the system remains stable, balanced, and introduces interpretable results across categories.

---

## Milestones and Core Components
V3 is developed through a series of incremental milestones, each targeting a specific limitation of the V2 inference system while maintaining overall system stability.

The primary focus of these milestones is to evolve board inference from a simple directional signal into a structured system that influences decision-making at every stage of the game.

Each milestone introduces new components while building on previous ones, ensuring that behavior remains interpretable and testable throughout development.

### Milestone 1 - Multi-Dimensional Board Inference (Foundation)
**Status**: Not complete

#### Purpose
To replace the single `board_read` with a richer internal model of the board

#### Core Changes
Replace `board_read` with multiple components:
- `depth_read`: percieved board depth
- `precision_read`: how tight or forgiving the board is
- `cutoff_estimate`: approximate threshold to make the board
- `cutoff_uncertainty`: confidence in the estimate

Expand board updates to incorporate:
- value of revealed answers
- frequency of strikes
- density of safe guesses

#### Key Outcome
[note: this can be subject to change depending on what actually happens]
- Players no longer evaluate the board as simply “easy” or “hard”
- Instead, they form a structured understanding of:
    - how many answers exist
    - how risky those answers are
    - how accurate they must be

#### Notes
- This milestone prioritizes structure over accuracy
- Initial implementations can be heuristic-based and approximate
- This serves as the foundation for all subsequent milestones

### Milestone 2 - Cutoff Estimation System
**Status**: Not complete

#### Purpose
To allow players to estimate the minimum threshold required to make the board, and update that estimate dynamically.

#### Core Changes
Introduce heuristic-based cutoff estimation:
- infer cutoff based on revealed answers and their ranks
- adjust estimate after:
    - high-value answers appearing lower than expected
    - low-value answers making the board
    - misses guesses

Track uncertainty in the estimate:
- early game: high uncertainty
- late game: more confidence

Integrate cutoff intro decision making:
- safe guesses must exceed estimated cutoff (with margin)
- risky guesses may fall below it

#### Key Outcome
[note: this can be subject to change depending on what actually happens]
Players begin to reason about the board explictly:
- "this should be safe"
- "this might not make it"

Reduces unrealistic misses and improves decision quality

#### Notes
[note: this can be subject to change depending on what actually happens]
- This should remain lightweight and heuristic-based in V3
- Full probabilistic modeling is reserved for future versions

### Milestone 3 - Precision and Category Shape Modeling
**Status**: Not complete

#### Purpose
model how forgiving the board is, not just how many answers exist

#### Core Changes
[nothing to put here yet]

#### Key Outcome
[nothing to put here yet]

#### Notes
[nothing to put here yet]

### Milestone 4 - Contextual Risk and Strategy
**Status**: Not complete

#### Purpose
make decisions depend on:
- turn postion (wrap-around)
- strike count
- score state
- board state (from M1-M3)

Additions:
1. wrap-around logic upgrade
    - instead of simple alternating:
        - evaluate 2 turn survival strategy
        - allow:
            - double-safe
            - safe + risky combo
            - desperation pair
2. score-state awareness expansion
    - refine as this already exists
        - players 'give up and have fun'
        - players press when behind
        - players protect lead more intelligently
3. strike psychology
    - enhance:
        - stricter filtering at 2 strikes
        - increased hesitation
        - reduced blind risk

#### Core Changes
[nothing to put here yet]

#### Key Outcome
[nothing to put here yet]

#### Notes
[nothing to put here yet]

### Milestone 5 - Human Bias and Player Identity
**Status**: Not complete

#### Purpose
introduce 'non-optimal but human' behavior

Additions:
1. comfort picks
    - favorite players
    - repeat names
    - 'this guy is always on the list'
2. archetype reasoning
    - 'obp guy'
    - 'played forever'
    - 'they had to walk him'
3. team bias
    - favorite team influence
    - known strengths / weaknesses
4. reaction trust
    - track which players give reliable reactions
    - update trust dynamically

#### Core Changes
[nothing to put here yet]

#### Key Outcome
[nothing to put here yet]

#### Notes
[nothing to put here yet]

### Milestone 6 - Calibration and Validation Pass
**Status**: Not complete

#### Purpose
stabilize system after all new complexity

- rerun validation suite
- tune
    - win rates (bring c1/c2 closer, boost c3 slightly)
    - solo metrics
    - variacne

focus metrics:
- solo started behind but lost rate
- average deficit
- strike distribution
- score variance

#### Core Changes
[nothing to put here yet]

#### Key Outcome
[nothing to put here yet]

#### Notes
[nothing to put here yet]

---

## Implementation Details
[nothing to put here yet, but more in depth technical explaination of what changed and how, with examples]

---

## Results
[nothing to put here yet]

### Raw Results
[make reference to `docs/supplements/v3_raw_results.md` which will most likely have to be made as well]

---

## Limitations 
[nothing to put here yet]

---

## Conclusions
[nothing to put here yet]

---