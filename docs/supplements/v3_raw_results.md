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

**Summary**:

M3 introduced lightweight board-shape inference on top of the existing cutoff estimation from M2.

The main goal was to begin separating where players think the line is and how forgiving the board feels around that line.

M3 added tracking for:
- local density near the cutoff
- surprise / expectation mismatch
- near-cutoff hits and misses

The milestones did not dramatically change gameplay outcomes, because the new signals are mostly observational at this stage. However, the added metrics provide useful diagnostics for future strategy logic and reveal important limits of the current abstract 1–100 answer model.

**Observed Progression:**
- Runs 1 and 2:
    - Initial M3 signals worked, but skewed heavily toward open/generous board interpretations
    - Local density and surprise both trended positive
    - Near-cutoff hits greatly outnumbered near-cutoff misses, causing density to overstate how open the board was
- Run 3:
    - Restored near-cutoff miss tracking
    - This made the miss metric technically active again, but near-cutoff misses remained extremely rare
    - Results were nearly identical to Run 2, showing that the issue was structural rather than a simple missing counter
- Runs 4 and 5:
    - Added an expected-hit-rate baseline and stronger density decay to reduce inflated local density readings
    - Adjusted surprise logic to reduce over-positive surprise accumulation
    - Final M3 state kept M2 behavior stable while producing more balanced board-shaped diagnostics

**Key Insights:**
1. M3 did not disrupt the M2 cutoff system
- Across M3 tuning, cutoff estimate and safe floor stayed stable
- Final M3 aggregate cutoff estimate remained around ~60
- Final safe flooor remained around ~48

2. Local density required a baseline correction
- Raw near-cutoff hit/miss tracking made the board look too open
- Near-cutoff hits greatly outmumbered near-cutoff misses
- Using an exepcted-hit-rate baseline produced a more realistic density signal

3. Surprise was intially too positive
- Early M3 runs treated too many low correct answers are generous surprises
- Later tuning reduced surprised accumulation without destabilizing gameplay
- This made board perception less generous-skewed

4. Near-cutoff misses remain structurally rare
- Even after restoring miss tracking, near-cutoff misses stayed very low
- This limits how much the current M3 system can infer about board tightness
- This likely reflects the currect abstract answer model more than a tuning issue

5. M3 is useful as a lightweight inference layer, not a full board-shape engine
- The model now tracts density and surprise
- However, true board-shape realism likely requires deeper candidate-generation, category-shape, or real-data modeling in a future version

### Run 1:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.643, avg_score=1776.6, median_score=1723.0, stdev=289.5, avg_strikes=2.95, first_out_rate=0.156
Contestant 2: win_rate=0.165, avg_score=1575.4, median_score=1574.0, stdev=204.5, avg_strikes=2.98, first_out_rate=0.452
Contestant 3: win_rate=0.192, avg_score=1385.5, median_score=1464.0, stdev=258.6, avg_strikes=2.96, first_out_rate=0.385
Last survivor but lost rate: 0.256
Solo started behind rate: 0.384
Solo started behind and lost rate: 0.666
Avg solo start deficit: 164.6
Avg solo turns taken: 2.24
Solo had winning answer rate: 0.102
Solo had winning answer given started behind rate: 0.267
Solo start deficit buckets: 1-75: 0.300, 76-150: 0.280, 151-250: 0.210, 251+: 0.210
Avg final board read: 0.091
Avg absolute final board read: 0.105
Strong harsh board rate: 0.000
Strong generous board rate: 0.251
Avg final cutoff estimate: 62.91
Avg final cutoff uncertainty: 0.355
Low uncertainty rate: 0.006
High cutoff rate: 0.190
Avg final safe floor: 50.78
Avg final local density read: 0.245
Avg final surprise read: 0.354
Avg final near-cutoff hits: 2.22
Avg final near-cutoff misses: 0.01

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.941, avg_score=2469.3, median_score=2550.0, stdev=502.3, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.010, avg_score=928.7, median_score=914.0, stdev=225.7, avg_strikes=3.00, first_out_rate=0.849
Contestant 3: win_rate=0.049, avg_score=1009.2, median_score=989.0, stdev=271.0, avg_strikes=3.00, first_out_rate=0.148
Last survivor but lost rate: 0.056
Solo started behind rate: 0.132
Solo started behind and lost rate: 0.428
Avg solo start deficit: 119.6
Avg solo turns taken: 9.86
Solo had winning answer rate: 0.066
Solo had winning answer given started behind rate: 0.504
Solo start deficit buckets: 1-75: 0.431, 76-150: 0.259, 151-250: 0.199, 251+: 0.112
Avg final board read: 0.048
Avg absolute final board read: 0.063
Strong harsh board rate: 0.000
Strong generous board rate: 0.111
Avg final cutoff estimate: 69.26
Avg final cutoff uncertainty: 0.475
Low uncertainty rate: 0.000
High cutoff rate: 0.495
Avg final safe floor: 56.41
Avg final local density read: 0.234
Avg final surprise read: 0.434
Avg final near-cutoff hits: 1.31
Avg final near-cutoff misses: 0.05

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.550, avg_score=1737.1, median_score=1730.0, stdev=91.3, avg_strikes=0.89, first_out_rate=0.001
Contestant 2: win_rate=0.200, avg_score=1648.6, median_score=1664.0, stdev=96.9, avg_strikes=2.01, first_out_rate=0.364
Contestant 3: win_rate=0.250, avg_score=1656.4, median_score=1673.0, stdev=115.5, avg_strikes=0.74, first_out_rate=0.087
Last survivor but lost rate: 0.037
Solo started behind rate: 0.058
Solo started behind and lost rate: 0.641
Avg solo start deficit: 105.1
Avg solo turns taken: 1.81
Solo had winning answer rate: 0.018
Solo had winning answer given started behind rate: 0.314
Solo start deficit buckets: 1-75: 0.357, 76-150: 0.447, 151-250: 0.158, 251+: 0.038
Avg final board read: -0.033
Avg absolute final board read: 0.055
Strong harsh board rate: 0.011
Strong generous board rate: 0.010
Avg final cutoff estimate: 44.97
Avg final cutoff uncertainty: 0.271
Low uncertainty rate: 0.324
High cutoff rate: 0.032
Avg final safe floor: 33.35
Avg final local density read: 0.356
Avg final surprise read: 0.286
Avg final near-cutoff hits: 2.81
Avg final near-cutoff misses: 0.00

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.608, avg_score=1749.3, median_score=1742.0, stdev=159.0, avg_strikes=2.32, first_out_rate=0.133
Contestant 2: win_rate=0.125, avg_score=1604.4, median_score=1624.0, stdev=144.2, avg_strikes=2.72, first_out_rate=0.613
Contestant 3: win_rate=0.267, avg_score=1594.8, median_score=1641.0, stdev=184.9, avg_strikes=2.28, first_out_rate=0.134
Last survivor but lost rate: 0.253
Solo started behind rate: 0.340
Solo started behind and lost rate: 0.745
Avg solo start deficit: 154.2
Avg solo turns taken: 1.84
Solo had winning answer rate: 0.070
Solo had winning answer given started behind rate: 0.207
Solo start deficit buckets: 1-75: 0.341, 76-150: 0.327, 151-250: 0.175, 251+: 0.157
Avg final board read: 0.021
Avg absolute final board read: 0.066
Strong harsh board rate: 0.001
Strong generous board rate: 0.085
Avg final cutoff estimate: 54.62
Avg final cutoff uncertainty: 0.305
Low uncertainty rate: 0.091
High cutoff rate: 0.066
Avg final safe floor: 42.79
Avg final local density read: 0.291
Avg final surprise read: 0.324
Avg final near-cutoff hits: 2.46
Avg final near-cutoff misses: 0.00

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.616, avg_score=1772.5, median_score=1938.5, stdev=759.9, avg_strikes=3.00, first_out_rate=0.032
Contestant 2: win_rate=0.354, avg_score=1416.5, median_score=1094.0, stdev=695.3, avg_strikes=3.00, first_out_rate=0.071
Contestant 3: win_rate=0.030, avg_score=691.0, median_score=659.0, stdev=251.7, avg_strikes=3.00, first_out_rate=0.897
Last survivor but lost rate: 0.127
Solo started behind rate: 0.337
Solo started behind and lost rate: 0.376
Avg solo start deficit: 108.0
Avg solo turns taken: 14.94
Solo had winning answer rate: 0.186
Solo had winning answer given started behind rate: 0.552
Solo start deficit buckets: 1-75: 0.453, 76-150: 0.293, 151-250: 0.174, 251+: 0.080
Avg final board read: 0.004
Avg absolute final board read: 0.040
Strong harsh board rate: 0.006
Strong generous board rate: 0.010
Avg final cutoff estimate: 70.38
Avg final cutoff uncertainty: 0.537
Low uncertainty rate: 0.000
High cutoff rate: 0.540
Avg final safe floor: 57.16
Avg final local density read: 0.218
Avg final surprise read: 0.459
Avg final near-cutoff hits: 0.88
Avg final near-cutoff misses: 0.09

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.672, avg_score=1901.0, avg_median_score=1936.7, avg_stdev=360.4, avg_strikes=2.43, avg_first_out_rate=0.065
Contestant 2: avg_win_rate=0.171, avg_score=1434.7, avg_median_score=1374.0, avg_stdev=273.3, avg_strikes=2.74, avg_first_out_rate=0.470
Contestant 3: avg_win_rate=0.158, avg_score=1267.4, avg_median_score=1285.2, avg_stdev=216.3, avg_strikes=2.40, avg_first_out_rate=0.330
Last survivor but lost rate: 0.146
Solo started behind rate: 0.250
Solo started behind and lost rate: 0.571
Avg solo start deficit: 130.3
Avg solo turns taken: 6.14
Solo had winning answer rate: 0.089
Solo had winning answer given started behind rate: 0.369
Solo start deficit buckets: 1-75: 0.376, 76-150: 0.321, 151-250: 0.183, 251+: 0.119
Avg final board read: 0.026
Avg absolute final board read: 0.066
Avg strong harsh board rate: 0.004
Avg strong generous board rate: 0.093
Avg final cutoff estimate: 60.43
Avg final cutoff uncertainty: 0.389
Avg low uncertainty rate: 0.084
Avg high cutoff rate: 0.265
Avg final safe floor: 48.10
Avg final local density read: 0.269
Avg final surprise read: 0.371
Avg final near-cutoff hits: 1.94
Avg final near-cutoff misses: 0.03
```

### Run 2:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.649, avg_score=1778.2, median_score=1725.0, stdev=288.3, avg_strikes=2.95, first_out_rate=0.154
Contestant 2: win_rate=0.163, avg_score=1576.0, median_score=1574.0, stdev=203.2, avg_strikes=2.97, first_out_rate=0.449
Contestant 3: win_rate=0.187, avg_score=1383.2, median_score=1460.0, stdev=256.9, avg_strikes=2.96, first_out_rate=0.389
Last survivor but lost rate: 0.256
Solo started behind rate: 0.383
Solo started behind and lost rate: 0.668
Avg solo start deficit: 163.2
Avg solo turns taken: 2.24
Solo had winning answer rate: 0.101
Solo had winning answer given started behind rate: 0.262
Solo start deficit buckets: 1-75: 0.306, 76-150: 0.273, 151-250: 0.218, 251+: 0.202
Avg final board read: 0.085
Avg absolute final board read: 0.105
Strong harsh board rate: 0.001
Strong generous board rate: 0.236
Avg final cutoff estimate: 63.15
Avg final cutoff uncertainty: 0.356
Low uncertainty rate: 0.006
High cutoff rate: 0.193
Avg final safe floor: 51.01
Avg final local density read: 0.294
Avg final surprise read: 0.338
Avg final near-cutoff hits: 3.45
Avg final near-cutoff misses: 0.00

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.946, avg_score=2480.5, median_score=2556.0, stdev=493.8, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.009, avg_score=927.3, median_score=913.0, stdev=225.4, avg_strikes=3.00, first_out_rate=0.851
Contestant 3: win_rate=0.045, avg_score=1003.3, median_score=981.0, stdev=266.2, avg_strikes=3.00, first_out_rate=0.147
Last survivor but lost rate: 0.053
Solo started behind rate: 0.124
Solo started behind and lost rate: 0.426
Avg solo start deficit: 119.1
Avg solo turns taken: 9.83
Solo had winning answer rate: 0.063
Solo had winning answer given started behind rate: 0.508
Solo start deficit buckets: 1-75: 0.436, 76-150: 0.267, 151-250: 0.182, 251+: 0.116
Avg final board read: 0.029
Avg absolute final board read: 0.072
Strong harsh board rate: 0.010
Strong generous board rate: 0.116
Avg final cutoff estimate: 69.34
Avg final cutoff uncertainty: 0.476
Low uncertainty rate: 0.000
High cutoff rate: 0.502
Avg final safe floor: 56.49
Avg final local density read: 0.270
Avg final surprise read: 0.413
Avg final near-cutoff hits: 2.12
Avg final near-cutoff misses: 0.00

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.543, avg_score=1736.0, median_score=1728.0, stdev=91.8, avg_strikes=0.91, first_out_rate=0.001
Contestant 2: win_rate=0.204, avg_score=1648.3, median_score=1664.0, stdev=96.7, avg_strikes=2.01, first_out_rate=0.369
Contestant 3: win_rate=0.253, avg_score=1657.3, median_score=1674.0, stdev=115.1, avg_strikes=0.76, first_out_rate=0.082
Last survivor but lost rate: 0.038
Solo started behind rate: 0.061
Solo started behind and lost rate: 0.621
Avg solo start deficit: 100.3
Avg solo turns taken: 1.89
Solo had winning answer rate: 0.021
Solo had winning answer given started behind rate: 0.333
Solo start deficit buckets: 1-75: 0.392, 76-150: 0.444, 151-250: 0.130, 251+: 0.034
Avg final board read: -0.054
Avg absolute final board read: 0.076
Strong harsh board rate: 0.050
Strong generous board rate: 0.009
Avg final cutoff estimate: 45.05
Avg final cutoff uncertainty: 0.272
Low uncertainty rate: 0.315
High cutoff rate: 0.032
Avg final safe floor: 33.42
Avg final local density read: 0.413
Avg final surprise read: 0.245
Avg final near-cutoff hits: 4.19
Avg final near-cutoff misses: 0.00

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.604, avg_score=1748.8, median_score=1741.0, stdev=158.2, avg_strikes=2.32, first_out_rate=0.132
Contestant 2: win_rate=0.130, avg_score=1605.4, median_score=1624.0, stdev=143.6, avg_strikes=2.72, first_out_rate=0.611
Contestant 3: win_rate=0.266, avg_score=1593.8, median_score=1639.0, stdev=184.3, avg_strikes=2.29, first_out_rate=0.137
Last survivor but lost rate: 0.257
Solo started behind rate: 0.347
Solo started behind and lost rate: 0.740
Avg solo start deficit: 152.7
Avg solo turns taken: 1.85
Solo had winning answer rate: 0.074
Solo had winning answer given started behind rate: 0.213
Solo start deficit buckets: 1-75: 0.337, 76-150: 0.334, 151-250: 0.177, 251+: 0.153
Avg final board read: 0.009
Avg absolute final board read: 0.078
Strong harsh board rate: 0.011
Strong generous board rate: 0.081
Avg final cutoff estimate: 54.79
Avg final cutoff uncertainty: 0.306
Low uncertainty rate: 0.086
High cutoff rate: 0.067
Avg final safe floor: 42.95
Avg final local density read: 0.367
Avg final surprise read: 0.290
Avg final near-cutoff hits: 3.82
Avg final near-cutoff misses: 0.00

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.616, avg_score=1780.0, median_score=1969.0, stdev=767.0, avg_strikes=3.00, first_out_rate=0.029
Contestant 2: win_rate=0.360, avg_score=1427.6, median_score=1092.0, stdev=705.9, avg_strikes=3.00, first_out_rate=0.070
Contestant 3: win_rate=0.024, avg_score=675.6, median_score=647.0, stdev=242.9, avg_strikes=3.00, first_out_rate=0.900
Last survivor but lost rate: 0.121
Solo started behind rate: 0.331
Solo started behind and lost rate: 0.365
Avg solo start deficit: 107.6
Avg solo turns taken: 15.51
Solo had winning answer rate: 0.185
Solo had winning answer given started behind rate: 0.559
Solo start deficit buckets: 1-75: 0.456, 76-150: 0.297, 151-250: 0.164, 251+: 0.083
Avg final board read: -0.029
Avg absolute final board read: 0.064
Strong harsh board rate: 0.063
Strong generous board rate: 0.011
Avg final cutoff estimate: 70.36
Avg final cutoff uncertainty: 0.541
Low uncertainty rate: 0.000
High cutoff rate: 0.542
Avg final safe floor: 57.11
Avg final local density read: 0.249
Avg final surprise read: 0.430
Avg final near-cutoff hits: 1.59
Avg final near-cutoff misses: 0.00

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.672, avg_score=1904.7, avg_median_score=1943.8, avg_stdev=359.8, avg_strikes=2.44, avg_first_out_rate=0.064
Contestant 2: avg_win_rate=0.173, avg_score=1437.0, avg_median_score=1373.4, avg_stdev=275.0, avg_strikes=2.74, avg_first_out_rate=0.470
Contestant 3: avg_win_rate=0.155, avg_score=1262.7, avg_median_score=1280.2, avg_stdev=213.1, avg_strikes=2.40, avg_first_out_rate=0.331
Last survivor but lost rate: 0.145
Solo started behind rate: 0.250
Solo started behind and lost rate: 0.564
Avg solo start deficit: 128.6
Avg solo turns taken: 6.27
Solo had winning answer rate: 0.089
Solo had winning answer given started behind rate: 0.375
Solo start deficit buckets: 1-75: 0.385, 76-150: 0.323, 151-250: 0.174, 251+: 0.118
Avg final board read: 0.008
Avg absolute final board read: 0.079
Avg strong harsh board rate: 0.027
Avg strong generous board rate: 0.091
Avg final cutoff estimate: 60.54
Avg final cutoff uncertainty: 0.390
Avg low uncertainty rate: 0.081
Avg high cutoff rate: 0.267
Avg final safe floor: 48.20
Avg final local density read: 0.319
Avg final surprise read: 0.343
Avg final near-cutoff hits: 3.03
Avg final near-cutoff misses: 0.00
```

### Run 3:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.649, avg_score=1778.2, median_score=1725.0, stdev=288.3, avg_strikes=2.95, first_out_rate=0.154
Contestant 2: win_rate=0.163, avg_score=1576.0, median_score=1574.0, stdev=203.2, avg_strikes=2.97, first_out_rate=0.449
Contestant 3: win_rate=0.187, avg_score=1383.2, median_score=1460.0, stdev=256.9, avg_strikes=2.96, first_out_rate=0.389
Last survivor but lost rate: 0.256
Solo started behind rate: 0.383
Solo started behind and lost rate: 0.668
Avg solo start deficit: 163.2
Avg solo turns taken: 2.24
Solo had winning answer rate: 0.101
Solo had winning answer given started behind rate: 0.262
Solo start deficit buckets: 1-75: 0.306, 76-150: 0.273, 151-250: 0.218, 251+: 0.202
Avg final board read: 0.085
Avg absolute final board read: 0.105
Strong harsh board rate: 0.001
Strong generous board rate: 0.236
Avg final cutoff estimate: 63.15
Avg final cutoff uncertainty: 0.356
Low uncertainty rate: 0.006
High cutoff rate: 0.193
Avg final safe floor: 51.01
Avg final local density read: 0.296
Avg final surprise read: 0.338
Avg final near-cutoff hits: 3.45
Avg final near-cutoff misses: 0.02

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.946, avg_score=2480.5, median_score=2556.0, stdev=493.8, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.009, avg_score=927.3, median_score=913.0, stdev=225.4, avg_strikes=3.00, first_out_rate=0.851
Contestant 3: win_rate=0.045, avg_score=1003.3, median_score=981.0, stdev=266.2, avg_strikes=3.00, first_out_rate=0.147
Last survivor but lost rate: 0.053
Solo started behind rate: 0.124
Solo started behind and lost rate: 0.426
Avg solo start deficit: 119.1
Avg solo turns taken: 9.83
Solo had winning answer rate: 0.063
Solo had winning answer given started behind rate: 0.508
Solo start deficit buckets: 1-75: 0.436, 76-150: 0.267, 151-250: 0.182, 251+: 0.116
Avg final board read: 0.029
Avg absolute final board read: 0.072
Strong harsh board rate: 0.010
Strong generous board rate: 0.116
Avg final cutoff estimate: 69.34
Avg final cutoff uncertainty: 0.476
Low uncertainty rate: 0.000
High cutoff rate: 0.502
Avg final safe floor: 56.49
Avg final local density read: 0.264
Avg final surprise read: 0.413
Avg final near-cutoff hits: 2.12
Avg final near-cutoff misses: 0.07

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.543, avg_score=1736.0, median_score=1728.0, stdev=91.8, avg_strikes=0.91, first_out_rate=0.001
Contestant 2: win_rate=0.204, avg_score=1648.3, median_score=1664.0, stdev=96.7, avg_strikes=2.01, first_out_rate=0.369
Contestant 3: win_rate=0.253, avg_score=1657.3, median_score=1674.0, stdev=115.1, avg_strikes=0.76, first_out_rate=0.082
Last survivor but lost rate: 0.038
Solo started behind rate: 0.061
Solo started behind and lost rate: 0.621
Avg solo start deficit: 100.3
Avg solo turns taken: 1.89
Solo had winning answer rate: 0.021
Solo had winning answer given started behind rate: 0.333
Solo start deficit buckets: 1-75: 0.392, 76-150: 0.444, 151-250: 0.130, 251+: 0.034
Avg final board read: -0.054
Avg absolute final board read: 0.076
Strong harsh board rate: 0.050
Strong generous board rate: 0.009
Avg final cutoff estimate: 45.05
Avg final cutoff uncertainty: 0.272
Low uncertainty rate: 0.315
High cutoff rate: 0.032
Avg final safe floor: 33.42
Avg final local density read: 0.413
Avg final surprise read: 0.245
Avg final near-cutoff hits: 4.19
Avg final near-cutoff misses: 0.00

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.604, avg_score=1748.8, median_score=1741.0, stdev=158.2, avg_strikes=2.32, first_out_rate=0.132
Contestant 2: win_rate=0.130, avg_score=1605.4, median_score=1624.0, stdev=143.6, avg_strikes=2.72, first_out_rate=0.611
Contestant 3: win_rate=0.266, avg_score=1593.8, median_score=1639.0, stdev=184.3, avg_strikes=2.29, first_out_rate=0.137
Last survivor but lost rate: 0.257
Solo started behind rate: 0.347
Solo started behind and lost rate: 0.740
Avg solo start deficit: 152.7
Avg solo turns taken: 1.85
Solo had winning answer rate: 0.074
Solo had winning answer given started behind rate: 0.213
Solo start deficit buckets: 1-75: 0.337, 76-150: 0.334, 151-250: 0.177, 251+: 0.153
Avg final board read: 0.009
Avg absolute final board read: 0.078
Strong harsh board rate: 0.011
Strong generous board rate: 0.081
Avg final cutoff estimate: 54.79
Avg final cutoff uncertainty: 0.306
Low uncertainty rate: 0.086
High cutoff rate: 0.067
Avg final safe floor: 42.95
Avg final local density read: 0.367
Avg final surprise read: 0.290
Avg final near-cutoff hits: 3.82
Avg final near-cutoff misses: 0.00

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.616, avg_score=1780.0, median_score=1969.0, stdev=767.0, avg_strikes=3.00, first_out_rate=0.029
Contestant 2: win_rate=0.360, avg_score=1427.6, median_score=1092.0, stdev=705.9, avg_strikes=3.00, first_out_rate=0.070
Contestant 3: win_rate=0.024, avg_score=675.6, median_score=647.0, stdev=242.9, avg_strikes=3.00, first_out_rate=0.900
Last survivor but lost rate: 0.121
Solo started behind rate: 0.331
Solo started behind and lost rate: 0.365
Avg solo start deficit: 107.6
Avg solo turns taken: 15.51
Solo had winning answer rate: 0.185
Solo had winning answer given started behind rate: 0.559
Solo start deficit buckets: 1-75: 0.456, 76-150: 0.297, 151-250: 0.164, 251+: 0.083
Avg final board read: -0.029
Avg absolute final board read: 0.064
Strong harsh board rate: 0.063
Strong generous board rate: 0.011
Avg final cutoff estimate: 70.36
Avg final cutoff uncertainty: 0.541
Low uncertainty rate: 0.000
High cutoff rate: 0.542
Avg final safe floor: 57.11
Avg final local density read: 0.239
Avg final surprise read: 0.430
Avg final near-cutoff hits: 1.59
Avg final near-cutoff misses: 0.13

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.672, avg_score=1904.7, avg_median_score=1943.8, avg_stdev=359.8, avg_strikes=2.44, avg_first_out_rate=0.064
Contestant 2: avg_win_rate=0.173, avg_score=1437.0, avg_median_score=1373.4, avg_stdev=275.0, avg_strikes=2.74, avg_first_out_rate=0.470
Contestant 3: avg_win_rate=0.155, avg_score=1262.7, avg_median_score=1280.2, avg_stdev=213.1, avg_strikes=2.40, avg_first_out_rate=0.331
Last survivor but lost rate: 0.145
Solo started behind rate: 0.250
Solo started behind and lost rate: 0.564
Avg solo start deficit: 128.6
Avg solo turns taken: 6.27
Solo had winning answer rate: 0.089
Solo had winning answer given started behind rate: 0.375
Solo start deficit buckets: 1-75: 0.385, 76-150: 0.323, 151-250: 0.174, 251+: 0.118
Avg final board read: 0.008
Avg absolute final board read: 0.079
Avg strong harsh board rate: 0.027
Avg strong generous board rate: 0.091
Avg final cutoff estimate: 60.54
Avg final cutoff uncertainty: 0.390
Avg low uncertainty rate: 0.081
Avg high cutoff rate: 0.267
Avg final safe floor: 48.20
Avg final local density read: 0.316
Avg final surprise read: 0.343
Avg final near-cutoff hits: 3.03
Avg final near-cutoff misses: 0.04
```

### Run 4:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.649, avg_score=1778.2, median_score=1725.0, stdev=288.3, avg_strikes=2.95, first_out_rate=0.154
Contestant 2: win_rate=0.163, avg_score=1576.0, median_score=1574.0, stdev=203.2, avg_strikes=2.97, first_out_rate=0.449
Contestant 3: win_rate=0.187, avg_score=1383.2, median_score=1460.0, stdev=256.9, avg_strikes=2.96, first_out_rate=0.389
Last survivor but lost rate: 0.256
Solo started behind rate: 0.383
Solo started behind and lost rate: 0.668
Avg solo start deficit: 163.2
Avg solo turns taken: 2.24
Solo had winning answer rate: 0.101
Solo had winning answer given started behind rate: 0.262
Solo start deficit buckets: 1-75: 0.306, 76-150: 0.273, 151-250: 0.218, 251+: 0.202
Avg final board read: 0.085
Avg absolute final board read: 0.105
Strong harsh board rate: 0.001
Strong generous board rate: 0.236
Avg final cutoff estimate: 63.15
Avg final cutoff uncertainty: 0.356
Low uncertainty rate: 0.006
High cutoff rate: 0.193
Avg final safe floor: 51.01
Avg final local density read: 0.071
Avg final surprise read: 0.338
Avg final near-cutoff hits: 3.45
Avg final near-cutoff misses: 0.02

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.946, avg_score=2480.5, median_score=2556.0, stdev=493.8, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.009, avg_score=927.3, median_score=913.0, stdev=225.4, avg_strikes=3.00, first_out_rate=0.851
Contestant 3: win_rate=0.045, avg_score=1003.3, median_score=981.0, stdev=266.2, avg_strikes=3.00, first_out_rate=0.147
Last survivor but lost rate: 0.053
Solo started behind rate: 0.124
Solo started behind and lost rate: 0.426
Avg solo start deficit: 119.1
Avg solo turns taken: 9.83
Solo had winning answer rate: 0.063
Solo had winning answer given started behind rate: 0.508
Solo start deficit buckets: 1-75: 0.436, 76-150: 0.267, 151-250: 0.182, 251+: 0.116
Avg final board read: 0.029
Avg absolute final board read: 0.072
Strong harsh board rate: 0.010
Strong generous board rate: 0.116
Avg final cutoff estimate: 69.34
Avg final cutoff uncertainty: 0.476
Low uncertainty rate: 0.000
High cutoff rate: 0.502
Avg final safe floor: 56.49
Avg final local density read: 0.052
Avg final surprise read: 0.413
Avg final near-cutoff hits: 2.12
Avg final near-cutoff misses: 0.07

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.543, avg_score=1736.0, median_score=1728.0, stdev=91.8, avg_strikes=0.91, first_out_rate=0.001
Contestant 2: win_rate=0.204, avg_score=1648.3, median_score=1664.0, stdev=96.7, avg_strikes=2.01, first_out_rate=0.369
Contestant 3: win_rate=0.253, avg_score=1657.3, median_score=1674.0, stdev=115.1, avg_strikes=0.76, first_out_rate=0.082
Last survivor but lost rate: 0.038
Solo started behind rate: 0.061
Solo started behind and lost rate: 0.621
Avg solo start deficit: 100.3
Avg solo turns taken: 1.89
Solo had winning answer rate: 0.021
Solo had winning answer given started behind rate: 0.333
Solo start deficit buckets: 1-75: 0.392, 76-150: 0.444, 151-250: 0.130, 251+: 0.034
Avg final board read: -0.054
Avg absolute final board read: 0.076
Strong harsh board rate: 0.050
Strong generous board rate: 0.009
Avg final cutoff estimate: 45.05
Avg final cutoff uncertainty: 0.272
Low uncertainty rate: 0.315
High cutoff rate: 0.032
Avg final safe floor: 33.42
Avg final local density read: 0.127
Avg final surprise read: 0.245
Avg final near-cutoff hits: 4.19
Avg final near-cutoff misses: 0.00

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.604, avg_score=1748.8, median_score=1741.0, stdev=158.2, avg_strikes=2.32, first_out_rate=0.132
Contestant 2: win_rate=0.130, avg_score=1605.4, median_score=1624.0, stdev=143.6, avg_strikes=2.72, first_out_rate=0.611
Contestant 3: win_rate=0.266, avg_score=1593.8, median_score=1639.0, stdev=184.3, avg_strikes=2.29, first_out_rate=0.137
Last survivor but lost rate: 0.257
Solo started behind rate: 0.347
Solo started behind and lost rate: 0.740
Avg solo start deficit: 152.7
Avg solo turns taken: 1.85
Solo had winning answer rate: 0.074
Solo had winning answer given started behind rate: 0.213
Solo start deficit buckets: 1-75: 0.337, 76-150: 0.334, 151-250: 0.177, 251+: 0.153
Avg final board read: 0.009
Avg absolute final board read: 0.078
Strong harsh board rate: 0.011
Strong generous board rate: 0.081
Avg final cutoff estimate: 54.79
Avg final cutoff uncertainty: 0.306
Low uncertainty rate: 0.086
High cutoff rate: 0.067
Avg final safe floor: 42.95
Avg final local density read: 0.102
Avg final surprise read: 0.290
Avg final near-cutoff hits: 3.82
Avg final near-cutoff misses: 0.00

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.616, avg_score=1780.0, median_score=1969.0, stdev=767.0, avg_strikes=3.00, first_out_rate=0.029
Contestant 2: win_rate=0.360, avg_score=1427.6, median_score=1092.0, stdev=705.9, avg_strikes=3.00, first_out_rate=0.070
Contestant 3: win_rate=0.024, avg_score=675.6, median_score=647.0, stdev=242.9, avg_strikes=3.00, first_out_rate=0.900
Last survivor but lost rate: 0.121
Solo started behind rate: 0.331
Solo started behind and lost rate: 0.365
Avg solo start deficit: 107.6
Avg solo turns taken: 15.51
Solo had winning answer rate: 0.185
Solo had winning answer given started behind rate: 0.559
Solo start deficit buckets: 1-75: 0.456, 76-150: 0.297, 151-250: 0.164, 251+: 0.083
Avg final board read: -0.029
Avg absolute final board read: 0.064
Strong harsh board rate: 0.063
Strong generous board rate: 0.011
Avg final cutoff estimate: 70.36
Avg final cutoff uncertainty: 0.541
Low uncertainty rate: 0.000
High cutoff rate: 0.542
Avg final safe floor: 57.11
Avg final local density read: 0.043
Avg final surprise read: 0.430
Avg final near-cutoff hits: 1.59
Avg final near-cutoff misses: 0.13

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.672, avg_score=1904.7, avg_median_score=1943.8, avg_stdev=359.8, avg_strikes=2.44, avg_first_out_rate=0.064
Contestant 2: avg_win_rate=0.173, avg_score=1437.0, avg_median_score=1373.4, avg_stdev=275.0, avg_strikes=2.74, avg_first_out_rate=0.470
Contestant 3: avg_win_rate=0.155, avg_score=1262.7, avg_median_score=1280.2, avg_stdev=213.1, avg_strikes=2.40, avg_first_out_rate=0.331
Last survivor but lost rate: 0.145
Solo started behind rate: 0.250
Solo started behind and lost rate: 0.564
Avg solo start deficit: 128.6
Avg solo turns taken: 6.27
Solo had winning answer rate: 0.089
Solo had winning answer given started behind rate: 0.375
Solo start deficit buckets: 1-75: 0.385, 76-150: 0.323, 151-250: 0.174, 251+: 0.118
Avg final board read: 0.008
Avg absolute final board read: 0.079
Avg strong harsh board rate: 0.027
Avg strong generous board rate: 0.091
Avg final cutoff estimate: 60.54
Avg final cutoff uncertainty: 0.390
Avg low uncertainty rate: 0.081
Avg high cutoff rate: 0.267
Avg final safe floor: 48.20
Avg final local density read: 0.079
Avg final surprise read: 0.343
Avg final near-cutoff hits: 3.03
Avg final near-cutoff misses: 0.04
```

