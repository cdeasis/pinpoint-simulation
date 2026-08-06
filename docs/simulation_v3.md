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

### Phsae 4 (Finalization):
6. Milestone 6 - Foul Off Rule and Final Validation

This implements the real game's new two strike foul off rule and validates the final V3 system before the V4 refactor.

---

## Roadmap Update: Foul Off Rule

During M5 development, the real game introduced a new two strike "foul off" rule:

> If a contestant is at 2 strikes and guesses an answer ranked 101-110, the guess earns 0 points but does not produce a strike. The contestant remains alive on two strikes.

This rule immediately affected gameplay and has since continued to be used in later episodes. Becaus ethe rule changes the structure of two strike survival, near cutoff misses, and late game strategy, it is treated as a fundamental game change rather than a small player identity tuning parameter.

Run 5 will remain the final old rule M5 pass. Its purpose is to preserve the best version of the original V3 player identity model before the rule change.

Milestone 6 will now focus on implementing the foul-off rule and validiating that the simulator remains stable afterward. Any larger strategic extensions that were originally considered for late M5 or M6, such as richer two-strike scoring diagnostics, eliminated-score targeting, victory-lap realism, or deeper calibration/exclusion category behavior, will be documented as future work and reserved for V5 or later.

V4 will remain a structural refactor only.

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
- Players not track board shape around the cutoff, not just the cutoff itself
- Added local density and surprise/volatility signals:
    - `local_density_read`
    - `surprise_read`
    - `near_cutoff_hits`
    - `near_cutoff_misses`
- Board interpretation now distinguishes between:
    - dense vs sparse boards
    - generous vs harsh outcomes
    - cutoff estimate vs board forgiveness
- M3 remained merely diagnostic and foundational, setting up M4 stategy behavior
- Main limitation: the abstract answer model still produces very few near-cutoff misses, limiting full precision realism

### At the end of M4
- Players now use board context, score position, strike state, and double-window rhythm to adjust risk
- `open` was decomposed into:
    - `dense`: board appears attackable
    - `generous`: board appears forgiving or surprising
- Dense boards became the primary aggression signal
- Generous boards became a softer looseness signal
- Tight boards now more reliably suppress risky behavior
- Double-window behavior now respects board context instead of using broad openness alone
- M4 is considered complete after Run 7

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
**Status**: Completed

#### Purpose
To model how answers are distributed around the cutoff, not just where the cutoff is

#### Core Changes
Players should infer:
- density: how many viable answers exist near the cutoff
- spacing: whether answers are clustered or sparse 
- consistency: whether similar guesses behave similarly

New Concepts to Introduce:

1. Local Density Signal
    - track recent near-cutoff hits and misses
    - compare observed hit rate against an expected hit-rate baseline
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
- Added first lightweight model of board game
- Players no longer only track "where is the line?", they now also begin tracking:
    - "does the area around the line feel dense or sparse?"
    - "are outcomes matching expectatioons?"
    - "does the boaord feel forgiving or precise?"

M3 preserves the stable cutoff behavior from M2 while adding diagnostic signals for local density and surprise.

The main outcome is not a major gameplay shift yet. Instead, M3 creates interpretable board-shape signals that can be used by later strategy systems, especially M4.

#### Notes
M3 was successful as a lightweight inference layer, but not as a full board-shape engine.

The final tuning stabilized local density and surprise readings without disrupting the M2 cutoff system. However, the current abstract answer model still produces very few near-cutoff misses, which limits how much the system can infer about true board tightness.

This suggests that deeper board-shape realism will likely require future structural changes, such as:
- richer category modeling
- better candidate-generation behavior
- hidden board-shape parameters
- eventual real-data integration

For V3, M3 is considered complete enough to support M4, where the next step is to let strategy respond to board-shape signals.

### Milestone 4 - Contextual Risk and Strategy & Multi-Turn Planning
**Status**: Completed

#### Purpose
To make player decisions respond to game context, not just the current best available guess.

M4 builds on the board-shape signals introduced in M3 and asks whether players can behave more like real contestants by adjusting risk based on:
- board context
- score position
- strike count
- double-window rhythm
- uncertainty around the cutoff

#### Core Changes
1. **Board-context helper**

A new context layer converts numeric inference signals into strategic labels:
- `open`: broad playable-board signal
- `dense`: many viable answers appear to exist near the cutoff
- `generous`: the board appears forgiving or surprising
- `tight`: the board appears punishing or precision-heavy
- `uncertain`: the player is still unsure where the cutoff is

2. **Context-aware pressure**

Normal safe/risky decisions now adjust based on board context:
- dense boards increase aggression
- generous boards give a smaller confidence boost
- tight and uncertain boards suppress risk
- strike danger further increases caution

3. **Score-aware strategy**

