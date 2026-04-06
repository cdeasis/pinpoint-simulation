# Simulation Engine - Version 1 (V1)

## Overview
Version 1 models the game using:
- Bucketed knowledge probabilties
- Heurestic decision-making (save vs risky vs blind guesses)
- A simple solo / endgame system
- Monte Carlo simulation across thousands of runs

It does **not** attempt to model:
- Specific player names
- Partial knowledge or uncertainty
- Real-time inference from the board

--- 

## Core Components

### 1. Player Profiles
Each contestant is defined by:
- `knowledge_by_bucket`: probability of knowing answers in each difficulty range
- `style`: baseline risk tendency (`balanced`, `volatile`, etc.)
- `category_modifiers`: weaknesses in specific category types

Behavioral modifiers:
- `blind_risk_base`
- `content_bias`
- `pressure_sensitivity`

---

### 2. Knowledge Model
In each game:
- Every answer (1–100) is sampled as **known** or **unknown**
- Probability depends on:
  - difficulty bucket
  - category difficulty
  - player modifiers

This creates a per-game "knowledge set" for each player.

---

### 3. Turn Strategy
Each turn follows:

1. Compute **social pressure**
   - based on score gap, strikes, and recent table behavior

2. Decide mode:
   - `safe`
   - `risky`
   - `blind_risk`

3. Select a guess:
   - safe → lower-value known answers  
   - risky → higher-value known answers  
   - blind → high-value unknown answers  

---

### 4. Game Flow
- Uses **snake order** for 3 players  
- Uses **alternating order** for 2 players  
- Players are eliminated at 3 strikes  

Game ends when:
- all players are eliminated OR  
- all answers are exhausted  

---

### 5. Solo (Endgame) Logic
When one player remains:

Behavior depends on score deficit:
- ahead → "victory lap"
- small deficit → mostly safe
- medium → mixed
- large → aggressive

Guess selection considers:
- answers that immediately win
- answers that reduce deficit

---

### 6. Metrics Tracked
Across simulations:
- Win rate
- Average / median score
- Score variance
- Strike averages
- First-out rate
- Last survivor but lost rate

Endgame metrics:
- Solo started behind rate
- Solo started behind and lost rate

---

## Results (Example)
```
=== Summary ===
Contestant 1: win_rate=0.471, avg_score=799.2, median_score=795.0, stdev=180.7, avg_strikes=3.00, first_out_rate=0.188
Contestant 2: win_rate=0.403, avg_score=774.1, median_score=766.0, stdev=175.6, avg_strikes=3.00, first_out_rate=0.235
Contestant 3: win_rate=0.126, avg_score=623.0, median_score=616.0, stdev=161.2, avg_strikes=3.00, first_out_rate=0.577
Last survivor but lost rate: 0.269
Solo started behind rate: 0.353
Solo started behind and lost rate: 0.762
```

---

## Key Achievements
- Captures risk vs safety tradeoffs  
- Produces relative contestant strength differences  
- Generates realistic score distributions  
- Models elimination order impact  
- Establishes a stable simulation framework  

---

## Limitations

### 1. Binary Knowledge Model
Players either:
- know answers perfectly OR  
- do not know them at all  

No modeling of:
- partial recall  
- uncertainty  
- educated guessing  

---

### 2. No Real Answer Representation
Answers are abstract integers (1–100)

This prevents modeling:
- famous vs obscure names  
- era/category bias  
- realistic inference  

---

### 3. Weak Solo Comeback Behavior
Observed:
- solo players lose most of the time when behind  

Cause:
- players only select from known answers  
- no plausible-but-uncertain guessing  

---

### 4. Limited Strategic Depth
Players do not:
- infer cutoff depth  
- react to surprising guesses  
- adapt dynamically  

---

## Conclusion
Version 1 achieves its goal:

> A stable, interpretable simulation using simple probabilistic and behavioral rules.

However, improving realism — especially in uncertainty and endgame behavior — requires a more advanced model, leading into Version 2.