### Run 5:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.651, avg_score=1778.8, median_score=1723.5, stdev=288.2, avg_strikes=2.95, first_out_rate=0.153
Contestant 2: win_rate=0.163, avg_score=1577.1, median_score=1575.0, stdev=202.8, avg_strikes=2.97, first_out_rate=0.448
Contestant 3: win_rate=0.186, avg_score=1381.5, median_score=1456.0, stdev=255.9, avg_strikes=2.96, first_out_rate=0.391
Last survivor but lost rate: 0.259
Solo started behind rate: 0.389
Solo started behind and lost rate: 0.666
Avg solo start deficit: 164.0
Avg solo turns taken: 2.24
Solo had winning answer rate: 0.101
Solo had winning answer given started behind rate: 0.259
Solo start deficit buckets: 1-75: 0.302, 76-150: 0.277, 151-250: 0.219, 251+: 0.203
Avg final board read: 0.037
Avg absolute final board read: 0.081
Strong harsh board rate: 0.014
Strong generous board rate: 0.094
Avg final cutoff estimate: 63.39
Avg final cutoff uncertainty: 0.357
Low uncertainty rate: 0.006
High cutoff rate: 0.198
Avg final safe floor: 51.24
Avg final local density read: 0.070
Avg final surprise read: 0.123
Avg final near-cutoff hits: 3.45
Avg final near-cutoff misses: 0.02

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.949, avg_score=2487.0, median_score=2562.5, stdev=488.0, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.009, avg_score=926.3, median_score=913.0, stdev=224.3, avg_strikes=3.00, first_out_rate=0.855
Contestant 3: win_rate=0.042, avg_score=999.9, median_score=980.0, stdev=263.9, avg_strikes=3.00, first_out_rate=0.143
Last survivor but lost rate: 0.051
Solo started behind rate: 0.121
Solo started behind and lost rate: 0.423
Avg solo start deficit: 120.0
Avg solo turns taken: 9.91
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.503
Solo start deficit buckets: 1-75: 0.429, 76-150: 0.274, 151-250: 0.178, 251+: 0.119
Avg final board read: -0.022
Avg absolute final board read: 0.073
Strong harsh board rate: 0.033
Strong generous board rate: 0.033
Avg final cutoff estimate: 69.40
Avg final cutoff uncertainty: 0.477
Low uncertainty rate: 0.000
High cutoff rate: 0.502
Avg final safe floor: 56.54
Avg final local density read: 0.052
Avg final surprise read: 0.181
Avg final near-cutoff hits: 2.12
Avg final near-cutoff misses: 0.07

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.514, avg_score=1732.0, median_score=1723.0, stdev=93.0, avg_strikes=0.98, first_out_rate=0.001
Contestant 2: win_rate=0.222, avg_score=1649.9, median_score=1665.0, stdev=97.6, avg_strikes=2.01, first_out_rate=0.367
Contestant 3: win_rate=0.264, avg_score=1657.5, median_score=1674.0, stdev=115.1, avg_strikes=0.83, first_out_rate=0.084
Last survivor but lost rate: 0.041
Solo started behind rate: 0.075
Solo started behind and lost rate: 0.554
Avg solo start deficit: 87.3
Avg solo turns taken: 2.16
Solo had winning answer rate: 0.030
Solo had winning answer given started behind rate: 0.403
Solo start deficit buckets: 1-75: 0.503, 76-150: 0.365, 151-250: 0.107, 251+: 0.025
Avg final board read: -0.094
Avg absolute final board read: 0.108
Strong harsh board rate: 0.176
Strong generous board rate: 0.001
Avg final cutoff estimate: 44.78
Avg final cutoff uncertainty: 0.273
Low uncertainty rate: 0.306
High cutoff rate: 0.032
Avg final safe floor: 33.14
Avg final local density read: 0.126
Avg final surprise read: 0.087
Avg final near-cutoff hits: 4.22
Avg final near-cutoff misses: 0.00

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.595, avg_score=1747.0, median_score=1736.0, stdev=157.8, avg_strikes=2.35, first_out_rate=0.128
Contestant 2: win_rate=0.138, avg_score=1607.3, median_score=1625.0, stdev=142.7, avg_strikes=2.72, first_out_rate=0.611
Contestant 3: win_rate=0.266, avg_score=1592.7, median_score=1639.0, stdev=183.4, avg_strikes=2.32, first_out_rate=0.139
Last survivor but lost rate: 0.260
Solo started behind rate: 0.357
Solo started behind and lost rate: 0.727
Avg solo start deficit: 148.6
Avg solo turns taken: 1.91
Solo had winning answer rate: 0.080
Solo had winning answer given started behind rate: 0.223
Solo start deficit buckets: 1-75: 0.360, 76-150: 0.323, 151-250: 0.174, 251+: 0.143
Avg final board read: -0.035
Avg absolute final board read: 0.087
Strong harsh board rate: 0.068
Strong generous board rate: 0.029
Avg final cutoff estimate: 54.95
Avg final cutoff uncertainty: 0.307
Low uncertainty rate: 0.081
High cutoff rate: 0.069
Avg final safe floor: 43.11
Avg final local density read: 0.101
Avg final surprise read: 0.098
Avg final near-cutoff hits: 3.83
Avg final near-cutoff misses: 0.00

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.615, avg_score=1787.6, median_score=2006.0, stdev=771.0, avg_strikes=3.00, first_out_rate=0.030
Contestant 2: win_rate=0.363, avg_score=1434.3, median_score=1093.0, stdev=712.3, avg_strikes=3.00, first_out_rate=0.062
Contestant 3: win_rate=0.022, avg_score=664.2, median_score=636.0, stdev=233.3, avg_strikes=3.00, first_out_rate=0.907
Last survivor but lost rate: 0.117
Solo started behind rate: 0.329
Solo started behind and lost rate: 0.355
Avg solo start deficit: 105.2
Avg solo turns taken: 15.87
Solo had winning answer rate: 0.186
Solo had winning answer given started behind rate: 0.566
Solo start deficit buckets: 1-75: 0.462, 76-150: 0.298, 151-250: 0.164, 251+: 0.076
Avg final board read: -0.075
Avg absolute final board read: 0.086
Strong harsh board rate: 0.129
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.37
Avg final cutoff uncertainty: 0.544
Low uncertainty rate: 0.000
High cutoff rate: 0.542
Avg final safe floor: 57.11
Avg final local density read: 0.044
Avg final surprise read: 0.202
Avg final near-cutoff hits: 1.58
Avg final near-cutoff misses: 0.12

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.665, avg_score=1906.5, avg_median_score=1950.2, avg_stdev=359.6, avg_strikes=2.46, avg_first_out_rate=0.063
Contestant 2: avg_win_rate=0.179, avg_score=1439.0, avg_median_score=1374.2, avg_stdev=275.9, avg_strikes=2.74, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.156, avg_score=1259.2, avg_median_score=1277.0, avg_stdev=210.3, avg_strikes=2.42, avg_first_out_rate=0.333
Last survivor but lost rate: 0.146
Solo started behind rate: 0.254
Solo started behind and lost rate: 0.545
Avg solo start deficit: 125.0
Avg solo turns taken: 6.42
Solo had winning answer rate: 0.092
Solo had winning answer given started behind rate: 0.391
Solo start deficit buckets: 1-75: 0.411, 76-150: 0.307, 151-250: 0.168, 251+: 0.113
Avg final board read: -0.038
Avg absolute final board read: 0.087
Avg strong harsh board rate: 0.084
Avg strong generous board rate: 0.032
Avg final cutoff estimate: 60.58
Avg final cutoff uncertainty: 0.392
Avg low uncertainty rate: 0.079
Avg high cutoff rate: 0.269
Avg final safe floor: 48.23
Avg final local density read: 0.079
Avg final surprise read: 0.138
Avg final near-cutoff hits: 3.04
Avg final near-cutoff misses: 0.04
```

**M3 Outcomes:**
- Added local density tracking around the estimate cutoff
- Added surprise tracking for outcomes that contradict expected board behavior
- Added near-cutoff hits/miss metrics
- Reduced inflated density readings through expected-hit-rate calibration
- Reduced over-positive surprise readings through stricter surprise triggers and faster decay
- Preserved the stable cutoff and safe-floor behavior achieved in M2

**Final aggregate M3 state:**
- Avg final cutoff estimate: ~60.5
- Avg final cutoff uncertainty: ~0.39
- Avg final safe floor: ~48.2
- Avg final local density read: ~0.98
- Avg final surprise read: ~0.14
- Avg near-cutoff hits: ~3.0
- Avg near-cutoff misses: ~0.04

**Key Observations:**
- M3 confirms that board-shape signals can be added without breaking existing behavior
- The strongest finding is that the current simulator natrually produces many more near-cutoff  misses
- Because of that, raw hit/miss density is biased unless corrected by an expected-hit baseline
- The final M3 version produces more interpretable diagnostic signals, but those signals are not yet deeply integrated into strategy
- A deeper M3 rework would likely require changing how answer candidates are generated or how categories represent true board shape
- For now, M3 is a successful lightweight extension and a good foundation for M4

---

## Milestone 4 - Contextual Risk and Strategy & Multi-Turn Planning

**Summary:**

Milestone 4 introduced contextual strategy on top of the board-shape signals created in M3. The goal was to move beyond single-turn safe/risky selection and allow player decisions to respond to score position, strike state, double-window rhythm, and inferred board context.

The final M4 state uses board context labels such as `open`, `dense`, `generous`, `tight`, and `uncertain` to influence player strategy. Dense boards act as the strongest aggression signal, generous boards act as a softer looseness signal, and tight boards suppress risky behavior. Double-window behavior was also updated so that risky/safe alternation depends on whether the board is actually attackable rather than simply “open.”

Across the full milestone, M4 remained stable while becoming more interpretable. The final run preserved category-sensitive behavior, with HR-style categories staying aggressive while bWAR/MVP-style categories remained more conservative.

**Observed Progression:**

M4 developed through several tuning and diagnostic stages:

- Run 1 introduced the first contextual risk behavior, but the initial tuning made C1 too dominant and C3 too weak.
- Run 2 restored stability and created the first healthy M4 baseline.
- Run 3 added context-action diagnostics without changing gameplay, confirming that the diagnostic layer was non-invasive.
- Run 4 tightened the `open` context definition after diagnostics showed it was triggering too broadly.
- Run 5 decomposed `open` into `dense` and `generous`, showing that open was a composite signal rather than one single board state.
- Run 6 made the dense/generous split behaviorally meaningful in normal decision pressure.
- Run 7 extended the same dense/generous/tight logic into double-window behavior and became the final M4 behavior state.

**Key Insights:**

- `open` was too broad when treated as a single aggression signal.
- `dense` is the clearest attackability signal and is much more predictive of risky behavior.
- `generous` indicates board looseness or surprising outcomes, but does not necessarily imply that players should become aggressive.
- `tight` contexts are highly meaningful and should override risky rhythm, especially in double-window spots.
- Double-window behavior works best when it preserves human-like risky/safe rhythm but filters that rhythm through board context.
- M4 increased strategic interpretability without destabilizing overall win distribution.

### Run 1

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.676, avg_score=1834.7, median_score=1792.0, stdev=316.1, avg_strikes=2.97, first_out_rate=0.088
Contestant 2: win_rate=0.204, avg_score=1615.4, median_score=1601.0, stdev=224.5, avg_strikes=2.98, first_out_rate=0.398
Contestant 3: win_rate=0.120, avg_score=1240.7, median_score=1179.0, stdev=266.4, avg_strikes=2.97, first_out_rate=0.503
Last survivor but lost rate: 0.295
Solo started behind rate: 0.407
Solo started behind and lost rate: 0.723
Avg solo start deficit: 308.7
Avg solo turns taken: 2.50
Solo had winning answer rate: 0.082
Solo had winning answer given started behind rate: 0.202
Solo start deficit buckets: 1-75: 0.186, 76-150: 0.200, 151-250: 0.152, 251+: 0.462
Avg final board read: 0.071
Avg absolute final board read: 0.122
Strong harsh board rate: 0.113
Strong generous board rate: 0.235
Avg final cutoff estimate: 62.32
Avg final cutoff uncertainty: 0.362
Low uncertainty rate: 0.099
High cutoff rate: 0.252
Avg final safe floor: 50.15
Avg final local density read: 0.087
Avg final surprise read: 0.132
Avg final near-cutoff hits: 4.02
Avg final near-cutoff misses: 0.03

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.961, avg_score=2556.4, median_score=2636.5, stdev=478.9, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.005, avg_score=910.1, median_score=899.0, stdev=216.4, avg_strikes=3.00, first_out_rate=0.887
Contestant 3: win_rate=0.034, avg_score=944.0, median_score=896.0, stdev=273.2, avg_strikes=3.00, first_out_rate=0.112
Last survivor but lost rate: 0.051
Solo started behind rate: 0.133
Solo started behind and lost rate: 0.387
Avg solo start deficit: 175.6
Avg solo turns taken: 12.15
Solo had winning answer rate: 0.063
Solo had winning answer given started behind rate: 0.473
Solo start deficit buckets: 1-75: 0.385, 76-150: 0.240, 151-250: 0.118, 251+: 0.257
Avg final board read: -0.016
Avg absolute final board read: 0.072
Strong harsh board rate: 0.039
Strong generous board rate: 0.039
Avg final cutoff estimate: 67.65
Avg final cutoff uncertainty: 0.478
Low uncertainty rate: 0.004
High cutoff rate: 0.416
Avg final safe floor: 54.78
Avg final local density read: 0.069
Avg final surprise read: 0.163
Avg final near-cutoff hits: 2.52
Avg final near-cutoff misses: 0.09

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.774, avg_score=1797.4, median_score=1782.0, stdev=98.0, avg_strikes=1.00, first_out_rate=0.002
Contestant 2: win_rate=0.117, avg_score=1666.2, median_score=1670.0, stdev=105.4, avg_strikes=1.97, first_out_rate=0.299
Contestant 3: win_rate=0.109, avg_score=1569.6, median_score=1615.0, stdev=156.3, avg_strikes=0.96, first_out_rate=0.054
Last survivor but lost rate: 0.162
Solo started behind rate: 0.204
Solo started behind and lost rate: 0.791
Avg solo start deficit: 214.2
Avg solo turns taken: 2.36
Solo had winning answer rate: 0.037
Solo had winning answer given started behind rate: 0.181
Solo start deficit buckets: 1-75: 0.121, 76-150: 0.439, 151-250: 0.150, 251+: 0.290
Avg final board read: -0.091
Avg absolute final board read: 0.135
Strong harsh board rate: 0.572
Strong generous board rate: 0.013
Avg final cutoff estimate: 48.42
Avg final cutoff uncertainty: 0.243
Low uncertainty rate: 0.635
High cutoff rate: 0.035
Avg final safe floor: 36.96
Avg final local density read: 0.117
Avg final surprise read: 0.121
Avg final near-cutoff hits: 2.97
Avg final near-cutoff misses: 0.00

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.680, avg_score=1781.5, median_score=1778.0, stdev=177.4, avg_strikes=2.43, first_out_rate=0.111
Contestant 2: win_rate=0.140, avg_score=1648.5, median_score=1656.0, stdev=148.8, avg_strikes=2.71, first_out_rate=0.565
Contestant 3: win_rate=0.181, avg_score=1498.1, median_score=1524.0, stdev=218.8, avg_strikes=2.42, first_out_rate=0.146
Last survivor but lost rate: 0.433
Solo started behind rate: 0.517
Solo started behind and lost rate: 0.837
Avg solo start deficit: 304.3
Avg solo turns taken: 2.03
Solo had winning answer rate: 0.061
Solo had winning answer given started behind rate: 0.117
Solo start deficit buckets: 1-75: 0.146, 76-150: 0.225, 151-250: 0.156, 251+: 0.473
Avg final board read: -0.013
Avg absolute final board read: 0.125
Strong harsh board rate: 0.326
Strong generous board rate: 0.091
Avg final cutoff estimate: 53.70
Avg final cutoff uncertainty: 0.295
Low uncertainty rate: 0.348
High cutoff rate: 0.124
Avg final safe floor: 41.93
Avg final local density read: 0.109
Avg final surprise read: 0.110
Avg final near-cutoff hits: 4.02
Avg final near-cutoff misses: 0.01

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.625, avg_score=1834.0, median_score=2170.0, stdev=836.3, avg_strikes=3.00, first_out_rate=0.010
Contestant 2: win_rate=0.358, avg_score=1421.8, median_score=1052.0, stdev=749.9, avg_strikes=3.00, first_out_rate=0.032
Contestant 3: win_rate=0.018, avg_score=578.6, median_score=527.0, stdev=237.5, avg_strikes=3.00, first_out_rate=0.958
Last survivor but lost rate: 0.133
Solo started behind rate: 0.356
Solo started behind and lost rate: 0.374
Avg solo start deficit: 122.6
Avg solo turns taken: 17.50
Solo had winning answer rate: 0.170
Solo had winning answer given started behind rate: 0.478
Solo start deficit buckets: 1-75: 0.381, 76-150: 0.306, 151-250: 0.212, 251+: 0.101
Avg final board read: -0.064
Avg absolute final board read: 0.079
Strong harsh board rate: 0.090
Strong generous board rate: 0.002
Avg final cutoff estimate: 67.95
Avg final cutoff uncertainty: 0.563
Low uncertainty rate: 0.000
High cutoff rate: 0.402
Avg final safe floor: 54.57
Avg final local density read: 0.053
Avg final surprise read: 0.196
Avg final near-cutoff hits: 1.79
Avg final near-cutoff misses: 0.07

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.743, avg_score=1960.8, avg_median_score=2031.7, avg_stdev=381.3, avg_strikes=2.48, avg_first_out_rate=0.043
Contestant 2: avg_win_rate=0.165, avg_score=1452.4, avg_median_score=1375.6, avg_stdev=289.0, avg_strikes=2.73, avg_first_out_rate=0.436
Contestant 3: avg_win_rate=0.092, avg_score=1166.2, avg_median_score=1148.2, avg_stdev=230.4, avg_strikes=2.47, avg_first_out_rate=0.354
Last survivor but lost rate: 0.215
Solo started behind rate: 0.324
Solo started behind and lost rate: 0.622
Avg solo start deficit: 225.1
Avg solo turns taken: 7.31
Solo had winning answer rate: 0.083
Solo had winning answer given started behind rate: 0.290
Solo start deficit buckets: 1-75: 0.244, 76-150: 0.282, 151-250: 0.158, 251+: 0.317
Avg final board read: -0.022
Avg absolute final board read: 0.107
Avg strong harsh board rate: 0.228
Avg strong generous board rate: 0.076
Avg final cutoff estimate: 60.01
Avg final cutoff uncertainty: 0.388
Avg low uncertainty rate: 0.217
Avg high cutoff rate: 0.245
Avg final safe floor: 47.68
Avg final local density read: 0.087
Avg final surprise read: 0.144
Avg final near-cutoff hits: 3.06
Avg final near-cutoff misses: 0.04
```

**Notes:**
- Unofficial run, tuning mistake made C1 too strong and C3 too weak
    - The following run, *Run 2* will address this issue

### Run 2:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.650, avg_score=1823.3, median_score=1763.0, stdev=326.9, avg_strikes=2.98, first_out_rate=0.089
Contestant 2: win_rate=0.190, avg_score=1600.4, median_score=1584.0, stdev=227.7, avg_strikes=2.99, first_out_rate=0.427
Contestant 3: win_rate=0.159, avg_score=1259.4, median_score=1179.0, stdev=282.1, avg_strikes=2.98, first_out_rate=0.478
Last survivor but lost rate: 0.250
Solo started behind rate: 0.382
Solo started behind and lost rate: 0.654
Avg solo start deficit: 269.4
Avg solo turns taken: 2.57
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.258
Solo start deficit buckets: 1-75: 0.264, 76-150: 0.216, 151-250: 0.130, 251+: 0.390
Avg final board read: 0.041
Avg absolute final board read: 0.098
Strong harsh board rate: 0.057
Strong generous board rate: 0.149
Avg final cutoff estimate: 66.53
Avg final cutoff uncertainty: 0.352
Low uncertainty rate: 0.045
High cutoff rate: 0.404
Avg final safe floor: 54.42
Avg final local density read: 0.056
Avg final surprise read: 0.170
Avg final near-cutoff hits: 2.83
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.746, risky=0.207, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.765, risky=0.235, blind_risk=0.000

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.959, avg_score=2579.5, median_score=2662.0, stdev=481.4, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.005, avg_score=892.3, median_score=883.0, stdev=219.3, avg_strikes=3.00, first_out_rate=0.879
Contestant 3: win_rate=0.036, avg_score=941.0, median_score=895.0, stdev=266.1, avg_strikes=3.00, first_out_rate=0.120
Last survivor but lost rate: 0.042
Solo started behind rate: 0.129
Solo started behind and lost rate: 0.326
Avg solo start deficit: 134.6
Avg solo turns taken: 13.30
Solo had winning answer rate: 0.071
Solo had winning answer given started behind rate: 0.553
Solo start deficit buckets: 1-75: 0.471, 76-150: 0.238, 151-250: 0.126, 251+: 0.166
Avg final board read: -0.034
Avg absolute final board read: 0.079
Strong harsh board rate: 0.046
Strong generous board rate: 0.023
Avg final cutoff estimate: 71.33
Avg final cutoff uncertainty: 0.462
Low uncertainty rate: 0.001
High cutoff rate: 0.634
Avg final safe floor: 58.56
Avg final local density read: 0.059
Avg final surprise read: 0.195
Avg final near-cutoff hits: 1.92
Avg final near-cutoff misses: 0.11
Mode rates: safe=0.635, risky=0.146, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.208
Double window mode rates: safe=0.818, risky=0.182, blind_risk=0.000

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.574, avg_score=1760.0, median_score=1744.0, stdev=100.9, avg_strikes=1.19, first_out_rate=0.002
Contestant 2: win_rate=0.208, avg_score=1673.1, median_score=1677.0, stdev=112.0, avg_strikes=2.03, first_out_rate=0.332
Contestant 3: win_rate=0.217, avg_score=1594.4, median_score=1642.0, stdev=158.0, avg_strikes=1.09, first_out_rate=0.059
Last survivor but lost rate: 0.135
Solo started behind rate: 0.204
Solo started behind and lost rate: 0.663
Avg solo start deficit: 187.9
Avg solo turns taken: 2.44
Solo had winning answer rate: 0.064
Solo had winning answer given started behind rate: 0.315
Solo start deficit buckets: 1-75: 0.339, 76-150: 0.261, 151-250: 0.113, 251+: 0.288
Avg final board read: -0.080
Avg absolute final board read: 0.107
Strong harsh board rate: 0.257
Strong generous board rate: 0.002
Avg final cutoff estimate: 52.34
Avg final cutoff uncertainty: 0.282
Low uncertainty rate: 0.313
High cutoff rate: 0.169
Avg final safe floor: 40.65
Avg final local density read: 0.080
Avg final surprise read: 0.159
Avg final near-cutoff hits: 2.57
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.495, risky=0.485, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.003
Double window mode rates: safe=0.482, risky=0.518, blind_risk=0.000

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.563, avg_score=1763.5, median_score=1748.0, stdev=183.1, avg_strikes=2.58, first_out_rate=0.090
Contestant 2: win_rate=0.165, avg_score=1648.4, median_score=1653.0, stdev=160.3, avg_strikes=2.78, first_out_rate=0.612
Contestant 3: win_rate=0.272, avg_score=1503.4, median_score=1561.0, stdev=234.5, avg_strikes=2.56, first_out_rate=0.160
Last survivor but lost rate: 0.362
Solo started behind rate: 0.470
Solo started behind and lost rate: 0.770
Avg solo start deficit: 284.5
Avg solo turns taken: 2.07
Solo had winning answer rate: 0.084
Solo had winning answer given started behind rate: 0.179
Solo start deficit buckets: 1-75: 0.275, 76-150: 0.189, 151-250: 0.108, 251+: 0.427
Avg final board read: -0.024
Avg absolute final board read: 0.098
Strong harsh board rate: 0.152
Strong generous board rate: 0.041
Avg final cutoff estimate: 58.76
Avg final cutoff uncertainty: 0.308
Low uncertainty rate: 0.168
High cutoff rate: 0.258
Avg final safe floor: 46.91
Avg final local density read: 0.072
Avg final surprise read: 0.151
Avg final near-cutoff hits: 2.91
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.641, risky=0.330, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.011
Double window mode rates: safe=0.629, risky=0.371, blind_risk=0.000

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.601, avg_score=1823.1, median_score=2136.0, stdev=846.7, avg_strikes=3.00, first_out_rate=0.014
Contestant 2: win_rate=0.379, avg_score=1453.3, median_score=1047.0, stdev=772.7, avg_strikes=3.00, first_out_rate=0.037
Contestant 3: win_rate=0.020, avg_score=578.1, median_score=523.0, stdev=237.8, avg_strikes=3.00, first_out_rate=0.949
Last survivor but lost rate: 0.105
Solo started behind rate: 0.341
Solo started behind and lost rate: 0.307
Avg solo start deficit: 107.3
Avg solo turns taken: 18.96
Solo had winning answer rate: 0.190
Solo had winning answer given started behind rate: 0.558
Solo start deficit buckets: 1-75: 0.449, 76-150: 0.304, 151-250: 0.169, 251+: 0.079
Avg final board read: -0.078
Avg absolute final board read: 0.089
Strong harsh board rate: 0.117
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.63
Avg final cutoff uncertainty: 0.535
Low uncertainty rate: 0.000
High cutoff rate: 0.573
Avg final safe floor: 57.42
Avg final local density read: 0.055
Avg final surprise read: 0.215
Avg final near-cutoff hits: 1.42
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.607, risky=0.121, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.258
Double window mode rates: safe=0.804, risky=0.196, blind_risk=0.000

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.669, avg_score=1949.9, avg_median_score=2010.6, avg_stdev=387.8, avg_strikes=2.55, avg_first_out_rate=0.039
Contestant 2: avg_win_rate=0.190, avg_score=1453.5, avg_median_score=1368.8, avg_stdev=298.4, avg_strikes=2.76, avg_first_out_rate=0.458
Contestant 3: avg_win_rate=0.141, avg_score=1175.3, avg_median_score=1160.0, avg_stdev=235.7, avg_strikes=2.53, avg_first_out_rate=0.353
Last survivor but lost rate: 0.179
Solo started behind rate: 0.305
Solo started behind and lost rate: 0.544
Avg solo start deficit: 196.7
Avg solo turns taken: 7.87
Solo had winning answer rate: 0.102
Solo had winning answer given started behind rate: 0.373
Solo start deficit buckets: 1-75: 0.360, 76-150: 0.241, 151-250: 0.129, 251+: 0.270
Avg final board read: -0.035
Avg absolute final board read: 0.094
Avg strong harsh board rate: 0.126
Avg strong generous board rate: 0.043
Avg final cutoff estimate: 63.92
Avg final cutoff uncertainty: 0.388
Avg low uncertainty rate: 0.105
Avg high cutoff rate: 0.407
Avg final safe floor: 51.59
Avg final local density read: 0.064
Avg final surprise read: 0.178
Avg final near-cutoff hits: 2.33
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.625, risky=0.261, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.099
Double window mode rates: safe=0.679, risky=0.321, blind_risk=0.000
```

**Notes:**

Comparing Runs 1 and 2, C1 dominance returned to normal:

| Metric | M4 Run 1 | M4 Run 2 | 
| - | - | - | 
| C1 WR | 0.743 | 0.669 |
| C2 WR | 0.165 | 0.190 |
| C3 WR | 0.092 | 0.141 |
| Last survivor but lost | 0.215 | 0.179 |
| Solo started behind rate | 0.324 | 0.305 |
| Solo Started behind / lost | 0.622 | 0.544 |
| Avg solo deficit | 255.1 | 196.7 |

Overall, Run 2 produces the first healthy M4 state. While comparable to the final run of M3, it does change in behavior but does not blow up the system. A full comparision is shown below:

| Metric | V3M3 Final | V3M4 Run 2 | Read |
| - | - | - | - |
| C1 WR | 0.665 | 0.669 | Basically stable |
| C2 WR | 0.179 | 0.190 | Slight gain |
| C3 WR | 0.156 | 0.145 | Slight loss |
| Last survivor but lost | 0.146 | 0.179 | Worse, but not catastrophic |
| Solo started behind / lost | 0.545 | 0.544 | Identicial |
| Avg solo deficit | 125.0 | 196.7 | Noticeably higher |
| Cutoff estimate | 60.58 | 63.92 | Higher |
| Safe floor | 48.23 | 51.59 | Higher |
| Local density | 0.079 | 0.064 | Lower |
| Surprise | 0.138 | 0.178 | Higher |

**Takeaway:**
- M4 thusfar did not destabilize win rates, but it changed the strategic environment:
    - Players are more playing more conservatively/contextually, cutoff estimates rise, safe floors rise, and solo deficits get larger when someone starts behind

**Conclusions:**

1. **Contestant balance is preserved**

M4 Run 2 is very close to M3 Final in overall win distribution, which suggests that M4 did not accidentally rewrite the enitre simulator, but rather it is influencing behavior wihtout erasing the existing player/category structure.

2. **M4 made the board feel higher/tighter**

Aggregate cutoff estimate rose from 60.58 to 63.92, high-cutoff rate rose from 0.269 to 0.407, and safe floor rose from 48.23 to 51.59

The main behavioral shift is that players are effectively playing around a more demanding perceived board.
- This makes sense if M4 is causing more conservative/double-window-aware behavior and reducing lower-risk exploratory guesses
- This also is not automatically bad, it just means that M4 pushes the game toward *'survive and manage around the line'* rather than *'take the best immediate guess'*, which is the milestone goal

3. **Solo deficits are the main thing to watch**

Average solo start deficit jumped from 125.0 to 196.7, and the 251+ deficit bucket jumped from 0.113 to 0.270. *However*, the solo started behind and lost rate stayed almost identicial, with 0.545 vs. 0.544.

M4 is thus creating larger deficits, but the solo player's actual failure rate given behind start is not worse, which suggests bigger deficits may be category / flow-driven rather than broken solo logic issue.

However, this is still something to monitor.

4. New mode metrics are already valuable

New aggregate M4 mode rates:
- `safe` = 0.625
- `risky` = 0.261
- `blind_risk` = 0.011
- `victory_lap` = 0.099
- `double-window safe` = 0.679
- `double-window risky` = 0.321

This gives clear pictures of what M4 is doing. Looking deeper, category-level mode rates already look sensible:
- HR since 2000 is aggressive: `risky`: 0.485, `double-window risky`: 0.518
- bWAR is conservative: `risky`: 0.146, `double-window risky`: 0.182
- MVP is conservative and victory-lap heavy: `victory_lap`: 0.258, `double-window risky`: 0.196

In conclusion, M4 Run 2 restored stability after the initial double-window aggression issue. Overall win distribution returned close to the final M3 baseline, while mode-rate diagnostics showed meaningful category-sensitive strategy behavior. The main remaining concern is that M4 raises perceived cutoff and safe-floor issues, creating larger solo deficits even though solo failure rate remains stable.

### Run 3

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.650, avg_score=1823.3, median_score=1763.0, stdev=326.9, avg_strikes=2.98, first_out_rate=0.089
Contestant 2: win_rate=0.190, avg_score=1600.4, median_score=1584.0, stdev=227.7, avg_strikes=2.99, first_out_rate=0.427
Contestant 3: win_rate=0.159, avg_score=1259.4, median_score=1179.0, stdev=282.1, avg_strikes=2.98, first_out_rate=0.478
Last survivor but lost rate: 0.250
Solo started behind rate: 0.382
Solo started behind and lost rate: 0.654
Avg solo start deficit: 269.4
Avg solo turns taken: 2.57
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.258
Solo start deficit buckets: 1-75: 0.264, 76-150: 0.216, 151-250: 0.130, 251+: 0.390
Avg final board read: 0.041
Avg absolute final board read: 0.098
Strong harsh board rate: 0.057
Strong generous board rate: 0.149
Avg final cutoff estimate: 66.53
Avg final cutoff uncertainty: 0.352
Low uncertainty rate: 0.045
High cutoff rate: 0.404
Avg final safe floor: 54.42
Avg final local density read: 0.056
Avg final surprise read: 0.170
Avg final near-cutoff hits: 2.83
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.746, risky=0.207, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.765, risky=0.235, blind_risk=0.000
Context rates: open=0.795, tight=0.094, uncertain=0.370, 
Context-action rates: risky_on_open=0.173, safe_on_tight=0.872, risky_on_uncertain=0.350, safe_on_uncertain=0.638, risky_on_double_window=0.235, safe_on_double_window=0.765

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.959, avg_score=2579.5, median_score=2662.0, stdev=481.4, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.005, avg_score=892.3, median_score=883.0, stdev=219.3, avg_strikes=3.00, first_out_rate=0.879
Contestant 3: win_rate=0.036, avg_score=941.0, median_score=895.0, stdev=266.1, avg_strikes=3.00, first_out_rate=0.120
Last survivor but lost rate: 0.042
Solo started behind rate: 0.129
Solo started behind and lost rate: 0.326
Avg solo start deficit: 134.6
Avg solo turns taken: 13.30
Solo had winning answer rate: 0.071
Solo had winning answer given started behind rate: 0.553
Solo start deficit buckets: 1-75: 0.471, 76-150: 0.238, 151-250: 0.126, 251+: 0.166
Avg final board read: -0.034
Avg absolute final board read: 0.079
Strong harsh board rate: 0.046
Strong generous board rate: 0.023
Avg final cutoff estimate: 71.33
Avg final cutoff uncertainty: 0.462
Low uncertainty rate: 0.001
High cutoff rate: 0.634
Avg final safe floor: 58.56
Avg final local density read: 0.059
Avg final surprise read: 0.195
Avg final near-cutoff hits: 1.92
Avg final near-cutoff misses: 0.11
Mode rates: safe=0.635, risky=0.146, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.208
Double window mode rates: safe=0.818, risky=0.182, blind_risk=0.000
Context rates: open=0.751, tight=0.205, uncertain=0.697, 
Context-action rates: risky_on_open=0.107, safe_on_tight=0.947, risky_on_uncertain=0.184, safe_on_uncertain=0.773, risky_on_double_window=0.182, safe_on_double_window=0.818

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.574, avg_score=1760.0, median_score=1744.0, stdev=100.9, avg_strikes=1.19, first_out_rate=0.002
Contestant 2: win_rate=0.208, avg_score=1673.1, median_score=1677.0, stdev=112.0, avg_strikes=2.03, first_out_rate=0.332
Contestant 3: win_rate=0.217, avg_score=1594.4, median_score=1642.0, stdev=158.0, avg_strikes=1.09, first_out_rate=0.059
Last survivor but lost rate: 0.135
Solo started behind rate: 0.204
Solo started behind and lost rate: 0.663
Avg solo start deficit: 187.9
Avg solo turns taken: 2.44
Solo had winning answer rate: 0.064
Solo had winning answer given started behind rate: 0.315
Solo start deficit buckets: 1-75: 0.339, 76-150: 0.261, 151-250: 0.113, 251+: 0.288
Avg final board read: -0.080
Avg absolute final board read: 0.107
Strong harsh board rate: 0.257
Strong generous board rate: 0.002
Avg final cutoff estimate: 52.34
Avg final cutoff uncertainty: 0.282
Low uncertainty rate: 0.313
High cutoff rate: 0.169
Avg final safe floor: 40.65
Avg final local density read: 0.080
Avg final surprise read: 0.159
Avg final near-cutoff hits: 2.57
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.495, risky=0.485, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.003
Double window mode rates: safe=0.482, risky=0.518, blind_risk=0.000
Context rates: open=0.806, tight=0.100, uncertain=0.323, 
Context-action rates: risky_on_open=0.499, safe_on_tight=0.708, risky_on_uncertain=0.583, safe_on_uncertain=0.402, risky_on_double_window=0.518, safe_on_double_window=0.482

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.563, avg_score=1763.5, median_score=1748.0, stdev=183.1, avg_strikes=2.58, first_out_rate=0.090
Contestant 2: win_rate=0.165, avg_score=1648.4, median_score=1653.0, stdev=160.3, avg_strikes=2.78, first_out_rate=0.612
Contestant 3: win_rate=0.272, avg_score=1503.4, median_score=1561.0, stdev=234.5, avg_strikes=2.56, first_out_rate=0.160
Last survivor but lost rate: 0.362
Solo started behind rate: 0.470
Solo started behind and lost rate: 0.770
Avg solo start deficit: 284.5
Avg solo turns taken: 2.07
Solo had winning answer rate: 0.084
Solo had winning answer given started behind rate: 0.179
Solo start deficit buckets: 1-75: 0.275, 76-150: 0.189, 151-250: 0.108, 251+: 0.427
Avg final board read: -0.024
Avg absolute final board read: 0.098
Strong harsh board rate: 0.152
Strong generous board rate: 0.041
Avg final cutoff estimate: 58.76
Avg final cutoff uncertainty: 0.308
Low uncertainty rate: 0.168
High cutoff rate: 0.258
Avg final safe floor: 46.91
Avg final local density read: 0.072
Avg final surprise read: 0.151
Avg final near-cutoff hits: 2.91
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.641, risky=0.330, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.011
Double window mode rates: safe=0.629, risky=0.371, blind_risk=0.000
Context rates: open=0.802, tight=0.110, uncertain=0.329, 
Context-action rates: risky_on_open=0.318, safe_on_tight=0.778, risky_on_uncertain=0.475, safe_on_uncertain=0.511, risky_on_double_window=0.371, safe_on_double_window=0.629

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.601, avg_score=1823.1, median_score=2136.0, stdev=846.7, avg_strikes=3.00, first_out_rate=0.014
Contestant 2: win_rate=0.379, avg_score=1453.3, median_score=1047.0, stdev=772.7, avg_strikes=3.00, first_out_rate=0.037
Contestant 3: win_rate=0.020, avg_score=578.1, median_score=523.0, stdev=237.8, avg_strikes=3.00, first_out_rate=0.949
Last survivor but lost rate: 0.105
Solo started behind rate: 0.341
Solo started behind and lost rate: 0.307
Avg solo start deficit: 107.3
Avg solo turns taken: 18.96
Solo had winning answer rate: 0.190
Solo had winning answer given started behind rate: 0.558
Solo start deficit buckets: 1-75: 0.449, 76-150: 0.304, 151-250: 0.169, 251+: 0.079
Avg final board read: -0.078
Avg absolute final board read: 0.089
Strong harsh board rate: 0.117
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.63
Avg final cutoff uncertainty: 0.535
Low uncertainty rate: 0.000
High cutoff rate: 0.573
Avg final safe floor: 57.42
Avg final local density read: 0.055
Avg final surprise read: 0.215
Avg final near-cutoff hits: 1.42
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.607, risky=0.121, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.258
Double window mode rates: safe=0.804, risky=0.196, blind_risk=0.000
Context rates: open=0.744, tight=0.250, uncertain=0.784, 
Context-action rates: risky_on_open=0.072, safe_on_tight=0.937, risky_on_uncertain=0.150, safe_on_uncertain=0.748, risky_on_double_window=0.196, safe_on_double_window=0.804

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.669, avg_score=1949.9, avg_median_score=2010.6, avg_stdev=387.8, avg_strikes=2.55, avg_first_out_rate=0.039
Contestant 2: avg_win_rate=0.190, avg_score=1453.5, avg_median_score=1368.8, avg_stdev=298.4, avg_strikes=2.76, avg_first_out_rate=0.458
Contestant 3: avg_win_rate=0.141, avg_score=1175.3, avg_median_score=1160.0, avg_stdev=235.7, avg_strikes=2.53, avg_first_out_rate=0.353
Last survivor but lost rate: 0.179
Solo started behind rate: 0.305
Solo started behind and lost rate: 0.544
Avg solo start deficit: 196.7
Avg solo turns taken: 7.87
Solo had winning answer rate: 0.102
Solo had winning answer given started behind rate: 0.373
Solo start deficit buckets: 1-75: 0.360, 76-150: 0.241, 151-250: 0.129, 251+: 0.270
Avg final board read: -0.035
Avg absolute final board read: 0.094
Avg strong harsh board rate: 0.126
Avg strong generous board rate: 0.043
Avg final cutoff estimate: 63.92
Avg final cutoff uncertainty: 0.388
Avg low uncertainty rate: 0.105
Avg high cutoff rate: 0.407
Avg final safe floor: 51.59
Avg final local density read: 0.064
Avg final surprise read: 0.178
Avg final near-cutoff hits: 2.33
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.625, risky=0.261, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.099
Double window mode rates: safe=0.679, risky=0.321, blind_risk=0.000
Context rates: open=0.781, tight=0.150, uncertain=0.493, 
Context-action rates: risky_on_open=0.242, safe_on_tight=0.876, risky_on_uncertain=0.293, safe_on_uncertain=0.659, risky_on_double_window=0.321, safe_on_double_window=0.679
```