Players now adjust risk based on score position:
- large leads encourage safer play
- large deficits allow more aggression
- score context interacts with strike state and board read

4. **Double-window strategy**

End-of-snake players now use a more contextual double-window rhythm:
- meaningful leads are protected
- strike danger suppresses risky alternation
- dense boards allow risky/safe rhythm
- generous boards only allow rhythm when the board is not tight

5. **Diagnostic visibility**

M4 added mode and context metrics, including:
- safe/risky/blind-risk rates
- double-window safe/risky rates
- open/tight/uncertain context rates
- dense/generous context rates
- context-action rates such as `risky_on_dense`, `safe_on_tight`, and `risky_on_double_window`


#### Key Outcome
M4 successfully introduced contextual strategy without destabilizing the simulator.

The final M4 behavior distinguishes between several types of board states:
- `dense` boards are attackable and support aggression
- `generous` boards are forgiving, but not necessarily aggressive
- `tight` boards push players toward survival
- `open` remains a broad descriptive label rather than a single aggression trigger

This produces more interpretable category-sensitive behavior. HR-style categories remain more aggressive, while bWAR/MVP-style categories remain more conservative. Double-window behavior also becomes more realistic because risky/safe rhythm now depends on whether the board actually supports that rhythm.

#### Notes
M4 was completed after several diagnostic and tuning runs.

The largest design insight was that `open` was too broad as a single strategy signal. Decomposing it into `dense` and `generous` made the system easier to interpret and allowed aggression to be tied more directly to density.

Remaining limitations are better suited for later milestones:
- player-profile calibration
- defensive survival strategy
- sharper cutoff discovery after near-line guesses
- richer category modeling

### Milestone 5 - Human Bias and Player Identity
**Status**: Completed

#### Purpose

To introduce lightweight player identity into the simulator without turing the model into a full human behavior engine.

M1-M4 focusd on broad interpretation and contextual strategy. M5 shifted the focus toward the contestants themselves: what kinds of categories they are comfortable with, what kinds of answers they trust, how they behave under pressure, and how their decision making changes by strike state.

The goal was not to make each contestant perfectly realisitic. Instead, M5 aimed to make player differences more visible, interpretable, and measurable while preserving the stability of the existing V3 system.

#### Core Changes

1. **Player Identity Fields**

M5 added new profile level fields that allow contestants to differ beyond raw knowledge and baseline risk style:

- `comfort_bias`
- `archetype_bias`
- `category_confidence`
- `familiarity_bias`
- `defensive_survival_bias`
- `safe_fallback_bias`
- `reaction_influence`
- `board_read_trust`
- `pressure_composure`
- `risk_identity`
- `two_strike_composure`

Not every field became behaviorally central during M5. Some fields remain structural placeholders for future versions, but the milestone established the broader identity framework.

2. **Category Confidence and Familiarity**

M5 made category tags more meaningful by allowing them to influence answer-state formation.

Players can now be more or less comfortable with category types such as:

- modern categories
- all-time categories
- WAR / advanced-stat categories
- awards categories
- counting-stat categories
- recent-player categories

These modifiers affect not only whether a player knows an answer, but also whether they recall it and trust it enough to guess.

3. **Answer Archetype Bias**

M5 added lightweight answer archetype behavior based on point-value bands.

Answers can function as broad archetypes such as:

- safe / low-value answers
- regular / mid-value answers
- star / high-value answers
- deep-cut / extreme high-value answers

This allows players to differ in what kinds of answers they tend to access and trust, even within the same category.

4. **Improved Diagnostic Visibility**

M5 added several diagnostic views that make player behavior easier to explain:

- answer-state summaries
- safe / risky / blind candidate counts
- per-player mode rates
- per-player mode hit rates
- average guess values by mode
- early-guess profiles
- strike-state mode rates
- strike-state hit rates
- two-strike survival summaries

These diagnostics became one of the most important parts of the milestone because they showed whether a player was losing due to knowledge, confidence, selection behavior, or strike-state strategy.

5. **Category Suite Expansion and Profile Refinement**

M5 expanded the validation suite so that player identity could be tested across more category shapes.

The milestone also refined C2’s WAR profile. The earlier broad WAR penalty was too blunt and made C2 nearly non-competitive in bWAR categories. Replacing it with more specific WAR subtype modifiers created a healthier distinction between hitter WAR, pitcher WAR, and all-time WAR behavior.

6. **Two-Strike Composure and C3 Identity**

The largest behavioral focus of M5 became two-strike identity.

Strike-state diagnostics showed that the simulator’s two-strike behavior was inverted from observed real-game behavior. C2 was surviving extremely well on two strikes, while C3 was collapsing. This happened because C3 was being forced into generic safe behavior at two strikes, despite having a weaker safe pool.

