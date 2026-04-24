# Simulation Engine - Version 3 (V3)

## Overview
The main purpose of V3 is to extend upon V2's rudimentary introduction of board inference. It addresses the question of:
> "Can we model how contestants interpret and adapt to the board in real time, rather than just react to internal knowledge?"

This version focuses on the modeling belief formation about the board, rather than just outcome-driven behavior.

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

## V3 Current State Summary

### At the end of M1
- Board understanding decomposed into:
    - `depth_read`, `precision_read`
    - `cutoff_estimate`, `cutoff_uncertainty`
- Replaces singular scalar `board_read` with multi-signal model
- Signals are directional and coarse (not fully realisitic yet)

### At the end of M2
- Players estimate and update cutoff dynamically
- Uncertainty evolves (high &rarr; partial convergence)
- Safe / risky behavior now tied to cutoff + margin
- Category-dependent behavior emerges
- Solo dynamics improved

#### Limitations
- Board perception still skewed toward harsh outcomes
- No modeling of anser density / culstering
- No "board phase" behavior (cold &rarr; heating up)

### At the end of M3
- fill this part out later

---

## Milestones and Core Components
V3 is developed through a series of incremental milestones, each targeting a specific limitation of the V2 inference system while maintaining overall system stability.

The primary focus of these milestones is to evolve board inference from a simple directional signal into a structured system that influences decision-making at every stage of the game.

Each milestone introduces new components while building on previous ones, ensuring that behavior remains interpretable and testable throughout development.

### Milestone 1 - Multi-Dimensional Board Inference (Foundation)
**Status**: Completed

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
- Players now maintain a structured internal model of the board using multiple signals instead of a singular scalar
- Board depth understanding is decomposed into:
    - depth (how many answers exist)
    - precision (how tight the board is)
    - cutoff estimate (where the line is)
    - cutoff uncertainty (confidence in that estimate)

This enables downstream systems (M2+) to operate on interpretable board beliefs rather than raw outcomes.

#### Notes
- The singals introduced in M1 are intentionally coarse and directional
- They provide strucutre, not full behavioral realism

### Milestone 2 - Cutoff Estimation System
**Status**: Completed

#### Purpose
To allow players to estimate the minimum threshold required to make the board, and update that estimate dynamically.

#### Core Changes
Introduce heuristic-based cutoff estimation:
- infer cutoff based on revealed answers and their ranks
- adjust estimate after:
    - high-value answers appearing lower than expected
    - low-value answers making the board
    - misses guesses
- selective update logic:
    - only near-cutoff answers meaningfully adjsut estimates
    - misses near the cutoff have stronger impact than distant misses

Track uncertainty in the estimate:
- early game: high uncertainty
- late game: more confidence

Integrate cutoff intro decision making:
- safe guesses must exceed estimated cutoff (with margin)
- risky guesses may fall below it

#### Key Outcome
- Players now explicitly estimate a cutoff threshold and adjust it dynamically based on revealed answers and misses
- Uncertainty evolves over time:
    - early game: high uncertainty
    - mid/late game: partial convergence
- Decision-making now meaningfully depends on:
    - estimated cutoff
    - uncertainty-adjusted safety margin

This produces realistic safe vs risky behavior, improved solo dynamics, and category-dependent play patterns

#### Notes
- Cutoff estimation stabilizes within a realistic range (~50-65), and safe-floor behavior aligns with expected gameplay
- **Limitation**: The model captures where the line is, but not yet how easy it is to play around that line

### Milestone 3 - Precision and Category Shape Modeling
**Status**: In Progress

#### Purpose
To model how answers are distributed around the cutoff, not just where the cutoff is

#### Core Changes
Players should infer:
- density: how many viable answers exist near the cutoff
- spacing: whether answers are clustered or sparse 
- consistency: whether similar guesses behave similarly

New Concepts to Introduce:

1. Local Density Signal
    - track how many recent correct answers fall within a brand (e.g. +/- 15 of cutoff)
    - high density &rarr; "board feels open"
    - low density &rarr; "board feels tight"

2. Volatility / Surprise Tracking
    - track how often outcomes contradict expectations
        - low is surprisingly safe &rarr; board is generous
        - high value misses &rarr; board is harsh