**Notes:**

Run 3 is a diagnostic-only run. No gameplay logic was changed from Run 2, only new context metrics were added.

The main output metrics remained identical to Run 2, confirming the new diagnostic layer was non-invasive and did not alter simluation behavior.

The new context metrics provided a clear view of how M4's strategy layer is behaving internally:

- `tight` contexts are rare but highly meaningful
    - Aggregate `tight_context_rate`: 0.150
    - Aggregate `safe_on_tight`: 0.876

When the board is identified as tight, players strongly shift toward survival-oriented safe play.

- `uncertain` contexts appear frequently:
    - Aggregate `uncertain_context_rate`: 0.493
    - Aggregate `safe_on_uncertain`: 0.659
    - Aggregate `risky_on_uncertain`: 0.293

Uncertainty generally suppresses risk, but does not eliminate aggression entirely.

- Double-window behavior appears well-tracked and category-sensitive:
    - Aggregate `risky_on_double_window`: 0.321
    - Aggregate `safe_on_double_window`: 0.679

For example, HR since 2000 was much more aggressive in double-window spots (`risky_on_double_window`: 0.518), while bWAR and MVP remained much more conservative.

- Main issue - `open` context appears too broad:
    - Aggregate `open_context_rate`: 0.781
    - Every category had an open-context rate above 0.740

Suggests that the current open-context definition is triggering too often, likely because `surprise_read` contributes heavily to the open flag.

**Takeaway:**

Overall, Run 3 confirmed that M4's diagnostic layer is working. The simulator now shows not only on which modes players choose, but also which board contexts are influencing those choices. The main target for the next run is tuning the open-context definition so that open states become rarer and more strategically meaningful.

**Conclusion:**

Run 3 successfully completed the diagnostic phase of M4. The added context metrics did not change simulation behavior, but they revealed that M4 is already producing meaningful context-aware strategy.

Tight boards push players strongly toward safe chooices, uncertainty generally reduces risk, and double-window behavior varies sensibly by category. The primary tuning target for Run 4 is the overly broad `open` context, which currently fires across nearly all categories at a high rate.

### Run 4

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.643, avg_score=1818.4, median_score=1751.0, stdev=325.6, avg_strikes=2.98, first_out_rate=0.086
Contestant 2: win_rate=0.193, avg_score=1595.4, median_score=1581.0, stdev=225.7, avg_strikes=2.99, first_out_rate=0.442
Contestant 3: win_rate=0.164, avg_score=1262.5, median_score=1183.0, stdev=281.2, avg_strikes=2.98, first_out_rate=0.466
Last survivor but lost rate: 0.251
Solo started behind rate: 0.391
Solo started behind and lost rate: 0.642
Avg solo start deficit: 270.1
Avg solo turns taken: 2.57
Solo had winning answer rate: 0.106
Solo had winning answer given started behind rate: 0.270
Solo start deficit buckets: 1-75: 0.272, 76-150: 0.209, 151-250: 0.132, 251+: 0.387
Avg final board read: 0.040
Avg absolute final board read: 0.097
Strong harsh board rate: 0.050
Strong generous board rate: 0.149
Avg final cutoff estimate: 66.84
Avg final cutoff uncertainty: 0.351
Low uncertainty rate: 0.043
High cutoff rate: 0.425
Avg final safe floor: 54.73
Avg final local density read: 0.054
Avg final surprise read: 0.174
Avg final near-cutoff hits: 2.74
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.750, risky=0.203, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.770, risky=0.230, blind_risk=0.000
Context rates: open=0.699, tight=0.093, uncertain=0.370, 
Context-action rates: risky_on_open=0.174, safe_on_tight=0.877, risky_on_uncertain=0.339, safe_on_uncertain=0.648, risky_on_double_window=0.230, safe_on_double_window=0.770

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.963, avg_score=2586.9, median_score=2663.0, stdev=472.2, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.004, avg_score=889.0, median_score=881.0, stdev=216.2, avg_strikes=3.00, first_out_rate=0.881
Contestant 3: win_rate=0.033, avg_score=940.0, median_score=895.0, stdev=263.1, avg_strikes=3.00, first_out_rate=0.118
Last survivor but lost rate: 0.041
Solo started behind rate: 0.127
Solo started behind and lost rate: 0.325
Avg solo start deficit: 136.1
Avg solo turns taken: 13.26
Solo had winning answer rate: 0.070
Solo had winning answer given started behind rate: 0.555
Solo start deficit buckets: 1-75: 0.484, 76-150: 0.217, 151-250: 0.121, 251+: 0.178
Avg final board read: -0.032
Avg absolute final board read: 0.079
Strong harsh board rate: 0.044
Strong generous board rate: 0.024
Avg final cutoff estimate: 71.60
Avg final cutoff uncertainty: 0.462
Low uncertainty rate: 0.001
High cutoff rate: 0.648
Avg final safe floor: 58.83
Avg final local density read: 0.059
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.90
Avg final near-cutoff misses: 0.12
Mode rates: safe=0.637, risky=0.142, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.210
Double window mode rates: safe=0.824, risky=0.176, blind_risk=0.000
Context rates: open=0.603, tight=0.200, uncertain=0.696, 
Context-action rates: risky_on_open=0.110, safe_on_tight=0.944, risky_on_uncertain=0.180, safe_on_uncertain=0.777, risky_on_double_window=0.176, safe_on_double_window=0.824

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.546, avg_score=1756.0, median_score=1739.0, stdev=99.9, avg_strikes=1.30, first_out_rate=0.002
Contestant 2: win_rate=0.225, avg_score=1674.3, median_score=1679.0, stdev=112.0, avg_strikes=2.08, first_out_rate=0.355
Contestant 3: win_rate=0.229, avg_score=1595.3, median_score=1643.0, stdev=158.0, avg_strikes=1.19, first_out_rate=0.069
Last survivor but lost rate: 0.144
Solo started behind rate: 0.232
Solo started behind and lost rate: 0.621
Avg solo start deficit: 179.2
Avg solo turns taken: 2.50
Solo had winning answer rate: 0.082
Solo had winning answer given started behind rate: 0.353
Solo start deficit buckets: 1-75: 0.392, 76-150: 0.242, 151-250: 0.104, 251+: 0.262
Avg final board read: -0.079
Avg absolute final board read: 0.103
Strong harsh board rate: 0.254
Strong generous board rate: 0.001
Avg final cutoff estimate: 52.66
Avg final cutoff uncertainty: 0.283
Low uncertainty rate: 0.298
High cutoff rate: 0.179
Avg final safe floor: 40.96
Avg final local density read: 0.077
Avg final surprise read: 0.163
Avg final near-cutoff hits: 2.54
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.504, risky=0.475, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.004
Double window mode rates: safe=0.494, risky=0.506, blind_risk=0.000
Context rates: open=0.740, tight=0.100, uncertain=0.323, 
Context-action rates: risky_on_open=0.501, safe_on_tight=0.723, risky_on_uncertain=0.570, safe_on_uncertain=0.414, risky_on_double_window=0.506, safe_on_double_window=0.494

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.548, avg_score=1759.4, median_score=1742.0, stdev=182.9, avg_strikes=2.64, first_out_rate=0.091
Contestant 2: win_rate=0.175, avg_score=1647.9, median_score=1653.0, stdev=161.1, avg_strikes=2.81, first_out_rate=0.622
Contestant 3: win_rate=0.277, avg_score=1504.5, median_score=1573.0, stdev=233.3, avg_strikes=2.62, first_out_rate=0.167
Last survivor but lost rate: 0.362
Solo started behind rate: 0.485
Solo started behind and lost rate: 0.747
Avg solo start deficit: 276.9
Avg solo turns taken: 2.12
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.205
Solo start deficit buckets: 1-75: 0.296, 76-150: 0.187, 151-250: 0.100, 251+: 0.417
Avg final board read: -0.023
Avg absolute final board read: 0.096
Strong harsh board rate: 0.142
Strong generous board rate: 0.043
Avg final cutoff estimate: 58.94
Avg final cutoff uncertainty: 0.308
Low uncertainty rate: 0.164
High cutoff rate: 0.274
Avg final safe floor: 47.09
Avg final local density read: 0.069
Avg final surprise read: 0.156
Avg final near-cutoff hits: 2.86
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.648, risky=0.321, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.012
Double window mode rates: safe=0.639, risky=0.361, blind_risk=0.000
Context rates: open=0.720, tight=0.107, uncertain=0.329, 
Context-action rates: risky_on_open=0.320, safe_on_tight=0.789, risky_on_uncertain=0.461, safe_on_uncertain=0.525, risky_on_double_window=0.361, safe_on_double_window=0.639

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.606, avg_score=1831.5, median_score=2165.0, stdev=849.6, avg_strikes=3.00, first_out_rate=0.014
Contestant 2: win_rate=0.375, avg_score=1444.4, median_score=1041.0, stdev=770.5, avg_strikes=3.00, first_out_rate=0.041
Contestant 3: win_rate=0.020, avg_score=574.9, median_score=522.0, stdev=233.6, avg_strikes=3.00, first_out_rate=0.945
Last survivor but lost rate: 0.105
Solo started behind rate: 0.338
Solo started behind and lost rate: 0.311
Avg solo start deficit: 104.2
Avg solo turns taken: 18.76
Solo had winning answer rate: 0.189
Solo had winning answer given started behind rate: 0.559
Solo start deficit buckets: 1-75: 0.463, 76-150: 0.297, 151-250: 0.167, 251+: 0.073
Avg final board read: -0.077
Avg absolute final board read: 0.088
Strong harsh board rate: 0.118
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.73
Avg final cutoff uncertainty: 0.536
Low uncertainty rate: 0.000
High cutoff rate: 0.578
Avg final safe floor: 57.52
Avg final local density read: 0.055
Avg final surprise read: 0.214
Avg final near-cutoff hits: 1.44
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.609, risky=0.119, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.259
Double window mode rates: safe=0.808, risky=0.192, blind_risk=0.000
Context rates: open=0.587, tight=0.249, uncertain=0.785, 
Context-action rates: risky_on_open=0.075, safe_on_tight=0.931, risky_on_uncertain=0.147, safe_on_uncertain=0.750, risky_on_double_window=0.192, safe_on_double_window=0.808

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.661, avg_score=1950.4, avg_median_score=2012.0, avg_stdev=386.0, avg_strikes=2.58, avg_first_out_rate=0.039
Contestant 2: avg_win_rate=0.194, avg_score=1450.2, avg_median_score=1367.0, avg_stdev=297.1, avg_strikes=2.78, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.144, avg_score=1175.5, avg_median_score=1163.2, avg_stdev=233.9, avg_strikes=2.56, avg_first_out_rate=0.353
Last survivor but lost rate: 0.181
Solo started behind rate: 0.314
Solo started behind and lost rate: 0.529
Avg solo start deficit: 193.3
Avg solo turns taken: 7.84
Solo had winning answer rate: 0.109
Solo had winning answer given started behind rate: 0.388
Solo start deficit buckets: 1-75: 0.381, 76-150: 0.231, 151-250: 0.125, 251+: 0.263
Avg final board read: -0.034
Avg absolute final board read: 0.093
Avg strong harsh board rate: 0.122
Avg strong generous board rate: 0.044
Avg final cutoff estimate: 64.15
Avg final cutoff uncertainty: 0.388
Avg low uncertainty rate: 0.101
Avg high cutoff rate: 0.421
Avg final safe floor: 51.83
Avg final local density read: 0.063
Avg final surprise read: 0.181
Avg final near-cutoff hits: 2.30
Avg final near-cutoff misses: 0.06
Mode rates: safe=0.630, risky=0.255, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.099
Double window mode rates: safe=0.687, risky=0.313, blind_risk=0.000
Context rates: open=0.672, tight=0.148, uncertain=0.493, 
Context-action rates: risky_on_open=0.252, safe_on_tight=0.877, risky_on_uncertain=0.286, safe_on_uncertain=0.666, risky_on_double_window=0.313, safe_on_double_window=0.687
```

**Notes:**

**Run 3 &rarr; Run 4 Aggregate Comparison**

| Metric | Run 3 | Run 4 | Read | 
| - | - | - | - |
| C1 WR | 0.669 | 0.661 | Stable/slightly lower
| C2 WR | 0.190 | 0.194 | Stable/slightly lower
| C3 WR | 0.141 | 0.144 | Stable/slightly lower
| Last survivor but lost | 0.179 | 0.181 | Basically unchanged
| Solo started behind/lost | 0.544 | 0.529 | Slightly better
| Avg solo deficit | 196.7 | 193.3 | Slightly better
| Avg cutoff estimate | 63.92 | 64.15 | Basically unchanged
| Avg safe floor | 51.59 | 51.83 | Basically unchanged
| Safe mode rate | 0.625 | 0.630 | Slightly safer
| Risky mode rate | 0.261 | 0.255 | Slightly less risky
| Double-window risky | 0.321 | 0.313 | Slightly less risky
| Open context rate | 0.781 | 0.672 | Clearly improved
| Risky-on-open | 0.242 | 0.252 | Slightly more meaningful
| Safe-on-tight | 0.876 | 0.877 | Basically unchanged

This is idea lfor a one-line turning run, as the main target metric moved a lot while the gameplay ecosystem barely moved.

The aggregate `open_context_rate` drop from 0.781 to 0.672 shows meaningful improvement. It did not become rare but it no longer is firing on nearly 80% of all decisions.

Looking at a per-category level:

| Category | Run 3 Risky-on-open | Run 4 Risky on Open 
| - | - | -
| OPS+ | 0.173 | 0.174
| bWAR | 0.107 | 0.110
| HR since 2000 | 0.499 | 0.501
| Hits since 1900 | 0.318 | 0.320
| MVP | 0.072 | 0.075

These barely moved, but that's important because the tuning **changed which states count as open** but did not change how much "open" affects decision pressure. As such, risk-on-open only nudged upward since the pressure effect stayed the same.
- This is not a problem, it just means that Run 4 mostly improved interpretability, not behavior.

**Takeaway:**

The single open-threshold change made `open` rarer without destabilizing the simulation.

The earlier diagnosis was correct in which the old `open` definition was too permissive, and tightening the thresholds improved the label's usefulness.

**Conclusions:**

1. **Tight and uncertainty remained stable**

Tight boards still create safe decisions:

- `safe_on_tight`: Run 3: 0.876 vs Run 4: 0.877

This is very important as the strongest healthy M4 behavior stayed intact.

Simiarly, uncertainty also basically stayed the same:

- `uncertainty_context_rate`: Run 3: 0.493 vs Run 4: 0.493
- `safe_on_uncertain`: Run 3: 0.659 vs Run 4: 0.666
- `risky_on_uncertain`: Run 3: 0.293 vs Run 4: 0.286

The open-threshold tuning did not accidentially disrupt the rest of the context system.

2. **Gameplay stability is very good**

The win rates barely shifted:
- Run 3 C1/C2/C3: 0.669/0.190/0.141
- Run 4 C1/C2/C3: 0.661/0.194/0.144

Though marginal, still positive movement because C1 came down a little and C2/C3 came up a little, all without creating a new imbalance.

Solo metrics also did not woren, in fact, they slightly improved:
- `solo started behind/lost`: Run 3: 0.544 vs Run 4: 0.529
- `avg solo deficit`: Run 3: 196.7 vs Run 4: 193.3

Run 4 did not harm the main system.

In conclusion, Run 4 applied a single tuning change to the `open` context definition, raising the local-density and surprise thresholds from `0.08 / 0.12` to `0.10 / 0.18`. The goal was to make open-context states rarer and more meaningful without changing broader strategy logic.

The run succeeded as a first tuning pass. Aggregate `open_context_rate` dropped from 0.781 to 0.672, while overall win rates, solo metrics, cutoff estimates, and safe-floor behavior remained stable. Category-level results also improved: harder categories such as bWAR and MVP saw larger reductions in open-context rate, while Home Runs since 2000 remained the most open category.

The main behavioral structure of M4 remained intact. `safe_on_tight` stayed very high at 0.877, uncertainty behavior remained stable, and double-window risky rate only moved slightly from 0.321 to 0.313. This suggests the tuning improved the interpretability of the open label without destabilizing the simulator.

The remaining insight is that `open` still appears to be a composite signal. It captures both answer-density and generosity/surprise, which may not always imply the same strategic behavior. A future diagnostic run should consider splitting open into sub-signals such as `dense` and `generous` to better understand what is driving open-context decisions.

### Run 5

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.643, avg_score=1818.4, median_score=1751.0, stdev=325.6, avg_strikes=2.98, first_out_rate=0.086
Contestant 2: win_rate=0.193, avg_score=1595.4, median_score=1581.0, stdev=225.7, avg_strikes=2.99, first_out_rate=0.442
Contestant 3: win_rate=0.164, avg_score=1262.5, median_score=1183.0, stdev=281.2, avg_strikes=2.98, first_out_rate=0.466
Last survivor but lost rate: 0.251
Solo started behind rate: 0.391
Solo started behind and lost rate: 0.642
Avg solo start deficit: 270.1
Avg solo turns taken: 2.57
Solo had winning answer rate: 0.106
Solo had winning answer given started behind rate: 0.270
Solo start deficit buckets: 1-75: 0.272, 76-150: 0.209, 151-250: 0.132, 251+: 0.387
Avg final board read: 0.040
Avg absolute final board read: 0.097
Strong harsh board rate: 0.050
Strong generous board rate: 0.149
Avg final cutoff estimate: 66.84
Avg final cutoff uncertainty: 0.351
Low uncertainty rate: 0.043
High cutoff rate: 0.425
Avg final safe floor: 54.73
Avg final local density read: 0.054
Avg final surprise read: 0.174
Avg final near-cutoff hits: 2.74
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.750, risky=0.203, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.770, risky=0.230, blind_risk=0.000
Context rates: open=0.699, dense=0.405, generous=0.349, dense_and_generous=0.055, tight=0.093, uncertain=0.370, 
Context-action rates: risky_on_open=0.174, risky_on_dense=0.256, risky_on_generous=0.062, risky_on_dense_and_generous=0.066, safe_on_tight=0.877, risky_on_uncertain=0.339, safe_on_uncertain=0.648, risky_on_double_window=0.230, safe_on_double_window=0.770

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.963, avg_score=2586.9, median_score=2663.0, stdev=472.2, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.004, avg_score=889.0, median_score=881.0, stdev=216.2, avg_strikes=3.00, first_out_rate=0.881
Contestant 3: win_rate=0.033, avg_score=940.0, median_score=895.0, stdev=263.1, avg_strikes=3.00, first_out_rate=0.118
Last survivor but lost rate: 0.041
Solo started behind rate: 0.127
Solo started behind and lost rate: 0.325
Avg solo start deficit: 136.1
Avg solo turns taken: 13.26
Solo had winning answer rate: 0.070
Solo had winning answer given started behind rate: 0.555
Solo start deficit buckets: 1-75: 0.484, 76-150: 0.217, 151-250: 0.121, 251+: 0.178
Avg final board read: -0.032
Avg absolute final board read: 0.079
Strong harsh board rate: 0.044
Strong generous board rate: 0.024
Avg final cutoff estimate: 71.60
Avg final cutoff uncertainty: 0.462
Low uncertainty rate: 0.001
High cutoff rate: 0.648
Avg final safe floor: 58.83
Avg final local density read: 0.059
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.90
Avg final near-cutoff misses: 0.12
Mode rates: safe=0.637, risky=0.142, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.210
Double window mode rates: safe=0.824, risky=0.176, blind_risk=0.000
Context rates: open=0.603, dense=0.281, generous=0.358, dense_and_generous=0.037, tight=0.200, uncertain=0.696, 
Context-action rates: risky_on_open=0.110, risky_on_dense=0.163, risky_on_generous=0.065, risky_on_dense_and_generous=0.076, safe_on_tight=0.944, risky_on_uncertain=0.180, safe_on_uncertain=0.777, risky_on_double_window=0.176, safe_on_double_window=0.824

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.546, avg_score=1756.0, median_score=1739.0, stdev=99.9, avg_strikes=1.30, first_out_rate=0.002
Contestant 2: win_rate=0.225, avg_score=1674.3, median_score=1679.0, stdev=112.0, avg_strikes=2.08, first_out_rate=0.355
Contestant 3: win_rate=0.229, avg_score=1595.3, median_score=1643.0, stdev=158.0, avg_strikes=1.19, first_out_rate=0.069
Last survivor but lost rate: 0.144
Solo started behind rate: 0.232
Solo started behind and lost rate: 0.621
Avg solo start deficit: 179.2
Avg solo turns taken: 2.50
Solo had winning answer rate: 0.082
Solo had winning answer given started behind rate: 0.353
Solo start deficit buckets: 1-75: 0.392, 76-150: 0.242, 151-250: 0.104, 251+: 0.262
Avg final board read: -0.079
Avg absolute final board read: 0.103
Strong harsh board rate: 0.254
Strong generous board rate: 0.001
Avg final cutoff estimate: 52.66
Avg final cutoff uncertainty: 0.283
Low uncertainty rate: 0.298
High cutoff rate: 0.179
Avg final safe floor: 40.96
Avg final local density read: 0.077
Avg final surprise read: 0.163
Avg final near-cutoff hits: 2.54
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.504, risky=0.475, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.004
Double window mode rates: safe=0.494, risky=0.506, blind_risk=0.000
Context rates: open=0.740, dense=0.566, generous=0.199, dense_and_generous=0.024, tight=0.100, uncertain=0.323, 
Context-action rates: risky_on_open=0.501, risky_on_dense=0.583, risky_on_generous=0.231, risky_on_dense_and_generous=0.193, safe_on_tight=0.723, risky_on_uncertain=0.570, safe_on_uncertain=0.414, risky_on_double_window=0.506, safe_on_double_window=0.494

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.548, avg_score=1759.4, median_score=1742.0, stdev=182.9, avg_strikes=2.64, first_out_rate=0.091
Contestant 2: win_rate=0.175, avg_score=1647.9, median_score=1653.0, stdev=161.1, avg_strikes=2.81, first_out_rate=0.622
Contestant 3: win_rate=0.277, avg_score=1504.5, median_score=1573.0, stdev=233.3, avg_strikes=2.62, first_out_rate=0.167
Last survivor but lost rate: 0.362
Solo started behind rate: 0.485
Solo started behind and lost rate: 0.747
Avg solo start deficit: 276.9
Avg solo turns taken: 2.12
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.205
Solo start deficit buckets: 1-75: 0.296, 76-150: 0.187, 151-250: 0.100, 251+: 0.417
Avg final board read: -0.023
Avg absolute final board read: 0.096
Strong harsh board rate: 0.142
Strong generous board rate: 0.043
Avg final cutoff estimate: 58.94
Avg final cutoff uncertainty: 0.308
Low uncertainty rate: 0.164
High cutoff rate: 0.274
Avg final safe floor: 47.09
Avg final local density read: 0.069
Avg final surprise read: 0.156
Avg final near-cutoff hits: 2.86
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.648, risky=0.321, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.012
Double window mode rates: safe=0.639, risky=0.361, blind_risk=0.000
Context rates: open=0.720, dense=0.489, generous=0.272, dense_and_generous=0.041, tight=0.107, uncertain=0.329, 
Context-action rates: risky_on_open=0.320, risky_on_dense=0.415, risky_on_generous=0.118, risky_on_dense_and_generous=0.119, safe_on_tight=0.789, risky_on_uncertain=0.461, safe_on_uncertain=0.525, risky_on_double_window=0.361, safe_on_double_window=0.639

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.606, avg_score=1831.5, median_score=2165.0, stdev=849.6, avg_strikes=3.00, first_out_rate=0.014
Contestant 2: win_rate=0.375, avg_score=1444.4, median_score=1041.0, stdev=770.5, avg_strikes=3.00, first_out_rate=0.041
Contestant 3: win_rate=0.020, avg_score=574.9, median_score=522.0, stdev=233.6, avg_strikes=3.00, first_out_rate=0.945
Last survivor but lost rate: 0.105
Solo started behind rate: 0.338
Solo started behind and lost rate: 0.311
Avg solo start deficit: 104.2
Avg solo turns taken: 18.76
Solo had winning answer rate: 0.189
Solo had winning answer given started behind rate: 0.559
Solo start deficit buckets: 1-75: 0.463, 76-150: 0.297, 151-250: 0.167, 251+: 0.073
Avg final board read: -0.077
Avg absolute final board read: 0.088
Strong harsh board rate: 0.118
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.73
Avg final cutoff uncertainty: 0.536
Low uncertainty rate: 0.000
High cutoff rate: 0.578
Avg final safe floor: 57.52
Avg final local density read: 0.055
Avg final surprise read: 0.214
Avg final near-cutoff hits: 1.44
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.609, risky=0.119, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.259
Double window mode rates: safe=0.808, risky=0.192, blind_risk=0.000
Context rates: open=0.587, dense=0.236, generous=0.371, dense_and_generous=0.019, tight=0.249, uncertain=0.785, 
Context-action rates: risky_on_open=0.075, risky_on_dense=0.126, risky_on_generous=0.045, risky_on_dense_and_generous=0.106, safe_on_tight=0.931, risky_on_uncertain=0.147, safe_on_uncertain=0.750, risky_on_double_window=0.192, safe_on_double_window=0.808

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.661, avg_score=1950.4, avg_median_score=2012.0, avg_stdev=386.0, avg_strikes=2.58, avg_first_out_rate=0.039
Contestant 2: avg_win_rate=0.194, avg_score=1450.2, avg_median_score=1367.0, avg_stdev=297.1, avg_strikes=2.78, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.144, avg_score=1175.5, avg_median_score=1163.2, avg_stdev=233.9, avg_strikes=2.56, avg_first_out_rate=0.353
Last survivor but lost rate: 0.181
Solo started behind rate: 0.314
Solo started behind and lost rate: 0.529
Avg solo start deficit: 193.3
Avg solo turns taken: 7.84
Solo had winning answer rate: 0.109
Solo had winning answer given started behind rate: 0.388
Solo start deficit buckets: 1-75: 0.381, 76-150: 0.231, 151-250: 0.125, 251+: 0.263
Avg final board read: -0.034
Avg absolute final board read: 0.093
Avg strong harsh board rate: 0.122
Avg strong generous board rate: 0.044
Avg final cutoff estimate: 64.15
Avg final cutoff uncertainty: 0.388
Avg low uncertainty rate: 0.101
Avg high cutoff rate: 0.421
Avg final safe floor: 51.83
Avg final local density read: 0.063
Avg final surprise read: 0.181
Avg final near-cutoff hits: 2.30
Avg final near-cutoff misses: 0.06
Mode rates: safe=0.630, risky=0.255, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.099
Double window mode rates: safe=0.687, risky=0.313, blind_risk=0.000
Context rates: open=0.672, dense=0.399, generous=0.308, dense_and_generous=0.036, tight=0.148, uncertain=0.493, 
Context-action rates: risky_on_open=0.252, risky_on_dense=0.363, risky_on_generous=0.091, risky_on_dense_and_generous=0.102, safe_on_tight=0.877, risky_on_uncertain=0.286, safe_on_uncertain=0.666, risky_on_double_window=0.313, safe_on_double_window=0.687
```