M5 added `two_strike_composure` so that composed two-strike players, especially C3, could take calculated survival risks instead of always defaulting to safe play.

Later runs refined this further through survival-risk selection. Instead of taking maximum-upside risky guesses at two strikes, C3 could select from a more playable risky pool near the estimated board line.

#### Key Outcome
M5 successfully added player identity without destabilizing the simulator.

The final M5 state allows contestants to differ in:

- category comfort
- answer familiarity
- confidence and trust
- safe/risky candidate pools
- early-game volatility
- strike-state behavior
- two-strike composure

The milestone also clarified that player realism cannot be represented only through global knowledge levels. A player may know an answer, fail to recall it, recall it but not trust it, or trust it only in certain category contexts. The M5 answer-state system gives the simulator a way to represent those differences while remaining interpretable.

Run 5.4 was selected as the final M5 state. It preserved the old-rule model while refining C3’s two-strike survival-risk behavior. The improvement was modest, but targeted: C3’s two-strike risky guesses became better selected, while C1 and C2 remained stable.

M5 does not fully solve every observed player behavior. Larger systems such as eliminated-score targeting, victory-lap realism, deeper calibration/exclusion behavior, table-reaction modeling, and foul-off-aware strategy are deferred to future versions.

#### Notes
M5 is considered complete after Run 5.4.

The final M5 model should be understood as the best old-rule version of the V3 player-identity system. During M5 development, the real game introduced and retained the new two-strike foul-off rule. Because that rule changes the game’s fundamental two-strike outcome structure, it is not treated as a late M5 player-identity tweak.

Instead, M6 will implement the foul-off rule as the final major V3 gameplay addition and validate that the simulator remains stable afterward.

### Milestone 6 - Calibration and Validation Pass
**Status**: Not complete

#### Purpose

To implement the real game’s new two-strike foul-off rule and validate the final V3 system after that rule change.

Originally, M6 was intended to be a pure calibration pass. However, during M5 development, the real game introduced and retained a new foul-off rule for near-miss guesses at two strikes. Because this rule directly affects two-strike survival, sudden-death behavior, and near-cutoff misses, it is now treated as the final major V3 gameplay addition.

M6 should remain narrow. Its purpose is not to add a large new strategic layer, but to add the foul-off rule, verify that existing M5 behavior remains stable, and document the final V3 state before V4.

#### Core Changes

1. **Foul-Off Rule Implementation**

Implement the new two-strike foul-off rule:

- If a contestant begins a turn on two strikes and makes a near-board miss in the 101-110 range, the guess earns 0 points but does not produce a strike.
- The contestant remains alive on two strikes.
- The foul-off consumes the contestant’s turn.

This creates a third two-strike outcome:

- correct answer: points + survive
- foul off: 0 points + survive
- normal miss: strikeout / elimination

This rule should apply globally rather than as a C3-specific bonus. Player identity should influence how often each contestant produces near-line guesses, but the rule itself is part of the game structure.

2. **Post-Rule Stability Check**

Compare M6 behavior against the final Run 5.4 old-rule state.

Important questions:

- Does two-strike survival increase for structural reasons?
- Does C3 benefit from near-line survivability without becoming artificially overpowered?
- Do C1 and C2 remain stable?
- Does sudden-death behavior become longer or more forgiving in a believable way?
- Does the rule create obvious distortions in win rate, first-out rate, or average score?

3. **Validation Suite Rerun**

Rerun the full category validation suite after implementing the foul-off rule.

Track the same major metrics used throughout V3:

- win rates
- average scores
- score variance
- strike distribution
- first-elimination rates
- last-survivor-but-lost rate
- solo started behind rate
- solo started behind and lost rate
- average solo deficit
- cutoff estimate / uncertainty
- density / generosity / tightness signals
- mode and context-action rates
- strike-state behavior
- two-strike survival behavior

4. **Final Regression Check**

Compare the final M6 state against earlier V3 baselines.

Useful comparison points:

- final M2 state
- final M3 state
- final M4 state
- final M5 state
- final M6 / final V3 state

The goal is to show what V3 gained over time without hiding tradeoffs.

5. **Document Future Work**

Any larger behavioral systems that remain incomplete should be documented as future work rather than added to V3.

Future work may include:

- eliminated-score targeting
- victory-lap realism
- deeper calibration/exclusion category behavior
- foul-off-aware strategy
- table-reaction modeling
- richer category modeling
- cleaner answer/rank representation
- real-data integration

These are better suited for V5 or later, after V4 refactors the codebase.

#### Key Outcome

M6 should produce the final stable V3 baseline.

The final V3 system should be:

- more realistic than V2
- more interpretable than earlier V3 milestones
- stable across multiple category types
- capable of explaining why players choose safe, risky, or survival-oriented strategies
- capable of modeling the real game’s current two-strike foul-off rule
- balanced enough that player outcomes remain believable