3. Precision Calibration
    - Instead of `precision_read += 0.02`, use:
        - repeated near-cutoff misses &rarr; high precision requirement
        - repeated near-cutoff hits &rarr; low precision requirement

4. Cutoff Confidence $\neq$ Board Forgiveness
    - V3 currently has uncertainty and precision loosely tied, however it is possible to be:
        - confident in cutoff BUT board is tight
        - uncertain BUT board is forgiving

#### Key Outcome
[high level for now, edit once finished]
- players no longer ask 'what is the line', they instead start asking 'how hard is it to land near the line?'

This is the missing realism layer

#### Notes
[nothing to put here yet]

### Milestone 4 - Contextual Risk and Strategy & Multi-Turn Planning
**Status**: Not complete

#### Purpose
To make decisions depend on future survival, not just current turn

#### Core Changes
1. 2-turn planning (wrap-around awareness)
    - evaluate survival across next two picks, instead of pick mode per turn
2. Combo Logic
    - allow for different 2-turn states:
        - safe + safe (protect)
        - safe + risky (balanced)
        - risky + risky (desperation)
3. Board-Aware Aggression:
    - aggressive only when
        - density is high (from M3)
    - conservative when;
        - precision is high
4. Strike-state psychology (upgrade)
    - not only just "2 strikes = safe" but also:
        - "2 strikes + tight board = ultra conservative"
        - "2 strikes + forgiving board = still take calculated risk"

#### Key Outcome
[high level for now, edit once finished]
players start behaving like:
- "i need to survive THIS turn AND set up the next one"

instead of:
- "what is the best guess right now?"

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

### Multi Signal Board Representation (M1)
[small note here: not sure if i want to rewrite the set of inference signals again as i already did so under the core changes in m1 description earlier, maybe find a way to reword this:]

V3 replaces the single `board_read` scalar with a structured set of inference signals:
- `depth_read`: perceived number of viable answers
- `precision_read`: perceived tightness near cutoff
- `cutoff_estimate`: estimated threshold required to make the board
- `cutoff_uncertainty`: confidence in the estimate

These signals are updated independently and combined when needed for decision-making

The key difference from V2 is that V2 used a signal directional signal, whereas V3 introduces separable dimensions of board understanding.

#### Board Signal Composition

A helper function (`get_board_signal`) combines inference signals:

`board_signal = 0.6 * depth_read - 0.4 * precision_read`

This allows dsepth and precision to act as opposing forces, and more stable and interpretable board perception.

### Cutoff Estimation System (M2)

Players maintain a dynamic estimate of the board cutoff using `state.cutoff_estimate` and `state.cutoff_uncertainty`.

#### Update Rules

Cutoff updates are event-driven, based on guess outcomes:
- Correct answers near cutoff
    - pull estimate toward revealed value
    - reduce uncertainty
- Misses near cutoff
    - push estimate upward
    - slightly reduce uncertainty
- Distant events
    - have reduced or no impact

Updates are weighted, not absolute:

`state.cutoff_estimate = (1 - weight) * old + weight * new`

#### Selective Update Logic

Not all events affect the cutoff equally:
- Only answers within a band (e.g. `cutoff_estimate - 30`) influence updates
- Near-boundary answers have stronger affects

This prevents runaway drift and ovveraction to irrelevant data.

#### Uncertainty Modeling

`cutoff_uncertainty` tracks confidence in the estimate:
- Starts high early game
- Decays gradually as informative events occur
- Decays faster on both near-cutoff hits and misses

Uncertainty directly affects decision-making.

#### Integration into Decision Logic

Cutoff estimate influences guess selection via a safety margin:

```
margin = 10 + 6 * cutoff_uncertainty
safe_floor = cutoff_estimate - margin
```

- high uncertainty &rarr; wider margin (more cautious)
- low uncertainty &rarr; tighter margin (more precise play)

This directly controls safe vs risky classification and candidate filtering.

**note**: next two sections can be expanded when m3+ are finished, everything above is good for m1 and m2.
#### Behavioral Impact

As a result of M1 + M2:
- players transition from static risk profiles (V2) to belief-driven behavior

Decisions also now depend on estimated cutoff, uncertainty level, and board interpretion signals.

#### Design Philosophy

V3 prioritizes interpretability over complexity and stability over perfect realism.

Inference is heuristic-based, intentionally lightweight, and designed to be extended in later milestones (M3+)

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