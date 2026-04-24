# V3 Raw Results and Validation Logs

This document contains raw outputs and intermediate benchmark runs from Version 3.

## Purpose:
- Preserve full validation outputs
- Show how results evolved across milestones
- Provide supporting evidence for conclusions in `simulation_v3.md`

Notes:
- Outputs are minimally edited
- Observations focus on behavioral trends, not implementation details
- Key takeways are summarized per section

---

## Summary of Progression

| Stage | Cutoff Estimate | Uncertainty | Safe Floor |Solo Loss Rate| Key Behavior |
| - | - | - | - | -| - | 
| M1 Final | ~baseline | ~baseline | ~baseline | ~0.48 | Representation changed, behavior stable
| M2 Run 1 | ~25 | ~0.11 | low (~10-20) | ~0.58 | Collapse to low cutoff
| M2 Run 2 | ~80 | ~0.85 | ~60+ | ~0.58 | Ceiling pinning
| M2 Final | ~60 | ~0.40 | ~48 | ~0.51 | Stable, category-sensitive

---

## Milestone 1 - Multi-Dimensional Board Inference

**Summary**:
- successfully replaced `board_read` with multi-state ssytem
- behavior remained stable, no major shifts in win rates or solo outcomes
- boaord perception became more balanced, no longer overly generous