**Notes:**

Run 5 worked as intended as a diagnostic run as the gameplay stayed identical to run 4, while the new metrics exposed what is actually driving `open`:

| Metric | Run 4 | Run 5 
| - | - | -
| C1 WR | 0.611 | 0.611
| C2 WR | 0.194 | 0.194
| C3 WR | 0.144 | 0.144
| Solo started behind/lost | 0.529 | 0.529
| Avg solo deficit | 193.3 | 193.3
| Mode safe | 0.630 | 0.630
| Mode risky | 0.255 | 0.255
| Double-window risky | 0.313 | 0.313
| Open context rate | 0.672 | 0.672

Run 5 only added visibility, `open = dense or generous` preserved Run 4 logic.

**Takeaway:**

`open` is mostly density-driven, but category-dependent:
- open = 0.672
- dense = 0.399
- generous = 0.308
- dense_and_generous = 0.036

This means that `open` is not one monolithic thing. It is usually either **dense** or **generous**, but rarely both at the same time, as the overlap is only 0.036.

In other words: Open is composite, and the two components are behaving differently.

**Density is the real aggression signal:**
- `risky_on_open` = 0.252
- `risky_on_dense` = 0.363
- `risky_on_generous` = 0.091
- `risky_on_dense_and_generous` = 0.102

This shows that density is much more predicitive of risk than generosity.

To put it plainly: When the board feels answer-rich near the line, players are more willing to attack. When the board merely feels generous or surprising, they are actually still conservative.

**Category-level results:**

The split also makes the categories make more sense:

| Category | Open | Dense | Generous | Dense + Generous | Read
| - | - | - | - | - | -
| OPS+ | 0.699 | 0.405 | 0.349 | 0.055 | Mixed open
| bWAR | 0.603 | 0.281 | 0.358 | 0.037 | More generous/uncertain than dense
| HR since 2000 | 0.740 | 0.566 | 0.199 | 0.024 | Strongly density-driven
| Hits since 1900 | 0.720 | 0.489 | 0.272 | 0.041 | Density-driven
| MVP | 0.587 | 0.236 | 0.371 | 0.019 | Generosity-driven, not attackable

HR and Hits are exactly where they're expected, as they are more `dense`, and their risky-on-dense rates are high:
- HR `risky_on_dense` = 0.583
- Hits `risky_on_dense` = 0.415

On the other hand, bWAR and MVP have more generous than dense signal, but their risky-on-generous rates are tiny:
- bWAR `risky_on_generous` = 0.065
- MVP `risky_on_generous` = 0.045

As a result categories can "feel open" because surprisng/generous outcomes happen, but the players still don't treat them as attackable, which is a very good distinction. 

In regards to the still-high open rate, Run 5 explains why it is high, despite in the previous run of Run 4, `open` did improve from 0.781 to 0.672. Because the system still uses `open = dense or generous`, any decision that is either density-positive or generosity-positive becomes open.
- Since dense is 0.399 and generous is 0.308, their union naturally gets up to 0.672
- The key is the low overlap of 0.036, as the `OR` condition adds them together more than it consolidates them

This means that the high open rate is not necessarily a bug, rather it means that `open` is currently a broad umbrella state.


**Conclusion:**
Run 5 is successful because it shows that `open` is not too high because one single signal is broken, rather it is high because `open` is a union of two mostly separate board signals.

The real strategic insight is that density creates attackability, while generosity creates board loosness/forgiveness, but not necessarily aggression.

### Run 6

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.643, avg_score=1818.1, median_score=1751.0, stdev=325.5, avg_strikes=2.98, first_out_rate=0.087
Contestant 2: win_rate=0.194, avg_score=1595.3, median_score=1581.0, stdev=225.6, avg_strikes=2.99, first_out_rate=0.440
Contestant 3: win_rate=0.163, avg_score=1262.4, median_score=1183.0, stdev=280.9, avg_strikes=2.98, first_out_rate=0.467
Last survivor but lost rate: 0.252
Solo started behind rate: 0.392
Solo started behind and lost rate: 0.643
Avg solo start deficit: 269.7
Avg solo turns taken: 2.57
Solo had winning answer rate: 0.105
Solo had winning answer given started behind rate: 0.269
Solo start deficit buckets: 1-75: 0.270, 76-150: 0.209, 151-250: 0.135, 251+: 0.386
Avg final board read: 0.040
Avg absolute final board read: 0.097
Strong harsh board rate: 0.050
Strong generous board rate: 0.150
Avg final cutoff estimate: 66.85
Avg final cutoff uncertainty: 0.351
Low uncertainty rate: 0.043
High cutoff rate: 0.426
Avg final safe floor: 54.74
Avg final local density read: 0.054
Avg final surprise read: 0.174
Avg final near-cutoff hits: 2.74
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.750, risky=0.203, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.770, risky=0.230, blind_risk=0.000
Context rates: open=0.699, dense=0.405, generous=0.349, dense_and_generous=0.055, tight=0.093, uncertain=0.370, 
Context-action rates: risky_on_open=0.174, risky_on_dense=0.256, risky_on_generous=0.061, risky_on_dense_and_generous=0.066, safe_on_tight=0.877, risky_on_uncertain=0.339, safe_on_uncertain=0.648, risky_on_double_window=0.230, safe_on_double_window=0.770

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.964, avg_score=2587.5, median_score=2663.0, stdev=471.4, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.004, avg_score=888.8, median_score=881.0, stdev=215.9, avg_strikes=3.00, first_out_rate=0.881
Contestant 3: win_rate=0.032, avg_score=939.6, median_score=895.0, stdev=262.4, avg_strikes=3.00, first_out_rate=0.118
Last survivor but lost rate: 0.041
Solo started behind rate: 0.125
Solo started behind and lost rate: 0.326
Avg solo start deficit: 136.8
Avg solo turns taken: 13.26
Solo had winning answer rate: 0.069
Solo had winning answer given started behind rate: 0.551
Solo start deficit buckets: 1-75: 0.480, 76-150: 0.217, 151-250: 0.125, 251+: 0.178
Avg final board read: -0.032
Avg absolute final board read: 0.079
Strong harsh board rate: 0.044
Strong generous board rate: 0.024
Avg final cutoff estimate: 71.60
Avg final cutoff uncertainty: 0.462
Low uncertainty rate: 0.001
High cutoff rate: 0.649
Avg final safe floor: 58.82
Avg final local density read: 0.059
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.90
Avg final near-cutoff misses: 0.12
Mode rates: safe=0.637, risky=0.142, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.210
Double window mode rates: safe=0.824, risky=0.176, blind_risk=0.000
Context rates: open=0.603, dense=0.281, generous=0.358, dense_and_generous=0.037, tight=0.200, uncertain=0.696, 
Context-action rates: risky_on_open=0.109, risky_on_dense=0.163, risky_on_generous=0.064, risky_on_dense_and_generous=0.077, safe_on_tight=0.944, risky_on_uncertain=0.180, safe_on_uncertain=0.777, risky_on_double_window=0.176, safe_on_double_window=0.824

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.548, avg_score=1756.0, median_score=1739.0, stdev=99.8, avg_strikes=1.30, first_out_rate=0.002
Contestant 2: win_rate=0.222, avg_score=1674.0, median_score=1679.0, stdev=111.8, avg_strikes=2.08, first_out_rate=0.355
Contestant 3: win_rate=0.230, avg_score=1595.5, median_score=1643.0, stdev=157.9, avg_strikes=1.19, first_out_rate=0.070
Last survivor but lost rate: 0.146
Solo started behind rate: 0.234
Solo started behind and lost rate: 0.624
Avg solo start deficit: 178.1
Avg solo turns taken: 2.50
Solo had winning answer rate: 0.081
Solo had winning answer given started behind rate: 0.348
Solo start deficit buckets: 1-75: 0.388, 76-150: 0.249, 151-250: 0.104, 251+: 0.259
Avg final board read: -0.078
Avg absolute final board read: 0.104
Strong harsh board rate: 0.254
Strong generous board rate: 0.001
Avg final cutoff estimate: 52.69
Avg final cutoff uncertainty: 0.283
Low uncertainty rate: 0.298
High cutoff rate: 0.179
Avg final safe floor: 40.99
Avg final local density read: 0.077
Avg final surprise read: 0.163
Avg final near-cutoff hits: 2.54
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.505, risky=0.474, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.004
Double window mode rates: safe=0.494, risky=0.506, blind_risk=0.000
Context rates: open=0.741, dense=0.566, generous=0.199, dense_and_generous=0.024, tight=0.100, uncertain=0.323, 
Context-action rates: risky_on_open=0.500, risky_on_dense=0.583, risky_on_generous=0.227, risky_on_dense_and_generous=0.193, safe_on_tight=0.725, risky_on_uncertain=0.570, safe_on_uncertain=0.414, risky_on_double_window=0.506, safe_on_double_window=0.494

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.550, avg_score=1759.8, median_score=1742.0, stdev=183.0, avg_strikes=2.63, first_out_rate=0.091
Contestant 2: win_rate=0.173, avg_score=1647.8, median_score=1653.0, stdev=161.1, avg_strikes=2.81, first_out_rate=0.621
Contestant 3: win_rate=0.277, avg_score=1504.6, median_score=1572.5, stdev=233.3, avg_strikes=2.62, first_out_rate=0.167
Last survivor but lost rate: 0.361
Solo started behind rate: 0.485
Solo started behind and lost rate: 0.746
Avg solo start deficit: 276.2
Avg solo turns taken: 2.12
Solo had winning answer rate: 0.098
Solo had winning answer given started behind rate: 0.202
Solo start deficit buckets: 1-75: 0.292, 76-150: 0.193, 151-250: 0.100, 251+: 0.415
Avg final board read: -0.022
Avg absolute final board read: 0.096
Strong harsh board rate: 0.142
Strong generous board rate: 0.043
Avg final cutoff estimate: 59.00
Avg final cutoff uncertainty: 0.309
Low uncertainty rate: 0.164
High cutoff rate: 0.274
Avg final safe floor: 47.15
Avg final local density read: 0.069
Avg final surprise read: 0.156
Avg final near-cutoff hits: 2.86
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.649, risky=0.321, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.012
Double window mode rates: safe=0.639, risky=0.361, blind_risk=0.000
Context rates: open=0.721, dense=0.489, generous=0.272, dense_and_generous=0.041, tight=0.107, uncertain=0.329, 
Context-action rates: risky_on_open=0.319, risky_on_dense=0.415, risky_on_generous=0.116, risky_on_dense_and_generous=0.119, safe_on_tight=0.789, risky_on_uncertain=0.461, safe_on_uncertain=0.525, risky_on_double_window=0.361, safe_on_double_window=0.639

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.607, avg_score=1833.3, median_score=2168.5, stdev=850.4, avg_strikes=3.00, first_out_rate=0.014
Contestant 2: win_rate=0.374, avg_score=1443.1, median_score=1039.0, stdev=770.3, avg_strikes=3.00, first_out_rate=0.041
Contestant 3: win_rate=0.019, avg_score=574.6, median_score=522.0, stdev=233.1, avg_strikes=3.00, first_out_rate=0.945
Last survivor but lost rate: 0.105
Solo started behind rate: 0.337
Solo started behind and lost rate: 0.312
Avg solo start deficit: 104.4
Avg solo turns taken: 18.78
Solo had winning answer rate: 0.188
Solo had winning answer given started behind rate: 0.558
Solo start deficit buckets: 1-75: 0.462, 76-150: 0.297, 151-250: 0.167, 251+: 0.073
Avg final board read: -0.077
Avg absolute final board read: 0.088
Strong harsh board rate: 0.118
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.72
Avg final cutoff uncertainty: 0.536
Low uncertainty rate: 0.000
High cutoff rate: 0.577
Avg final safe floor: 57.50
Avg final local density read: 0.055
Avg final surprise read: 0.214
Avg final near-cutoff hits: 1.43
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.609, risky=0.118, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.259
Double window mode rates: safe=0.808, risky=0.192, blind_risk=0.000
Context rates: open=0.587, dense=0.236, generous=0.371, dense_and_generous=0.019, tight=0.249, uncertain=0.785, 
Context-action rates: risky_on_open=0.075, risky_on_dense=0.126, risky_on_generous=0.044, risky_on_dense_and_generous=0.106, safe_on_tight=0.932, risky_on_uncertain=0.146, safe_on_uncertain=0.750, risky_on_double_window=0.192, safe_on_double_window=0.808

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.662, avg_score=1951.0, avg_median_score=2012.7, avg_stdev=386.0, avg_strikes=2.58, avg_first_out_rate=0.039
Contestant 2: avg_win_rate=0.193, avg_score=1449.8, avg_median_score=1366.6, avg_stdev=297.0, avg_strikes=2.78, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.144, avg_score=1175.3, avg_median_score=1163.1, avg_stdev=233.5, avg_strikes=2.56, avg_first_out_rate=0.354
Last survivor but lost rate: 0.181
Solo started behind rate: 0.314
Solo started behind and lost rate: 0.530
Avg solo start deficit: 193.0
Avg solo turns taken: 7.85
Solo had winning answer rate: 0.108
Solo had winning answer given started behind rate: 0.386
Solo start deficit buckets: 1-75: 0.379, 76-150: 0.233, 151-250: 0.126, 251+: 0.262
Avg final board read: -0.034
Avg absolute final board read: 0.093
Avg strong harsh board rate: 0.122
Avg strong generous board rate: 0.044
Avg final cutoff estimate: 64.17
Avg final cutoff uncertainty: 0.388
Avg low uncertainty rate: 0.101
Avg high cutoff rate: 0.421
Avg final safe floor: 51.84
Avg final local density read: 0.063
Avg final surprise read: 0.181
Avg final near-cutoff hits: 2.30
Avg final near-cutoff misses: 0.06
Mode rates: safe=0.631, risky=0.255, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.099
Double window mode rates: safe=0.687, risky=0.313, blind_risk=0.000
Context rates: open=0.672, dense=0.399, generous=0.308, dense_and_generous=0.035, tight=0.147, uncertain=0.493, 
Context-action rates: risky_on_open=0.252, risky_on_dense=0.363, risky_on_generous=0.090, risky_on_dense_and_generous=0.102, safe_on_tight=0.878, risky_on_uncertain=0.286, safe_on_uncertain=0.666, risky_on_double_window=0.313, safe_on_double_window=0.687
```

**Notes:**

The change made in behavior from Run 5 to Run 6: 

Run 5:
```
if ctx["open"] and player_state.strikes == 0:
    pressure += 0.06
```

Run 6:
```
if ctx["dense"] and player_state.strikes == 0:
    pressure += 0.06
elif ctx["generous"] and player_state.strikes == 0:
    pressure += 0.02
```

This means that `open` still exists as a broad context label, but it no longer directly drives pressure, instead:
- dense = full aggression bonus
- generous = small confidence/looseness bonus

**Run 5 &rarr; Run 6: almost no destabilization**

Across categories, both runs are extremely close:

| Metric | Run 5 | Run 6 | Read
| - | - | - | -
| OPS+ C1 WR | 0.643 | 0.643 | Unchanged
| bWAR C1 WR | 0.963 | 0.964 | Tiny shift
| HR C1 WR | 0.546 | 0.548 | Tiny shift
| Hits C1 WR | 0.548 | 0.550 | Tiny shift
| MVP C1 WR | 0.606 | 0.607 | Tiny shift

The category-level mode rates also barely moved. This means that the adjustment did not break the simulator, it preserved the existing strategic environment.

**Takeaway:**

`generous` was already weak as an aggression driver:
- `risky_on_dense` = much higher
- `risky_on_generous` = much lower

Examples of Run 6 keeping that behavior:

| Category | Run 6 risky_on_dense | Run 6 risky_on_generous
| - | - | -
| OPS+ | 0.256 | 0.061
| bWAR | 0.163 | 0.064
| HR since 2000 | 0.583 | 0.227
| Hits since 1900 | 0.415 | 0.116
| MVP | 0.126 | 0.044

The model is saying something important:
- Density creates attackability
- Generosity creates board loosness, but not necessarily aggression

However, there was also not a big behavioral shift. It is important that the change is conceptually cleaner, but numerically small.
- This is due to a lot of the decisions that mattered were probably already being shaped by other factors:
    - base player style
    - score gap
    - strike count
    - double-window logic
    - uncertainty
    - tight-board penalties
    - solo/endagme modes

Further, many `generous` states were already low-risk environments where players are not close to crossing the `risk_score >= 0.5` threshold.
- Reducing the generous bonus from effecively `+0.06` under the old `open` logic to `+0.02` did not move many decisions across the safe/risky boundary

**Conclusion:**

Run 6 applied the dense/generous split behaviorally. In previous runs, the broad `open` context gave a full aggression bonus whenever either density or generosity was present. Run 6 changed this so that dense boards receive the full aggression bonus, while generous boards receive only a smaller pressure increase.

The results were highly stable compared to Run 5. Win rates, solo metrics, mode rates, and category behavior changed only marginally. This suggests that the dense/generous split can be introduced into player decision-making without destabilizing the simulator.

The main conceptual improvement is that M4 now distinguishes between two kinds of openness: density-driven attackability and generosity-driven board looseness. Density remains the much stronger predictor of risky behavior, while generosity alone continues to produce more conservative play. This matches the observed behavior from real episodes, where players attack when there are many viable near-line answers, but do not necessarily become aggressive simply because the board feels forgiving.

One caveat is that the double-window branch still uses the broad `open` context as its gate for risky/safe alternation. This is acceptable for now, but it remains a possible future tuning point if double-window behavior needs to distinguish dense and generous boards more explicitly.

### Run 7

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.642, avg_score=1817.0, median_score=1746.0, stdev=325.2, avg_strikes=2.98, first_out_rate=0.086
Contestant 2: win_rate=0.198, avg_score=1598.1, median_score=1582.0, stdev=223.6, avg_strikes=2.99, first_out_rate=0.439
Contestant 3: win_rate=0.159, avg_score=1259.5, median_score=1183.5, stdev=276.8, avg_strikes=2.98, first_out_rate=0.469
Last survivor but lost rate: 0.252
Solo started behind rate: 0.398
Solo started behind and lost rate: 0.634
Avg solo start deficit: 263.5
Avg solo turns taken: 2.56
Solo had winning answer rate: 0.113
Solo had winning answer given started behind rate: 0.285
Solo start deficit buckets: 1-75: 0.292, 76-150: 0.203, 151-250: 0.129, 251+: 0.376
Avg final board read: 0.044
Avg absolute final board read: 0.095
Strong harsh board rate: 0.049
Strong generous board rate: 0.150
Avg final cutoff estimate: 67.26
Avg final cutoff uncertainty: 0.353
Low uncertainty rate: 0.043
High cutoff rate: 0.428
Avg final safe floor: 55.14
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.73
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.755, risky=0.198, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.777, risky=0.223, blind_risk=0.000
Context rates: open=0.703, dense=0.405, generous=0.352, dense_and_generous=0.055, tight=0.089, uncertain=0.370, 
Context-action rates: risky_on_open=0.166, risky_on_dense=0.256, risky_on_generous=0.048, risky_on_dense_and_generous=0.066, safe_on_tight=0.951, risky_on_uncertain=0.339, safe_on_uncertain=0.648, risky_on_double_window=0.223, safe_on_double_window=0.777

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.966, avg_score=2594.2, median_score=2667.0, stdev=463.9, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.004, avg_score=888.1, median_score=880.0, stdev=215.8, avg_strikes=3.00, first_out_rate=0.882
Contestant 3: win_rate=0.030, avg_score=936.2, median_score=894.0, stdev=258.6, avg_strikes=3.00, first_out_rate=0.117
Last survivor but lost rate: 0.036
Solo started behind rate: 0.117
Solo started behind and lost rate: 0.307
Avg solo start deficit: 133.1
Avg solo turns taken: 13.63
Solo had winning answer rate: 0.068
Solo had winning answer given started behind rate: 0.579
Solo start deficit buckets: 1-75: 0.512, 76-150: 0.205, 151-250: 0.110, 251+: 0.173
Avg final board read: -0.031
Avg absolute final board read: 0.079
Strong harsh board rate: 0.043
Strong generous board rate: 0.025
Avg final cutoff estimate: 71.67
Avg final cutoff uncertainty: 0.463
Low uncertainty rate: 0.001
High cutoff rate: 0.651
Avg final safe floor: 58.89
Avg final local density read: 0.059
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.91
Avg final near-cutoff misses: 0.12
Mode rates: safe=0.637, risky=0.140, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.211
Double window mode rates: safe=0.829, risky=0.171, blind_risk=0.000
Context rates: open=0.603, dense=0.282, generous=0.358, dense_and_generous=0.037, tight=0.199, uncertain=0.698, 
Context-action rates: risky_on_open=0.106, risky_on_dense=0.162, risky_on_generous=0.058, risky_on_dense_and_generous=0.076, safe_on_tight=0.962, risky_on_uncertain=0.178, safe_on_uncertain=0.779, risky_on_double_window=0.171, safe_on_double_window=0.829

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.540, avg_score=1753.7, median_score=1736.0, stdev=99.4, avg_strikes=1.32, first_out_rate=0.002
Contestant 2: win_rate=0.232, avg_score=1675.6, median_score=1681.0, stdev=110.4, avg_strikes=2.09, first_out_rate=0.360
Contestant 3: win_rate=0.228, avg_score=1595.8, median_score=1644.0, stdev=155.7, avg_strikes=1.21, first_out_rate=0.071
Last survivor but lost rate: 0.143
Solo started behind rate: 0.232
Solo started behind and lost rate: 0.617
Avg solo start deficit: 176.5
Avg solo turns taken: 2.53
Solo had winning answer rate: 0.083
Solo had winning answer given started behind rate: 0.358
Solo start deficit buckets: 1-75: 0.402, 76-150: 0.233, 151-250: 0.104, 251+: 0.261
Avg final board read: -0.074
Avg absolute final board read: 0.101
Strong harsh board rate: 0.255
Strong generous board rate: 0.001
Avg final cutoff estimate: 53.04
Avg final cutoff uncertainty: 0.285
Low uncertainty rate: 0.297
High cutoff rate: 0.182
Avg final safe floor: 41.33
Avg final local density read: 0.076
Avg final surprise read: 0.166
Avg final near-cutoff hits: 2.52
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.512, risky=0.467, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.004
Double window mode rates: safe=0.504, risky=0.496, blind_risk=0.000
Context rates: open=0.745, dense=0.565, generous=0.204, dense_and_generous=0.024, tight=0.097, uncertain=0.323, 
Context-action rates: risky_on_open=0.488, risky_on_dense=0.583, risky_on_generous=0.189, risky_on_dense_and_generous=0.193, safe_on_tight=0.810, risky_on_uncertain=0.570, safe_on_uncertain=0.414, risky_on_double_window=0.496, safe_on_double_window=0.504

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.550, avg_score=1759.9, median_score=1738.0, stdev=180.9, avg_strikes=2.64, first_out_rate=0.090
Contestant 2: win_rate=0.179, avg_score=1650.5, median_score=1654.0, stdev=157.4, avg_strikes=2.81, first_out_rate=0.623
Contestant 3: win_rate=0.271, avg_score=1501.7, median_score=1572.0, stdev=230.0, avg_strikes=2.62, first_out_rate=0.168
Last survivor but lost rate: 0.358
Solo started behind rate: 0.484
Solo started behind and lost rate: 0.740
Avg solo start deficit: 273.4
Avg solo turns taken: 2.14
Solo had winning answer rate: 0.100
Solo had winning answer given started behind rate: 0.207
Solo start deficit buckets: 1-75: 0.300, 76-150: 0.190, 151-250: 0.100, 251+: 0.410
Avg final board read: -0.017
Avg absolute final board read: 0.092
Strong harsh board rate: 0.140
Strong generous board rate: 0.043
Avg final cutoff estimate: 59.68
Avg final cutoff uncertainty: 0.311
Low uncertainty rate: 0.163
High cutoff rate: 0.276
Avg final safe floor: 47.81
Avg final local density read: 0.067
Avg final surprise read: 0.160
Avg final near-cutoff hits: 2.83
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.656, risky=0.314, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.012
Double window mode rates: safe=0.649, risky=0.351, blind_risk=0.000
Context rates: open=0.726, dense=0.488, generous=0.279, dense_and_generous=0.041, tight=0.101, uncertain=0.329, 
Context-action rates: risky_on_open=0.307, risky_on_dense=0.415, risky_on_generous=0.090, risky_on_dense_and_generous=0.118, safe_on_tight=0.879, risky_on_uncertain=0.461, safe_on_uncertain=0.525, risky_on_double_window=0.351, safe_on_double_window=0.649

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.602, avg_score=1834.0, median_score=2180.0, stdev=859.1, avg_strikes=3.00, first_out_rate=0.012
Contestant 2: win_rate=0.383, avg_score=1454.7, median_score=1039.0, stdev=779.6, avg_strikes=3.00, first_out_rate=0.037
Contestant 3: win_rate=0.015, avg_score=566.6, median_score=519.0, stdev=223.9, avg_strikes=3.00, first_out_rate=0.951
Last survivor but lost rate: 0.099
Solo started behind rate: 0.335
Solo started behind and lost rate: 0.296
Avg solo start deficit: 102.8
Avg solo turns taken: 19.56
Solo had winning answer rate: 0.191
Solo had winning answer given started behind rate: 0.571
Solo start deficit buckets: 1-75: 0.471, 76-150: 0.296, 151-250: 0.161, 251+: 0.072
Avg final board read: -0.076
Avg absolute final board read: 0.088
Strong harsh board rate: 0.116
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.50
Avg final cutoff uncertainty: 0.539
Low uncertainty rate: 0.000
High cutoff rate: 0.561
Avg final safe floor: 57.26
Avg final local density read: 0.056
Avg final surprise read: 0.215
Avg final near-cutoff hits: 1.44
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.610, risky=0.113, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.264
Double window mode rates: safe=0.820, risky=0.180, blind_risk=0.000
Context rates: open=0.589, dense=0.239, generous=0.368, dense_and_generous=0.019, tight=0.246, uncertain=0.785, 
Context-action rates: risky_on_open=0.066, risky_on_dense=0.123, risky_on_generous=0.030, risky_on_dense_and_generous=0.106, safe_on_tight=0.955, risky_on_uncertain=0.140, safe_on_uncertain=0.753, risky_on_double_window=0.180, safe_on_double_window=0.820

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.660, avg_score=1951.8, avg_median_score=2013.4, avg_stdev=385.7, avg_strikes=2.59, avg_first_out_rate=0.038
Contestant 2: avg_win_rate=0.199, avg_score=1453.4, avg_median_score=1367.2, avg_stdev=297.3, avg_strikes=2.78, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.140, avg_score=1171.9, avg_median_score=1162.5, avg_stdev=229.0, avg_strikes=2.56, avg_first_out_rate=0.355
Last survivor but lost rate: 0.178
Solo started behind rate: 0.313
Solo started behind and lost rate: 0.519
Avg solo start deficit: 189.8
Avg solo turns taken: 8.08
Solo had winning answer rate: 0.111
Solo had winning answer given started behind rate: 0.400
Solo start deficit buckets: 1-75: 0.395, 76-150: 0.225, 151-250: 0.121, 251+: 0.258
Avg final board read: -0.031
Avg absolute final board read: 0.091
Avg strong harsh board rate: 0.121
Avg strong generous board rate: 0.044
Avg final cutoff estimate: 64.43
Avg final cutoff uncertainty: 0.390
Avg low uncertainty rate: 0.101
Avg high cutoff rate: 0.420
Avg final safe floor: 52.09
Avg final local density read: 0.062
Avg final surprise read: 0.183
Avg final near-cutoff hits: 2.29
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.635, risky=0.250, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.101
Double window mode rates: safe=0.695, risky=0.305, blind_risk=0.000
Context rates: open=0.675, dense=0.400, generous=0.311, dense_and_generous=0.035, tight=0.144, uncertain=0.494, 
Context-action rates: risky_on_open=0.243, risky_on_dense=0.363, risky_on_generous=0.073, risky_on_dense_and_generous=0.102, safe_on_tight=0.926, risky_on_uncertain=0.283, safe_on_uncertain=0.667, risky_on_double_window=0.305, safe_on_double_window=0.695
```

**Notes:**

Run 7 was a curiosity test that targeted one part of M4 that was still using broad `open` behavior, which was the double-window alternation gate. Run 7 makes that gate more context-aware by changing `if player_state.strikes == 0 and ctx["open"]` to `if ... ctx["dense"] or (ctx["generous"] and not ctx["tight"])`.

Dense boards still allow risky/safe rhythm, generous boards allow it only if the board is not tight, and tight generous boards no longer get treated as freely attackable.

**Takeaway:**

The biggest visible effect is that the double-window behavior got a little safer:

| Category | Run 6 double risky | Run 7 double risky
| - | - | -
| OPS+ | 0.230 | 0.233
| bWAR | 0.176 | 0.171
| HR since 2000 | 0.506 | 0.496
| Hits since 1900 | 0.361 | 0.351
| MVP | 0.192 | 0.180

The Run 7 change did exactly as it was intended to do by not destroying the double-window rhythm, but filtering out some riskier alternation spots when `open` was only generous/tight rather than truly attackable

Category behavior also still makes sense:

| Metric | Result
| - | -
| HR risky | 0.467
| HR double-window | 0.496
| HR risky_on_dense| 0.583
| MVP risky | 0.113
| MVP double-window risky | 0.180
| bWAR risky | 0.140
| bWAR double-window risky | 0.171

