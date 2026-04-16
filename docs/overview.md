# Pinpoint Simulation Engine

**Author:** cdeasis <br>
**Date:** March 2026

---

## Overview
This project is a simulation engine for the game ***Pinpoint*** (as seen on JM Baseball on Youtube), modeled using a probabilisitc and behavioral framework.

It simulates how contestants perform across many games by modeling:
- Player knowledge
- Risk-taking behavior
- Decision-making under pressure
- Game dynamics (turn order, elimination, solo phase)

This began as a **for-fun side project**, but has evolved into a structural simulation system and sandbox for modeling decision-making under uncertainty.

---

## What is Pinpoint?

Pinpoint is a competitive game with the following structure:
- Players take turns guessing answers from a hidden ranked list (1-100)
- Each correct guess awards points equal to its value
- The last remaining player continues guessing solo until they get 3 strikes
- The winner is the player with the highest score

### Key Dynamics
- High-value answers are harder to know
- Players constantly balance **risk vs safety**
- The **solo phase** often determines the winner

--- 

## Simulation Design Philosophy
This project evolves across versions, gradually increasing in realism:
- **V1**
> "Can we reproduce realistic outcomes using simple probabilistic + behavioral rules?"
- **V2**
> "Can we model uncertainty, recall, and inference to better match real contestant behavior?
- **V3 (future, goal uncertain yet, but most likely):**
> "Can we simulate realistic game dynamics using real answer data and adaptive strategies?"

---

## Evolution Overview
- **V1:** Probablistic + heuristic baseline model
- **V2:** Adds uncertainty, recall, and confidence
- **V3 (future):** Real data + adaptive strategies 

---

## Project Goals
- Simulate how different contestants perform across many games
- Model player knowledge, uncertainty, and behavior
- Explore how game structure affects outcomes
- Iteratively improve realism through versioned development

---

## Example Output
```
=== Summary ===
Contestant 1: win_rate:0.727, avg_score=1842.6, median_score=1865.5
Contestant 2: win_rate=0.165, avg_score=1581.6, median_score=1605.0
Contestant 3: win_rate=0.108, avg_score=1453.8, median_score=1451.0

```

## Documentation
Technical breakdowns are organized by version:
- `docs/simulation_v1.md`: Version 1 (baseline model)
- `docs/simulation_v2.md`: Version 2 (probabilistic + behavioral system)
- `docs/supplements/v2_raw_results.md`: Full validation outputs and benchmark runs

Each version documents:
- goals and design decisions
- implementation details
- results and limitations

---

## Current State
V2 is complete and represents a major evolution of the simulation engine. The system now includes:
- A **non-binary knowledge model** (knowledge / recall / confidence)
- **Probabilistic guess generation and resolution**
- **Dynamic risk-basd decision making**
- A **reworked solo/endgame system**
- A **multi-category validation framework**
- A lightweight **board inference system**

Key improvements over V1:
- More realistic game state distributions  
- Reduced extreme solo failure rates  
- Increased comeback viability  
- Behavior that adapts to both internal state and board conditions

The engine has transitioned from a rule-based simulation to a dynamic system capable of producing emergent gameplay patterns.

---

### Current Focus (Looking Ahead)
Future development (V3+) will focus on:
- Structured answer objects (real players, stats, metadata)
- Improved category modeling and calibration
- Deeper inference systems (cutoff estimation, opponent modeling)
- Multi-turn planning and strategy

---

## Final Thoughts
This project started as curiosity. I was wondering whether it was possible to estimate contestant performance and expected outcomes in Pinpoint. I then embarked on this journey to model it all out, and overtime it evolved into a strucutred simulation engine, a sandbox for modeling decision-making, and a stepping stone toward advanced behavioral modeling. And most importantly, a really fun system to build and iterate on.