**Key Result**:
- structural success without behavioral disruption
- confirms M1 successfully refactored representation layer

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.666, avg_score=1840.2, median_score=1781.0, stdev=296.2, avg_strikes=2.95, first_out_rate=0.055
Contestant 2: win_rate=0.276, avg_score=1631.0, median_score=1595.0, stdev=244.7, avg_strikes=2.97, first_out_rate=0.186
Contestant 3: win_rate=0.058, avg_score=1307.1, median_score=1309.0, stdev=224.2, avg_strikes=2.97, first_out_rate=0.751
Last survivor but lost rate: 0.088
Solo started behind rate: 0.223
Solo started behind and lost rate: 0.394
Avg solo start deficit: 82.8
Avg solo turns taken: 3.34
Solo had winning answer rate: 0.124
Solo had winning answer given started behind rate: 0.555
Solo start deficit buckets: 1-75: 0.567, 76-150: 0.260, 151-250: 0.144, 251+: 0.030
Avg final board read: 0.107
Avg absolute final board read: 0.116
Strong harsh board rate: 0.004
Strong generous board rate: 0.125

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.856, avg_score=2454.5, median_score=2673.0, stdev=751.6, avg_strikes=3.00, first_out_rate=0.000
Contestant 2: win_rate=0.073, avg_score=846.2, median_score=841.5, stdev=178.8, avg_strikes=3.00, first_out_rate=0.831
Contestant 3: win_rate=0.072, avg_score=887.5, median_score=877.0, stdev=213.2, avg_strikes=3.00, first_out_rate=0.169
Last survivor but lost rate: 0.139
Solo started behind rate: 0.430
Solo started behind and lost rate: 0.323
Avg solo start deficit: 107.7
Avg solo turns taken: 20.04
Solo had winning answer rate: 0.233
Solo had winning answer given started behind rate: 0.542
Solo start deficit buckets: 1-75: 0.429, 76-150: 0.304, 151-250: 0.198, 251+: 0.069
Avg final board read: -0.030
Avg absolute final board read: 0.082
Strong harsh board rate: 0.058
Strong generous board rate: 0.016

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.662, avg_score=1765.1, median_score=1752.0, stdev=101.6, avg_strikes=0.84, first_out_rate=0.002
Contestant 2: win_rate=0.249, avg_score=1650.1, median_score=1667.0, stdev=110.0, avg_strikes=1.97, first_out_rate=0.298
Contestant 3: win_rate=0.089, avg_score=1627.0, median_score=1645.0, stdev=114.6, avg_strikes=1.07, first_out_rate=0.146
Last survivor but lost rate: 0.049
Solo started behind rate: 0.063
Solo started behind and lost rate: 0.782
Avg solo start deficit: 120.9
Avg solo turns taken: 1.52
Solo had winning answer rate: 0.013
Solo had winning answer given started behind rate: 0.208
Solo start deficit buckets: 1-75: 0.180, 76-150: 0.539, 151-250: 0.266, 251+: 0.016
Avg final board read: 0.102
Avg absolute final board read: 0.107
Strong harsh board rate: 0.001
Strong generous board rate: 0.353

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.694, avg_score=1802.3, median_score=1770.0, stdev=180.1, avg_strikes=2.35, first_out_rate=0.069
Contestant 2: win_rate=0.185, avg_score=1629.7, median_score=1634.0, stdev=150.3, avg_strikes=2.69, first_out_rate=0.397
Contestant 3: win_rate=0.120, avg_score=1536.1, median_score=1576.0, stdev=173.0, avg_strikes=2.51, first_out_rate=0.411
Last survivor but lost rate: 0.154
Solo started behind rate: 0.233
Solo started behind and lost rate: 0.661
Avg solo start deficit: 108.5
Avg solo turns taken: 1.81
Solo had winning answer rate: 0.071
Solo had winning answer given started behind rate: 0.304
Solo start deficit buckets: 1-75: 0.361, 76-150: 0.364, 151-250: 0.236, 251+: 0.039
Avg final board read: 0.108
Avg absolute final board read: 0.116
Strong harsh board rate: 0.004
Strong generous board rate: 0.286

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.606, avg_score=1868.9, median_score=2274.0, stdev=856.4, avg_strikes=3.00, first_out_rate=0.008
Contestant 2: win_rate=0.388, avg_score=1469.8, median_score=1050.0, stdev=784.9, avg_strikes=3.00, first_out_rate=0.024
Contestant 3: win_rate=0.006, avg_score=546.0, median_score=524.0, stdev=180.3, avg_strikes=3.00, first_out_rate=0.969
Last survivor but lost rate: 0.086
Solo started behind rate: 0.341
Solo started behind and lost rate: 0.251
Avg solo start deficit: 88.6
Avg solo turns taken: 21.66
Solo had winning answer rate: 0.217
Solo had winning answer given started behind rate: 0.636
Solo start deficit buckets: 1-75: 0.524, 76-150: 0.299, 151-250: 0.144, 251+: 0.033
Avg final board read: -0.084
Avg absolute final board read: 0.096
Strong harsh board rate: 0.225
Strong generous board rate: 0.000

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.697, avg_score=1946.2, avg_median_score=2050.0, avg_stdev=437.2, avg_strikes=2.43, avg_first_out_rate=0.027
Contestant 2: avg_win_rate=0.234, avg_score=1445.4, avg_median_score=1357.5, avg_stdev=293.7, avg_strikes=2.73, avg_first_out_rate=0.347
Contestant 3: avg_win_rate=0.069, avg_score=1180.7, avg_median_score=1186.2, avg_stdev=181.1, avg_strikes=2.51, avg_first_out_rate=0.489
Last survivor but lost rate: 0.103
Solo started behind rate: 0.258
Solo started behind and lost rate: 0.482
Avg solo start deficit: 101.7
Avg solo turns taken: 9.67
Solo had winning answer rate: 0.132
Solo had winning answer given started behind rate: 0.449
Solo start deficit buckets: 1-75: 0.412, 76-150: 0.353, 151-250: 0.198, 251+: 0.037
Avg final board read: 0.040
Avg absolute final board read: 0.103
Avg strong harsh board rate: 0.058
Avg strong generous board rate: 0.156
```

**Core Result**:
- Win rate distribution remained nearly identicial to V2
- Solo metrics showed minimal change:
    - solo behind rate: ~0.265 &rarr; ~0.258
    - solo loss rate: ~0.436 &rarr; ~0.482
- Score and strike distributions remained stable

This shows the system's internal representation changed, but the behavior did not, exactly the goal of M1

**Board Perception Shift (Major):**

V2:
- avg board read: ~0.144
- strong generous: ~0.63-0.90

V3M1:
- avg board read: ~0.040
- strong generous: ~0.156

V2 had a strong bias towards 'generous boards', and nearly all categories were interpreted as easy/deep.

The root of this was V2 uses a singular scalar in `board_read += siginals`, which is overly addative, has no opposing forces, and drifted positive easily.

---

## Milestone 2 - Cutoff Estimation System

**Summary**:

M2 introduced dynamic cutoff estimation and uncertainty modeling

**Observed Progression:**
- Run 1: collapsed to low cutoff (overly safe behavior)
- Run 2: collapse to high cutoff (overly strict behavior)
- Runs 3-5: gradual stabilization
- Final Runs (6-7): stable, category-sensitive behavior

**Key Insights:**
1. Cutoff estimation strongly influences behavior
- small changes in update logic produce large behavioral shifts

2. System is highly sensitive to calibration
- incorrect weighting leads to collapse states (low or high cutoff)

3. Stable equilibrium achieved
- final runs avoid extreme behavior
- category differences emerge naturally

4. Limitation remains
- board perception skewed towards harsh outcomes
- no modeling of answer density of clustering

### Run 1

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.638, avg_score=1795.6, median_score=1722.0, stdev=289.1, avg_strikes=2.99, first_out_rate=0.134
Contestant 2: win_rate=0.267, avg_score=1628.9, median_score=1605.0, stdev=214.6, avg_strikes=3.00, first_out_rate=0.424
Contestant 3: win_rate=0.095, avg_score=1309.4, median_score=1352.0, stdev=221.4, avg_strikes=2.99, first_out_rate=0.440
Last survivor but lost rate: 0.302
Solo started behind rate: 0.454
Solo started behind and lost rate: 0.665
Avg solo start deficit: 199.0
Avg solo turns taken: 2.42
Solo had winning answer rate: 0.122
Solo had winning answer given started behind rate: 0.268
Solo start deficit buckets: 1-75: 0.253, 76-150: 0.222, 151-250: 0.233, 251+: 0.292
Avg final board read: -0.154
Avg absolute final board read: 0.168
Strong harsh board rate: 0.718
Strong generous board rate: 0.000
Avg final cutoff estimate: 30.81
Avg final cutoff uncertainty: 0.100
Low uncertainty rate: 1.000
High cutoff rate: 0.088

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.947, avg_score=2538.9, median_score=2630.0, stdev=535.4, avg_strikes=3.00, first_out_rate=0.005
Contestant 2: win_rate=0.012, avg_score=871.2, median_score=844.0, stdev=245.8, avg_strikes=3.00, first_out_rate=0.904
Contestant 3: win_rate=0.041, avg_score=989.8, median_score=954.0, stdev=270.4, avg_strikes=3.00, first_out_rate=0.091
Last survivor but lost rate: 0.058
Solo started behind rate: 0.152
Solo started behind and lost rate: 0.383
Avg solo start deficit: 113.6
Avg solo turns taken: 14.32
Solo had winning answer rate: 0.083
Solo had winning answer given started behind rate: 0.547
Solo start deficit buckets: 1-75: 0.474, 76-150: 0.261, 151-250: 0.153, 251+: 0.112
Avg final board read: -0.140
Avg absolute final board read: 0.146
Strong harsh board rate: 0.540
Strong generous board rate: 0.001
Avg final cutoff estimate: 30.55
Avg final cutoff uncertainty: 0.118
Low uncertainty rate: 0.996
High cutoff rate: 0.000

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.422, avg_score=1716.7, median_score=1704.0, stdev=89.0, avg_strikes=1.67, first_out_rate=0.001
Contestant 2: win_rate=0.446, avg_score=1706.3, median_score=1707.0, stdev=89.7, avg_strikes=2.26, first_out_rate=0.433
Contestant 3: win_rate=0.132, avg_score=1600.3, median_score=1602.0, stdev=92.2, avg_strikes=1.66, first_out_rate=0.148
Last survivor but lost rate: 0.209
Solo started behind rate: 0.305
Solo started behind and lost rate: 0.686
Avg solo start deficit: 122.7
Avg solo turns taken: 3.00
Solo had winning answer rate: 0.088
Solo had winning answer given started behind rate: 0.288
Solo start deficit buckets: 1-75: 0.287, 76-150: 0.385, 151-250: 0.276, 251+: 0.052
Avg final board read: -0.183
Avg absolute final board read: 0.184
Strong harsh board rate: 0.971
Strong generous board rate: 0.002
Avg final cutoff estimate: 17.67
Avg final cutoff uncertainty: 0.100
Low uncertainty rate: 1.000
High cutoff rate: 0.003

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.544, avg_score=1745.3, median_score=1711.0, stdev=160.8, avg_strikes=2.79, first_out_rate=0.121
Contestant 2: win_rate=0.310, avg_score=1658.9, median_score=1658.0, stdev=126.5, avg_strikes=2.89, first_out_rate=0.634
Contestant 3: win_rate=0.146, avg_score=1524.5, median_score=1540.0, stdev=147.8, avg_strikes=2.79, first_out_rate=0.198
Last survivor but lost rate: 0.430
Solo started behind rate: 0.558
Solo started behind and lost rate: 0.770
Avg solo start deficit: 169.3
Avg solo turns taken: 2.38
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.177
Solo start deficit buckets: 1-75: 0.217, 76-150: 0.265, 151-250: 0.316, 251+: 0.203
Avg final board read: -0.185
Avg absolute final board read: 0.190
Strong harsh board rate: 0.924
Strong generous board rate: 0.001
Avg final cutoff estimate: 20.89
Avg final cutoff uncertainty: 0.100
Low uncertainty rate: 1.000
High cutoff rate: 0.023

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.646, avg_score=1838.5, median_score=2082.0, stdev=757.2, avg_strikes=3.00, first_out_rate=0.039
Contestant 2: win_rate=0.325, avg_score=1398.5, median_score=1091.0, stdev=679.9, avg_strikes=3.00, first_out_rate=0.076
Contestant 3: win_rate=0.029, avg_score=672.0, median_score=637.0, stdev=257.1, avg_strikes=3.00, first_out_rate=0.885
Last survivor but lost rate: 0.110
Solo started behind rate: 0.280
Solo started behind and lost rate: 0.391
Avg solo start deficit: 115.4
Avg solo turns taken: 14.10
Solo had winning answer rate: 0.143
Solo had winning answer given started behind rate: 0.510
Solo start deficit buckets: 1-75: 0.411, 76-150: 0.311, 151-250: 0.187, 251+: 0.091
Avg final board read: -0.156
Avg absolute final board read: 0.160
Strong harsh board rate: 0.640
Strong generous board rate: 0.001
Avg final cutoff estimate: 27.00
Avg final cutoff uncertainty: 0.136
Low uncertainty rate: 0.960
High cutoff rate: 0.000

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.639, avg_score=1927.0, avg_median_score=1969.8, avg_stdev=366.3, avg_strikes=2.69, avg_first_out_rate=0.060
Contestant 2: avg_win_rate=0.272, avg_score=1452.8, avg_median_score=1381.0, avg_stdev=271.3, avg_strikes=2.83, avg_first_out_rate=0.494
Contestant 3: avg_win_rate=0.089, avg_score=1219.2, avg_median_score=1217.0, avg_stdev=197.8, avg_strikes=2.69, avg_first_out_rate=0.352
Last survivor but lost rate: 0.222
Solo started behind rate: 0.350
Solo started behind and lost rate: 0.579
Avg solo start deficit: 144.0
Avg solo turns taken: 7.24
Solo had winning answer rate: 0.107
Solo had winning answer given started behind rate: 0.358
Solo start deficit buckets: 1-75: 0.328, 76-150: 0.289, 151-250: 0.233, 251+: 0.150
Avg final board read: -0.164
Avg absolute final board read: 0.170
Avg strong harsh board rate: 0.759
Avg strong generous board rate: 0.001
Avg final cutoff estimate: 25.38
Avg final cutoff uncertainty: 0.111
Avg low uncertainty rate: 0.991
Avg high cutoff rate: 0.023
```