From this, HR since 2000 remains the most aggressive category, which is good because the category is dense, recent, and answer-rich, which should still support aggression.

On the contrary, MVP and bWAR remain conservative, which also makes sense because those categories are less broadly attackable even when they produce generous/surprising outcomes

The main improvement is that safe-on-tight became cleaner:

| Category | Run 6 safe-on-tight | Run 7 safe-on-tight
| - | - | -
| OPS + | 0.877 | 0.951
| bWAR | 0.944 | 0.962
| HR | 0.725 | 0.810
| Hits | 0.789 | 0.879
| MVP | 0.932 | 0.955

This is meaningful improvement as tight contexts are now much more consistently survival-oriented across every category, especially HR and Hits
- Previously, even tight boards could still get double-window alternation through braod `open`, which has now been addressed

In other words, the context-aware model depicts:
- Dense board: allow aggression
- Generous but not tight: allow some rhythm
- Tight board: survival overrides rhythm

It must also be stated that the model was also not destabilized, as win rates remained largely unchanged, or otherwise moved only slightly.

**Conclusion:**

Run 7 extended the dense/generous split into the double-window logic. In previous runs, double-window risky/safe alternation still used the broad `open` context as its gate. Run 7 changed this so that dense boards continue to allow alternation, while generous boards only allow alternation when the board is not also tight.

The results were stable overall. Win rates and category identities remained close to Run 6, but double-window risky rates decreased slightly across all categories. More importantly, `safe_on_tight` increased meaningfully, suggesting that tight-board contexts now override risky/safe rhythm more consistently.

This makes Run 7 conceptually cleaner than Run 6. Dense contexts remain the main attackability signal, generous contexts remain a softer looseness signal, and tight contexts now more reliably force survival-oriented play. Run 7 is therefore a strong candidate for the final M4 behavior state.

**M4 Outcomes:**

Milestone 4 successfully added contextual strategy and multi-turn awareness to the simulator without destabilizing the broader V3 system.

The final M4 state allows players to adjust risk based on:
- board context
- strike count
- score position
- cutoff uncertainty
- double-window rhythm

The milestone also clarified the meaning of `open` as a board context. Early M4 diagnostics showed that `open` was too broad when treated as a single aggression signal. Later runs decomposed `open` into `dense` and `generous`, which made the strategy layer more interpretable.

The final model treats:
- `dense` as the main attackability signal
- `generous` as a softer looseness / forgiveness signal
- `tight` as a survival-oriented signal
- `open` as a broad descriptive umbrella

Run 7 was selected as the final M4 behavior state because it preserved stability while making double-window behavior more context-aware. Dense boards still allow risky/safe rhythm, generous boards allow rhythm only when the board is not tight, and tight boards more reliably push players toward safe play.

**Final aggregate M4 state:**

The final M4 version remains close to the stable M3/M4 baseline while producing more interpretable strategy behavior.

At the aggregate level, the final M4 state shows:
- Stable win distribution across contestants
- Category-sensitive safe/risky behavior
- Stronger survival behavior on tight boards
- More meaningful separation between density-driven aggression and generosity-driven looseness
- Double-window behavior that remains human-like but is no longer driven by broad `open` alone

The final strategy profile is:

- HR-style categories remain aggressive
    - high dense rate
    - high risky-on-dense rate
    - high double-window risky rate

- bWAR / MVP-style categories remain conservative
    - higher uncertainty
    - higher tightness
    - lower risky-on-generous rate
    - higher safe-on-tight rate

- Hits / OPS+ sit between those extremes
    - playable but not as aggressively open as HR
    - more mixed dense/generous behavior

Most importantly, the final M4 state does not suggest that contextual strategy broke the simulator. Instead, it gives the simulator a clearer way to explain *why* players are choosing safe, risky, or double-window rhythm decisions.

**Key Observations:**

1. **`open` is useful, but too broad to be the main aggression trigger**

The milestone showed that `open` should remain as a descriptive board label, but not as the sole driver of risk. Open states can come from either density or generosity, and those do not imply the same strategic response.

2. **Density is the clearest attackability signal**

Across the later runs, `risky_on_dense` was consistently higher than `risky_on_generous`. This suggests that players should become more aggressive when the board appears answer-rich near the cutoff, not merely when surprising outcomes occur.

3. **Generosity is not the same as attackability**

A generous board may feel forgiving, but it does not always mean there are many viable answers left. This was especially clear in harder categories, where generosity could be present without producing much risky behavior.

4. **Tight boards should override rhythm**

Run 7 showed that double-window behavior becomes cleaner when tight-board contexts suppress risky/safe alternation. This improved the model conceptually because survival pressure now overrides rhythm when the board appears precision-heavy.

5. **Double-window behavior remains important**

End-of-snake turns still need special handling. The final M4 logic preserves human-like alternating behavior, but filters it through board context so that the simulator does not blindly alternate risky/safe picks in bad board states.

6. **M4 is complete enough for V3**

Further tuning of dense/generous pressure or double-window thresholds would likely produce diminishing returns. Remaining issues, such as player-profile calibration, defensive survival logic, sharper cutoff discovery, and richer category realism, are better suited for later milestones or future versions.

---

## Milestone 5 - Human Bias and Player Identity

**Summary:**
fill out when complete

**Observed Progression:**
fill out when complete

**Key Insights:**
fill out when complete

### Run 1

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.642, avg_score=1817.0, median_score=1746.0, stdev=325.2, avg_strikes=2.98, first_out_rate=0.086
Contestant 2: win_rate=0.198, avg_score=1598.1, median_score=1582.0, stdev=223.6, avg_strikes=2.99, first_out_rate=0.439
Contestant 3: win_rate=0.159, avg_score=1259.5, median_score=1183.5, stdev=276.8, avg_strikes=2.98, first_out_rate=0.469
Last survivor but lost rate: 0.252
Solo started behind rate: 0.398
Solo started behind and lost rate: 0.634
Avg solo start deficit: 263.5
Avg solo turns taken: 2.56
Solo had winning answer rate: 0.113
Solo had winning answer given started behind rate: 0.285
Solo start deficit buckets: 1-75: 0.292, 76-150: 0.203, 151-250: 0.129, 251+: 0.376
Avg final board read: 0.044
Avg absolute final board read: 0.095
Strong harsh board rate: 0.049
Strong generous board rate: 0.150
Avg final cutoff estimate: 67.26
Avg final cutoff uncertainty: 0.353
Low uncertainty rate: 0.043
High cutoff rate: 0.428
Avg final safe floor: 55.14
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.73
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.755, risky=0.198, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.777, risky=0.223, blind_risk=0.000
Context rates: open=0.703, dense=0.405, generous=0.352, dense_and_generous=0.055, tight=0.089, uncertain=0.370, 
Context-action rates: risky_on_open=0.166, risky_on_dense=0.256, risky_on_generous=0.048, risky_on_dense_and_generous=0.066, safe_on_tight=0.951, risky_on_uncertain=0.339, safe_on_uncertain=0.648, risky_on_double_window=0.223, safe_on_double_window=0.777

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.966, avg_score=2594.2, median_score=2667.0, stdev=463.9, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.004, avg_score=888.1, median_score=880.0, stdev=215.8, avg_strikes=3.00, first_out_rate=0.882
Contestant 3: win_rate=0.030, avg_score=936.2, median_score=894.0, stdev=258.6, avg_strikes=3.00, first_out_rate=0.117
Last survivor but lost rate: 0.036
Solo started behind rate: 0.117
Solo started behind and lost rate: 0.307
Avg solo start deficit: 133.1
Avg solo turns taken: 13.63
Solo had winning answer rate: 0.068
Solo had winning answer given started behind rate: 0.579
Solo start deficit buckets: 1-75: 0.512, 76-150: 0.205, 151-250: 0.110, 251+: 0.173
Avg final board read: -0.031
Avg absolute final board read: 0.079
Strong harsh board rate: 0.043
Strong generous board rate: 0.025
Avg final cutoff estimate: 71.67
Avg final cutoff uncertainty: 0.463
Low uncertainty rate: 0.001
High cutoff rate: 0.651
Avg final safe floor: 58.89
Avg final local density read: 0.059
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.91
Avg final near-cutoff misses: 0.12
Mode rates: safe=0.637, risky=0.140, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.211
Double window mode rates: safe=0.829, risky=0.171, blind_risk=0.000
Context rates: open=0.603, dense=0.282, generous=0.358, dense_and_generous=0.037, tight=0.199, uncertain=0.698, 
Context-action rates: risky_on_open=0.106, risky_on_dense=0.162, risky_on_generous=0.058, risky_on_dense_and_generous=0.076, safe_on_tight=0.962, risky_on_uncertain=0.178, safe_on_uncertain=0.779, risky_on_double_window=0.171, safe_on_double_window=0.829

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.540, avg_score=1753.7, median_score=1736.0, stdev=99.4, avg_strikes=1.32, first_out_rate=0.002
Contestant 2: win_rate=0.232, avg_score=1675.6, median_score=1681.0, stdev=110.4, avg_strikes=2.09, first_out_rate=0.360
Contestant 3: win_rate=0.228, avg_score=1595.8, median_score=1644.0, stdev=155.7, avg_strikes=1.21, first_out_rate=0.071
Last survivor but lost rate: 0.143
Solo started behind rate: 0.232
Solo started behind and lost rate: 0.617
Avg solo start deficit: 176.5
Avg solo turns taken: 2.53
Solo had winning answer rate: 0.083
Solo had winning answer given started behind rate: 0.358
Solo start deficit buckets: 1-75: 0.402, 76-150: 0.233, 151-250: 0.104, 251+: 0.261
Avg final board read: -0.074
Avg absolute final board read: 0.101
Strong harsh board rate: 0.255
Strong generous board rate: 0.001
Avg final cutoff estimate: 53.04
Avg final cutoff uncertainty: 0.285
Low uncertainty rate: 0.297
High cutoff rate: 0.182
Avg final safe floor: 41.33
Avg final local density read: 0.076
Avg final surprise read: 0.166
Avg final near-cutoff hits: 2.52
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.512, risky=0.467, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.004
Double window mode rates: safe=0.504, risky=0.496, blind_risk=0.000
Context rates: open=0.745, dense=0.565, generous=0.204, dense_and_generous=0.024, tight=0.097, uncertain=0.323, 
Context-action rates: risky_on_open=0.488, risky_on_dense=0.583, risky_on_generous=0.189, risky_on_dense_and_generous=0.193, safe_on_tight=0.810, risky_on_uncertain=0.570, safe_on_uncertain=0.414, risky_on_double_window=0.496, safe_on_double_window=0.504

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.550, avg_score=1759.9, median_score=1738.0, stdev=180.9, avg_strikes=2.64, first_out_rate=0.090
Contestant 2: win_rate=0.179, avg_score=1650.5, median_score=1654.0, stdev=157.4, avg_strikes=2.81, first_out_rate=0.623
Contestant 3: win_rate=0.271, avg_score=1501.7, median_score=1572.0, stdev=230.0, avg_strikes=2.62, first_out_rate=0.168
Last survivor but lost rate: 0.358
Solo started behind rate: 0.484
Solo started behind and lost rate: 0.740
Avg solo start deficit: 273.4
Avg solo turns taken: 2.14
Solo had winning answer rate: 0.100
Solo had winning answer given started behind rate: 0.207
Solo start deficit buckets: 1-75: 0.300, 76-150: 0.190, 151-250: 0.100, 251+: 0.410
Avg final board read: -0.017
Avg absolute final board read: 0.092
Strong harsh board rate: 0.140
Strong generous board rate: 0.043
Avg final cutoff estimate: 59.68
Avg final cutoff uncertainty: 0.311
Low uncertainty rate: 0.163
High cutoff rate: 0.276
Avg final safe floor: 47.81
Avg final local density read: 0.067
Avg final surprise read: 0.160
Avg final near-cutoff hits: 2.83
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.656, risky=0.314, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.012
Double window mode rates: safe=0.649, risky=0.351, blind_risk=0.000
Context rates: open=0.726, dense=0.488, generous=0.279, dense_and_generous=0.041, tight=0.101, uncertain=0.329, 
Context-action rates: risky_on_open=0.307, risky_on_dense=0.415, risky_on_generous=0.090, risky_on_dense_and_generous=0.118, safe_on_tight=0.879, risky_on_uncertain=0.461, safe_on_uncertain=0.525, risky_on_double_window=0.351, safe_on_double_window=0.649

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.602, avg_score=1834.0, median_score=2180.0, stdev=859.1, avg_strikes=3.00, first_out_rate=0.012
Contestant 2: win_rate=0.383, avg_score=1454.7, median_score=1039.0, stdev=779.6, avg_strikes=3.00, first_out_rate=0.037
Contestant 3: win_rate=0.015, avg_score=566.6, median_score=519.0, stdev=223.9, avg_strikes=3.00, first_out_rate=0.951
Last survivor but lost rate: 0.099
Solo started behind rate: 0.335
Solo started behind and lost rate: 0.296
Avg solo start deficit: 102.8
Avg solo turns taken: 19.56
Solo had winning answer rate: 0.191
Solo had winning answer given started behind rate: 0.571
Solo start deficit buckets: 1-75: 0.471, 76-150: 0.296, 151-250: 0.161, 251+: 0.072
Avg final board read: -0.076
Avg absolute final board read: 0.088
Strong harsh board rate: 0.116
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.50
Avg final cutoff uncertainty: 0.539
Low uncertainty rate: 0.000
High cutoff rate: 0.561
Avg final safe floor: 57.26
Avg final local density read: 0.056
Avg final surprise read: 0.215
Avg final near-cutoff hits: 1.44
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.610, risky=0.113, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.264
Double window mode rates: safe=0.820, risky=0.180, blind_risk=0.000
Context rates: open=0.589, dense=0.239, generous=0.368, dense_and_generous=0.019, tight=0.246, uncertain=0.785, 
Context-action rates: risky_on_open=0.066, risky_on_dense=0.123, risky_on_generous=0.030, risky_on_dense_and_generous=0.106, safe_on_tight=0.955, risky_on_uncertain=0.140, safe_on_uncertain=0.753, risky_on_double_window=0.180, safe_on_double_window=0.820

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.660, avg_score=1951.8, avg_median_score=2013.4, avg_stdev=385.7, avg_strikes=2.59, avg_first_out_rate=0.038
Contestant 2: avg_win_rate=0.199, avg_score=1453.4, avg_median_score=1367.2, avg_stdev=297.3, avg_strikes=2.78, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.140, avg_score=1171.9, avg_median_score=1162.5, avg_stdev=229.0, avg_strikes=2.56, avg_first_out_rate=0.355
Last survivor but lost rate: 0.178
Solo started behind rate: 0.313
Solo started behind and lost rate: 0.519
Avg solo start deficit: 189.8
Avg solo turns taken: 8.08
Solo had winning answer rate: 0.111
Solo had winning answer given started behind rate: 0.400
Solo start deficit buckets: 1-75: 0.395, 76-150: 0.225, 151-250: 0.121, 251+: 0.258
Avg final board read: -0.031
Avg absolute final board read: 0.091
Avg strong harsh board rate: 0.121
Avg strong generous board rate: 0.044
Avg final cutoff estimate: 64.43
Avg final cutoff uncertainty: 0.390
Avg low uncertainty rate: 0.101
Avg high cutoff rate: 0.420
Avg final safe floor: 52.09
Avg final local density read: 0.062
Avg final surprise read: 0.183
Avg final near-cutoff hits: 2.29
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.635, risky=0.250, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.101
Double window mode rates: safe=0.695, risky=0.305, blind_risk=0.000
Context rates: open=0.675, dense=0.400, generous=0.311, dense_and_generous=0.035, tight=0.144, uncertain=0.494, 
Context-action rates: risky_on_open=0.243, risky_on_dense=0.363, risky_on_generous=0.073, risky_on_dense_and_generous=0.102, safe_on_tight=0.926, risky_on_uncertain=0.283, safe_on_uncertain=0.667, risky_on_double_window=0.305, safe_on_double_window=0.695
PS C:\Users\smart\OneDrive\Desktop\Projects\Simulations>  c:; cd 'c:\Users\smart\OneDrive\Desktop\Projects\Simulations'; & 'c:\python313\python.exe' 'c:\Users\smart\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '61817' '--' 'c:\Users\smart\OneDrive\Desktop\Projects\Simulations\Pinpoint\src\v3\simulator_v3.py' 

=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.642, avg_score=1817.0, median_score=1746.0, stdev=325.2, avg_strikes=2.98, first_out_rate=0.086
Contestant 2: win_rate=0.198, avg_score=1598.1, median_score=1582.0, stdev=223.6, avg_strikes=2.99, first_out_rate=0.439
Contestant 3: win_rate=0.159, avg_score=1259.5, median_score=1183.5, stdev=276.8, avg_strikes=2.98, first_out_rate=0.469
Last survivor but lost rate: 0.252
Solo started behind rate: 0.398
Solo started behind and lost rate: 0.634
Avg solo start deficit: 263.5
Avg solo turns taken: 2.56
Solo had winning answer rate: 0.113
Solo had winning answer given started behind rate: 0.285
Solo start deficit buckets: 1-75: 0.292, 76-150: 0.203, 151-250: 0.129, 251+: 0.376
Avg final board read: 0.044
Avg absolute final board read: 0.095
Strong harsh board rate: 0.049
Strong generous board rate: 0.150
Avg final cutoff estimate: 67.26
Avg final cutoff uncertainty: 0.353
Low uncertainty rate: 0.043
High cutoff rate: 0.428
Avg final safe floor: 55.14
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.73
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.755, risky=0.198, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.032
Double window mode rates: safe=0.777, risky=0.223, blind_risk=0.000
Context rates: open=0.703, dense=0.405, generous=0.352, dense_and_generous=0.055, tight=0.089, uncertain=0.370, 
Context-action rates: risky_on_open=0.166, risky_on_dense=0.256, risky_on_generous=0.048, risky_on_dense_and_generous=0.066, safe_on_tight=0.951, risky_on_uncertain=0.339, safe_on_uncertain=0.648, risky_on_double_window=0.223, safe_on_double_window=0.777

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.966, avg_score=2594.2, median_score=2667.0, stdev=463.9, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.004, avg_score=888.1, median_score=880.0, stdev=215.8, avg_strikes=3.00, first_out_rate=0.882
Contestant 3: win_rate=0.030, avg_score=936.2, median_score=894.0, stdev=258.6, avg_strikes=3.00, first_out_rate=0.117
Last survivor but lost rate: 0.036
Solo started behind rate: 0.117
Solo started behind and lost rate: 0.307
Avg solo start deficit: 133.1
Avg solo turns taken: 13.63
Solo had winning answer rate: 0.068
Solo had winning answer given started behind rate: 0.579
Solo start deficit buckets: 1-75: 0.512, 76-150: 0.205, 151-250: 0.110, 251+: 0.173
Avg final board read: -0.031
Avg absolute final board read: 0.079
Strong harsh board rate: 0.043
Strong generous board rate: 0.025
Avg final cutoff estimate: 71.67
Avg final cutoff uncertainty: 0.463
Low uncertainty rate: 0.001
High cutoff rate: 0.651
Avg final safe floor: 58.89
Avg final local density read: 0.059
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.91
Avg final near-cutoff misses: 0.12
Mode rates: safe=0.637, risky=0.140, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.211
Double window mode rates: safe=0.829, risky=0.171, blind_risk=0.000
Context rates: open=0.603, dense=0.282, generous=0.358, dense_and_generous=0.037, tight=0.199, uncertain=0.698, 
Context-action rates: risky_on_open=0.106, risky_on_dense=0.162, risky_on_generous=0.058, risky_on_dense_and_generous=0.076, safe_on_tight=0.962, risky_on_uncertain=0.178, safe_on_uncertain=0.779, risky_on_double_window=0.171, safe_on_double_window=0.829

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.540, avg_score=1753.7, median_score=1736.0, stdev=99.4, avg_strikes=1.32, first_out_rate=0.002
Contestant 2: win_rate=0.232, avg_score=1675.6, median_score=1681.0, stdev=110.4, avg_strikes=2.09, first_out_rate=0.360
Contestant 3: win_rate=0.228, avg_score=1595.8, median_score=1644.0, stdev=155.7, avg_strikes=1.21, first_out_rate=0.071
Last survivor but lost rate: 0.143
Solo started behind rate: 0.232
Solo started behind and lost rate: 0.617
Avg solo start deficit: 176.5
Avg solo turns taken: 2.53
Solo had winning answer rate: 0.083
Solo had winning answer given started behind rate: 0.358
Solo start deficit buckets: 1-75: 0.402, 76-150: 0.233, 151-250: 0.104, 251+: 0.261
Avg final board read: -0.074
Avg absolute final board read: 0.101
Strong harsh board rate: 0.255
Strong generous board rate: 0.001
Avg final cutoff estimate: 53.04
Avg final cutoff uncertainty: 0.285
Low uncertainty rate: 0.297
High cutoff rate: 0.182
Avg final safe floor: 41.33
Avg final local density read: 0.076
Avg final surprise read: 0.166
Avg final near-cutoff hits: 2.52
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.512, risky=0.467, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.004
Double window mode rates: safe=0.504, risky=0.496, blind_risk=0.000
Context rates: open=0.745, dense=0.565, generous=0.204, dense_and_generous=0.024, tight=0.097, uncertain=0.323, 
Context-action rates: risky_on_open=0.488, risky_on_dense=0.583, risky_on_generous=0.189, risky_on_dense_and_generous=0.193, safe_on_tight=0.810, risky_on_uncertain=0.570, safe_on_uncertain=0.414, risky_on_double_window=0.496, safe_on_double_window=0.504

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.550, avg_score=1759.9, median_score=1738.0, stdev=180.9, avg_strikes=2.64, first_out_rate=0.090
Contestant 2: win_rate=0.179, avg_score=1650.5, median_score=1654.0, stdev=157.4, avg_strikes=2.81, first_out_rate=0.623
Contestant 3: win_rate=0.271, avg_score=1501.7, median_score=1572.0, stdev=230.0, avg_strikes=2.62, first_out_rate=0.168
Last survivor but lost rate: 0.358
Solo started behind rate: 0.484
Solo started behind and lost rate: 0.740
Avg solo start deficit: 273.4
Avg solo turns taken: 2.14
Solo had winning answer rate: 0.100
Solo had winning answer given started behind rate: 0.207
Solo start deficit buckets: 1-75: 0.300, 76-150: 0.190, 151-250: 0.100, 251+: 0.410
Avg final board read: -0.017
Avg absolute final board read: 0.092
Strong harsh board rate: 0.140
Strong generous board rate: 0.043
Avg final cutoff estimate: 59.68
Avg final cutoff uncertainty: 0.311
Low uncertainty rate: 0.163
High cutoff rate: 0.276
Avg final safe floor: 47.81
Avg final local density read: 0.067
Avg final surprise read: 0.160
Avg final near-cutoff hits: 2.83
Avg final near-cutoff misses: 0.02
Mode rates: safe=0.656, risky=0.314, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.012
Double window mode rates: safe=0.649, risky=0.351, blind_risk=0.000
Context rates: open=0.726, dense=0.488, generous=0.279, dense_and_generous=0.041, tight=0.101, uncertain=0.329, 
Context-action rates: risky_on_open=0.307, risky_on_dense=0.415, risky_on_generous=0.090, risky_on_dense_and_generous=0.118, safe_on_tight=0.879, risky_on_uncertain=0.461, safe_on_uncertain=0.525, risky_on_double_window=0.351, safe_on_double_window=0.649

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.602, avg_score=1834.0, median_score=2180.0, stdev=859.1, avg_strikes=3.00, first_out_rate=0.012
Contestant 2: win_rate=0.383, avg_score=1454.7, median_score=1039.0, stdev=779.6, avg_strikes=3.00, first_out_rate=0.037
Contestant 3: win_rate=0.015, avg_score=566.6, median_score=519.0, stdev=223.9, avg_strikes=3.00, first_out_rate=0.951
Last survivor but lost rate: 0.099
Solo started behind rate: 0.335
Solo started behind and lost rate: 0.296
Avg solo start deficit: 102.8
Avg solo turns taken: 19.56
Solo had winning answer rate: 0.191
Solo had winning answer given started behind rate: 0.571
Solo start deficit buckets: 1-75: 0.471, 76-150: 0.296, 151-250: 0.161, 251+: 0.072
Avg final board read: -0.076
Avg absolute final board read: 0.088
Strong harsh board rate: 0.116
Strong generous board rate: 0.001
Avg final cutoff estimate: 70.50
Avg final cutoff uncertainty: 0.539
Low uncertainty rate: 0.000
High cutoff rate: 0.561
Avg final safe floor: 57.26
Avg final local density read: 0.056
Avg final surprise read: 0.215
Avg final near-cutoff hits: 1.44
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.610, risky=0.113, blind_risk=0.009, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.264
Double window mode rates: safe=0.820, risky=0.180, blind_risk=0.000
Context rates: open=0.589, dense=0.239, generous=0.368, dense_and_generous=0.019, tight=0.246, uncertain=0.785, 
Context-action rates: risky_on_open=0.066, risky_on_dense=0.123, risky_on_generous=0.030, risky_on_dense_and_generous=0.106, safe_on_tight=0.955, risky_on_uncertain=0.140, safe_on_uncertain=0.753, risky_on_double_window=0.180, safe_on_double_window=0.820

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.660, avg_score=1951.8, avg_median_score=2013.4, avg_stdev=385.7, avg_strikes=2.59, avg_first_out_rate=0.038
Contestant 2: avg_win_rate=0.199, avg_score=1453.4, avg_median_score=1367.2, avg_stdev=297.3, avg_strikes=2.78, avg_first_out_rate=0.468
Contestant 3: avg_win_rate=0.140, avg_score=1171.9, avg_median_score=1162.5, avg_stdev=229.0, avg_strikes=2.56, avg_first_out_rate=0.355
Last survivor but lost rate: 0.178
Solo started behind rate: 0.313
Solo started behind and lost rate: 0.519
Avg solo start deficit: 189.8
Avg solo turns taken: 8.08
Solo had winning answer rate: 0.111
Solo had winning answer given started behind rate: 0.400
Solo start deficit buckets: 1-75: 0.395, 76-150: 0.225, 151-250: 0.121, 251+: 0.258
Avg final board read: -0.031
Avg absolute final board read: 0.091
Avg strong harsh board rate: 0.121
Avg strong generous board rate: 0.044
Avg final cutoff estimate: 64.43
Avg final cutoff uncertainty: 0.390
Avg low uncertainty rate: 0.101
Avg high cutoff rate: 0.420
Avg final safe floor: 52.09
Avg final local density read: 0.062
Avg final surprise read: 0.183
Avg final near-cutoff hits: 2.29
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.635, risky=0.250, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.101
Double window mode rates: safe=0.695, risky=0.305, blind_risk=0.000
Context rates: open=0.675, dense=0.400, generous=0.311, dense_and_generous=0.035, tight=0.144, uncertain=0.494, 
Context-action rates: risky_on_open=0.243, risky_on_dense=0.363, risky_on_generous=0.073, risky_on_dense_and_generous=0.102, safe_on_tight=0.926, risky_on_uncertain=0.283, safe_on_uncertain=0.667, risky_on_double_window=0.305, safe_on_double_window=0.695
```

**Notes:**

Run 1 added the initial M5 player-identity fields to `PlayerProfile`:
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

**Conclusion:**

No new fields were writed into behavior yet. As expected, Run 1 matched Run 0 / the final M4 baseline. This confirms that the M5 identity scaffolding was added without changing gameplay.

Run 1 therefore serves as a clean structural checkpoint before M5 begins modifying recall, confidence, risk, fallback behavior, and defensive survival strategy.

### Run 2.1

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.638, avg_score=1799.0, median_score=1736.0, stdev=300.6, avg_strikes=2.97, first_out_rate=0.088
Contestant 2: win_rate=0.176, avg_score=1597.2, median_score=1593.0, stdev=200.3, avg_strikes=2.98, first_out_rate=0.474
Contestant 3: win_rate=0.186, avg_score=1307.4, median_score=1251.0, stdev=275.5, avg_strikes=2.97, first_out_rate=0.429
Last survivor but lost rate: 0.244
Solo started behind rate: 0.395
Solo started behind and lost rate: 0.619
Avg solo start deficit: 242.0
Avg solo turns taken: 2.41
Solo had winning answer rate: 0.120
Solo had winning answer given started behind rate: 0.305
Solo start deficit buckets: 1-75: 0.343, 76-150: 0.202, 151-250: 0.125, 251+: 0.329
Avg final board read: 0.030
Avg absolute final board read: 0.091
Strong harsh board rate: 0.061
Strong generous board rate: 0.119
Avg final cutoff estimate: 66.29
Avg final cutoff uncertainty: 0.344
Low uncertainty rate: 0.052
High cutoff rate: 0.403
Avg final safe floor: 54.23
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.65
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.742, risky=0.216, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.027
Double window mode rates: safe=0.756, risky=0.244, blind_risk=0.000
Context rates: open=0.707, dense=0.418, generous=0.340, dense_and_generous=0.051, tight=0.094, uncertain=0.354, 
Context-action rates: risky_on_open=0.189, risky_on_dense=0.283, risky_on_generous=0.056, risky_on_dense_and_generous=0.077, safe_on_tight=0.944, risky_on_uncertain=0.364, safe_on_uncertain=0.623, risky_on_double_window=0.244, safe_on_double_window=0.756

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.980, avg_score=2672.0, median_score=2723.0, stdev=429.3, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.005, avg_score=938.0, median_score=929.0, stdev=221.2, avg_strikes=3.00, first_out_rate=0.786
Contestant 3: win_rate=0.014, avg_score=896.4, median_score=852.0, stdev=259.9, avg_strikes=3.00, first_out_rate=0.214
Last survivor but lost rate: 0.023
Solo started behind rate: 0.092
Solo started behind and lost rate: 0.254
Avg solo start deficit: 120.5
Avg solo turns taken: 14.61
Solo had winning answer rate: 0.054
Solo had winning answer given started behind rate: 0.590
Solo start deficit buckets: 1-75: 0.504, 76-150: 0.256, 151-250: 0.113, 251+: 0.128
Avg final board read: -0.031
Avg absolute final board read: 0.076
Strong harsh board rate: 0.035
Strong generous board rate: 0.019
Avg final cutoff estimate: 71.64
Avg final cutoff uncertainty: 0.451
Low uncertainty rate: 0.001
High cutoff rate: 0.650
Avg final safe floor: 58.94
Avg final local density read: 0.064
Avg final surprise read: 0.199
Avg final near-cutoff hits: 1.88
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.634, risky=0.139, blind_risk=0.009, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.000, victory_lap=0.216
Double window mode rates: safe=0.834, risky=0.166, blind_risk=0.000
Context rates: open=0.611, dense=0.319, generous=0.341, dense_and_generous=0.049, tight=0.170, uncertain=0.664, 
Context-action rates: risky_on_open=0.103, risky_on_dense=0.149, risky_on_generous=0.053, risky_on_dense_and_generous=0.056, safe_on_tight=0.958, risky_on_uncertain=0.182, safe_on_uncertain=0.782, risky_on_double_window=0.166, safe_on_double_window=0.834

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.486, avg_score=1735.4, median_score=1723.0, stdev=89.4, avg_strikes=1.02, first_out_rate=0.001
Contestant 2: win_rate=0.271, avg_score=1680.6, median_score=1686.0, stdev=99.5, avg_strikes=1.93, first_out_rate=0.282
Contestant 3: win_rate=0.243, avg_score=1620.4, median_score=1657.0, stdev=129.9, avg_strikes=0.89, first_out_rate=0.050
Last survivor but lost rate: 0.076
Solo started behind rate: 0.147
Solo started behind and lost rate: 0.518
Avg solo start deficit: 125.8
Avg solo turns taken: 2.70
Solo had winning answer rate: 0.068
Solo had winning answer given started behind rate: 0.460
Solo start deficit buckets: 1-75: 0.495, 76-150: 0.227, 151-250: 0.102, 251+: 0.176
Avg final board read: -0.082
Avg absolute final board read: 0.099
Strong harsh board rate: 0.254
Strong generous board rate: 0.000
Avg final cutoff estimate: 52.50
Avg final cutoff uncertainty: 0.284
Low uncertainty rate: 0.291
High cutoff rate: 0.164
Avg final safe floor: 40.80
Avg final local density read: 0.073
Avg final surprise read: 0.175
Avg final near-cutoff hits: 2.38
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.491, risky=0.490, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.003
Double window mode rates: safe=0.483, risky=0.517, blind_risk=0.000
Context rates: open=0.746, dense=0.565, generous=0.201, dense_and_generous=0.020, tight=0.097, uncertain=0.323, 
Context-action rates: risky_on_open=0.514, risky_on_dense=0.608, risky_on_generous=0.222, risky_on_dense_and_generous=0.247, safe_on_tight=0.822, risky_on_uncertain=0.586, safe_on_uncertain=0.398, risky_on_double_window=0.517, safe_on_double_window=0.483

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.504, avg_score=1730.0, median_score=1718.0, stdev=152.4, avg_strikes=2.44, first_out_rate=0.082
Contestant 2: win_rate=0.192, avg_score=1643.9, median_score=1650.0, stdev=144.9, avg_strikes=2.71, first_out_rate=0.610
Contestant 3: win_rate=0.304, avg_score=1564.3, median_score=1627.0, stdev=194.2, avg_strikes=2.41, first_out_rate=0.122
Last survivor but lost rate: 0.325
Solo started behind rate: 0.443
Solo started behind and lost rate: 0.733
Avg solo start deficit: 216.5
Avg solo turns taken: 2.20
Solo had winning answer rate: 0.098
Solo had winning answer given started behind rate: 0.222
Solo start deficit buckets: 1-75: 0.353, 76-150: 0.213, 151-250: 0.111, 251+: 0.323
Avg final board read: -0.046
Avg absolute final board read: 0.093
Strong harsh board rate: 0.189
Strong generous board rate: 0.011
Avg final cutoff estimate: 56.62
Avg final cutoff uncertainty: 0.299
Low uncertainty rate: 0.218
High cutoff rate: 0.238
Avg final safe floor: 44.82
Avg final local density read: 0.074
Avg final surprise read: 0.154
Avg final near-cutoff hits: 2.85
Avg final near-cutoff misses: 0.01
Mode rates: safe=0.607, risky=0.365, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.010
Double window mode rates: safe=0.592, risky=0.408, blind_risk=0.000
Context rates: open=0.731, dense=0.518, generous=0.245, dense_and_generous=0.032, tight=0.111, uncertain=0.325, 
Context-action rates: risky_on_open=0.371, risky_on_dense=0.477, risky_on_generous=0.117, risky_on_dense_and_generous=0.150, safe_on_tight=0.857, risky_on_uncertain=0.497, safe_on_uncertain=0.489, risky_on_double_window=0.408, safe_on_double_window=0.592

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.660, avg_score=1993.3, median_score=2320.0, stdev=780.8, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.336, avg_score=1446.4, median_score=1143.0, stdev=671.1, avg_strikes=3.00, first_out_rate=0.011
Contestant 3: win_rate=0.004, avg_score=539.9, median_score=492.5, stdev=220.8, avg_strikes=3.00, first_out_rate=0.987
Last survivor but lost rate: 0.107
Solo started behind rate: 0.338
Solo started behind and lost rate: 0.317
Avg solo start deficit: 113.1
Avg solo turns taken: 17.22
Solo had winning answer rate: 0.180
Solo had winning answer given started behind rate: 0.531
Solo start deficit buckets: 1-75: 0.429, 76-150: 0.296, 151-250: 0.183, 251+: 0.092
Avg final board read: -0.056
Avg absolute final board read: 0.083
Strong harsh board rate: 0.116
Strong generous board rate: 0.005
Avg final cutoff estimate: 71.51
Avg final cutoff uncertainty: 0.519
Low uncertainty rate: 0.000
High cutoff rate: 0.614
Avg final safe floor: 58.40
Avg final local density read: 0.062
Avg final surprise read: 0.207
Avg final near-cutoff hits: 1.69
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.644, risky=0.114, blind_risk=0.011, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.227
Double window mode rates: safe=0.805, risky=0.195, blind_risk=0.000
Context rates: open=0.596, dense=0.248, generous=0.375, dense_and_generous=0.028, tight=0.214, uncertain=0.783, 
Context-action rates: risky_on_open=0.067, risky_on_dense=0.129, risky_on_generous=0.028, risky_on_dense_and_generous=0.080, safe_on_tight=0.969, risky_on_uncertain=0.140, safe_on_uncertain=0.779, risky_on_double_window=0.195, safe_on_double_window=0.805

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.654, avg_score=1985.9, avg_median_score=2044.0, avg_stdev=350.5, avg_strikes=2.49, avg_first_out_rate=0.035
Contestant 2: avg_win_rate=0.196, avg_score=1461.2, avg_median_score=1400.2, avg_stdev=267.4, avg_strikes=2.73, avg_first_out_rate=0.432
Contestant 3: avg_win_rate=0.150, avg_score=1185.7, avg_median_score=1175.9, avg_stdev=216.1, avg_strikes=2.46, avg_first_out_rate=0.360
Last survivor but lost rate: 0.155
Solo started behind rate: 0.283
Solo started behind and lost rate: 0.488
Avg solo start deficit: 163.6
Avg solo turns taken: 7.83
Solo had winning answer rate: 0.104
Solo had winning answer given started behind rate: 0.422
Solo start deficit buckets: 1-75: 0.425, 76-150: 0.239, 151-250: 0.127, 251+: 0.210
Avg final board read: -0.037
Avg absolute final board read: 0.088
Avg strong harsh board rate: 0.131
Avg strong generous board rate: 0.031
Avg final cutoff estimate: 63.71
Avg final cutoff uncertainty: 0.379
Avg low uncertainty rate: 0.112
Avg high cutoff rate: 0.414
Avg final safe floor: 51.44
Avg final local density read: 0.065
Avg final surprise read: 0.182
Avg final near-cutoff hits: 2.29
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.623, risky=0.267, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.094
Double window mode rates: safe=0.671, risky=0.329, blind_risk=0.000
Context rates: open=0.680, dense=0.417, generous=0.299, dense_and_generous=0.036, tight=0.136, uncertain=0.484, 
Context-action rates: risky_on_open=0.266, risky_on_dense=0.384, risky_on_generous=0.082, risky_on_dense_and_generous=0.104, safe_on_tight=0.923, risky_on_uncertain=0.295, safe_on_uncertain=0.665, risky_on_double_window=0.329, safe_on_double_window=0.671
```

