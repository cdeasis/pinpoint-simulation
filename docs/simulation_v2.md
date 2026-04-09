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

## Milestones and Core Components Implementation 

[high level purpose of each milestone, status, what each one was intended to achieve]

### Milestone 1 - Non-Binary Knowledge System
**Status:** Completed

This milestone introduces a new logic system for what a guess is, thus moving off V1's binary knowledge system.

(rewrite this part later)
Changes include:
- `Set[int]` in V1 to `Dict[int, AnswerState]`
- new `AnswerState` dataclass
- [add other changes here]

[concluding statement goes here, also something about how there's a lot of bridges and such, and majority of the tests and results were to see if the engine still runs after implementing new knowledge system, the numbers themselves didn't matter]

### Milestone 2 - Probabilistic Guess Generation
**Status:** Completed

This milestone introduces [fill this out later, here the values actually start to matter again, but not entirely]

Results from best run midway (find a way to reword this):
```
=== Summary ===
Contestant 1: win_rate=0.613, avg_score=1669.7, median_score=1463.5, stdev=990.4, avg_strikes=3.00, first_out_rate=0.162
Contestant 2: win_rate=0.211, avg_score=1057.0, median_score=838.0, stdev=771.9, avg_strikes=3.00, first_out_rate=0.426
Contestant 3: win_rate=0.176, avg_score=940.1, median_score=823.0, stdev=561.0, avg_strikes=3.00, first_out_rate=0.412
Last survivor but lost rate: 0.127
Solo started behind rate: 0.273
Solo started behind and lost rate: 0.464
```

At this point, the win rates are the closest to the final result of V1, however ongoing issues remain including:
- `Solo started but behind rate` is still high at ~46%, but significant improvement from V1
- Win rates are a bit spread for contestant 1 and 2
- Standard deviation (probably biggest issue) is too high

Best overall run (concludes milestone 2, find better way to reword this):
```
=== Summary ===
Contestant 1: win_rate=0.726, avg_score=1844.8, median_score=1859.0, stdev=235.4, avg_strikes=2.54, first_out_rate=0.071
Contestant 2: win_rate=0.163, avg_score=1581.6, median_score=1605.0, stdev=192.7, avg_strikes=2.80, first_out_rate=0.213
Contestant 3: win_rate=0.111, avg_score=1454.3, median_score=1450.0, stdev=217.1, avg_strikes=2.81, first_out_rate=0.667
Last survivor but lost rate: 0.289
Solo started behind rate: 0.315
Solo started behind and lost rate: 0.918
```

[conclusions, tidy this part later]
- stdev is much better
- solo started behind but lost rate balloned (almost impossible now)
- win rates elevated, gap wider between contestants 1 and 2
- not concerned about solo started behind but lost, haven't addressed that fully yet

### Milestone 3 - Solo / Endgame Rework
[this is the most important one, or at least the major one, used to address the solo win rate issue, now just under the new knowledge system logic]

**Status:** In progress

[get to this after]

### Milestone 4 - Board Inference
**Status:** Not Complete

[fill this out later]

---

## Implementation Details
[go into the specifiics of how things are implemented, specific elements, etc.]
ex:
- `AnswerState`
- guess generation
- guess resolution
- mode selection
- solo logic
- inference logic
- things like noise etc, variance, etc.

---

## Validation Strategy
To avoid overfitting to a single category, V2 introduces a multi-category validation suite. This includes:
- varying category difficulty
- category-specific modifiers
- cross-simulation comparison

The purpose of this was to ensure generalization, validate behavioral consistency and to detect tuning bias.

results for now (just place them here):

```

=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.722, avg_score=1842.2, median_score=1852.0, stdev=234.6, avg_strikes=2.53, first_out_rate=0.073
Contestant 2: win_rate=0.168, avg_score=1583.0, median_score=1607.0, stdev=192.2, avg_strikes=2.80, first_out_rate=0.210
Contestant 3: win_rate=0.110, avg_score=1454.6, median_score=1450.0, stdev=217.3, avg_strikes=2.81, first_out_rate=0.667
Last survivor but lost rate: 0.295
Solo started behind rate: 0.320
Solo started behind and lost rate: 0.922

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.795, avg_score=1850.1, median_score=1916.0, stdev=457.5, avg_strikes=3.00, first_out_rate=0.003
Contestant 2: win_rate=0.093, avg_score=1180.6, median_score=1176.0, stdev=176.9, avg_strikes=3.00, first_out_rate=0.579
Contestant 3: win_rate=0.113, avg_score=1167.1, median_score=1142.0, stdev=230.8, avg_strikes=3.00, first_out_rate=0.419
Last survivor but lost rate: 0.208
Solo started behind rate: 0.348
Solo started behind and lost rate: 0.599

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.681, avg_score=1819.3, median_score=1766.0, stdev=159.9, avg_strikes=0.34, first_out_rate=0.000
Contestant 2: win_rate=0.274, avg_score=1622.0, median_score=1677.0, stdev=137.3, avg_strikes=1.63, first_out_rate=0.112
Contestant 3: win_rate=0.046, avg_score=1608.7, median_score=1652.0, stdev=166.9, avg_strikes=0.75, first_out_rate=0.157
Last survivor but lost rate: 0.001
Solo started behind rate: 0.001
Solo started behind and lost rate: 0.800

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.744, avg_score=1857.9, median_score=1845.0, stdev=203.9, avg_strikes=1.06, first_out_rate=0.030
Contestant 2: win_rate=0.154, avg_score=1587.6, median_score=1643.0, stdev=173.4, avg_strikes=2.14, first_out_rate=0.225
Contestant 3: win_rate=0.102, avg_score=1577.9, median_score=1620.0, stdev=197.0, avg_strikes=1.83, first_out_rate=0.414
Last survivor but lost rate: 0.109
Solo started behind rate: 0.114
Solo started behind and lost rate: 0.953

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.659, avg_score=1550.1, median_score=1484.0, stdev=378.5, avg_strikes=3.00, first_out_rate=0.019
Contestant 2: win_rate=0.291, avg_score=1364.6, median_score=1311.0, stdev=301.9, avg_strikes=3.00, first_out_rate=0.030
Contestant 3: win_rate=0.050, avg_score=901.6, median_score=873.5, stdev=232.3, avg_strikes=3.00, first_out_rate=0.951
Last survivor but lost rate: 0.361
Solo started behind rate: 0.403
Solo started behind and lost rate: 0.897

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.720, avg_score=1783.9, avg_median_score=1772.6, avg_stdev=286.9, avg_strikes=1.99, avg_first_out_rate=0.025
Contestant 2: avg_win_rate=0.196, avg_score=1467.6, avg_median_score=1482.8, avg_stdev=196.3, avg_strikes=2.51, avg_first_out_rate=0.231
Contestant 3: avg_win_rate=0.084, avg_score=1342.0, avg_median_score=1347.5, avg_stdev=208.8, avg_strikes=2.28, avg_first_out_rate=0.522
Last survivor but lost rate: 0.195
Solo started behind rate: 0.237
Solo started behind and lost rate: 0.834
```

takeaway: multi category validation suite works, just need to do miilestones 3 (especially) and 4 to fix solo win rate.
---

## Results
[results per milestone + validation strategy can go here, show evolution, obviously leave this blank for now, not at this point]

---

## Limitations
[not at this point yet either]

## Conclusions
[general remarks regarding v2]