### Run 2

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.650, avg_score=1787.8, median_score=1727.0, stdev=290.0, avg_strikes=2.96, first_out_rate=0.148
Contestant 2: win_rate=0.188, avg_score=1592.7, median_score=1581.0, stdev=210.3, avg_strikes=2.98, first_out_rate=0.422
Contestant 3: win_rate=0.162, avg_score=1354.8, median_score=1426.0, stdev=249.9, avg_strikes=2.97, first_out_rate=0.422
Last survivor but lost rate: 0.250
Solo started behind rate: 0.383
Solo started behind and lost rate: 0.652
Avg solo start deficit: 169.0
Avg solo turns taken: 2.21
Solo had winning answer rate: 0.100
Solo had winning answer given started behind rate: 0.260
Solo start deficit buckets: 1-75: 0.292, 76-150: 0.282, 151-250: 0.223, 251+: 0.204
Avg final board read: -0.079
Avg absolute final board read: 0.088
Strong harsh board rate: 0.174
Strong generous board rate: 0.000
Avg final cutoff estimate: 79.77
Avg final cutoff uncertainty: 0.838
Low uncertainty rate: 0.000
High cutoff rate: 1.000
Avg final safe floor: 61.39

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.948, avg_score=2484.4, median_score=2558.0, stdev=488.8, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.011, avg_score=933.4, median_score=918.0, stdev=227.5, avg_strikes=3.00, first_out_rate=0.849
Contestant 3: win_rate=0.041, avg_score=992.8, median_score=971.0, stdev=257.0, avg_strikes=3.00, first_out_rate=0.149
Last survivor but lost rate: 0.051
Solo started behind rate: 0.120
Solo started behind and lost rate: 0.422
Avg solo start deficit: 118.3
Avg solo turns taken: 9.71
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.512
Solo start deficit buckets: 1-75: 0.432, 76-150: 0.277, 151-250: 0.178, 251+: 0.114
Avg final board read: -0.115
Avg absolute final board read: 0.120
Strong harsh board rate: 0.362
Strong generous board rate: 0.000
Avg final cutoff estimate: 79.11
Avg final cutoff uncertainty: 0.868
Low uncertainty rate: 0.000
High cutoff rate: 1.000
Avg final safe floor: 60.43

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.667, avg_score=1755.5, median_score=1749.0, stdev=81.6, avg_strikes=0.94, first_out_rate=0.001
Contestant 2: win_rate=0.245, avg_score=1667.5, median_score=1682.0, stdev=88.5, avg_strikes=2.02, first_out_rate=0.315
Contestant 3: win_rate=0.088, avg_score=1615.2, median_score=1626.0, stdev=104.6, avg_strikes=0.83, first_out_rate=0.095
Last survivor but lost rate: 0.064
Solo started behind rate: 0.093
Solo started behind and lost rate: 0.688
Avg solo start deficit: 117.3
Avg solo turns taken: 2.04
Solo had winning answer rate: 0.026
Solo had winning answer given started behind rate: 0.282
Solo start deficit buckets: 1-75: 0.309, 76-150: 0.416, 151-250: 0.215, 251+: 0.060
Avg final board read: -0.120
Avg absolute final board read: 0.120
Strong harsh board rate: 0.186
Strong generous board rate: 0.000
Avg final cutoff estimate: 79.93
Avg final cutoff uncertainty: 0.832
Low uncertainty rate: 0.000
High cutoff rate: 1.000
Avg final safe floor: 61.61

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.672, avg_score=1761.5, median_score=1750.5, stdev=155.1, avg_strikes=2.35, first_out_rate=0.125
Contestant 2: win_rate=0.146, avg_score=1626.6, median_score=1641.0, stdev=130.9, avg_strikes=2.73, first_out_rate=0.578
Contestant 3: win_rate=0.183, avg_score=1556.0, median_score=1592.0, stdev=171.9, avg_strikes=2.34, first_out_rate=0.151
Last survivor but lost rate: 0.298
Solo started behind rate: 0.389
Solo started behind and lost rate: 0.767
Avg solo start deficit: 159.9
Avg solo turns taken: 1.91
Solo had winning answer rate: 0.074
Solo had winning answer given started behind rate: 0.189
Solo start deficit buckets: 1-75: 0.299, 76-150: 0.303, 151-250: 0.227, 251+: 0.171
Avg final board read: -0.113
Avg absolute final board read: 0.114
Strong harsh board rate: 0.267
Strong generous board rate: 0.000
Avg final cutoff estimate: 79.87
Avg final cutoff uncertainty: 0.832
Low uncertainty rate: 0.000
High cutoff rate: 1.000
Avg final safe floor: 61.55

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.616, avg_score=1772.1, median_score=1956.0, stdev=773.7, avg_strikes=3.00, first_out_rate=0.023
Contestant 2: win_rate=0.370, avg_score=1436.1, median_score=1090.0, stdev=711.4, avg_strikes=3.00, first_out_rate=0.044
Contestant 3: win_rate=0.013, avg_score=657.4, median_score=643.0, stdev=212.8, avg_strikes=3.00, first_out_rate=0.933
Last survivor but lost rate: 0.132
Solo started behind rate: 0.343
Solo started behind and lost rate: 0.384
Avg solo start deficit: 110.9
Avg solo turns taken: 15.34
Solo had winning answer rate: 0.185
Solo had winning answer given started behind rate: 0.542
Solo start deficit buckets: 1-75: 0.437, 76-150: 0.295, 151-250: 0.176, 251+: 0.092
Avg final board read: -0.152
Avg absolute final board read: 0.152
Strong harsh board rate: 0.568
Strong generous board rate: 0.000
Avg final cutoff estimate: 78.95
Avg final cutoff uncertainty: 0.887
Low uncertainty rate: 0.000
High cutoff rate: 0.998
Avg final safe floor: 60.09

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.711, avg_score=1912.3, avg_median_score=1948.1, avg_stdev=357.8, avg_strikes=2.45, avg_first_out_rate=0.060
Contestant 2: avg_win_rate=0.192, avg_score=1451.2, avg_median_score=1382.4, avg_stdev=273.7, avg_strikes=2.75, avg_first_out_rate=0.442
Contestant 3: avg_win_rate=0.097, avg_score=1235.3, avg_median_score=1251.6, avg_stdev=199.2, avg_strikes=2.43, avg_first_out_rate=0.350
Last survivor but lost rate: 0.159
Solo started behind rate: 0.265
Solo started behind and lost rate: 0.583
Avg solo start deficit: 135.1
Avg solo turns taken: 6.24
Solo had winning answer rate: 0.089
Solo had winning answer given started behind rate: 0.357
Solo start deficit buckets: 1-75: 0.354, 76-150: 0.314, 151-250: 0.204, 251+: 0.128
Avg final board read: -0.116
Avg absolute final board read: 0.119
Avg strong harsh board rate: 0.311
Avg strong generous board rate: 0.000
Avg final cutoff estimate: 79.53
Avg final cutoff uncertainty: 0.851
Avg low uncertainty rate: 0.000
Avg high cutoff rate: 1.000
Avg final safe floor: 61.01
```

### Run 3

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.644, avg_score=1781.1, median_score=1718.0, stdev=288.6, avg_strikes=2.97, first_out_rate=0.148
Contestant 2: win_rate=0.189, avg_score=1591.8, median_score=1582.0, stdev=206.4, avg_strikes=2.98, first_out_rate=0.439
Contestant 3: win_rate=0.167, avg_score=1359.5, median_score=1428.5, stdev=250.0, avg_strikes=2.97, first_out_rate=0.407
Last survivor but lost rate: 0.260
Solo started behind rate: 0.397
Solo started behind and lost rate: 0.655
Avg solo start deficit: 171.5
Avg solo turns taken: 2.21
Solo had winning answer rate: 0.108
Solo had winning answer given started behind rate: 0.272
Solo start deficit buckets: 1-75: 0.307, 76-150: 0.261, 151-250: 0.220, 251+: 0.212
Avg final board read: -0.080
Avg absolute final board read: 0.090
Strong harsh board rate: 0.195
Strong generous board rate: 0.000
Avg final cutoff estimate: 73.38
Avg final cutoff uncertainty: 0.575
Low uncertainty rate: 0.000
High cutoff rate: 0.780
Avg final safe floor: 57.63

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.947, avg_score=2485.7, median_score=2557.0, stdev=484.4, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.012, avg_score=932.2, median_score=915.0, stdev=228.9, avg_strikes=3.00, first_out_rate=0.856
Contestant 3: win_rate=0.042, avg_score=995.2, median_score=975.0, stdev=257.9, avg_strikes=3.00, first_out_rate=0.142
Last survivor but lost rate: 0.045
Solo started behind rate: 0.112
Solo started behind and lost rate: 0.402
Avg solo start deficit: 119.9
Avg solo turns taken: 9.65
Solo had winning answer rate: 0.058
Solo had winning answer given started behind rate: 0.518
Solo start deficit buckets: 1-75: 0.450, 76-150: 0.272, 151-250: 0.169, 251+: 0.109
Avg final board read: -0.113
Avg absolute final board read: 0.118
Strong harsh board rate: 0.349
Strong generous board rate: 0.000
Avg final cutoff estimate: 74.70
Avg final cutoff uncertainty: 0.652
Low uncertainty rate: 0.000
High cutoff rate: 0.852
Avg final safe floor: 58.18

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.601, avg_score=1742.6, median_score=1739.0, stdev=90.0, avg_strikes=1.03, first_out_rate=0.002
Contestant 2: win_rate=0.262, avg_score=1667.1, median_score=1681.0, stdev=91.2, avg_strikes=2.05, first_out_rate=0.325
Contestant 3: win_rate=0.137, avg_score=1625.5, median_score=1638.0, stdev=106.8, avg_strikes=0.94, first_out_rate=0.104
Last survivor but lost rate: 0.055
Solo started behind rate: 0.098
Solo started behind and lost rate: 0.568
Avg solo start deficit: 93.7
Avg solo turns taken: 2.35
Solo had winning answer rate: 0.039
Solo had winning answer given started behind rate: 0.402
Solo start deficit buckets: 1-75: 0.456, 76-150: 0.370, 151-250: 0.143, 251+: 0.031
Avg final board read: -0.125
Avg absolute final board read: 0.125
Strong harsh board rate: 0.257
Strong generous board rate: 0.000
Avg final cutoff estimate: 72.78
Avg final cutoff uncertainty: 0.556
Low uncertainty rate: 0.000
High cutoff rate: 0.837
Avg final safe floor: 57.21

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.606, avg_score=1747.8, median_score=1735.0, stdev=160.5, avg_strikes=2.45, first_out_rate=0.122
Contestant 2: win_rate=0.166, avg_score=1623.8, median_score=1636.0, stdev=132.2, avg_strikes=2.78, first_out_rate=0.603
Contestant 3: win_rate=0.228, avg_score=1567.3, median_score=1609.0, stdev=175.6, avg_strikes=2.44, first_out_rate=0.155
Last survivor but lost rate: 0.288
Solo started behind rate: 0.402
Solo started behind and lost rate: 0.718
Avg solo start deficit: 147.8
Avg solo turns taken: 2.04
Solo had winning answer rate: 0.094
Solo had winning answer given started behind rate: 0.235
Solo start deficit buckets: 1-75: 0.346, 76-150: 0.307, 151-250: 0.197, 251+: 0.151
Avg final board read: -0.119
Avg absolute final board read: 0.120
Strong harsh board rate: 0.339
Strong generous board rate: 0.000
Avg final cutoff estimate: 70.99
Avg final cutoff uncertainty: 0.554
Low uncertainty rate: 0.000
High cutoff rate: 0.736
Avg final safe floor: 55.45

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.612, avg_score=1775.8, median_score=1970.0, stdev=772.7, avg_strikes=3.00, first_out_rate=0.022
Contestant 2: win_rate=0.373, avg_score=1440.7, median_score=1095.0, stdev=713.1, avg_strikes=3.00, first_out_rate=0.045
Contestant 3: win_rate=0.015, avg_score=658.4, median_score=647.0, stdev=214.9, avg_strikes=3.00, first_out_rate=0.933
Last survivor but lost rate: 0.125
Solo started behind rate: 0.339
Solo started behind and lost rate: 0.369
Avg solo start deficit: 109.2
Avg solo turns taken: 15.79
Solo had winning answer rate: 0.186
Solo had winning answer given started behind rate: 0.549
Solo start deficit buckets: 1-75: 0.453, 76-150: 0.288, 151-250: 0.171, 251+: 0.088
Avg final board read: -0.151
Avg absolute final board read: 0.151
Strong harsh board rate: 0.559
Strong generous board rate: 0.000
Avg final cutoff estimate: 74.86
Avg final cutoff uncertainty: 0.700
Low uncertainty rate: 0.000
High cutoff rate: 0.844
Avg final safe floor: 57.86

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.682, avg_score=1906.6, avg_median_score=1943.8, avg_stdev=359.2, avg_strikes=2.49, avg_first_out_rate=0.059
Contestant 2: avg_win_rate=0.200, avg_score=1451.1, avg_median_score=1381.8, avg_stdev=274.4, avg_strikes=2.76, avg_first_out_rate=0.454
Contestant 3: avg_win_rate=0.118, avg_score=1241.2, avg_median_score=1259.5, avg_stdev=201.0, avg_strikes=2.47, avg_first_out_rate=0.348
Last survivor but lost rate: 0.155
Solo started behind rate: 0.269
Solo started behind and lost rate: 0.542
Avg solo start deficit: 128.4
Avg solo turns taken: 6.41
Solo had winning answer rate: 0.097
Solo had winning answer given started behind rate: 0.395
Solo start deficit buckets: 1-75: 0.402, 76-150: 0.300, 151-250: 0.180, 251+: 0.118
Avg final board read: -0.117
Avg absolute final board read: 0.121
Avg strong harsh board rate: 0.340
Avg strong generous board rate: 0.000
Avg final cutoff estimate: 73.34
Avg final cutoff uncertainty: 0.608
Avg low uncertainty rate: 0.000
Avg high cutoff rate: 0.810
Avg final safe floor: 57.27
```