**Notes:**

Run 2.1 did exactly as it was intended to:
- C1 WR: 0.660 &rarr; 0.654
- C2 WR: 0.199 &rarr; 0.196
- C3 WR: 0.140 &rarr; 0.150

Healthy first M5 behavior shift, as the simulator became a little more aggressive, solo/endgame outcomes improved, and C3 gained slightly without blowing up the model

Key Note:

`familiarity_mult` was not added, only has `category_confidence_mult`, which does mean that familiarity was not added for this run, but will be added to future runs to influence trust. Run 2.2 (below) and beyond adds `confidence *= familiarity_mult` in addition to `confidence *=category_confidence_mult`

**Takeaway:**

Category-level interpretation:
- HR since 2000
    - C1 WR: 0.540 &rarr; 0.486
    - C2 WR: 0.232 &rarr; 0.271
    - C3 WR: 0.228 &rarr; 0.243
    - Risky rate: 0.467 &rarr; 0.490
    - Double-window risky: 0.496 &rarr; 0.517
    - Solo behind/lost: 0.617 &rarr; 0.518

Modern/counting-stat identity helps C2 and C3, and the category becomes more attackable without turning chaotic

- Hit since 1900
    - C1 WR: 0.550 &rarr; 0.504
    - C2 WR: 0.179 &rarr; 0.192
    - C3 WR: 0.271 &rarr; 0.304
    - Risky rate: 0.314 &rarr; 0.365
    - Double-window risky: 0.351 &rarr; 0.408

Makes sense because Hits now has both `all_time` and `counting_stat` tags, so it gives C1 some all-time comfort while also letting C2/C3 benefit from counting-stat identity

Things to watch:

1. bWAR became even more C1-dominant
- C1 WR: 0.966 &rarr; 0.980
- C2 WR: 0.004 &rarr; 0.005
- C3 WR: 0.030 &rarr; 0.014

Probably is due to C1 getting both `all_time` and `war` boosts, while C3 gets a `war` penalty and C2 has the existing `category_modifiers={"war": 0.78}` weakness
- Not a bug, but it may be too harsh if the goal is to keep bWAR difficult without making it almost unwinnable for C2/C3

2. MVP became more C1-heavy
- C1 WR: 0.602 &rarr; 0.660
- C2 WR: 0.383 &rarr; 0.336
- C3 WR: 0.015 &rarr; 0.004

This is due to MVP having the tags `{"awards", "all_time", "star"}`
- C1 gets `all_time` + `awards` confidence
- C2 gets `awards`
- C3 gets an `awards` penalty
- category tag `"star"` does **not** interact with `archetype_bias` because `archetype_bias` is applied through `bucket_archetype_tags(points)`, not category tags
    - As such, MVP's `"star"` tag currently only matters if someone has `"star"` inside `category_confidence` or `familiarity_bias`, which currently they do not
        - Again, not a bug, but something to be aware of

**Conclusion:**

Run 2.1 successfully wired player identity into answer-state formation. Category tags, familiarity, and abstract answer archetypes now affect knowledge, recall, and confidence. The run produced meaningful identity-driven movement: modern/counting categories became more competitive for C2/C3, while HR and Hits became more aggressive and less C1-dominated.

The main side effect was that bWAR and MVP became more C1-heavy, likely due to stacked all-time/WAR/awards boosts and C3's penalties in those categories. This is not treated as a structural failure, but it is noted as a future calibration point.

### Run 2.2

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.655, avg_score=1811.8, median_score=1748.0, stdev=301.1, avg_strikes=2.97, first_out_rate=0.086
Contestant 2: win_rate=0.166, avg_score=1595.9, median_score=1595.0, stdev=195.7, avg_strikes=2.98, first_out_rate=0.473
Contestant 3: win_rate=0.179, avg_score=1308.0, median_score=1254.0, stdev=275.3, avg_strikes=2.97, first_out_rate=0.431
Last survivor but lost rate: 0.245
Solo started behind rate: 0.391
Solo started behind and lost rate: 0.627
Avg solo start deficit: 242.0
Avg solo turns taken: 2.38
Solo had winning answer rate: 0.118
Solo had winning answer given started behind rate: 0.301
Solo start deficit buckets: 1-75: 0.345, 76-150: 0.203, 151-250: 0.127, 251+: 0.324
Avg final board read: 0.030
Avg absolute final board read: 0.092
Strong harsh board rate: 0.063
Strong generous board rate: 0.125
Avg final cutoff estimate: 66.20
Avg final cutoff uncertainty: 0.343
Low uncertainty rate: 0.054
High cutoff rate: 0.402
Avg final safe floor: 54.14
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.66
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.740, risky=0.217, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.027
Double window mode rates: safe=0.755, risky=0.245, blind_risk=0.000
Context rates: open=0.707, dense=0.420, generous=0.338, dense_and_generous=0.051, tight=0.093, uncertain=0.352, 
Context-action rates: risky_on_open=0.191, risky_on_dense=0.285, risky_on_generous=0.057, risky_on_dense_and_generous=0.074, safe_on_tight=0.942, risky_on_uncertain=0.367, safe_on_uncertain=0.620, risky_on_double_window=0.245, safe_on_double_window=0.755

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.982, avg_score=2685.1, median_score=2736.0, stdev=429.2, avg_strikes=3.00, first_out_rate=0.000
Contestant 2: win_rate=0.005, avg_score=941.1, median_score=931.0, stdev=223.5, avg_strikes=3.00, first_out_rate=0.786
Contestant 3: win_rate=0.013, avg_score=902.6, median_score=855.0, stdev=262.9, avg_strikes=3.00, first_out_rate=0.213
Last survivor but lost rate: 0.023
Solo started behind rate: 0.087
Solo started behind and lost rate: 0.268
Avg solo start deficit: 123.9
Avg solo turns taken: 13.83
Solo had winning answer rate: 0.052
Solo had winning answer given started behind rate: 0.604
Solo start deficit buckets: 1-75: 0.518, 76-150: 0.235, 151-250: 0.110, 251+: 0.137
Avg final board read: -0.029
Avg absolute final board read: 0.075
Strong harsh board rate: 0.034
Strong generous board rate: 0.017
Avg final cutoff estimate: 71.74
Avg final cutoff uncertainty: 0.447
Low uncertainty rate: 0.001
High cutoff rate: 0.656
Avg final safe floor: 59.06
Avg final local density read: 0.064
Avg final surprise read: 0.199
Avg final near-cutoff hits: 1.88
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.635, risky=0.140, blind_risk=0.009, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.000, victory_lap=0.214
Double window mode rates: safe=0.834, risky=0.166, blind_risk=0.000
Context rates: open=0.611, dense=0.326, generous=0.338, dense_and_generous=0.052, tight=0.162, uncertain=0.653, 
Context-action rates: risky_on_open=0.105, risky_on_dense=0.150, risky_on_generous=0.053, risky_on_dense_and_generous=0.053, safe_on_tight=0.958, risky_on_uncertain=0.185, safe_on_uncertain=0.782, risky_on_double_window=0.166, safe_on_double_window=0.834

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.466, avg_score=1729.3, median_score=1717.0, stdev=88.4, avg_strikes=0.92, first_out_rate=0.001
Contestant 2: win_rate=0.280, avg_score=1680.2, median_score=1686.0, stdev=97.0, avg_strikes=1.87, first_out_rate=0.247
Contestant 3: win_rate=0.254, avg_score=1629.6, median_score=1664.0, stdev=124.7, avg_strikes=0.77, first_out_rate=0.039
Last survivor but lost rate: 0.057
Solo started behind rate: 0.115
Solo started behind and lost rate: 0.498
Avg solo start deficit: 118.1
Avg solo turns taken: 2.74
Solo had winning answer rate: 0.056
Solo had winning answer given started behind rate: 0.491
Solo start deficit buckets: 1-75: 0.517, 76-150: 0.216, 151-250: 0.112, 251+: 0.155
Avg final board read: -0.086
Avg absolute final board read: 0.101
Strong harsh board rate: 0.258
Strong generous board rate: 0.000
Avg final cutoff estimate: 52.02
Avg final cutoff uncertainty: 0.282
Low uncertainty rate: 0.295
High cutoff rate: 0.156
Avg final safe floor: 40.33
Avg final local density read: 0.073
Avg final surprise read: 0.176
Avg final near-cutoff hits: 2.38
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.480, risky=0.501, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.003
Double window mode rates: safe=0.472, risky=0.528, blind_risk=0.000
Context rates: open=0.746, dense=0.569, generous=0.196, dense_and_generous=0.019, tight=0.095, uncertain=0.323, 
Context-action rates: risky_on_open=0.526, risky_on_dense=0.617, risky_on_generous=0.236, risky_on_dense_and_generous=0.265, safe_on_tight=0.820, risky_on_uncertain=0.595, safe_on_uncertain=0.389, risky_on_double_window=0.528, safe_on_double_window=0.472

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.504, avg_score=1730.0, median_score=1720.0, stdev=147.2, avg_strikes=2.37, first_out_rate=0.079
Contestant 2: win_rate=0.194, avg_score=1650.0, median_score=1656.0, stdev=139.5, avg_strikes=2.66, first_out_rate=0.591
Contestant 3: win_rate=0.302, avg_score=1567.7, median_score=1626.0, stdev=189.9, avg_strikes=2.33, first_out_rate=0.117
Last survivor but lost rate: 0.321
Solo started behind rate: 0.439
Solo started behind and lost rate: 0.732
Avg solo start deficit: 217.4
Avg solo turns taken: 2.21
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.226
Solo start deficit buckets: 1-75: 0.347, 76-150: 0.208, 151-250: 0.113, 251+: 0.331
Avg final board read: -0.048
Avg absolute final board read: 0.094
Strong harsh board rate: 0.196
Strong generous board rate: 0.011
Avg final cutoff estimate: 55.97
Avg final cutoff uncertainty: 0.297
Low uncertainty rate: 0.231
High cutoff rate: 0.228
Avg final safe floor: 44.19
Avg final local density read: 0.076
Avg final surprise read: 0.152
Avg final near-cutoff hits: 2.87
Avg final near-cutoff misses: 0.01
Mode rates: safe=0.597, risky=0.375, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.009
Double window mode rates: safe=0.583, risky=0.417, blind_risk=0.000
Context rates: open=0.733, dense=0.526, generous=0.239, dense_and_generous=0.032, tight=0.110, uncertain=0.324, 
Context-action rates: risky_on_open=0.382, risky_on_dense=0.487, risky_on_generous=0.121, risky_on_dense_and_generous=0.150, safe_on_tight=0.847, risky_on_uncertain=0.505, safe_on_uncertain=0.480, risky_on_double_window=0.417, safe_on_double_window=0.583

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.698, avg_score=2073.7, median_score=2389.5, stdev=761.2, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.298, avg_score=1393.4, median_score=1136.0, stdev=626.3, avg_strikes=3.00, first_out_rate=0.011
Contestant 3: win_rate=0.003, avg_score=542.3, median_score=495.0, stdev=223.2, avg_strikes=3.00, first_out_rate=0.987
Last survivor but lost rate: 0.100
Solo started behind rate: 0.336
Solo started behind and lost rate: 0.298
Avg solo start deficit: 111.6
Avg solo turns taken: 17.50
Solo had winning answer rate: 0.182
Solo had winning answer given started behind rate: 0.543
Solo start deficit buckets: 1-75: 0.442, 76-150: 0.289, 151-250: 0.180, 251+: 0.090
Avg final board read: -0.054
Avg absolute final board read: 0.082
Strong harsh board rate: 0.116
Strong generous board rate: 0.006
Avg final cutoff estimate: 71.57
Avg final cutoff uncertainty: 0.516
Low uncertainty rate: 0.000
High cutoff rate: 0.619
Avg final safe floor: 58.48
Avg final local density read: 0.063
Avg final surprise read: 0.206
Avg final near-cutoff hits: 1.73
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.645, risky=0.114, blind_risk=0.011, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.225
Double window mode rates: safe=0.805, risky=0.195, blind_risk=0.000
Context rates: open=0.598, dense=0.252, generous=0.375, dense_and_generous=0.029, tight=0.210, uncertain=0.781, 
Context-action rates: risky_on_open=0.068, risky_on_dense=0.129, risky_on_generous=0.027, risky_on_dense_and_generous=0.079, safe_on_tight=0.969, risky_on_uncertain=0.141, safe_on_uncertain=0.782, risky_on_double_window=0.195, safe_on_double_window=0.805

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.661, avg_score=2006.0, avg_median_score=2062.1, avg_stdev=345.4, avg_strikes=2.45, avg_first_out_rate=0.034
Contestant 2: avg_win_rate=0.189, avg_score=1452.1, avg_median_score=1400.8, avg_stdev=256.4, avg_strikes=2.70, avg_first_out_rate=0.422
Contestant 3: avg_win_rate=0.150, avg_score=1190.1, avg_median_score=1178.8, avg_stdev=215.2, avg_strikes=2.42, avg_first_out_rate=0.357
Last survivor but lost rate: 0.149
Solo started behind rate: 0.273
Solo started behind and lost rate: 0.484
Avg solo start deficit: 162.6
Avg solo turns taken: 7.73
Solo had winning answer rate: 0.102
Solo had winning answer given started behind rate: 0.433
Solo start deficit buckets: 1-75: 0.434, 76-150: 0.230, 151-250: 0.128, 251+: 0.208
Avg final board read: -0.037
Avg absolute final board read: 0.089
Avg strong harsh board rate: 0.134
Avg strong generous board rate: 0.032
Avg final cutoff estimate: 63.50
Avg final cutoff uncertainty: 0.377
Avg low uncertainty rate: 0.116
Avg high cutoff rate: 0.413
Avg final safe floor: 51.24
Avg final local density read: 0.066
Avg final surprise read: 0.182
Avg final near-cutoff hits: 2.30
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.620, risky=0.272, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.093
Double window mode rates: safe=0.666, risky=0.334, blind_risk=0.000
Context rates: open=0.681, dense=0.421, generous=0.296, dense_and_generous=0.037, tight=0.133, uncertain=0.481, 
Context-action rates: risky_on_open=0.271, risky_on_dense=0.389, risky_on_generous=0.083, risky_on_dense_and_generous=0.102, safe_on_tight=0.920, risky_on_uncertain=0.298, safe_on_uncertain=0.663, risky_on_double_window=0.334, safe_on_double_window=0.666
```

**Notes:**

Run 2.1 added M5 identity into answer-state formation

Run 2.2 made familiarity stronger by letting it affect both recall and confidence.

The effect of that extra confidence is small globally, but it meaningfully changes the categories where familiarity tags are active

**Takeaway:**

Aggregate Comparison

| Metric | Run 1 | Run 2.1 | Run 2.2
| - | - | - | -
| C1 WR | 0.660 | 0.654 | 0.661
| C2 WR | 0.199 | 0.196 | 0.189
| C3 WR | 0.140 | 0.150 | 0.150
| Safe rate | 0.635 | 0.623 | 0.620
| Risky Rate | 0.250 | 0.267 | 0.272
| Double-window risky | 0.305 | 0.329 | 0.334
| Last survivor but lost | 0.178 | 0.155 | 0.149
| Solo behind/lost | 0.519 | 0.488 | 0.484
| Avg solo deficit | 189.8 | 163.6 | 162.6

Run 2.1 made the game a bit more agggressive and a bit less solo-punishing. It also slightly lifted C3 and reduced C1 dominance overall, though not in every category

Run 2.2 nudges the same direction behaviorally - slightly more risky, slightly less safe, slightly better endgame/solo metrics. However, it also gives some strength back to C1 and slightly hurts C2 overall.

Adding `confidence *= familiarity_mult` means familiar categories no longer just help a player remember answers, they also make the player more willing to trust those answers.

**Conclusion:**

Run 2.1 wired category identity, familiarity, and archetype bias into answer-state formation. Familiarity affected recall, category confidence affected confidence, and archetype bias affected baseline knowledge. This produced the first meaningful M5 identity movement: modern/counting categories became more competitive for C2/C3, overall safe rates fell slightly, risky rates increased, and solo/endgame metrics improved.

Run 2.2 additionally allowed familiarity to affect confidence. This made familiarity more behaviorally meaningful, since familiar answers were not only easier to recall but also easier for players to trust. The aggregate effect was modest but directionally consistent: risky rate and double-window risky rate increased slightly, while last-survivor-but-lost and solo-behind-loss rates improved.

The main tradeoff was category balance. Run 2.2 improved modern/counting-stat behavior, especially HR, where C2 and C3 became more competitive. However, it also amplified C1 dominance in bWAR and MVP, likely due to stacked all-time/WAR/awards familiarity and confidence effects. This is not considered a structural failure, but it is noted as a future calibration point.

### Run 2.3

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.655, avg_score=1811.8, median_score=1748.0, stdev=301.1, avg_strikes=2.97, first_out_rate=0.086
Contestant 2: win_rate=0.166, avg_score=1595.9, median_score=1595.0, stdev=195.7, avg_strikes=2.98, first_out_rate=0.473
Contestant 3: win_rate=0.179, avg_score=1308.0, median_score=1254.0, stdev=275.3, avg_strikes=2.97, first_out_rate=0.431
Last survivor but lost rate: 0.245
Solo started behind rate: 0.391
Solo started behind and lost rate: 0.627
Avg solo start deficit: 242.0
Avg solo turns taken: 2.38
Solo had winning answer rate: 0.118
Solo had winning answer given started behind rate: 0.301
Solo start deficit buckets: 1-75: 0.345, 76-150: 0.203, 151-250: 0.127, 251+: 0.324
Avg final board read: 0.030
Avg absolute final board read: 0.092
Strong harsh board rate: 0.063
Strong generous board rate: 0.125
Avg final cutoff estimate: 66.20
Avg final cutoff uncertainty: 0.343
Low uncertainty rate: 0.054
High cutoff rate: 0.402
Avg final safe floor: 54.14
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.66
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.740, risky=0.217, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.027
Double window mode rates: safe=0.755, risky=0.245, blind_risk=0.000
Context rates: open=0.707, dense=0.420, generous=0.338, dense_and_generous=0.051, tight=0.093, uncertain=0.352, 
Context-action rates: risky_on_open=0.191, risky_on_dense=0.285, risky_on_generous=0.057, risky_on_dense_and_generous=0.074, safe_on_tight=0.942, risky_on_uncertain=0.367, safe_on_uncertain=0.620, risky_on_double_window=0.245, safe_on_double_window=0.755
Answer-state summary:
  Contestant 1: knowledge=0.217, recall=0.199, confidence=0.219, safe_candidates=83.4, risky_candidates=98.5, blind_candidates=1.2
  Contestant 2: knowledge=0.215, recall=0.193, confidence=0.206, safe_candidates=81.6, risky_candidates=97.2, blind_candidates=2.4
  Contestant 3: knowledge=0.174, recall=0.156, confidence=0.167, safe_candidates=56.4, risky_candidates=90.7, blind_candidates=7.8
Player mode rates:
  Contestant 1: safe=0.736, risky=0.200, blind=0.001, victory_lap=0.059
  Contestant 2: safe=0.768, risky=0.192, blind=0.027, victory_lap=0.010
  Contestant 3: safe=0.717, risky=0.261, blind=0.001, victory_lap=0.010
Player mode hit rates:
  Contestant 1: safe=0.939, risky=0.939, blind=0.038, desperation=0.193
  Contestant 2: safe=0.953, risky=0.890, blind=0.052, desperation=0.129
  Contestant 3: safe=0.934, risky=0.920, blind=0.051, desperation=0.130
Player avg guess values:
  Contestant 1: safe=45.0, risky=78.0, blind=95.6
  Contestant 2: safe=43.7, risky=81.5, blind=95.6
  Contestant 3: safe=33.8, risky=65.0, blind=96.1
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.606, high_70_89=0.029, deep_90_100=0.365, early_strike=0.051
  Contestant 2: top_15=0.000, mid_16_69=0.061, high_70_89=0.099, deep_90_100=0.837, early_strike=0.207
  Contestant 3: top_15=0.000, mid_16_69=0.603, high_70_89=0.293, deep_90_100=0.104, early_strike=0.064

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.982, avg_score=2685.1, median_score=2736.0, stdev=429.2, avg_strikes=3.00, first_out_rate=0.000
Contestant 2: win_rate=0.005, avg_score=941.1, median_score=931.0, stdev=223.5, avg_strikes=3.00, first_out_rate=0.786
Contestant 3: win_rate=0.013, avg_score=902.6, median_score=855.0, stdev=262.9, avg_strikes=3.00, first_out_rate=0.213
Last survivor but lost rate: 0.023
Solo started behind rate: 0.087
Solo started behind and lost rate: 0.268
Avg solo start deficit: 123.9
Avg solo turns taken: 13.83
Solo had winning answer rate: 0.052
Solo had winning answer given started behind rate: 0.604
Solo start deficit buckets: 1-75: 0.518, 76-150: 0.235, 151-250: 0.110, 251+: 0.137
Avg final board read: -0.029
Avg absolute final board read: 0.075
Strong harsh board rate: 0.034
Strong generous board rate: 0.017
Avg final cutoff estimate: 71.74
Avg final cutoff uncertainty: 0.447
Low uncertainty rate: 0.001
High cutoff rate: 0.656
Avg final safe floor: 59.06
Avg final local density read: 0.064
Avg final surprise read: 0.199
Avg final near-cutoff hits: 1.88
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.635, risky=0.140, blind_risk=0.009, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.000, victory_lap=0.214
Double window mode rates: safe=0.834, risky=0.166, blind_risk=0.000
Context rates: open=0.611, dense=0.326, generous=0.338, dense_and_generous=0.052, tight=0.162, uncertain=0.653, 
Context-action rates: risky_on_open=0.105, risky_on_dense=0.150, risky_on_generous=0.053, risky_on_dense_and_generous=0.053, safe_on_tight=0.958, risky_on_uncertain=0.185, safe_on_uncertain=0.782, risky_on_double_window=0.166, safe_on_double_window=0.834
Answer-state summary:
  Contestant 1: knowledge=0.181, recall=0.168, confidence=0.188, safe_candidates=69.7, risky_candidates=96.1, blind_candidates=2.9
  Contestant 2: knowledge=0.139, recall=0.125, confidence=0.131, safe_candidates=25.0, risky_candidates=87.4, blind_candidates=11.1
  Contestant 3: knowledge=0.145, recall=0.130, confidence=0.131, safe_candidates=32.1, risky_candidates=82.6, blind_candidates=16.0
Player mode rates:
  Contestant 1: safe=0.497, risky=0.062, blind=0.002, victory_lap=0.437
  Contestant 2: safe=0.755, risky=0.220, blind=0.025, victory_lap=0.000
  Contestant 3: safe=0.780, risky=0.209, blind=0.010, victory_lap=0.001
Player mode hit rates:
  Contestant 1: safe=0.996, risky=0.870, blind=0.062, desperation=0.161
  Contestant 2: safe=0.932, risky=0.788, blind=0.054, desperation=0.333
  Contestant 3: safe=0.928, risky=0.809, blind=0.043, desperation=0.124
Player avg guess values:
  Contestant 1: safe=45.4, risky=88.3, blind=95.2
  Contestant 2: safe=34.2, risky=81.2, blind=89.0
  Contestant 3: safe=28.0, risky=71.7, blind=88.7
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.609, high_70_89=0.083, deep_90_100=0.308, early_strike=0.066
  Contestant 2: top_15=0.000, mid_16_69=0.085, high_70_89=0.712, deep_90_100=0.203, early_strike=0.238
  Contestant 3: top_15=0.001, mid_16_69=0.609, high_70_89=0.352, deep_90_100=0.038, early_strike=0.089

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.466, avg_score=1729.3, median_score=1717.0, stdev=88.4, avg_strikes=0.92, first_out_rate=0.001
Contestant 2: win_rate=0.280, avg_score=1680.2, median_score=1686.0, stdev=97.0, avg_strikes=1.87, first_out_rate=0.247
Contestant 3: win_rate=0.254, avg_score=1629.6, median_score=1664.0, stdev=124.7, avg_strikes=0.77, first_out_rate=0.039
Last survivor but lost rate: 0.057
Solo started behind rate: 0.115
Solo started behind and lost rate: 0.498
Avg solo start deficit: 118.1
Avg solo turns taken: 2.74
Solo had winning answer rate: 0.056
Solo had winning answer given started behind rate: 0.491
Solo start deficit buckets: 1-75: 0.517, 76-150: 0.216, 151-250: 0.112, 251+: 0.155
Avg final board read: -0.086
Avg absolute final board read: 0.101
Strong harsh board rate: 0.258
Strong generous board rate: 0.000
Avg final cutoff estimate: 52.02
Avg final cutoff uncertainty: 0.282
Low uncertainty rate: 0.295
High cutoff rate: 0.156
Avg final safe floor: 40.33
Avg final local density read: 0.073
Avg final surprise read: 0.176
Avg final near-cutoff hits: 2.38
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.480, risky=0.501, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.003
Double window mode rates: safe=0.472, risky=0.528, blind_risk=0.000
Context rates: open=0.746, dense=0.569, generous=0.196, dense_and_generous=0.019, tight=0.095, uncertain=0.323, 
Context-action rates: risky_on_open=0.526, risky_on_dense=0.617, risky_on_generous=0.236, risky_on_dense_and_generous=0.265, safe_on_tight=0.820, risky_on_uncertain=0.595, safe_on_uncertain=0.389, risky_on_double_window=0.528, safe_on_double_window=0.472
Answer-state summary:
  Contestant 1: knowledge=0.304, recall=0.274, confidence=0.292, safe_candidates=94.4, risky_candidates=100.0, blind_candidates=0.0
  Contestant 2: knowledge=0.300, recall=0.292, confidence=0.351, safe_candidates=95.9, risky_candidates=100.0, blind_candidates=0.0
  Contestant 3: knowledge=0.243, recall=0.237, confidence=0.282, safe_candidates=86.7, risky_candidates=98.6, blind_candidates=0.7
Player mode rates:
  Contestant 1: safe=0.448, risky=0.552, blind=0.000, victory_lap=0.000
  Contestant 2: safe=0.501, risky=0.458, blind=0.040, victory_lap=0.001
  Contestant 3: safe=0.493, risky=0.494, blind=0.000, victory_lap=0.008
Player mode hit rates:
  Contestant 1: safe=0.951, risky=0.992, blind=0.000, desperation=0.000
  Contestant 2: safe=0.975, risky=0.997, blind=0.000, desperation=0.053
  Contestant 3: safe=0.993, risky=0.985, blind=0.000, desperation=0.051
Player avg guess values:
  Contestant 1: safe=40.3, risky=60.2, blind=0.0
  Contestant 2: safe=36.5, risky=67.9, blind=0.0
  Contestant 3: safe=41.2, risky=55.7, blind=97.6
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.528, high_70_89=0.000, deep_90_100=0.472, early_strike=0.001
  Contestant 2: top_15=0.000, mid_16_69=0.052, high_70_89=0.000, deep_90_100=0.899, early_strike=0.049
  Contestant 3: top_15=0.000, mid_16_69=0.524, high_70_89=0.015, deep_90_100=0.461, early_strike=0.056

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.504, avg_score=1730.0, median_score=1720.0, stdev=147.2, avg_strikes=2.37, first_out_rate=0.079
Contestant 2: win_rate=0.194, avg_score=1650.0, median_score=1656.0, stdev=139.5, avg_strikes=2.66, first_out_rate=0.591
Contestant 3: win_rate=0.302, avg_score=1567.7, median_score=1626.0, stdev=189.9, avg_strikes=2.33, first_out_rate=0.117
Last survivor but lost rate: 0.321
Solo started behind rate: 0.439
Solo started behind and lost rate: 0.732
Avg solo start deficit: 217.4
Avg solo turns taken: 2.21
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.226
Solo start deficit buckets: 1-75: 0.347, 76-150: 0.208, 151-250: 0.113, 251+: 0.331
Avg final board read: -0.048
Avg absolute final board read: 0.094
Strong harsh board rate: 0.196
Strong generous board rate: 0.011
Avg final cutoff estimate: 55.97
Avg final cutoff uncertainty: 0.297
Low uncertainty rate: 0.231
High cutoff rate: 0.228
Avg final safe floor: 44.19
Avg final local density read: 0.076
Avg final surprise read: 0.152
Avg final near-cutoff hits: 2.87
Avg final near-cutoff misses: 0.01
Mode rates: safe=0.597, risky=0.375, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.009
Double window mode rates: safe=0.583, risky=0.417, blind_risk=0.000
Context rates: open=0.733, dense=0.526, generous=0.239, dense_and_generous=0.032, tight=0.110, uncertain=0.324, 
Context-action rates: risky_on_open=0.382, risky_on_dense=0.487, risky_on_generous=0.121, risky_on_dense_and_generous=0.150, safe_on_tight=0.847, risky_on_uncertain=0.505, safe_on_uncertain=0.480, risky_on_double_window=0.417, safe_on_double_window=0.583
Answer-state summary:
  Contestant 1: knowledge=0.253, recall=0.233, confidence=0.255, safe_candidates=90.3, risky_candidates=99.8, blind_candidates=0.2
  Contestant 2: knowledge=0.250, recall=0.234, confidence=0.264, safe_candidates=90.4, risky_candidates=99.6, blind_candidates=0.2
  Contestant 3: knowledge=0.203, recall=0.188, confidence=0.209, safe_candidates=73.4, risky_candidates=95.0, blind_candidates=3.8
Player mode rates:
  Contestant 1: safe=0.602, risky=0.389, blind=0.000, victory_lap=0.008
  Contestant 2: safe=0.640, risky=0.321, blind=0.033, victory_lap=0.004
  Contestant 3: safe=0.551, risky=0.413, blind=0.001, victory_lap=0.016
Player mode hit rates:
  Contestant 1: safe=0.907, risky=0.984, blind=0.000, desperation=0.135
  Contestant 2: safe=0.953, risky=0.968, blind=0.007, desperation=0.014
  Contestant 3: safe=0.963, risky=0.969, blind=0.027, desperation=0.084
Player avg guess values:
  Contestant 1: safe=42.1, risky=65.8, blind=95.5
  Contestant 2: safe=40.0, risky=74.0, blind=96.1
  Contestant 3: safe=38.7, risky=57.8, blind=97.4
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.556, high_70_89=0.005, deep_90_100=0.439, early_strike=0.022
  Contestant 2: top_15=0.000, mid_16_69=0.057, high_70_89=0.001, deep_90_100=0.902, early_strike=0.109
  Contestant 3: top_15=0.000, mid_16_69=0.553, high_70_89=0.192, deep_90_100=0.255, early_strike=0.060

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.698, avg_score=2073.7, median_score=2389.5, stdev=761.2, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.298, avg_score=1393.4, median_score=1136.0, stdev=626.3, avg_strikes=3.00, first_out_rate=0.011
Contestant 3: win_rate=0.003, avg_score=542.3, median_score=495.0, stdev=223.2, avg_strikes=3.00, first_out_rate=0.987
Last survivor but lost rate: 0.100
Solo started behind rate: 0.336
Solo started behind and lost rate: 0.298
Avg solo start deficit: 111.6
Avg solo turns taken: 17.50
Solo had winning answer rate: 0.182
Solo had winning answer given started behind rate: 0.543
Solo start deficit buckets: 1-75: 0.442, 76-150: 0.289, 151-250: 0.180, 251+: 0.090
Avg final board read: -0.054
Avg absolute final board read: 0.082
Strong harsh board rate: 0.116
Strong generous board rate: 0.006
Avg final cutoff estimate: 71.57
Avg final cutoff uncertainty: 0.516
Low uncertainty rate: 0.000
High cutoff rate: 0.619
Avg final safe floor: 58.48
Avg final local density read: 0.063
Avg final surprise read: 0.206
Avg final near-cutoff hits: 1.73
Avg final near-cutoff misses: 0.09
Mode rates: safe=0.645, risky=0.114, blind_risk=0.011, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.225
Double window mode rates: safe=0.805, risky=0.195, blind_risk=0.000
Context rates: open=0.598, dense=0.252, generous=0.375, dense_and_generous=0.029, tight=0.210, uncertain=0.781, 
Context-action rates: risky_on_open=0.068, risky_on_dense=0.129, risky_on_generous=0.027, risky_on_dense_and_generous=0.079, safe_on_tight=0.969, risky_on_uncertain=0.141, safe_on_uncertain=0.782, risky_on_double_window=0.195, safe_on_double_window=0.805
Answer-state summary:
  Contestant 1: knowledge=0.152, recall=0.140, confidence=0.155, safe_candidates=44.1, risky_candidates=91.9, blind_candidates=6.3
  Contestant 2: knowledge=0.150, recall=0.135, confidence=0.149, safe_candidates=38.6, risky_candidates=90.9, blind_candidates=7.3
  Contestant 3: knowledge=0.122, recall=0.109, confidence=0.111, safe_candidates=14.9, risky_candidates=72.9, blind_candidates=24.6
Player mode rates:
  Contestant 1: safe=0.546, risky=0.074, blind=0.004, victory_lap=0.369
  Contestant 2: safe=0.699, risky=0.114, blind=0.027, victory_lap=0.157
  Contestant 3: safe=0.789, risky=0.210, blind=0.000, victory_lap=0.001
Player mode hit rates:
  Contestant 1: safe=0.969, risky=0.842, blind=0.059, desperation=0.190
  Contestant 2: safe=0.951, risky=0.824, blind=0.057, desperation=0.203
  Contestant 3: safe=0.861, risky=0.767, blind=0.000, desperation=0.242
Player avg guess values:
  Contestant 1: safe=37.5, risky=85.3, blind=92.8
  Contestant 2: safe=37.6, risky=85.6, blind=92.4
  Contestant 3: safe=25.5, risky=71.7, blind=87.5
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.593, high_70_89=0.235, deep_90_100=0.172, early_strike=0.070
  Contestant 2: top_15=0.000, mid_16_69=0.133, high_70_89=0.576, deep_90_100=0.291, early_strike=0.195
  Contestant 3: top_15=0.086, mid_16_69=0.541, high_70_89=0.359, deep_90_100=0.015, early_strike=0.102

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.661, avg_score=2006.0, avg_median_score=2062.1, avg_stdev=345.4, avg_strikes=2.45, avg_first_out_rate=0.034
Contestant 2: avg_win_rate=0.189, avg_score=1452.1, avg_median_score=1400.8, avg_stdev=256.4, avg_strikes=2.70, avg_first_out_rate=0.422
Contestant 3: avg_win_rate=0.150, avg_score=1190.1, avg_median_score=1178.8, avg_stdev=215.2, avg_strikes=2.42, avg_first_out_rate=0.357
Last survivor but lost rate: 0.149
Solo started behind rate: 0.273
Solo started behind and lost rate: 0.484
Avg solo start deficit: 162.6
Avg solo turns taken: 7.73
Solo had winning answer rate: 0.102
Solo had winning answer given started behind rate: 0.433
Solo start deficit buckets: 1-75: 0.434, 76-150: 0.230, 151-250: 0.128, 251+: 0.208
Avg final board read: -0.037
Avg absolute final board read: 0.089
Avg strong harsh board rate: 0.134
Avg strong generous board rate: 0.032
Avg final cutoff estimate: 63.50
Avg final cutoff uncertainty: 0.377
Avg low uncertainty rate: 0.116
Avg high cutoff rate: 0.413
Avg final safe floor: 51.24
Avg final local density read: 0.066
Avg final surprise read: 0.182
Avg final near-cutoff hits: 2.30
Avg final near-cutoff misses: 0.05
Mode rates: safe=0.620, risky=0.272, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.003, victory_lap=0.093
Double window mode rates: safe=0.666, risky=0.334, blind_risk=0.000
Context rates: open=0.681, dense=0.421, generous=0.296, dense_and_generous=0.037, tight=0.133, uncertain=0.481, 
Context-action rates: risky_on_open=0.271, risky_on_dense=0.389, risky_on_generous=0.083, risky_on_dense_and_generous=0.102, safe_on_tight=0.920, risky_on_uncertain=0.298, safe_on_uncertain=0.663, risky_on_double_window=0.334, safe_on_double_window=0.666
Aggregate answer-state summary:
Contestant 1: knowledge=0.222, recall=0.203, confidence=0.222, safe_candidates=76.4, risky_candidates=97.3
Contestant 2: knowledge=0.211, recall=0.196, confidence=0.220, safe_candidates=66.3, risky_candidates=95.0
Contestant 3: knowledge=0.177, recall=0.164, confidence=0.180, safe_candidates=52.7, risky_candidates=87.9
```

