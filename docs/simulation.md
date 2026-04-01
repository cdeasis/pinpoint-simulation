# Pinpoint Simulation Engine

**Author:** cdeasis <br>
**Date:** March 2026

## Purpose
This project is a simulation of the game **Pinpoint** (as seen on JM Baseball on YouTube), modeled using a probalistic and behavorial framework.

The goals of this project are:
- Simulate how different contestants perofrm across many games
- Model player knowledge, risk-taking, and decision-making
- Explore how game dynamics (order, pressure, elimination) affect outcomes
- Iteratively improve realism through multiple versions of this model

This is a **for-fun side project**, but designed with enough structure to resemble a real simluation system.

## Evolution Overview
- **V1:** Probabilistic + heuristic baseline model
- **V2:** Adds uncertainty, recall, and inference
- **V3 (future):** Real data + adaptive strategies

---

## What is Pinpoint?
Pinpoint is a competitive guessing game involving more or less the following:
- Players take turns guessing answers from a hidden list for a specific category (ranked 1-100). Some examples include:
    - Most home runs hit since 2000
    - Player single team WAR
    - All time OPS+
- Each correct guess awards points equal to its value
- Incorrect guess results in strikes (3 strikes = elimination)
- The last remaining player continues guessing solo until they get 3 strikes
- The winner is the player with the highest score

Key Dynamics:
- High-value answers are harder to know
- Risk vs saftey is constant
- Endgame (solo phase) often determines the winner

## Simulation Design Philosophy
This simulation begins with simplified abstractions and progressively increases realism across versions.

Version 1 focuses on:
> "Can we reproduce realistic outcomes using simple probabilistic + behavioral rules?"

Version 2 focuses on:
> "Can we model uncertainty, recall, and inference to better match real contestant behavior?"

Version 3 (future):
> "Can we simulate realistic game dynamics using real answer data and adaptive strategies?"

---

## Version 1 (V1)

### Overview
Version 1 models the game using:
- Bucketed knowledge probabilities
- Heuristic decision-making (save vs risky vs blind guesses)
- A simple solo / endgame system
- Monte Carlo simulation across thousands of runs

It does **not** attempt to model:
- Specific player names
- Partial knowledge or uncertainty
- Real-time inference from the board

### Core Components

#### 1. **Player Profiles**
Each contestant is defined by:
- `knowledge_by_bucket`: probablity of knowing answers in each difficulty range
- `style`: baseline risk tendency (`balanced`, `volatile`, etc.)
- `category_modifiers`: weaknesses in specific category types
- Behavioral modifiers:
    - `blind_risk_base`
    - `content_bias`
    - `pressure_sensitivity`

#### 2. **Knowledge Model**
In each game:
- Every answer (1-100) is sampled as **known** or **unknown**
- Probability depends on:
    - difficulty bucket
    - category difficulty
    - player modifiers 

This thus creates a per-game "knowledge set" for each player

#### 3. **Turn Strategy**
In each turn:<br>
1. Compute **social pressure**
    - based on score gap, strikes, and recent table behavior
2. Decide mode:
    - `safe`
    - `risky`
    - `blind_risk`
3. Select a guess:
    - safe: lower-value known answers
    - risky: higher-value known answers
    - blind: high-value unknown answers

#### 4. **Game Flow**
- Uses **snake order** for 3 players
- Switches to **alternating order** for 2 players
- Players are eliminated at 3 strikes
- The game continues until:
    - all players eliminated OR
    - answers exhausted

#### 5. **Solo (Endgame) Logic**
When one player remains:
- Behavior depends on score deficit:
    - ahead: "victory lap"
    - small deficit: mostly safe
    - medium: mixed
    - large: aggressive
- Guess selection considers:
    - answers that can immediately win
    - answers that reduce deficit

#### 6. **Metrics Tracked**
Across simulations:
- Win rate
- Average / median score
- Score variance
- Strike averages
- First-out rate
- Last survivor but lost rate

Additional endgame metrics:
- Solo started behind rate
- Solo started behind and lost rate

### Results (Example)
Typical outcomes:
- Contestants 1 and 2 are close in strength
- Contestant 3 is clearly weaker
- Scores fall into a realistic range
- First elimination patterns match expectations

### Key Achievements
Version 1 successfully achieved the following:
- Risk vs safety tradeoffs
- Realtive contestant strength differences
- Score distributions across many games
- Importance of elimination order
- Structured simulation framework

### Limitations
Despite baseline expectations being met, Version 1 contained various limitations:

#### 1. **Binary Knowledge Model**
Players either:
- know answers perfectly OR
- have no access to it

There is no:
- partial recall
- uncertainty
- educated guessing

#### 2. **No Real Answer Representation**
Answers are just integers (1-100)

This prevents:
- modeling famous vs obscure names
- era/category bias
- realistic inference

#### 3. **Weak Solo Comeback Behavior**
Observed metrics:
- **Solo started behind and lost ~75% of the time**

In reality:
- players often come back and win

Cause:
- players can only choose from **known answers**
- no ability to take plausible-but-uncertain guesses

#### 4. **Limited Strategic Depth**
Players do not:
- infer cutoff depth
- react to surprising guesses
- anticipate opponents' knowledge

### Conclusion of Version 1
Version 1 achieves its goal:
> A stable, tunable, and interpretable simulation of Pinpoint using simple proabilistic data

However, further realism, especially pertaining to endgame behavior, requires a more advanced model

---

## Version 2 (In Progress)

### Goal
The main purpose of Version 2, beyond extending Version 1, is to tackle the question of:
> "Can we move beyond binary knowledge by modeling uncertainty, recall, and inference to better replicate real contestant decision-making?"

### Planned Improvements

#### 1. Knowledge vs Recall vs Confidence
The goal is to separate:
- knowing something
- recalling it under pressure
- being willing to guess it

#### 2. Uncertain / Plausible Guesses
Key mindset to introduce:
- "I think this might be on the list"

This is critical for:
- comebacks
- mid-risk decisions
- realism

#### 3. Real Answer Objects
Replace `1-100` with structured answers, such as:
- name
- value
- obscurity
- category tags

#### 4. Category Types
Instead of only difficulty (as is the case in V1):
- WAR-heavy
- Old-era
- Modern players
- Awards-based
- Niche Categories

#### 5. Board Inference
Players will now be able to:
- update beliefs based on revealed answers
- estimate cutoff depth
- adjust risk dynamically

#### 6. Improved Solo Logic
As this was one of the main short comings of V1, in V2, solo player will:
- use confidence-weighted guesses
- plan comebacks based on deficit
- take calculated risks beyond known answers

### Expected Impact
Version 2 should:
- Reduce unrealistic solo losses
- Improve mid-game realism
- Better match contestant behavior
- Allow richer experimentation

---

## Future Directions
Possible extensions beyond V2:
- Player-specific personalities (e.g., aggressive vs analytical)
- Simulation of specific real contestants
- Category-specific tuning
- Visualization of game trajectories
- Integration with real Pinpoint data

---

## Final Thoughts
This project started as a fun idea. I am a huge fan of JM Baseball's gameshows on YouTube, and the Pinpoint Challenge is one of the newer games they've played. I originally was interested in if was possible to calculate the expected value of the contestants per game and per category, and if it was possible to reliably predict outcomes of the games. I thus thought it would be fun to simulate the game, and over time, it gradually evolved into a structured simulation system, a sandbox for modeling human decision-making, and a stepping stone toward more complex behavioral modeling, and I had a lot of fun playing around with it along the way.