### Run 4

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.620, avg_score=1775.2, median_score=1708.0, stdev=289.5, avg_strikes=2.99, first_out_rate=0.154
Contestant 2: win_rate=0.220, avg_score=1597.0, median_score=1587.0, stdev=205.4, avg_strikes=2.99, first_out_rate=0.453
Contestant 3: win_rate=0.160, avg_score=1352.8, median_score=1415.5, stdev=244.8, avg_strikes=2.99, first_out_rate=0.391
Last survivor but lost rate: 0.288
Solo started behind rate: 0.442
Solo started behind and lost rate: 0.652
Avg solo start deficit: 178.9
Avg solo turns taken: 2.26
Solo had winning answer rate: 0.119
Solo had winning answer given started behind rate: 0.268
Solo start deficit buckets: 1-75: 0.288, 76-150: 0.250, 151-250: 0.222, 251+: 0.240
Avg final board read: -0.087
Avg absolute final board read: 0.098
Strong harsh board rate: 0.270
Strong generous board rate: 0.000
Avg final cutoff estimate: 53.80
Avg final cutoff uncertainty: 0.330
Low uncertainty rate: 0.157
High cutoff rate: 0.172
Avg final safe floor: 40.51

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.951, avg_score=2474.1, median_score=2555.0, stdev=487.8, avg_strikes=3.00, first_out_rate=0.004
Contestant 2: win_rate=0.007, avg_score=928.8, median_score=911.0, stdev=229.3, avg_strikes=3.00, first_out_rate=0.873
Contestant 3: win_rate=0.042, avg_score=1005.7, median_score=985.0, stdev=261.0, avg_strikes=3.00, first_out_rate=0.124
Last survivor but lost rate: 0.057
Solo started behind rate: 0.113
Solo started behind and lost rate: 0.504
Avg solo start deficit: 148.1
Avg solo turns taken: 7.28
Solo had winning answer rate: 0.046
Solo had winning answer given started behind rate: 0.407
Solo start deficit buckets: 1-75: 0.359, 76-150: 0.248, 151-250: 0.207, 251+: 0.186
Avg final board read: -0.109
Avg absolute final board read: 0.115
Strong harsh board rate: 0.310
Strong generous board rate: 0.000
Avg final cutoff estimate: 62.67
Avg final cutoff uncertainty: 0.448
Low uncertainty rate: 0.005
High cutoff rate: 0.282
Avg final safe floor: 48.18

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.404, avg_score=1707.8, median_score=1695.0, stdev=96.4, avg_strikes=1.56, first_out_rate=0.002
Contestant 2: win_rate=0.371, avg_score=1684.7, median_score=1689.0, stdev=92.6, avg_strikes=2.17, first_out_rate=0.406
Contestant 3: win_rate=0.225, avg_score=1631.1, median_score=1642.0, stdev=106.7, avg_strikes=1.52, first_out_rate=0.120
Last survivor but lost rate: 0.151
Solo started behind rate: 0.251
Solo started behind and lost rate: 0.602
Avg solo start deficit: 94.7
Avg solo turns taken: 3.00
Solo had winning answer rate: 0.090
Solo had winning answer given started behind rate: 0.357
Solo start deficit buckets: 1-75: 0.434, 76-150: 0.389, 151-250: 0.159, 251+: 0.018
Avg final board read: -0.166
Avg absolute final board read: 0.167
Strong harsh board rate: 0.815
Strong generous board rate: 0.000
Avg final cutoff estimate: 31.07
Avg final cutoff uncertainty: 0.228
Low uncertainty rate: 0.785
High cutoff rate: 0.029
Avg final safe floor: 18.79

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.477, avg_score=1724.1, median_score=1695.0, stdev=161.2, avg_strikes=2.73, first_out_rate=0.130
Contestant 2: win_rate=0.281, avg_score=1641.3, median_score=1650.0, stdev=135.6, avg_strikes=2.87, first_out_rate=0.638
Contestant 3: win_rate=0.242, avg_score=1561.2, median_score=1596.0, stdev=174.6, avg_strikes=2.70, first_out_rate=0.165
Last survivor but lost rate: 0.372
Solo started behind rate: 0.503
Solo started behind and lost rate: 0.738
Avg solo start deficit: 149.5
Avg solo turns taken: 2.29
Solo had winning answer rate: 0.103
Solo had winning answer given started behind rate: 0.204
Solo start deficit buckets: 1-75: 0.303, 76-150: 0.325, 151-250: 0.233, 251+: 0.139
Avg final board read: -0.144
Avg absolute final board read: 0.146
Strong harsh board rate: 0.608
Strong generous board rate: 0.000
Avg final cutoff estimate: 40.09
Avg final cutoff uncertainty: 0.264
Low uncertainty rate: 0.521
High cutoff rate: 0.064
Avg final safe floor: 27.44

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.618, avg_score=1783.3, median_score=1996.0, stdev=772.4, avg_strikes=3.00, first_out_rate=0.024
Contestant 2: win_rate=0.368, avg_score=1437.8, median_score=1093.0, stdev=710.5, avg_strikes=3.00, first_out_rate=0.054
Contestant 3: win_rate=0.014, avg_score=658.1, median_score=644.0, stdev=215.4, avg_strikes=3.00, first_out_rate=0.922
Last survivor but lost rate: 0.125
Solo started behind rate: 0.330
Solo started behind and lost rate: 0.380
Avg solo start deficit: 108.9
Avg solo turns taken: 15.46
Solo had winning answer rate: 0.180
Solo had winning answer given started behind rate: 0.545
Solo start deficit buckets: 1-75: 0.444, 76-150: 0.302, 151-250: 0.167, 251+: 0.087
Avg final board read: -0.150
Avg absolute final board read: 0.150
Strong harsh board rate: 0.546
Strong generous board rate: 0.000
Avg final cutoff estimate: 65.17
Avg final cutoff uncertainty: 0.526
Low uncertainty rate: 0.000
High cutoff rate: 0.342
Avg final safe floor: 49.90

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.614, avg_score=1892.9, avg_median_score=1929.8, avg_stdev=361.5, avg_strikes=2.66, avg_first_out_rate=0.063
Contestant 2: avg_win_rate=0.249, avg_score=1457.9, avg_median_score=1386.0, avg_stdev=274.7, avg_strikes=2.81, avg_first_out_rate=0.485
Contestant 3: avg_win_rate=0.137, avg_score=1241.8, avg_median_score=1256.5, avg_stdev=200.5, avg_strikes=2.64, avg_first_out_rate=0.344
Last survivor but lost rate: 0.199
Solo started behind rate: 0.328
Solo started behind and lost rate: 0.575
Avg solo start deficit: 136.0
Avg solo turns taken: 6.06
Solo had winning answer rate: 0.107
Solo had winning answer given started behind rate: 0.356
Solo start deficit buckets: 1-75: 0.365, 76-150: 0.303, 151-250: 0.198, 251+: 0.134
Avg final board read: -0.131
Avg absolute final board read: 0.135
Avg strong harsh board rate: 0.510
Avg strong generous board rate: 0.000
Avg final cutoff estimate: 50.56
Avg final cutoff uncertainty: 0.359
Avg low uncertainty rate: 0.294
Avg high cutoff rate: 0.178
Avg final safe floor: 36.97
```

### Run 5

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.635, avg_score=1775.3, median_score=1711.0, stdev=289.1, avg_strikes=2.98, first_out_rate=0.154
Contestant 2: win_rate=0.193, avg_score=1585.3, median_score=1582.0, stdev=198.9, avg_strikes=2.99, first_out_rate=0.464
Contestant 3: win_rate=0.172, avg_score=1364.2, median_score=1426.0, stdev=247.5, avg_strikes=2.98, first_out_rate=0.378
Last survivor but lost rate: 0.297
Solo started behind rate: 0.444
Solo started behind and lost rate: 0.670
Avg solo start deficit: 176.2
Avg solo turns taken: 2.28
Solo had winning answer rate: 0.111
Solo had winning answer given started behind rate: 0.249
Solo start deficit buckets: 1-75: 0.274, 76-150: 0.261, 151-250: 0.222, 251+: 0.242
Avg final board read: -0.069
Avg absolute final board read: 0.085
Strong harsh board rate: 0.213
Strong generous board rate: 0.001
Avg final cutoff estimate: 53.27
Avg final cutoff uncertainty: 0.313
Low uncertainty rate: 0.204
High cutoff rate: 0.110
Avg final safe floor: 40.14

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.952, avg_score=2498.6, median_score=2574.0, stdev=479.3, avg_strikes=3.00, first_out_rate=0.003
Contestant 2: win_rate=0.009, avg_score=923.2, median_score=908.5, stdev=223.7, avg_strikes=3.00, first_out_rate=0.859
Contestant 3: win_rate=0.039, avg_score=991.3, median_score=972.0, stdev=254.7, avg_strikes=3.00, first_out_rate=0.139
Last survivor but lost rate: 0.051
Solo started behind rate: 0.115
Solo started behind and lost rate: 0.444
Avg solo start deficit: 127.8
Avg solo turns taken: 9.31
Solo had winning answer rate: 0.056
Solo had winning answer given started behind rate: 0.485
Solo start deficit buckets: 1-75: 0.425, 76-150: 0.239, 151-250: 0.183, 251+: 0.153
Avg final board read: -0.097
Avg absolute final board read: 0.107
Strong harsh board rate: 0.239
Strong generous board rate: 0.000
Avg final cutoff estimate: 62.85
Avg final cutoff uncertainty: 0.453
Low uncertainty rate: 0.005
High cutoff rate: 0.232
Avg final safe floor: 48.32

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.398, avg_score=1710.0, median_score=1696.0, stdev=97.9, avg_strikes=1.50, first_out_rate=0.002
Contestant 2: win_rate=0.345, avg_score=1676.3, median_score=1680.0, stdev=95.9, avg_strikes=2.13, first_out_rate=0.394
Contestant 3: win_rate=0.257, avg_score=1637.7, median_score=1652.0, stdev=110.3, avg_strikes=1.44, first_out_rate=0.115
Last survivor but lost rate: 0.120
Solo started behind rate: 0.211
Solo started behind and lost rate: 0.569
Avg solo start deficit: 88.1
Avg solo turns taken: 2.98
Solo had winning answer rate: 0.083
Solo had winning answer given started behind rate: 0.393
Solo start deficit buckets: 1-75: 0.495, 76-150: 0.344, 151-250: 0.142, 251+: 0.019
Avg final board read: -0.163
Avg absolute final board read: 0.164
Strong harsh board rate: 0.812
Strong generous board rate: 0.000
Avg final cutoff estimate: 28.38
Avg final cutoff uncertainty: 0.187
Low uncertainty rate: 0.901
High cutoff rate: 0.005
Avg final safe floor: 16.51

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.488, avg_score=1725.5, median_score=1701.0, stdev=160.5, avg_strikes=2.69, first_out_rate=0.130
Contestant 2: win_rate=0.259, avg_score=1632.9, median_score=1645.0, stdev=139.4, avg_strikes=2.85, first_out_rate=0.639
Contestant 3: win_rate=0.253, avg_score=1568.7, median_score=1608.0, stdev=176.7, avg_strikes=2.67, first_out_rate=0.157
Last survivor but lost rate: 0.363
Solo started behind rate: 0.495
Solo started behind and lost rate: 0.734
Avg solo start deficit: 151.6
Avg solo turns taken: 2.24
Solo had winning answer rate: 0.107
Solo had winning answer given started behind rate: 0.216
Solo start deficit buckets: 1-75: 0.317, 76-150: 0.313, 151-250: 0.213, 251+: 0.157
Avg final board read: -0.132
Avg absolute final board read: 0.137
Strong harsh board rate: 0.553
Strong generous board rate: 0.000
Avg final cutoff estimate: 39.16
Avg final cutoff uncertainty: 0.234
Low uncertainty rate: 0.622
High cutoff rate: 0.029
Avg final safe floor: 26.82

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.613, avg_score=1805.6, median_score=2078.0, stdev=780.4, avg_strikes=3.00, first_out_rate=0.020
Contestant 2: win_rate=0.374, avg_score=1450.3, median_score=1094.0, stdev=723.3, avg_strikes=3.00, first_out_rate=0.042
Contestant 3: win_rate=0.012, avg_score=640.3, median_score=628.0, stdev=207.9, avg_strikes=3.00, first_out_rate=0.938
Last survivor but lost rate: 0.106
Solo started behind rate: 0.314
Solo started behind and lost rate: 0.337
Avg solo start deficit: 101.7
Avg solo turns taken: 16.57
Solo had winning answer rate: 0.184
Solo had winning answer given started behind rate: 0.584
Solo start deficit buckets: 1-75: 0.489, 76-150: 0.273, 151-250: 0.164, 251+: 0.073
Avg final board read: -0.140
Avg absolute final board read: 0.140
Strong harsh board rate: 0.456
Strong generous board rate: 0.000
Avg final cutoff estimate: 65.12
Avg final cutoff uncertainty: 0.534
Low uncertainty rate: 0.000
High cutoff rate: 0.311
Avg final safe floor: 49.78

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.617, avg_score=1903.0, avg_median_score=1952.0, avg_stdev=361.4, avg_strikes=2.63, avg_first_out_rate=0.062
Contestant 2: avg_win_rate=0.236, avg_score=1453.6, avg_median_score=1381.9, avg_stdev=276.3, avg_strikes=2.80, avg_first_out_rate=0.480
Contestant 3: avg_win_rate=0.147, avg_score=1240.4, avg_median_score=1257.2, avg_stdev=199.4, avg_strikes=2.62, avg_first_out_rate=0.345
Last survivor but lost rate: 0.188
Solo started behind rate: 0.316
Solo started behind and lost rate: 0.551
Avg solo start deficit: 129.1
Avg solo turns taken: 6.68
Solo had winning answer rate: 0.108
Solo had winning answer given started behind rate: 0.386
Solo start deficit buckets: 1-75: 0.400, 76-150: 0.286, 151-250: 0.185, 251+: 0.129
Avg final board read: -0.120
Avg absolute final board read: 0.127
Avg strong harsh board rate: 0.455
Avg strong generous board rate: 0.000
Avg final cutoff estimate: 49.76
Avg final cutoff uncertainty: 0.344
Avg low uncertainty rate: 0.346
Avg high cutoff rate: 0.138
Avg final safe floor: 36.32
```