**Notes:**

No new behavior was altered, however new metrics do provide much better visibility into why the model behaves the way it does.

**Takeaway:**

1. **Implementation is confirmed to be diagnostic-only**

Aggregate gameplay numbers match Run 2.2, Run 2.3 is thus a clearn run for the Run 2 phase

2. **Answer-state metrics explain C1's dominance****

| Contestant | knowledge | recall | confidence | safe_candidates | risky_candidates
| - | - | - | - | - | -
| C1 | 0.222 | 0.203 | 0.222 | 76.4 | 97.3
| C2 | 0.211 | 0.196 | 0.220 | 66.3 | 95.0
| C3 | 0.177 | 0.164 | 0.180 | 52.7 | 87.9

C1 is thus has **far more safe candidates** especially in hard categories, which matters because safe candidates are what let a player survive, accumulate poitns, and get into victory-lap states.

C2 is actually close to C1 in average confidence, but the safe-candidate gap is meaningful
- C2's issue is not a lack of playable answers, it is due to having fewer high-confidence/safe answers, which makes him more vulnerable to early elimination in harder categories

3. **bWAR's problem is now very obvious**

| Contestant | bWAR safe_candidates | bWAR Win Rate
| - | - | -
| C1 | 69.7 | 0.982
| C2 | 25.0 | 0.005
| C3 | 31.1 | 0.013

The current `war: 0.78` penalty for C2 is too blunt. It is not creating "C2 miscalibrates WAR sometimes", rather it creats "C2 has almost no safe WAR board", which explains why he is basically dead in bWAR

4. **MVP has the same issue, but for C3**

| Contestant | MVP safe_candidates | MVP Win Rate
| - | - | -
| C1 | 44.1 | 0.698
| C2 | 38.6 | 0.298
| C3 | 14.9 | 0.003

Similarly to C2 with bWAR, MVP not functioning as a "hard but playable" category, rather it plays as "C3 has no safe board."
- This may be fine if MVP remains an extreme stress-test category, but it confirms that the model should not be over-calibrated around MVP

5. **HR shows what the model looks like when C2/C3 have real playable boards**

| Contestant | HR safe_candidates | HR Win Rate | HR confidence
| - | - | - | -
| C1 | 94.4 | 0.466 | 0.292
| C2 | 95.9 | 0.280 | 0.351
| C3 | 86.7 | 0.254 | 0.282

This is expected from an open, modern, familiar category
- C2 even has the highest confidence

The M5 profile system is working on modern/counting categories. The issue is that some hard categories are creating extreme safe-candidate gaps

6. **Player mode rates are very useful**

OPS+:

| Contestant | safe | risky | blind
| - | - | - | -
| C1 | 0.736 | 0.200 | 0.001
| C2 | 0.768 | 0.192 | 0.027
| C3 | 0.717 | 0.261 | 0.001

C3 is more aggresive than C1/C2, while C2 has more blind-risk behavior

HR:

| Contestant | safe | risky | blind
| - | - | - | -
| C1 | 0.448 | 0.522 | 0.000
| C2 | 0.501 | 0.458 | 0.040
| C3 | 0.493 | 0.494 | 0.000

Everyone is willing to attack in an open category, but C2's blind risk tendency still stands out

MVP:

| Contestant | victory_lap
| - | - 
| C1 | 0.369
| C2 | 0.157
| C3 | 0.001

Clear category imbalance, C3 basically never reaches a meaningful endgame state

7. **Hit rates show that risky does not mean "bad"**

risky hit:

| Contestant | HR | Hits | MVP | bWAR 
| - | - | - | - | -
| C1 | 0.992 | 0.984 | 0.842 | 0.870
| C2 | 0.997 | 0.968 | 0.824 | 0.788
| C3 | 0.985 | 0.969 | 0.767 | 0.809

- "risky" in the current model often means **higher-value but still highly playable**, but not truly reckless
  - this is okay, but still worth noticing
- "risky" becomes more dangerous in harder categories
  - thus, hit-rate metrics are doing their job as they show when risky behavior is actually reckless versus just assertive

8. **Early-guess profile is interesting, but reveals a modeling artifact**

Early profile shows C2 opening with extreme guesses a lot:
- OPS+: deep_90_100 = 0.827
- HR: deep_90_100 = 0.899
- Hits: deep_90_100 = 0.902

This may be due to C2's `style="volatile"` tag as well as not having double-window toggling like C1/C3
- Thus C2 is opening many games by selecting from the top of the risky pool
  - Interesting shift, but may not map cleanly to real life, as C3 is noted to often be the early volatile one, however the simulator has this as C2

C3 does still show some "mixed/extreme" early behavior, especially in MVP:
- top_15=0.086
- high_70_90=0.359
- early_strike=0.102

Overall, this suggests that the current C3 profile is not fully capturing real life observations
- C3 is risky, but "early extreme outcomes" are being distributed differently than expected
  - This is NOT a Run 2 problem, it's a good setup for later strike-state/early-volatility M5 work

**Conclusion:**

Run 2.3 added diagnostic metrics without changing gameplay. The run confirmed that the M5 answer-state identity layer is working as intended, while also revealing where the current validation suite is too blunt.

The new answer-state metrics showed that C1's dominance comes largely from having more safe candidates, especially in hard categories. In All-Time bWAR, C1 averaged 69.7 safe candidates compared to only 25.0 for C2 and 32.1 for C3, explaining the extreme C1 win rate. In modern/counting categories like Home Runs since 2000, candidate pools were much closer, and win rates became much more balanced.

The new mode and hit-rate metrics also showed that risky behavior is often highly successful in open categories, meaning “risky” currently represents assertive high-value play more than reckless guessing. Early-game metrics showed useful player-style separation, but also suggested that the current model does not yet fully capture C3's real-world early volatility and two-strike resilience.

Run 2.3 therefore closes the initial M5 answer-state identity phase. The next step should be expanding the validation suite and refining category tags before adding more player-behavior systems.

### Run 3

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.655, avg_score=1811.8, median_score=1748.0, stdev=301.1, avg_strikes=2.97, first_out_rate=0.086
Contestant 2: win_rate=0.166, avg_score=1595.9, median_score=1595.0, stdev=195.7, avg_strikes=2.98, first_out_rate=0.473
Contestant 3: win_rate=0.179, avg_score=1308.0, median_score=1254.0, stdev=275.3, avg_strikes=2.97, first_out_rate=0.431
Last survivor but lost rate: 0.245
Solo started behind rate: 0.391
Solo started behind and lost rate: 0.627
Avg solo start deficit: 242.0
Avg solo turns taken: 2.38
Solo had winning answer rate: 0.118
Solo had winning answer given started behind rate: 0.301
Solo start deficit buckets: 1-75: 0.345, 76-150: 0.203, 151-250: 0.127, 251+: 0.324
Avg final board read: 0.030
Avg absolute final board read: 0.092
Strong harsh board rate: 0.063
Strong generous board rate: 0.125
Avg final cutoff estimate: 66.20
Avg final cutoff uncertainty: 0.343
Low uncertainty rate: 0.054
High cutoff rate: 0.402
Avg final safe floor: 54.14
Avg final local density read: 0.053
Avg final surprise read: 0.177
Avg final near-cutoff hits: 2.66
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.740, risky=0.217, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.027
Double window mode rates: safe=0.755, risky=0.245, blind_risk=0.000
Context rates: open=0.707, dense=0.420, generous=0.338, dense_and_generous=0.051, tight=0.093, uncertain=0.352, 
Context-action rates: risky_on_open=0.191, risky_on_dense=0.285, risky_on_generous=0.057, risky_on_dense_and_generous=0.074, safe_on_tight=0.942, risky_on_uncertain=0.367, safe_on_uncertain=0.620, risky_on_double_window=0.245, safe_on_double_window=0.755
Answer-state summary:
  Contestant 1: knowledge=0.217, recall=0.199, confidence=0.219, safe_candidates=83.4, risky_candidates=98.5, blind_candidates=1.2
  Contestant 2: knowledge=0.215, recall=0.193, confidence=0.206, safe_candidates=81.6, risky_candidates=97.2, blind_candidates=2.4
  Contestant 3: knowledge=0.174, recall=0.156, confidence=0.167, safe_candidates=56.4, risky_candidates=90.7, blind_candidates=7.8
Player mode rates:
  Contestant 1: safe=0.736, risky=0.200, blind=0.001, victory_lap=0.059
  Contestant 2: safe=0.768, risky=0.192, blind=0.027, victory_lap=0.010
  Contestant 3: safe=0.717, risky=0.261, blind=0.001, victory_lap=0.010
Player mode hit rates:
  Contestant 1: safe=0.939, risky=0.939, blind=0.038, desperation=0.193
  Contestant 2: safe=0.953, risky=0.890, blind=0.052, desperation=0.129
  Contestant 3: safe=0.934, risky=0.920, blind=0.051, desperation=0.130
Player avg guess values:
  Contestant 1: safe=45.0, risky=78.0, blind=95.6
  Contestant 2: safe=43.7, risky=81.5, blind=95.6
  Contestant 3: safe=33.8, risky=65.0, blind=96.1
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.606, high_70_89=0.029, deep_90_100=0.365, early_strike=0.051
  Contestant 2: top_15=0.000, mid_16_69=0.061, high_70_89=0.099, deep_90_100=0.837, early_strike=0.207
  Contestant 3: top_15=0.000, mid_16_69=0.603, high_70_89=0.293, deep_90_100=0.104, early_strike=0.064

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.843, avg_score=2166.8, median_score=2295.0, stdev=486.0, avg_strikes=3.00, first_out_rate=0.018
Contestant 2: win_rate=0.110, avg_score=1387.9, median_score=1363.0, stdev=265.3, avg_strikes=3.00, first_out_rate=0.150
Contestant 3: win_rate=0.047, avg_score=925.9, median_score=847.0, stdev=282.0, avg_strikes=3.00, first_out_rate=0.832
Last survivor but lost rate: 0.084
Solo started behind rate: 0.228
Solo started behind and lost rate: 0.367
Avg solo start deficit: 128.3
Avg solo turns taken: 6.73
Solo had winning answer rate: 0.113
Solo had winning answer given started behind rate: 0.495
Solo start deficit buckets: 1-75: 0.441, 76-150: 0.278, 151-250: 0.162, 251+: 0.120
Avg final board read: 0.040
Avg absolute final board read: 0.075
Strong harsh board rate: 0.014
Strong generous board rate: 0.133
Avg final cutoff estimate: 70.44
Avg final cutoff uncertainty: 0.420
Low uncertainty rate: 0.006
High cutoff rate: 0.585
Avg final safe floor: 57.92
Avg final local density read: 0.054
Avg final surprise read: 0.183
Avg final near-cutoff hits: 2.67
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.733, risky=0.150, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.104
Double window mode rates: safe=0.822, risky=0.178, blind_risk=0.000
Context rates: open=0.648, dense=0.314, generous=0.381, dense_and_generous=0.048, tight=0.118, uncertain=0.597, 
Context-action rates: risky_on_open=0.109, risky_on_dense=0.192, risky_on_generous=0.034, risky_on_dense_and_generous=0.052, safe_on_tight=0.982, risky_on_uncertain=0.202, safe_on_uncertain=0.782, risky_on_double_window=0.178, safe_on_double_window=0.822
Answer-state summary:
  Contestant 1: knowledge=0.181, recall=0.168, confidence=0.188, safe_candidates=69.7, risky_candidates=96.1, blind_candidates=2.9
  Contestant 2: knowledge=0.170, recall=0.153, confidence=0.163, safe_candidates=56.3, risky_candidates=93.5, blind_candidates=5.3
  Contestant 3: knowledge=0.145, recall=0.130, confidence=0.139, safe_candidates=36.0, risky_candidates=84.1, blind_candidates=13.5
Player mode rates:
  Contestant 1: safe=0.645, risky=0.111, blind=0.002, victory_lap=0.238
  Contestant 2: safe=0.784, risky=0.164, blind=0.029, victory_lap=0.021
  Contestant 3: safe=0.804, risky=0.190, blind=0.000, victory_lap=0.003
Player mode hit rates:
  Contestant 1: safe=0.975, risky=0.892, blind=0.053, desperation=0.226
  Contestant 2: safe=0.948, risky=0.875, blind=0.054, desperation=0.195
  Contestant 3: safe=0.915, risky=0.837, blind=0.064, desperation=0.141
Player avg guess values:
  Contestant 1: safe=44.5, risky=84.8, blind=95.3
  Contestant 2: safe=40.1, risky=83.1, blind=94.5
  Contestant 3: safe=28.7, risky=70.6, blind=92.7
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.591, high_70_89=0.101, deep_90_100=0.308, early_strike=0.066
  Contestant 2: top_15=0.000, mid_16_69=0.084, high_70_89=0.471, deep_90_100=0.445, early_strike=0.181
  Contestant 3: top_15=0.000, mid_16_69=0.585, high_70_89=0.368, deep_90_100=0.047, early_strike=0.089

=== Category: Hitter bWAR since 2000 ===
Contestant 1: win_rate=0.543, avg_score=1708.1, median_score=1672.0, stdev=290.7, avg_strikes=2.98, first_out_rate=0.106
Contestant 2: win_rate=0.237, avg_score=1614.1, median_score=1594.0, stdev=218.5, avg_strikes=2.99, first_out_rate=0.473
Contestant 3: win_rate=0.220, avg_score=1325.9, median_score=1287.0, stdev=268.0, avg_strikes=2.98, first_out_rate=0.413
Last survivor but lost rate: 0.259
Solo started behind rate: 0.417
Solo started behind and lost rate: 0.621
Avg solo start deficit: 236.5
Avg solo turns taken: 2.39
Solo had winning answer rate: 0.120
Solo had winning answer given started behind rate: 0.289
Solo start deficit buckets: 1-75: 0.314, 76-150: 0.198, 151-250: 0.137, 251+: 0.350
Avg final board read: 0.025
Avg absolute final board read: 0.087
Strong harsh board rate: 0.061
Strong generous board rate: 0.089
Avg final cutoff estimate: 65.30
Avg final cutoff uncertainty: 0.347
Low uncertainty rate: 0.053
High cutoff rate: 0.367
Avg final safe floor: 53.22
Avg final local density read: 0.055
Avg final surprise read: 0.171
Avg final near-cutoff hits: 2.74
Avg final near-cutoff misses: 0.04
Mode rates: safe=0.736, risky=0.223, blind_risk=0.010, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.004, victory_lap=0.026
Double window mode rates: safe=0.747, risky=0.253, blind_risk=0.000
Context rates: open=0.706, dense=0.419, generous=0.338, dense_and_generous=0.051, tight=0.099, uncertain=0.357, 
Context-action rates: risky_on_open=0.197, risky_on_dense=0.295, risky_on_generous=0.060, risky_on_dense_and_generous=0.091, safe_on_tight=0.942, risky_on_uncertain=0.369, safe_on_uncertain=0.617, risky_on_double_window=0.253, safe_on_double_window=0.747
Answer-state summary:
  Contestant 1: knowledge=0.205, recall=0.187, confidence=0.204, safe_candidates=78.8, risky_candidates=97.6, blind_candidates=1.9
  Contestant 2: knowledge=0.197, recall=0.188, confidence=0.222, safe_candidates=81.5, risky_candidates=97.4, blind_candidates=1.6
  Contestant 3: knowledge=0.164, recall=0.155, confidence=0.174, safe_candidates=57.6, risky_candidates=91.1, blind_candidates=6.9
Player mode rates:
  Contestant 1: safe=0.729, risky=0.219, blind=0.001, victory_lap=0.047
  Contestant 2: safe=0.763, risky=0.191, blind=0.029, victory_lap=0.016
  Contestant 3: safe=0.716, risky=0.259, blind=0.001, victory_lap=0.012
Player mode hit rates:
  Contestant 1: safe=0.936, risky=0.937, blind=0.041, desperation=0.193
  Contestant 2: safe=0.953, risky=0.900, blind=0.046, desperation=0.136
  Contestant 3: safe=0.935, risky=0.922, blind=0.054, desperation=0.151
Player avg guess values:
  Contestant 1: safe=42.8, risky=75.6, blind=95.7
  Contestant 2: safe=43.8, risky=82.8, blind=95.5
  Contestant 3: safe=34.3, risky=65.8, blind=95.7
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.597, high_70_89=0.065, deep_90_100=0.338, early_strike=0.058
  Contestant 2: top_15=0.000, mid_16_69=0.062, high_70_89=0.087, deep_90_100=0.842, early_strike=0.185
  Contestant 3: top_15=0.000, mid_16_69=0.593, high_70_89=0.289, deep_90_100=0.117, early_strike=0.066

=== Category: Pitcher bWAR since 2000 ===
Contestant 1: win_rate=0.872, avg_score=2237.7, median_score=2375.5, stdev=532.0, avg_strikes=3.00, first_out_rate=0.009
Contestant 2: win_rate=0.068, avg_score=1171.7, median_score=1146.0, stdev=264.5, avg_strikes=3.00, first_out_rate=0.390
Contestant 3: win_rate=0.060, avg_score=923.0, median_score=856.0, stdev=280.2, avg_strikes=3.00, first_out_rate=0.601
Last survivor but lost rate: 0.077
Solo started behind rate: 0.226
Solo started behind and lost rate: 0.341
Avg solo start deficit: 136.0
Avg solo turns taken: 9.86
Solo had winning answer rate: 0.114
Solo had winning answer given started behind rate: 0.504
Solo start deficit buckets: 1-75: 0.434, 76-150: 0.260, 151-250: 0.152, 251+: 0.154
Avg final board read: 0.013
Avg absolute final board read: 0.066
Strong harsh board rate: 0.011
Strong generous board rate: 0.072
Avg final cutoff estimate: 69.85
Avg final cutoff uncertainty: 0.449
Low uncertainty rate: 0.003
High cutoff rate: 0.546
Avg final safe floor: 57.16
Avg final local density read: 0.053
Avg final surprise read: 0.181
Avg final near-cutoff hits: 2.41
Avg final near-cutoff misses: 0.07
Mode rates: safe=0.691, risky=0.147, blind_risk=0.009, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.150
Double window mode rates: safe=0.825, risky=0.175, blind_risk=0.000
Context rates: open=0.620, dense=0.273, generous=0.382, dense_and_generous=0.035, tight=0.170, uncertain=0.692, 
Context-action rates: risky_on_open=0.107, risky_on_dense=0.195, risky_on_generous=0.043, risky_on_dense_and_generous=0.083, safe_on_tight=0.982, risky_on_uncertain=0.179, safe_on_uncertain=0.790, risky_on_double_window=0.175, safe_on_double_window=0.825
Answer-state summary:
  Contestant 1: knowledge=0.173, recall=0.157, confidence=0.172, safe_candidates=60.8, risky_candidates=94.7, blind_candidates=4.2
  Contestant 2: knowledge=0.146, recall=0.137, confidence=0.149, safe_candidates=39.9, risky_candidates=91.1, blind_candidates=7.2
  Contestant 3: knowledge=0.138, recall=0.131, confidence=0.140, safe_candidates=36.7, risky_candidates=84.3, blind_candidates=13.2
Player mode rates:
  Contestant 1: safe=0.566, risky=0.098, blind=0.001, victory_lap=0.330
  Contestant 2: safe=0.776, risky=0.180, blind=0.027, victory_lap=0.016
  Contestant 3: safe=0.798, risky=0.190, blind=0.003, victory_lap=0.006
Player mode hit rates:
  Contestant 1: safe=0.980, risky=0.879, blind=0.063, desperation=0.222
  Contestant 2: safe=0.940, risky=0.836, blind=0.062, desperation=0.192
  Contestant 3: safe=0.916, risky=0.829, blind=0.040, desperation=0.178
Player avg guess values:
  Contestant 1: safe=41.8, risky=83.9, blind=94.5
  Contestant 2: safe=37.1, risky=82.7, blind=92.7
  Contestant 3: safe=29.4, risky=72.3, blind=91.4
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.598, high_70_89=0.158, deep_90_100=0.244, early_strike=0.065
  Contestant 2: top_15=0.000, mid_16_69=0.084, high_70_89=0.605, deep_90_100=0.311, early_strike=0.202
  Contestant 3: top_15=0.000, mid_16_69=0.595, high_70_89=0.355, deep_90_100=0.050, early_strike=0.089

=== Category: All-Time ERA+ ===
Contestant 1: win_rate=0.806, avg_score=2266.0, median_score=2492.0, stdev=666.7, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.189, avg_score=1270.4, median_score=1141.5, stdev=466.8, avg_strikes=3.00, first_out_rate=0.022
Contestant 3: win_rate=0.005, avg_score=594.4, median_score=543.0, stdev=231.3, avg_strikes=3.00, first_out_rate=0.977
Last survivor but lost rate: 0.084
Solo started behind rate: 0.300
Solo started behind and lost rate: 0.280
Avg solo start deficit: 109.6
Avg solo turns taken: 16.63
Solo had winning answer rate: 0.164
Solo had winning answer given started behind rate: 0.547
Solo start deficit buckets: 1-75: 0.444, 76-150: 0.293, 151-250: 0.176, 251+: 0.087
Avg final board read: -0.042
Avg absolute final board read: 0.081
Strong harsh board rate: 0.090
Strong generous board rate: 0.014
Avg final cutoff estimate: 71.84
Avg final cutoff uncertainty: 0.499
Low uncertainty rate: 0.000
High cutoff rate: 0.646
Avg final safe floor: 58.85
Avg final local density read: 0.062
Avg final surprise read: 0.208
Avg final near-cutoff hits: 1.79
Avg final near-cutoff misses: 0.08
Mode rates: safe=0.656, risky=0.119, blind_risk=0.011, chip_away=0.000, exact_win=0.002, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.211
Double window mode rates: safe=0.810, risky=0.190, blind_risk=0.000
Context rates: open=0.610, dense=0.264, generous=0.379, dense_and_generous=0.033, tight=0.195, uncertain=0.764, 
Context-action rates: risky_on_open=0.074, risky_on_dense=0.139, risky_on_generous=0.029, risky_on_dense_and_generous=0.070, safe_on_tight=0.974, risky_on_uncertain=0.148, safe_on_uncertain=0.789, risky_on_double_window=0.190, safe_on_double_window=0.810
Answer-state summary:
  Contestant 1: knowledge=0.158, recall=0.145, confidence=0.159, safe_candidates=49.8, risky_candidates=92.9, blind_candidates=5.6
  Contestant 2: knowledge=0.156, recall=0.141, confidence=0.144, safe_candidates=39.6, risky_candidates=91.1, blind_candidates=8.0
  Contestant 3: knowledge=0.127, recall=0.114, confidence=0.112, safe_candidates=16.8, risky_candidates=74.4, blind_candidates=24.1
Player mode rates:
  Contestant 1: safe=0.527, risky=0.075, blind=0.004, victory_lap=0.388
  Contestant 2: safe=0.761, risky=0.131, blind=0.029, victory_lap=0.078
  Contestant 3: safe=0.795, risky=0.203, blind=0.000, victory_lap=0.001
Player mode hit rates:
  Contestant 1: safe=0.981, risky=0.858, blind=0.049, desperation=0.182
  Contestant 2: safe=0.945, risky=0.832, blind=0.052, desperation=0.159
  Contestant 3: safe=0.873, risky=0.776, blind=0.111, desperation=0.162
Player avg guess values:
  Contestant 1: safe=38.5, risky=85.5, blind=93.3
  Contestant 2: safe=37.8, risky=85.1, blind=92.1
  Contestant 3: safe=26.0, risky=71.5, blind=91.5
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.588, high_70_89=0.213, deep_90_100=0.199, early_strike=0.070
  Contestant 2: top_15=0.000, mid_16_69=0.123, high_70_89=0.587, deep_90_100=0.291, early_strike=0.191
  Contestant 3: top_15=0.058, mid_16_69=0.554, high_70_89=0.371, deep_90_100=0.017, early_strike=0.104