M6 should end with a clear final V3 state that can be preserved before moving into V4.

#### Notes
M6 is both a rule-implementation milestone and a final validation milestone.

The foul-off rule is the only major new gameplay addition planned for M6. Any issues discovered after implementation should be handled conservatively. Small tuning changes are acceptable if they are necessary to preserve stability, but larger strategic rewrites should be documented as future work.

The goal is to finish V3 cleanly, not to keep extending it indefinitely. V4 will focus on restructuring the codebase, while larger new features and deeper behavioral systems will be reserved for V5 or later.

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

**note**: next two sections can be expanded when m3+ are finished, everything above is good for M1 and M2.
#### Behavioral Impact

As a result of M1 + M2:
- players transition from static risk profiles (V2) to belief-driven behavior

Decisions also now depend on estimated cutoff, uncertainty level, and board interpretion signals.

#### Design Philosophy

V3 prioritizes interpretability over complexity and stability over perfect realism.

Inference is heuristic-based, intentionally lightweight, and designed to be extended in later milestones (M3+)

### Precision and Category Shape Modeling (M3)

M3 adds a lightweight model of board shape around the cutoff. M2 asks
> "Where is the line?"

while M3 beginas asking
> "What does the area around the line feel like?"

#### Local Density Tracking

Players track whether recent near-cutoff guesses suggest a dense or sparce board.

New states values include:
- `local_density_read`
- `near_cutoff_hits`
- `near_cutoff_misses`

When enough near-cutoff events occur, the simulator compares the observed hit rate against an expected baseline. 
- If near-cutoff guesses are making the board more often than expected, the board begins to feel denser
- If near-cutoff guesses miss, the board begins to feel tighter or more sparse

#### Surprise / Volatility Tracking

M3 also tracks whether outcomes contradict player expectations with `surprise_read`. Examples include:
- a low-value answer making the board increases the sense that the board is generous
- a high-value miss suggests the board may be harsh or precision-heavy

This allows the model to separate cutoff knowledge froom board forgivness. A player can be confident about the cutoff while still thinking the board is tight, or uncertain about the cutoff while sensing that the board is forgiving.

#### Near-Cutoff Event Tracking

M3 introduces a near-cutoff band around the player's current estimate. Guesses near this band become more informative than distant events.

This supports future strategic decisions by producing interpretable board-shape signals:
- dense vs sparse 
- generous vs harsh
- predictable vs surprising

#### Behavioral Impacat

M3 does not dramatically rewrite player behavior by itself. Its main purpose is to create board-shape signals that later strategy systems can use.

The final M3 state preserved the stability of M2 while adding the foundation for M4's contextual strategy layer.

### Contextual Strategy Planning (M4)

M4 connects the inference signals from M1-M3 to player decision-making.

The main addition is a board-context helper:

```
def get_board_context(state):
    ...
```

This converts raw inference values into strategic labels such as:
- dense
- generous
- open
- tight
- uncertain

#### Dense, Generous, and Open

M4 originally treated `open` as one broad signal. Later diagnostic runs showed that open was actually composite, so it was split into:
- `dense = state.local_density>read >= threshold`
- `generous = state.surprise_read >= threshold`
- `open = dense or generous`

This distinction became important because density and generosity imply different behavior:
- `dense` means the board appears attackable
- `generous` means the board appears forgiving or surprising
- `open` remains a broad descriptive label

The final M4 strategy uses density as the stronger aggression signal and generosity as a softer confidence signal.

#### Context-Aware Pressure

Normal mode selection now adjusts pressure based on board context:

```
if ctx["dense"] and player_state.strikes == 0:
    pressure += ...
elif ctx["generous"] and player_state.strikes == 0:
    pressure += ...
```

Risky is also reduced when:
- the board is tight
- cutoff uncertainty is high
- the player already has strikes
- the player is protecting a meaningful lead

This creates more realistic decision-making than static safe/risky tenderness.

#### Score and Strike Awareness

M4 adds lightweight score-position logic:
- players with large leads become more conservative
- players trailing by large margins may allow more risk
- strike danger suppresses risky behavior

This does not make players fully optimal, but it gives them basic strategic awareness.

#### Double-Window Logic

End-of-snake players receive special handling because they often act in back-to-back turns.

The final M4 double-window logic allows risky/safe rhythm when:
- the player has no strikes
- the board is dense, or
- the board is generous and not tight

This preserves human-like behavior while preventing tight boards from being treated as freely attackable

#### Diagnostics

M4 also adds metrics to make strategy behavior inspectable:
- mode rates
- double-window mode rates
- context rates
- context-action rates

These diagnostics were essential for identifying that `open` was too broad and for validating the final dense/generous/tight behavior.

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