### Run 6

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.648, avg_score=1778.8, median_score=1719.0, stdev=287.4, avg_strikes=2.97, first_out_rate=0.149
Contestant 2: win_rate=0.179, avg_score=1581.2, median_score=1579.0, stdev=202.1, avg_strikes=2.98, first_out_rate=0.448
Contestant 3: win_rate=0.173, avg_score=1372.8, median_score=1443.0, stdev=250.3, avg_strikes=2.97, first_out_rate=0.396
Last survivor but lost rate: 0.266
Solo started behind rate: 0.408
Solo started behind and lost rate: 0.651
Avg solo start deficit: 162.3
Avg solo turns taken: 2.28
Solo had winning answer rate: 0.109
Solo had winning answer given started behind rate: 0.267
Solo start deficit buckets: 1-75: 0.302, 76-150: 0.280, 151-250: 0.221, 251+: 0.197
Avg final board read: -0.064
Avg absolute final board read: 0.080
Strong harsh board rate: 0.167
Strong generous board rate: 0.001
Avg final cutoff estimate: 63.94
Avg final cutoff uncertainty: 0.362
Low uncertainty rate: 0.004
High cutoff rate: 0.217
Avg final safe floor: 50.32

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.951, avg_score=2501.8, median_score=2573.0, stdev=480.7, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.012, avg_score=924.8, median_score=912.0, stdev=223.2, avg_strikes=3.00, first_out_rate=0.850
Contestant 3: win_rate=0.037, avg_score=986.7, median_score=970.5, stdev=254.4, avg_strikes=3.00, first_out_rate=0.149
Last survivor but lost rate: 0.048
Solo started behind rate: 0.118
Solo started behind and lost rate: 0.408
Avg solo start deficit: 119.3
Avg solo turns taken: 10.14
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.520
Solo start deficit buckets: 1-75: 0.438, 76-150: 0.269, 151-250: 0.175, 251+: 0.118
Avg final board read: -0.099
Avg absolute final board read: 0.109
Strong harsh board rate: 0.253
Strong generous board rate: 0.000
Avg final cutoff estimate: 69.21
Avg final cutoff uncertainty: 0.480
Low uncertainty rate: 0.000
High cutoff rate: 0.485
Avg final safe floor: 54.41

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.435, avg_score=1718.0, median_score=1708.0, stdev=97.4, avg_strikes=1.24, first_out_rate=0.001
Contestant 2: win_rate=0.283, avg_score=1657.9, median_score=1670.0, stdev=98.2, avg_strikes=2.03, first_out_rate=0.346
Contestant 3: win_rate=0.281, avg_score=1654.4, median_score=1671.0, stdev=113.8, avg_strikes=1.13, first_out_rate=0.095
Last survivor but lost rate: 0.063
Solo started behind rate: 0.129
Solo started behind and lost rate: 0.490
Avg solo start deficit: 71.0
Avg solo turns taken: 2.71
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.473
Solo start deficit buckets: 1-75: 0.604, 76-150: 0.315, 151-250: 0.066, 251+: 0.016
Avg final board read: -0.145
Avg absolute final board read: 0.145
Strong harsh board rate: 0.581
Strong generous board rate: 0.000
Avg final cutoff estimate: 44.73
Avg final cutoff uncertainty: 0.279
Low uncertainty rate: 0.271
High cutoff rate: 0.032
Avg final safe floor: 31.94

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.529, avg_score=1735.5, median_score=1716.0, stdev=159.8, avg_strikes=2.52, first_out_rate=0.123
Contestant 2: win_rate=0.193, avg_score=1616.2, median_score=1630.5, stdev=139.9, avg_strikes=2.79, first_out_rate=0.606
Contestant 3: win_rate=0.278, avg_score=1584.9, median_score=1630.0, stdev=179.6, avg_strikes=2.50, first_out_rate=0.159
Last survivor but lost rate: 0.272
Solo started behind rate: 0.400
Solo started behind and lost rate: 0.679
Avg solo start deficit: 139.2
Avg solo turns taken: 2.12
Solo had winning answer rate: 0.106
Solo had winning answer given started behind rate: 0.264
Solo start deficit buckets: 1-75: 0.393, 76-150: 0.316, 151-250: 0.166, 251+: 0.125
Avg final board read: -0.116
Avg absolute final board read: 0.120
Strong harsh board rate: 0.398
Strong generous board rate: 0.000
Avg final cutoff estimate: 55.19
Avg final cutoff uncertainty: 0.314
Low uncertainty rate: 0.065
High cutoff rate: 0.084
Avg final safe floor: 42.05

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.614, avg_score=1802.9, median_score=2063.0, stdev=782.7, avg_strikes=3.00, first_out_rate=0.018
Contestant 2: win_rate=0.375, avg_score=1452.3, median_score=1094.0, stdev=726.3, avg_strikes=3.00, first_out_rate=0.039
Contestant 3: win_rate=0.011, avg_score=638.2, median_score=626.0, stdev=205.7, avg_strikes=3.00, first_out_rate=0.943
Last survivor but lost rate: 0.109
Solo started behind rate: 0.321
Solo started behind and lost rate: 0.340
Avg solo start deficit: 102.3
Avg solo turns taken: 16.81
Solo had winning answer rate: 0.187
Solo had winning answer given started behind rate: 0.582
Solo start deficit buckets: 1-75: 0.477, 76-150: 0.293, 151-250: 0.160, 251+: 0.070
Avg final board read: -0.140
Avg absolute final board read: 0.141
Strong harsh board rate: 0.462
Strong generous board rate: 0.000
Avg final cutoff estimate: 70.31
Avg final cutoff uncertainty: 0.549
Low uncertainty rate: 0.000
High cutoff rate: 0.536
Avg final safe floor: 54.82

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.635, avg_score=1907.4, avg_median_score=1955.8, avg_stdev=361.6, avg_strikes=2.55, avg_first_out_rate=0.058
Contestant 2: avg_win_rate=0.208, avg_score=1446.5, avg_median_score=1377.1, avg_stdev=278.0, avg_strikes=2.76, avg_first_out_rate=0.458
Contestant 3: avg_win_rate=0.156, avg_score=1247.4, avg_median_score=1268.1, avg_stdev=200.8, avg_strikes=2.52, avg_first_out_rate=0.348
Last survivor but lost rate: 0.152
Solo started behind rate: 0.275
Solo started behind and lost rate: 0.514
Avg solo start deficit: 118.8
Avg solo turns taken: 6.81
Solo had winning answer rate: 0.105
Solo had winning answer given started behind rate: 0.421
Solo start deficit buckets: 1-75: 0.443, 76-150: 0.295, 151-250: 0.158, 251+: 0.105
Avg final board read: -0.113
Avg absolute final board read: 0.119
Avg strong harsh board rate: 0.372
Avg strong generous board rate: 0.000
Avg final cutoff estimate: 60.68
Avg final cutoff uncertainty: 0.397
Avg low uncertainty rate: 0.068
Avg high cutoff rate: 0.271
Avg final safe floor: 46.71
```

### Run 7 (Final M2)

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.648, avg_score=1778.8, median_score=1719.0, stdev=287.4, avg_strikes=2.97, first_out_rate=0.149
Contestant 2: win_rate=0.179, avg_score=1581.2, median_score=1579.0, stdev=202.1, avg_strikes=2.98, first_out_rate=0.448
Contestant 3: win_rate=0.173, avg_score=1372.8, median_score=1443.0, stdev=250.3, avg_strikes=2.97, first_out_rate=0.396
Last survivor but lost rate: 0.266
Solo started behind rate: 0.408
Solo started behind and lost rate: 0.651
Avg solo start deficit: 162.3
Avg solo turns taken: 2.28
Solo had winning answer rate: 0.109
Solo had winning answer given started behind rate: 0.267
Solo start deficit buckets: 1-75: 0.302, 76-150: 0.280, 151-250: 0.221, 251+: 0.197
Avg final board read: -0.064
Avg absolute final board read: 0.080
Strong harsh board rate: 0.167
Strong generous board rate: 0.001
Avg final cutoff estimate: 63.94
Avg final cutoff uncertainty: 0.362
Low uncertainty rate: 0.004
High cutoff rate: 0.217
Avg final safe floor: 51.77

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.951, avg_score=2501.8, median_score=2573.0, stdev=480.7, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.012, avg_score=924.8, median_score=912.0, stdev=223.2, avg_strikes=3.00, first_out_rate=0.850
Contestant 3: win_rate=0.037, avg_score=986.7, median_score=970.5, stdev=254.4, avg_strikes=3.00, first_out_rate=0.149
Last survivor but lost rate: 0.048
Solo started behind rate: 0.118
Solo started behind and lost rate: 0.408
Avg solo start deficit: 119.3
Avg solo turns taken: 10.14
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.520
Solo start deficit buckets: 1-75: 0.438, 76-150: 0.269, 151-250: 0.175, 251+: 0.118
Avg final board read: -0.099
Avg absolute final board read: 0.109
Strong harsh board rate: 0.253
Strong generous board rate: 0.000
Avg final cutoff estimate: 69.21
Avg final cutoff uncertainty: 0.480
Low uncertainty rate: 0.000
High cutoff rate: 0.485
Avg final safe floor: 56.33

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.435, avg_score=1718.0, median_score=1708.0, stdev=97.4, avg_strikes=1.24, first_out_rate=0.001
Contestant 2: win_rate=0.283, avg_score=1657.9, median_score=1670.0, stdev=98.2, avg_strikes=2.03, first_out_rate=0.346
Contestant 3: win_rate=0.281, avg_score=1654.4, median_score=1671.0, stdev=113.8, avg_strikes=1.13, first_out_rate=0.095
Last survivor but lost rate: 0.063
Solo started behind rate: 0.129
Solo started behind and lost rate: 0.490
Avg solo start deficit: 71.0
Avg solo turns taken: 2.71
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.473
Solo start deficit buckets: 1-75: 0.604, 76-150: 0.315, 151-250: 0.066, 251+: 0.016
Avg final board read: -0.145
Avg absolute final board read: 0.145
Strong harsh board rate: 0.581
Strong generous board rate: 0.000
Avg final cutoff estimate: 44.73
Avg final cutoff uncertainty: 0.279
Low uncertainty rate: 0.271
High cutoff rate: 0.032
Avg final safe floor: 33.05

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.529, avg_score=1735.5, median_score=1716.0, stdev=159.8, avg_strikes=2.52, first_out_rate=0.123
Contestant 2: win_rate=0.193, avg_score=1616.2, median_score=1630.5, stdev=139.9, avg_strikes=2.79, first_out_rate=0.606
Contestant 3: win_rate=0.278, avg_score=1584.9, median_score=1630.0, stdev=179.6, avg_strikes=2.50, first_out_rate=0.159
Last survivor but lost rate: 0.272
Solo started behind rate: 0.400
Solo started behind and lost rate: 0.679
Avg solo start deficit: 139.2
Avg solo turns taken: 2.12
Solo had winning answer rate: 0.106
Solo had winning answer given started behind rate: 0.264
Solo start deficit buckets: 1-75: 0.393, 76-150: 0.316, 151-250: 0.166, 251+: 0.125
Avg final board read: -0.116
Avg absolute final board read: 0.120
Strong harsh board rate: 0.398
Strong generous board rate: 0.000
Avg final cutoff estimate: 55.19
Avg final cutoff uncertainty: 0.314
Low uncertainty rate: 0.065
High cutoff rate: 0.084
Avg final safe floor: 43.30

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.614, avg_score=1802.9, median_score=2063.0, stdev=782.7, avg_strikes=3.00, first_out_rate=0.018
Contestant 2: win_rate=0.375, avg_score=1452.3, median_score=1094.0, stdev=726.3, avg_strikes=3.00, first_out_rate=0.039
Contestant 3: win_rate=0.011, avg_score=638.2, median_score=626.0, stdev=205.7, avg_strikes=3.00, first_out_rate=0.943
Last survivor but lost rate: 0.109
Solo started behind rate: 0.321
Solo started behind and lost rate: 0.340
Avg solo start deficit: 102.3
Avg solo turns taken: 16.81
Solo had winning answer rate: 0.187
Solo had winning answer given started behind rate: 0.582
Solo start deficit buckets: 1-75: 0.477, 76-150: 0.293, 151-250: 0.160, 251+: 0.070
Avg final board read: -0.140
Avg absolute final board read: 0.141
Strong harsh board rate: 0.462
Strong generous board rate: 0.000
Avg final cutoff estimate: 70.31
Avg final cutoff uncertainty: 0.549
Low uncertainty rate: 0.000
High cutoff rate: 0.536
Avg final safe floor: 57.02

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.635, avg_score=1907.4, avg_median_score=1955.8, avg_stdev=361.6, avg_strikes=2.55, avg_first_out_rate=0.058
Contestant 2: avg_win_rate=0.208, avg_score=1446.5, avg_median_score=1377.1, avg_stdev=278.0, avg_strikes=2.76, avg_first_out_rate=0.458
Contestant 3: avg_win_rate=0.156, avg_score=1247.4, avg_median_score=1268.1, avg_stdev=200.8, avg_strikes=2.52, avg_first_out_rate=0.348
Last survivor but lost rate: 0.152
Solo started behind rate: 0.275
Solo started behind and lost rate: 0.514
Avg solo start deficit: 118.8
Avg solo turns taken: 6.81
Solo had winning answer rate: 0.105
Solo had winning answer given started behind rate: 0.421
Solo start deficit buckets: 1-75: 0.443, 76-150: 0.295, 151-250: 0.158, 251+: 0.105
Avg final board read: -0.113
Avg absolute final board read: 0.119
Avg strong harsh board rate: 0.372
Avg strong generous board rate: 0.000
Avg final cutoff estimate: 60.68
Avg final cutoff uncertainty: 0.397
Avg low uncertainty rate: 0.068
Avg high cutoff rate: 0.271
Avg final safe floor: 48.30
```

**M2 Outcomes:**
- Successfully introduced belief-drawn cutoff estimation
- Behavior now adapts dyamically to inferred board state
- Category-dependent gameplay is preserved

**Remaining Issues:**
- Board feel (harsh vs generous) is imbalanced
- No modeling of density / clustering
- No phase-shift behavior ('heating up')

---

## Milestone 3 - Precision and Category Shape Modeling