=== Category: Pitcher Strikeouts since 2010 ===
Contestant 1: win_rate=0.423, avg_score=1715.9, median_score=1706.0, stdev=81.8, avg_strikes=0.64, first_out_rate=0.000
Contestant 2: win_rate=0.296, avg_score=1675.7, median_score=1683.0, stdev=90.2, avg_strikes=1.70, first_out_rate=0.148
Contestant 3: win_rate=0.281, avg_score=1654.6, median_score=1678.0, stdev=105.3, avg_strikes=0.41, first_out_rate=0.015
Last survivor but lost rate: 0.020
Solo started behind rate: 0.047
Solo started behind and lost rate: 0.424
Avg solo start deficit: 93.8
Avg solo turns taken: 3.00
Solo had winning answer rate: 0.027
Solo had winning answer given started behind rate: 0.576
Solo start deficit buckets: 1-75: 0.586, 76-150: 0.222, 151-250: 0.099, 251+: 0.093
Avg final board read: -0.096
Avg absolute final board read: 0.105
Strong harsh board rate: 0.260
Strong generous board rate: 0.000
Avg final cutoff estimate: 50.96
Avg final cutoff uncertainty: 0.281
Low uncertainty rate: 0.295
High cutoff rate: 0.124
Avg final safe floor: 39.28
Avg final local density read: 0.071
Avg final surprise read: 0.184
Avg final near-cutoff hits: 2.27
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.450, risky=0.534, blind_risk=0.013, chip_away=0.000, exact_win=0.000, comeback=0.000, high_upside=0.000, desperation=0.000, victory_lap=0.002
Double window mode rates: safe=0.442, risky=0.558, blind_risk=0.000
Context rates: open=0.748, dense=0.575, generous=0.189, dense_and_generous=0.016, tight=0.089, uncertain=0.323, 
Context-action rates: risky_on_open=0.562, risky_on_dense=0.647, risky_on_generous=0.283, risky_on_dense_and_generous=0.328, safe_on_tight=0.823, risky_on_uncertain=0.620, safe_on_uncertain=0.364, risky_on_double_window=0.558, safe_on_double_window=0.442
Answer-state summary:
  Contestant 1: knowledge=0.317, recall=0.285, confidence=0.304, safe_candidates=95.3, risky_candidates=100.0, blind_candidates=0.0
  Contestant 2: knowledge=0.313, recall=0.317, confidence=0.402, safe_candidates=97.4, risky_candidates=100.0, blind_candidates=0.0
  Contestant 3: knowledge=0.254, recall=0.257, confidence=0.322, safe_candidates=89.6, risky_candidates=99.3, blind_candidates=0.1
Player mode rates:
  Contestant 1: safe=0.416, risky=0.584, blind=0.000, victory_lap=0.000
  Contestant 2: safe=0.467, risky=0.492, blind=0.040, victory_lap=0.001
  Contestant 3: safe=0.467, risky=0.527, blind=0.000, victory_lap=0.004
Player mode hit rates:
  Contestant 1: safe=0.969, risky=0.990, blind=0.000, desperation=0.000
  Contestant 2: safe=0.983, risky=0.997, blind=0.000, desperation=0.000
  Contestant 3: safe=0.997, risky=0.990, blind=0.000, desperation=0.040
Player avg guess values:
  Contestant 1: safe=39.8, risky=58.9, blind=0.0
  Contestant 2: safe=35.8, risky=66.3, blind=0.0
  Contestant 3: safe=41.5, risky=55.7, blind=98.5
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.526, high_70_89=0.000, deep_90_100=0.474, early_strike=0.000
  Contestant 2: top_15=0.000, mid_16_69=0.034, high_70_89=0.000, deep_90_100=0.917, early_strike=0.049
  Contestant 3: top_15=0.000, mid_16_69=0.524, high_70_89=0.002, deep_90_100=0.473, early_strike=0.035

=== Category: Home Runs since 2020 ===
Contestant 1: win_rate=0.400, avg_score=1707.0, median_score=1701.0, stdev=75.3, avg_strikes=0.48, first_out_rate=0.000
Contestant 2: win_rate=0.278, avg_score=1665.5, median_score=1675.0, stdev=88.1, avg_strikes=1.59, first_out_rate=0.067
Contestant 3: win_rate=0.322, avg_score=1676.8, median_score=1690.0, stdev=87.3, avg_strikes=0.16, first_out_rate=0.002
Last survivor but lost rate: 0.004
Solo started behind rate: 0.010
Solo started behind and lost rate: 0.417
Avg solo start deficit: 97.0
Avg solo turns taken: 3.12
Solo had winning answer rate: 0.006
Solo had winning answer given started behind rate: 0.583
Solo start deficit buckets: 1-75: 0.604, 76-150: 0.177, 151-250: 0.125, 251+: 0.094
Avg final board read: -0.103
Avg absolute final board read: 0.109
Strong harsh board rate: 0.253
Strong generous board rate: 0.000
Avg final cutoff estimate: 50.05
Avg final cutoff uncertainty: 0.280
Low uncertainty rate: 0.285
High cutoff rate: 0.095
Avg final safe floor: 38.37
Avg final local density read: 0.069
Avg final surprise read: 0.190
Avg final near-cutoff hits: 2.24
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.425, risky=0.561, blind_risk=0.013, chip_away=0.000, exact_win=0.000, comeback=0.000, high_upside=0.000, desperation=0.000, victory_lap=0.000
Double window mode rates: safe=0.419, risky=0.581, blind_risk=0.000
Context rates: open=0.750, dense=0.578, generous=0.186, dense_and_generous=0.014, tight=0.083, uncertain=0.322, 
Context-action rates: risky_on_open=0.590, risky_on_dense=0.669, risky_on_generous=0.329, risky_on_dense_and_generous=0.386, safe_on_tight=0.820, risky_on_uncertain=0.639, safe_on_uncertain=0.345, risky_on_double_window=0.581, safe_on_double_window=0.419
Answer-state summary:
  Contestant 1: knowledge=0.346, recall=0.311, confidence=0.332, safe_candidates=97.4, risky_candidates=100.0, blind_candidates=0.0
  Contestant 2: knowledge=0.341, recall=0.346, confidence=0.438, safe_candidates=98.7, risky_candidates=100.0, blind_candidates=0.0
  Contestant 3: knowledge=0.277, recall=0.280, confidence=0.352, safe_candidates=92.2, risky_candidates=99.8, blind_candidates=0.0
Player mode rates:
  Contestant 1: safe=0.395, risky=0.605, blind=0.000, victory_lap=0.000
  Contestant 2: safe=0.437, risky=0.522, blind=0.040, victory_lap=0.000
  Contestant 3: safe=0.443, risky=0.555, blind=0.000, victory_lap=0.001
Player mode hit rates:
  Contestant 1: safe=0.980, risky=0.989, blind=0.000, desperation=0.000
  Contestant 2: safe=0.991, risky=0.996, blind=0.000, desperation=0.000
  Contestant 3: safe=0.999, risky=0.994, blind=0.000, desperation=0.034
Player avg guess values:
  Contestant 1: safe=39.7, risky=58.0, blind=0.0
  Contestant 2: safe=35.0, risky=64.9, blind=0.0
  Contestant 3: safe=41.7, risky=55.9, blind=0.0
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.525, high_70_89=0.000, deep_90_100=0.475, early_strike=0.000
  Contestant 2: top_15=0.000, mid_16_69=0.019, high_70_89=0.000, deep_90_100=0.932, early_strike=0.049
  Contestant 3: top_15=0.000, mid_16_69=0.524, high_70_89=0.000, deep_90_100=0.476, early_strike=0.020

=== Category: Stolen Bases since 2000 ===
Contestant 1: win_rate=0.402, avg_score=1691.0, median_score=1695.0, stdev=139.5, avg_strikes=2.22, first_out_rate=0.104
Contestant 2: win_rate=0.246, avg_score=1661.9, median_score=1664.5, stdev=127.7, avg_strikes=2.56, first_out_rate=0.531
Contestant 3: win_rate=0.352, avg_score=1608.3, median_score=1653.0, stdev=165.0, avg_strikes=2.14, first_out_rate=0.092
Last survivor but lost rate: 0.265
Solo started behind rate: 0.378
Solo started behind and lost rate: 0.700
Avg solo start deficit: 190.3
Avg solo turns taken: 2.32
Solo had winning answer rate: 0.100
Solo had winning answer given started behind rate: 0.265
Solo start deficit buckets: 1-75: 0.368, 76-150: 0.194, 151-250: 0.137, 251+: 0.302
Avg final board read: -0.057
Avg absolute final board read: 0.092
Strong harsh board rate: 0.208
Strong generous board rate: 0.001
Avg final cutoff estimate: 55.17
Avg final cutoff uncertainty: 0.293
Low uncertainty rate: 0.252
High cutoff rate: 0.219
Avg final safe floor: 43.41
Avg final local density read: 0.078
Avg final surprise read: 0.152
Avg final near-cutoff hits: 2.82
Avg final near-cutoff misses: 0.01
Mode rates: safe=0.581, risky=0.391, blind_risk=0.012, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.005, victory_lap=0.009
Double window mode rates: safe=0.568, risky=0.432, blind_risk=0.000
Context rates: open=0.736, dense=0.536, generous=0.229, dense_and_generous=0.030, tight=0.112, uncertain=0.323, 
Context-action rates: risky_on_open=0.402, risky_on_dense=0.504, risky_on_generous=0.133, risky_on_dense_and_generous=0.167, safe_on_tight=0.842, risky_on_uncertain=0.513, safe_on_uncertain=0.472, risky_on_double_window=0.432, safe_on_double_window=0.568
Answer-state summary:
  Contestant 1: knowledge=0.253, recall=0.228, confidence=0.243, safe_candidates=89.4, risky_candidates=99.7, blind_candidates=0.4
  Contestant 2: knowledge=0.250, recall=0.244, confidence=0.293, safe_candidates=91.9, risky_candidates=99.8, blind_candidates=0.0
  Contestant 3: knowledge=0.203, recall=0.197, confidence=0.235, safe_candidates=77.7, risky_candidates=96.2, blind_candidates=2.5
Player mode rates:
  Contestant 1: safe=0.583, risky=0.411, blind=0.000, victory_lap=0.004
  Contestant 2: safe=0.621, risky=0.339, blind=0.035, victory_lap=0.004
  Contestant 3: safe=0.541, risky=0.422, blind=0.001, victory_lap=0.019
Player mode hit rates:
  Contestant 1: safe=0.911, risky=0.981, blind=0.026, desperation=0.103
  Contestant 2: safe=0.954, risky=0.979, blind=0.001, desperation=0.020
  Contestant 3: safe=0.969, risky=0.974, blind=0.033, desperation=0.082
Player avg guess values:
  Contestant 1: safe=41.3, risky=63.7, blind=96.8
  Contestant 2: safe=39.5, risky=73.4, blind=96.5
  Contestant 3: safe=40.0, risky=58.0, blind=97.5
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.546, high_70_89=0.012, deep_90_100=0.442, early_strike=0.032
  Contestant 2: top_15=0.000, mid_16_69=0.061, high_70_89=0.001, deep_90_100=0.890, early_strike=0.088
  Contestant 3: top_15=0.000, mid_16_69=0.543, high_70_89=0.122, deep_90_100=0.335, early_strike=0.064

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.466, avg_score=1729.3, median_score=1717.0, stdev=88.4, avg_strikes=0.92, first_out_rate=0.001
Contestant 2: win_rate=0.280, avg_score=1680.2, median_score=1686.0, stdev=97.0, avg_strikes=1.87, first_out_rate=0.247
Contestant 3: win_rate=0.254, avg_score=1629.6, median_score=1664.0, stdev=124.7, avg_strikes=0.77, first_out_rate=0.039
Last survivor but lost rate: 0.057
Solo started behind rate: 0.115
Solo started behind and lost rate: 0.498
Avg solo start deficit: 118.1
Avg solo turns taken: 2.74
Solo had winning answer rate: 0.056
Solo had winning answer given started behind rate: 0.491
Solo start deficit buckets: 1-75: 0.517, 76-150: 0.216, 151-250: 0.112, 251+: 0.155
Avg final board read: -0.086
Avg absolute final board read: 0.101
Strong harsh board rate: 0.258
Strong generous board rate: 0.000
Avg final cutoff estimate: 52.02
Avg final cutoff uncertainty: 0.282
Low uncertainty rate: 0.295
High cutoff rate: 0.156
Avg final safe floor: 40.33
Avg final local density read: 0.073
Avg final surprise read: 0.176
Avg final near-cutoff hits: 2.38
Avg final near-cutoff misses: 0.00
Mode rates: safe=0.480, risky=0.501, blind_risk=0.013, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.001, victory_lap=0.003
Double window mode rates: safe=0.472, risky=0.528, blind_risk=0.000
Context rates: open=0.746, dense=0.569, generous=0.196, dense_and_generous=0.019, tight=0.095, uncertain=0.323, 
Context-action rates: risky_on_open=0.526, risky_on_dense=0.617, risky_on_generous=0.236, risky_on_dense_and_generous=0.265, safe_on_tight=0.820, risky_on_uncertain=0.595, safe_on_uncertain=0.389, risky_on_double_window=0.528, safe_on_double_window=0.472
Answer-state summary:
  Contestant 1: knowledge=0.304, recall=0.274, confidence=0.292, safe_candidates=94.4, risky_candidates=100.0, blind_candidates=0.0
  Contestant 2: knowledge=0.300, recall=0.292, confidence=0.351, safe_candidates=95.9, risky_candidates=100.0, blind_candidates=0.0
  Contestant 3: knowledge=0.243, recall=0.237, confidence=0.282, safe_candidates=86.7, risky_candidates=98.6, blind_candidates=0.7
Player mode rates:
  Contestant 1: safe=0.448, risky=0.552, blind=0.000, victory_lap=0.000
  Contestant 2: safe=0.501, risky=0.458, blind=0.040, victory_lap=0.001
  Contestant 3: safe=0.493, risky=0.494, blind=0.000, victory_lap=0.008
Player mode hit rates:
  Contestant 1: safe=0.951, risky=0.992, blind=0.000, desperation=0.000
  Contestant 2: safe=0.975, risky=0.997, blind=0.000, desperation=0.053
  Contestant 3: safe=0.993, risky=0.985, blind=0.000, desperation=0.051
Player avg guess values:
  Contestant 1: safe=40.3, risky=60.2, blind=0.0
  Contestant 2: safe=36.5, risky=67.9, blind=0.0
  Contestant 3: safe=41.2, risky=55.7, blind=97.6
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.528, high_70_89=0.000, deep_90_100=0.472, early_strike=0.001
  Contestant 2: top_15=0.000, mid_16_69=0.052, high_70_89=0.000, deep_90_100=0.899, early_strike=0.049
  Contestant 3: top_15=0.000, mid_16_69=0.524, high_70_89=0.015, deep_90_100=0.461, early_strike=0.056

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.504, avg_score=1730.0, median_score=1720.0, stdev=147.2, avg_strikes=2.37, first_out_rate=0.079
Contestant 2: win_rate=0.194, avg_score=1650.0, median_score=1656.0, stdev=139.5, avg_strikes=2.66, first_out_rate=0.591
Contestant 3: win_rate=0.302, avg_score=1567.7, median_score=1626.0, stdev=189.9, avg_strikes=2.33, first_out_rate=0.117
Last survivor but lost rate: 0.321
Solo started behind rate: 0.439
Solo started behind and lost rate: 0.732
Avg solo start deficit: 217.4
Avg solo turns taken: 2.21
Solo had winning answer rate: 0.099
Solo had winning answer given started behind rate: 0.226
Solo start deficit buckets: 1-75: 0.347, 76-150: 0.208, 151-250: 0.113, 251+: 0.331
Avg final board read: -0.048
Avg absolute final board read: 0.094
Strong harsh board rate: 0.196
Strong generous board rate: 0.011
Avg final cutoff estimate: 55.97
Avg final cutoff uncertainty: 0.297
Low uncertainty rate: 0.231
High cutoff rate: 0.228
Avg final safe floor: 44.19
Avg final local density read: 0.076
Avg final surprise read: 0.152
Avg final near-cutoff hits: 2.87
Avg final near-cutoff misses: 0.01
Mode rates: safe=0.597, risky=0.375, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.006, victory_lap=0.009
Double window mode rates: safe=0.583, risky=0.417, blind_risk=0.000
Context rates: open=0.733, dense=0.526, generous=0.239, dense_and_generous=0.032, tight=0.110, uncertain=0.324, 
Context-action rates: risky_on_open=0.382, risky_on_dense=0.487, risky_on_generous=0.121, risky_on_dense_and_generous=0.150, safe_on_tight=0.847, risky_on_uncertain=0.505, safe_on_uncertain=0.480, risky_on_double_window=0.417, safe_on_double_window=0.583
Answer-state summary:
  Contestant 1: knowledge=0.253, recall=0.233, confidence=0.255, safe_candidates=90.3, risky_candidates=99.8, blind_candidates=0.2
  Contestant 2: knowledge=0.250, recall=0.234, confidence=0.264, safe_candidates=90.4, risky_candidates=99.6, blind_candidates=0.2
  Contestant 3: knowledge=0.203, recall=0.188, confidence=0.209, safe_candidates=73.4, risky_candidates=95.0, blind_candidates=3.8
Player mode rates:
  Contestant 1: safe=0.602, risky=0.389, blind=0.000, victory_lap=0.008
  Contestant 2: safe=0.640, risky=0.321, blind=0.033, victory_lap=0.004
  Contestant 3: safe=0.551, risky=0.413, blind=0.001, victory_lap=0.016
Player mode hit rates:
  Contestant 1: safe=0.907, risky=0.984, blind=0.000, desperation=0.135
  Contestant 2: safe=0.953, risky=0.968, blind=0.007, desperation=0.014
  Contestant 3: safe=0.963, risky=0.969, blind=0.027, desperation=0.084
Player avg guess values:
  Contestant 1: safe=42.1, risky=65.8, blind=95.5
  Contestant 2: safe=40.0, risky=74.0, blind=96.1
  Contestant 3: safe=38.7, risky=57.8, blind=97.4
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.556, high_70_89=0.005, deep_90_100=0.439, early_strike=0.022
  Contestant 2: top_15=0.000, mid_16_69=0.057, high_70_89=0.001, deep_90_100=0.902, early_strike=0.109
  Contestant 3: top_15=0.000, mid_16_69=0.553, high_70_89=0.192, deep_90_100=0.255, early_strike=0.060

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.774, avg_score=2260.4, median_score=2554.0, stdev=753.8, avg_strikes=3.00, first_out_rate=0.001
Contestant 2: win_rate=0.224, avg_score=1266.4, median_score=1081.0, stdev=558.9, avg_strikes=3.00, first_out_rate=0.006
Contestant 3: win_rate=0.001, avg_score=466.5, median_score=422.0, stdev=213.0, avg_strikes=3.00, first_out_rate=0.994
Last survivor but lost rate: 0.095
Solo started behind rate: 0.343
Solo started behind and lost rate: 0.278
Avg solo start deficit: 112.2
Avg solo turns taken: 19.90
Solo had winning answer rate: 0.179
Solo had winning answer given started behind rate: 0.522
Solo start deficit buckets: 1-75: 0.430, 76-150: 0.287, 151-250: 0.203, 251+: 0.080
Avg final board read: -0.058
Avg absolute final board read: 0.083
Strong harsh board rate: 0.135
Strong generous board rate: 0.004
Avg final cutoff estimate: 71.34
Avg final cutoff uncertainty: 0.524
Low uncertainty rate: 0.000
High cutoff rate: 0.609
Avg final safe floor: 58.20
Avg final local density read: 0.069
Avg final surprise read: 0.197
Avg final near-cutoff hits: 1.81
Avg final near-cutoff misses: 0.10
Mode rates: safe=0.625, risky=0.108, blind_risk=0.011, chip_away=0.000, exact_win=0.003, comeback=0.001, high_upside=0.000, desperation=0.002, victory_lap=0.251
Double window mode rates: safe=0.791, risky=0.209, blind_risk=0.000
Context rates: open=0.595, dense=0.265, generous=0.357, dense_and_generous=0.027, tight=0.210, uncertain=0.775, 
Context-action rates: risky_on_open=0.061, risky_on_dense=0.110, risky_on_generous=0.025, risky_on_dense_and_generous=0.067, safe_on_tight=0.960, risky_on_uncertain=0.136, safe_on_uncertain=0.775, risky_on_double_window=0.209, safe_on_double_window=0.791
Answer-state summary:
  Contestant 1: knowledge=0.152, recall=0.140, confidence=0.155, safe_candidates=44.1, risky_candidates=91.9, blind_candidates=6.3
  Contestant 2: knowledge=0.150, recall=0.135, confidence=0.143, safe_candidates=35.6, risky_candidates=90.3, blind_candidates=8.3
  Contestant 3: knowledge=0.122, recall=0.109, confidence=0.102, safe_candidates=11.8, risky_candidates=69.6, blind_candidates=30.2
Player mode rates:
  Contestant 1: safe=0.503, risky=0.061, blind=0.004, victory_lap=0.423
  Contestant 2: safe=0.738, risky=0.116, blind=0.028, victory_lap=0.115
  Contestant 3: safe=0.768, risky=0.232, blind=0.000, victory_lap=0.000
Player mode hit rates:
  Contestant 1: safe=0.978, risky=0.838, blind=0.056, desperation=0.172
  Contestant 2: safe=0.945, risky=0.817, blind=0.056, desperation=0.197
  Contestant 3: safe=0.837, risky=0.757, blind=0.000, desperation=0.133
Player avg guess values:
  Contestant 1: safe=36.9, risky=86.0, blind=92.5
  Contestant 2: safe=37.0, risky=85.6, blind=91.7
  Contestant 3: safe=24.8, risky=70.6, blind=90.7
Early guess profile:
  Contestant 1: top_15=0.000, mid_16_69=0.603, high_70_89=0.229, deep_90_100=0.168, early_strike=0.072
  Contestant 2: top_15=0.000, mid_16_69=0.151, high_70_89=0.589, deep_90_100=0.261, early_strike=0.197
  Contestant 3: top_15=0.129, mid_16_69=0.523, high_70_89=0.337, deep_90_100=0.011, early_strike=0.102

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.608, avg_score=1911.3, avg_median_score=1970.5, avg_stdev=323.9, avg_strikes=2.23, avg_first_out_rate=0.037
Contestant 2: avg_win_rate=0.208, avg_score=1512.7, avg_median_score=1480.5, avg_stdev=228.4, avg_strikes=2.58, avg_first_out_rate=0.282
Contestant 3: avg_win_rate=0.184, avg_score=1243.7, avg_median_score=1229.1, avg_stdev=202.0, avg_strikes=2.16, avg_first_out_rate=0.410
Last survivor but lost rate: 0.137
Solo started behind rate: 0.263
Solo started behind and lost rate: 0.480
Avg solo start deficit: 152.8
Avg solo turns taken: 6.48
Solo had winning answer rate: 0.100
Solo had winning answer given started behind rate: 0.436
Solo start deficit buckets: 1-75: 0.439, 76-150: 0.231, 151-250: 0.140, 251+: 0.190
Avg final board read: -0.035
Avg absolute final board read: 0.090
Avg strong harsh board rate: 0.141
Avg strong generous board rate: 0.041
Avg final cutoff estimate: 61.74
Avg final cutoff uncertainty: 0.365
Avg low uncertainty rate: 0.134
Avg high cutoff rate: 0.362
Avg final safe floor: 49.55
Avg final local density read: 0.065
Avg final surprise read: 0.179
Avg final near-cutoff hits: 2.42
Avg final near-cutoff misses: 0.03
Mode rates: safe=0.610, risky=0.305, blind_risk=0.011, chip_away=0.000, exact_win=0.001, comeback=0.000, high_upside=0.000, desperation=0.002, victory_lap=0.070
Double window mode rates: safe=0.637, risky=0.363, blind_risk=0.000
Context rates: open=0.692, dense=0.433, generous=0.291, dense_and_generous=0.032, tight=0.124, uncertain=0.464, 
Context-action rates: risky_on_open=0.308, risky_on_dense=0.436, risky_on_generous=0.097, risky_on_dense_and_generous=0.122, safe_on_tight=0.917, risky_on_uncertain=0.325, safe_on_uncertain=0.641, risky_on_double_window=0.363, safe_on_double_window=0.637
Aggregate answer-state summary:
Contestant 1: knowledge=0.233, recall=0.212, confidence=0.229, safe_candidates=77.6, risky_candidates=97.4 
Contestant 2: knowledge=0.226, recall=0.216, confidence=0.252, safe_candidates=73.5, risky_candidates=96.4 
Contestant 3: knowledge=0.186, recall=0.178, confidence=0.203, safe_candidates=57.7, risky_candidates=89.3 
```

**Notes:**

Changing C2's old blunt `war: 0.78` profile to a nuanced WAR profile and adding modern/recent/counting/hitter-WAR confidence/familiarity boosts was a step in the right direction:
```
category_modifiers={
  "war": 0.98,
  "hitter_war": 1.02,
  "pitcher_war": 0.90,
  "career_war": 0.97,
}
```
- The expanded category suite is more informative than the original five-category suite.
- The old broad WAR penalty was too blunt.
- Hitter WAR and pitcher WAR behave meaningfully differently.
- ERA+ functions as a closed calibration stress test.
- Modern/open counting categories produce healthier competition.
- Stolen Bases since 2000 is a good addition and behaves like a moderately open archetype-heavy category.

**Takeaway:**

1. All-Time bWAR is no longer completely broken

All-Time bWAR:
| Contestant | Run 2.3 | Run 3
| - | - | -
| C1 | 0.982 | 0.843
| C2 | 0.005 | 0.110
| C3 | 0.013 | 0.047

It is still C1-dominant, as it should be, but it no longer shows "C2 has no chance". This is further explained by the metrics:

bWAR safe candidates:
| Contestant | Run 2.3 | Run 3
| C1 | 69.7 | 69.7
| C2 | 25.0 | 56.3
| C3 | 32.1 | 36.0

This is a huge improvement as C2's broad WAR penalty was suppressing him too hard, and Run 3 comfirms that by replacing it with subtype tags was the right direction

2. Hitter WAR vs Pitcher WAR split is working

| Contestant | Hitter bWAR Win Rate | Hitter bWAR safe candidates | Pitcher bWAR Win Rate | Pitcher bWAR safe candidates
| - | - | - | - | -
| C1 | 0.543 | 78.8 | 0.872 | 60.8
| C2 | 0.237 | 81.5 | 0.068 | 39.9
| C3 | 0.220 | 57.6 | 0.060 | 36.7

Overall results:
- C2 is genuinely competitive in hitter WAR
  - has even more safe candidates than the other contestants and a higher confidence than C1
  - C1 still wins more because of turn structure, safer baseline, less early volatility, and probably stronger scoring/survival instincts
- Hitter vs Pitcher discrepancy preserves the notion that "pitcher WAR is harder/calibration heavy"
  - C2 is not dead like old all-time bWAR, but is still clearly weaker here
    - This is still much better than the old broad `war: 0.78`

Thus, the WAR subtype system works.

3. ERA+ is behaving like a closed calibration stress test

All-Time ERA+:
| Contestant | Win Rate | safe candidates
| - | - | -
| C1 | 0.806 | 49.8
| C2 | 0.189 | 39.6
| C3 | 0.005 | 16.8

Other metrics:
- tight=0.195
- uncertain=0.764
- safe rate=0.656
- risky rate=0.119

The board is closed, uncertain, and unforgiving
- C3 basically has no safe board
- C2 is competitive but still clearly disadvantaged
- C1 still dominates, but not in the same way as old bWAR
- Adding `pitcher_calibration` to ERA+ was a good idea
  - It gives ERA+ overlap with pitcher-stat intuition, while `closed_calibration` still captures the extreme unforgiving board feel

4. Open modern categories are in a very good spot

Pitcher Strikeouts since 2010
| Contestant | Win Rate | safe candidates
| - | - | -
| C1 | 0.423 | 95.3
| C2 | 0.296 | 97.4
| C3 | 0.281 | 89.6

Other metrics:
- safe=0.450
- risky=0.534
- open=0.748
- dense=0.575

This is a strong "in the group's wheelhouse" category
- C2 and C3 are competitive
- C1 is slightly ahead, and the mode/context metrics show an aggresive dense board

Home Runs since 2020
| Contestant | Win Rate | safe candidates
| - | - | -
| C1 | 0.400 | 97.4
| C2 | 0.278 | 98.7
| C3 | 0.322 | 92.2

Other metrics:
- safe=0.425
- risky=0.561
- open=0.750
- dense=0.578

One of the healthiest-looking categories in the whole suite
- C3 becomes genuinely competitive, which should fit his profile for him being dangerous in modern/open categories

Stole Bases since 2000
| Contestant | Win Rate | safe candidates
| - | - | -
| C1 | 0.402 | 89.4
| C2 | 0.246 | 91.9
| C3 | 0.352 | 77.7

Other metrics:
- safe=0.581
- risky=0.391
- open=0.736
- dense=0.536

It's not as easy/open as HR 2020 or pitcher strikeouts, but this still looks good
- It is clearly playable and archetype-heavy
- Difficulty `3.0` looks reasonable based on the output

5. Aggregate changed in healthy direction, but do not over read it

The aggregate is not comparable to Run 2.3 because Run 3 features more categories. However, comparing the new aggregate with the previous smaller-suite aggregate:

| Contestant | Run 2.3 Aggregate | Run 3 Aggregate
| - | - | -
| C1 | 0.661 | 0.608
| C2 | 0.189 | 0.208
| C3 | 0.150 | 0.184

This is a better shape
- C1 is still dominant, but less absurdly so
- C2 improves a bit
- C3 improves meaningfully because the expanded suite gives him more favorable/open categories

This is overall directionally closer to the real show, but does not force a match

6. C2 is improved, but still structurally 

C2's WAR adjustment worked, but C2 still has 2 recurring issues:
- Early volatility / deep shots:
  - C2's early guess profile is still extremely deep-shot heavy in many categories:
    - OPS+ deep_90_100: 0.837
    - Hitter bWAR deep_90_100: 0.842
    - HR 2020 deep_90_100: 0.932
    - Hits deep_90_100: 0.902
  - This means that his profile is producing huge early upside but also early strike exposure
    - He often has playable boards but gives away first-out equity
- C1 gets more victory-lap states:
  - In hard categories, C1's mode profile often has large victory-lap rates, meaning he reaches dominant endgame positions more often
  - C2's answer stats can be decent, but C1 survives and converts more consistently

The next C2 work probably should not be 'more knowledge', rather it should be behavior/profile tuning:
- less self-destructive volatility
- better conversion
- better pressure composure

7. C3 is still not quite right, but the suite now exposes why

C3 looks good in open modern categories:
- HR 2020: 0.322
- Stolen bases: 0.352
- Pitcher Strikeouts: 0.281
- Hits: 0.302

However, he remains completely dead in closed/historical calibration categories:
- ERA+: 0.005
- MVP: 0.001
- All-Time bWAR: 0.047

This isn't necessarily wrong, as the model captures some volatility, but mostly through C2's early deep-shot profile and C3's weaker answer pool in hard categories
- This does not yet model "C3 gets to two strikes early and then becomes dangerous"

**Conclusion:**

Run 3 expanded the validation suite and replaced C2's broad WAR penalty with subtype-specific WAR modifiers. This produced a much healthier category structure. All-Time bWAR remained C1-favored, but C2 was no longer effectively dead in the category. Hitter bWAR since 2000 became meaningfully competitive for C2, while Pitcher bWAR since 2000 remained much more C1-favored, matching the intended distinction between hitter WAR comfort and pitcher WAR calibration difficulty.

The new open modern categories also behaved well. Pitcher Strikeouts since 2010, Home Runs since 2020, and Stolen Bases since 2000 produced much more balanced win distributions and high dense/open context rates. ERA+ behaved as a closed calibration stress test, with high uncertainty and strong C1 advantage.

Overall, Run 3 suggests that the M5 identity system benefits significantly from a more specific category suite. The next step is not more category tuning, but measuring player behavior by strike state before adding two-strike identity logic.

**M5 Outcomes:**
fill out when complete

**Final aggregate M5 state:**
fill out when complete

**Key Observations:**
fill out when complete

---

## Milestone 6 - Calibration and Validation Pass

**Summary:**
fill out when complete

**Observed Progression:**
fill out when complete

**Key Insights:**
fill out when complete

### Run 1

**M6 Outcomes:**
fill out when complete

**Final aggregate M6 state:**
fill out when complete

**Key Observations:**
fill out when complete