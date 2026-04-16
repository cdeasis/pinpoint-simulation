# V2 Raw Results & Validation Logs

This document contains raw outputs and intermediate benchmark runs from Version 2

## Purpose:
- Preserve full validation outputs
- Show how results evolved across milestones
- Provide supporting evidence for conclusions in `simulation_v2.md`

Notes:
- Outputs are minimally edited
- Key takeways are summarized per section

---

## Summary of Progression


| Stage | Avg Solo Deficit | Solo Loss Rate | Winning Answer Rate |
| - | - | - | -| 
| M2 Final | ~190 | ~0.91 | ~0.06 |
| M3 Initial | ~190 | ~0.72 | ~0.06 |
| M3 Final | ~135 | ~0.60 | ~0.10 |
| M4 Final | ~93 | ~ 0.43 | ~0.14 |

---

## Milestone 2 - Baseline Behavior

Key Observations:
- Stable but overly deterministic system
- High solo failure rate (~0.90 when behind)
- Large variance reduction compared to earlier runs
- No Board awareness or adaptive behavior

### M2 Midway Run:

```
=== Summary ===
Contestant 1: win_rate=0.613, avg_score=1669.7, median_score=1463.5, stdev=990.4, avg_strikes=3.00, first_out_rate=0.162
Contestant 2: win_rate=0.211, avg_score=1057.0, median_score=838.0, stdev=771.9, avg_strikes=3.00, first_out_rate=0.426
Contestant 3: win_rate=0.176, avg_score=940.1, median_score=823.0, stdev=561.0, avg_strikes=3.00, first_out_rate=0.412
Last survivor but lost rate: 0.127
Solo started behind rate: 0.273
Solo started behind and lost rate: 0.464
```

### M2 Concluding Run: 

```
=== Summary ===
Contestant 1: win_rate=0.726, avg_score=1844.8, median_score=1859.0, stdev=235.4, avg_strikes=2.54, first_out_rate=0.071
Contestant 2: win_rate=0.163, avg_score=1581.6, median_score=1605.0, stdev=192.7, avg_strikes=2.80, first_out_rate=0.213
Contestant 3: win_rate=0.111, avg_score=1454.3, median_score=1450.0, stdev=217.1, avg_strikes=2.81, first_out_rate=0.667
Last survivor but lost rate: 0.289
Solo started behind rate: 0.315
Solo started behind and lost rate: 0.918
```

---

## Multi-Category Validation Suite (Initial)

Key Observations:
- Consistent dominance by Contestant 1 (~0.72 WR)
- Extremely high solo failure rate (~0.83)

Later Key Observations:
- Large solo deficits emerging (~170-190)
- Indicates upstream imbalance, not just solo logic issues

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

---

## Milestone 3 - Evolution Section (MOST IMPORTANT)

### Key Insight:
The primary issue was not solo decision-making quality. Instead it was that the game state entering solo was often unwinnable.

Evidence:
- Avg solo deficit $\approx$ 190
- Solo winning-answer availability $\approx$ 6%
- Avg solo turns $\approx$ 2-3

Interpretation:
- Players required 3–4 correct answers to win
- But only had 2–3 turns available

This means that most solo scenarios were structurally impossible

Conclusion:
Improving solo logic alone would not fix outcomes — upstream game dynamics had to change.

### M3 First Run Results:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.716, avg_score=1848.4, median_score=1865.0, stdev=236.7, avg_strikes=2.54, first_out_rate=0.068
Contestant 2: win_rate=0.184, avg_score=1580.0, median_score=1598.0, stdev=202.4, avg_strikes=2.80, first_out_rate=0.210
Contestant 3: win_rate=0.100, avg_score=1453.9, median_score=1451.0, stdev=216.2, avg_strikes=2.82, first_out_rate=0.671
Last survivor but lost rate: 0.265
Solo started behind rate: 0.333
Solo started behind and lost rate: 0.797

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.774, avg_score=1974.0, median_score=2129.0, stdev=534.9, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.090, avg_score=1180.4, median_score=1176.0, stdev=176.8, avg_strikes=3.00, first_out_rate=0.576
Contestant 3: win_rate=0.136, avg_score=1166.2, median_score=1140.0, stdev=230.5, avg_strikes=3.00, first_out_rate=0.422
Last survivor but lost rate: 0.222
Solo started behind rate: 0.347
Solo started behind and lost rate: 0.640

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.671, avg_score=1818.3, median_score=1766.0, stdev=160.1, avg_strikes=0.34, first_out_rate=0.000
Contestant 2: win_rate=0.282, avg_score=1622.5, median_score=1677.0, stdev=136.7, avg_strikes=1.64, first_out_rate=0.118
Contestant 3: win_rate=0.047, avg_score=1609.2, median_score=1652.0, stdev=165.2, avg_strikes=0.75, first_out_rate=0.157
Last survivor but lost rate: 0.001
Solo started behind rate: 0.001
Solo started behind and lost rate: 0.750

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.744, avg_score=1861.4, median_score=1850.0, stdev=203.7, avg_strikes=1.06, first_out_rate=0.030
Contestant 2: win_rate=0.158, avg_score=1584.0, median_score=1637.0, stdev=176.1, avg_strikes=2.15, first_out_rate=0.225
Contestant 3: win_rate=0.098, avg_score=1577.5, median_score=1619.0, stdev=197.7, avg_strikes=1.84, first_out_rate=0.417
Last survivor but lost rate: 0.090
Solo started behind rate: 0.109
Solo started behind and lost rate: 0.831

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.664, avg_score=1704.4, median_score=1707.0, stdev=454.6, avg_strikes=3.00, first_out_rate=0.019
Contestant 2: win_rate=0.298, avg_score=1429.7, median_score=1295.0, stdev=411.1, avg_strikes=3.00, first_out_rate=0.030
Contestant 3: win_rate=0.038, avg_score=902.1, median_score=874.0, stdev=233.8, avg_strikes=3.00, first_out_rate=0.951
Last survivor but lost rate: 0.241
Solo started behind rate: 0.404
Solo started behind and lost rate: 0.597

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.714, avg_score=1841.3, avg_median_score=1863.4, avg_stdev=318.0, avg_strikes=1.99, avg_first_out_rate=0.024
Contestant 2: avg_win_rate=0.202, avg_score=1479.3, avg_median_score=1476.6, avg_stdev=220.6, avg_strikes=2.52, avg_first_out_rate=0.232
Contestant 3: avg_win_rate=0.084, avg_score=1341.8, avg_median_score=1347.2, avg_stdev=208.7, avg_strikes=2.28, avg_first_out_rate=0.524
Last survivor but lost rate: 0.164
Solo started behind rate: 0.239
Solo started behind and lost rate: 0.723
```

### M3 First Run With Solo Metrics:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.717, avg_score=1842.1, median_score=1856.0, stdev=238.5, avg_strikes=2.54, first_out_rate=0.065
Contestant 2: win_rate=0.178, avg_score=1567.4, median_score=1594.0, stdev=188.1, avg_strikes=2.80, first_out_rate=0.214
Contestant 3: win_rate=0.105, avg_score=1453.0, median_score=1450.5, stdev=219.6, avg_strikes=2.82, first_out_rate=0.671
Last survivor but lost rate: 0.257
Solo started behind rate: 0.324
Solo started behind and lost rate: 0.792
Avg solo start deficit: 203.6
Avg solo turns taken: 1.62
Solo had winning answer rate: 0.060

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.770, avg_score=1959.6, median_score=2124.0, stdev=540.2, avg_strikes=3.00, first_out_rate=0.002
Contestant 2: win_rate=0.091, avg_score=1180.4, median_score=1177.0, stdev=175.4, avg_strikes=3.00, first_out_rate=0.579
Contestant 3: win_rate=0.139, avg_score=1166.4, median_score=1143.0, stdev=230.4, avg_strikes=3.00, first_out_rate=0.419
Last survivor but lost rate: 0.228
Solo started behind rate: 0.348
Solo started behind and lost rate: 0.654
Avg solo start deficit: 184.4
Avg solo turns taken: 5.35
Solo had winning answer rate: 0.102

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.679, avg_score=1820.1, median_score=1769.0, stdev=159.2, avg_strikes=0.33, first_out_rate=0.000
Contestant 2: win_rate=0.271, avg_score=1617.1, median_score=1672.0, stdev=140.0, avg_strikes=1.66, first_out_rate=0.122
Contestant 3: win_rate=0.049, avg_score=1612.7, median_score=1654.0, stdev=164.9, avg_strikes=0.74, first_out_rate=0.155
Last survivor but lost rate: 0.001
Solo started behind rate: 0.002
Solo started behind and lost rate: 0.688
Avg solo start deficit: 188.9
Avg solo turns taken: 1.94
Solo had winning answer rate: 0.001

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.740, avg_score=1856.7, median_score=1847.0, stdev=203.5, avg_strikes=1.06, first_out_rate=0.031
Contestant 2: win_rate=0.162, avg_score=1582.9, median_score=1641.0, stdev=172.5, avg_strikes=2.15, first_out_rate=0.228
Contestant 3: win_rate=0.098, avg_score=1579.6, median_score=1622.0, stdev=197.4, avg_strikes=1.82, first_out_rate=0.411
Last survivor but lost rate: 0.092
Solo started behind rate: 0.113
Solo started behind and lost rate: 0.815
Avg solo start deficit: 192.2
Avg solo turns taken: 1.65
Solo had winning answer rate: 0.019

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.664, avg_score=1645.2, median_score=1542.0, stdev=451.3, avg_strikes=3.00, first_out_rate=0.018
Contestant 2: win_rate=0.296, avg_score=1361.1, median_score=1278.0, stdev=355.3, avg_strikes=3.00, first_out_rate=0.028
Contestant 3: win_rate=0.040, avg_score=901.4, median_score=875.0, stdev=231.3, avg_strikes=3.00, first_out_rate=0.954
Last survivor but lost rate: 0.239
Solo started behind rate: 0.393
Solo started behind and lost rate: 0.608
Avg solo start deficit: 181.9
Avg solo turns taken: 3.38
Solo had winning answer rate: 0.134

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.714, avg_score=1824.8, avg_median_score=1827.6, avg_stdev=318.5, avg_strikes=1.99, avg_first_out_rate=0.023
Contestant 2: avg_win_rate=0.200, avg_score=1461.8, avg_median_score=1472.4, avg_stdev=206.2, avg_strikes=2.52, avg_first_out_rate=0.234
Contestant 3: avg_win_rate=0.086, avg_score=1342.6, avg_median_score=1348.9, avg_stdev=208.7, avg_strikes=2.28, avg_first_out_rate=0.522
Last survivor but lost rate: 0.163
Solo started behind rate: 0.236
Solo started behind and lost rate: 0.711
Avg solo start deficit: 190.2
Avg solo turns taken: 2.79
Solo had winning answer rate: 0.063
```

### M3 Bucketed Checkpoint Run:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.672, avg_score=1846.4, median_score=1805.0, stdev=308.4, avg_strikes=2.95, first_out_rate=0.069
Contestant 2: win_rate=0.254, avg_score=1595.2, median_score=1584.0, stdev=263.1, avg_strikes=2.97, first_out_rate=0.199
Contestant 3: win_rate=0.074, avg_score=1335.6, median_score=1338.0, stdev=248.6, avg_strikes=2.97, first_out_rate=0.727
Last survivor but lost rate: 0.148
Solo started behind rate: 0.291
Solo started behind and lost rate: 0.510
Avg solo start deficit: 123.9
Avg solo turns taken: 2.98
Solo had winning answer rate: 0.123
Solo had winning answer given started behind rate: 0.424
Solo start deficit buckets: 1-75: 0.398, 76-150: 0.307, 151-250: 0.182, 251+: 0.113

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.776, avg_score=2222.5, median_score=2499.0, stdev=822.9, avg_strikes=3.00, first_out_rate=0.000
Contestant 2: win_rate=0.083, avg_score=896.1, median_score=887.0, stdev=200.6, avg_strikes=3.00, first_out_rate=0.795
Contestant 3: win_rate=0.141, avg_score=958.7, median_score=937.0, stdev=251.3, avg_strikes=3.00, first_out_rate=0.205
Last survivor but lost rate: 0.220
Solo started behind rate: 0.379
Solo started behind and lost rate: 0.581
Avg solo start deficit: 169.6
Avg solo turns taken: 11.22
Solo had winning answer rate: 0.134
Solo had winning answer given started behind rate: 0.353
Solo start deficit buckets: 1-75: 0.273, 76-150: 0.238, 151-250: 0.245, 251+: 0.244

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.727, avg_score=1789.2, median_score=1766.0, stdev=111.0, avg_strikes=0.93, first_out_rate=0.002
Contestant 2: win_rate=0.222, avg_score=1631.1, median_score=1668.0, stdev=143.6, avg_strikes=2.04, first_out_rate=0.340
Contestant 3: win_rate=0.051, avg_score=1621.6, median_score=1635.0, stdev=135.0, avg_strikes=1.10, first_out_rate=0.173
Last survivor but lost rate: 0.054
Solo started behind rate: 0.068
Solo started behind and lost rate: 0.798
Avg solo start deficit: 139.4
Avg solo turns taken: 1.54
Solo had winning answer rate: 0.012
Solo had winning answer given started behind rate: 0.182
Solo start deficit buckets: 1-75: 0.142, 76-150: 0.442, 151-250: 0.366, 251+: 0.050

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.713, avg_score=1817.0, median_score=1787.0, stdev=196.6, avg_strikes=2.34, first_out_rate=0.089
Contestant 2: win_rate=0.160, avg_score=1594.1, median_score=1633.0, stdev=192.2, avg_strikes=2.70, first_out_rate=0.412
Contestant 3: win_rate=0.127, avg_score=1556.8, median_score=1590.0, stdev=198.7, avg_strikes=2.47, first_out_rate=0.394
Last survivor but lost rate: 0.192
Solo started behind rate: 0.268
Solo started behind and lost rate: 0.717
Avg solo start deficit: 130.1
Avg solo turns taken: 1.83
Solo had winning answer rate: 0.062
Solo had winning answer given started behind rate: 0.233
Solo start deficit buckets: 1-75: 0.289, 76-150: 0.355, 151-250: 0.256, 251+: 0.100

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.623, avg_score=1787.7, median_score=2041.5, stdev=788.2, avg_strikes=3.00, first_out_rate=0.016
Contestant 2: win_rate=0.361, avg_score=1410.6, median_score=1078.0, stdev=712.6, avg_strikes=3.00, first_out_rate=0.038
Contestant 3: win_rate=0.016, avg_score=651.3, median_score=623.0, stdev=233.0, avg_strikes=3.00, first_out_rate=0.946
Last survivor but lost rate: 0.147
Solo started behind rate: 0.357
Solo started behind and lost rate: 0.412
Avg solo start deficit: 115.6
Avg solo turns taken: 15.42
Solo had winning answer rate: 0.187
Solo had winning answer given started behind rate: 0.525
Solo start deficit buckets: 1-75: 0.437, 76-150: 0.282, 151-250: 0.177, 251+: 0.105

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.702, avg_score=1892.6, avg_median_score=1979.7, avg_stdev=445.4, avg_strikes=2.44, avg_first_out_rate=0.035
Contestant 2: avg_win_rate=0.216, avg_score=1425.4, avg_median_score=1370.0, avg_stdev=302.4, avg_strikes=2.74, avg_first_out_rate=0.357
Contestant 3: avg_win_rate=0.082, avg_score=1224.8, avg_median_score=1224.6, avg_stdev=213.3, avg_strikes=2.51, avg_first_out_rate=0.489
Last survivor but lost rate: 0.152
Solo started behind rate: 0.273
Solo started behind and lost rate: 0.604
Avg solo start deficit: 135.7
Avg solo turns taken: 6.60
Solo had winning answer rate: 0.104
Solo had winning answer given started behind rate: 0.343
Solo start deficit buckets: 1-75: 0.308, 76-150: 0.325, 151-250: 0.245, 251+: 0.122
```

### Milestone 3 Outcomes

- Reduced solo deficits (~190 → ~135)
- Increased comeback viability
- Introduced structured solo decision modes
- Added diagnostic metrics (major improvement)

Important:
- Win rate imbalance remained largely unchanged
- Indicates solo improvements are localized, not global

---

## Milestone 4 - Board Inference & Adaptive Behavior

Key Additions:
- Board depth inference (harsh vs generous)
- Risk adjustment based on inferred board state
- Light table-reaction effects

Goal:
Players react to revealed information, not just internal state

### M4 Run 1:

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.669, avg_score=1844.9, median_score=1798.0, stdev=299.1, avg_strikes=2.95, first_out_rate=0.070
Contestant 2: win_rate=0.263, avg_score=1616.4, median_score=1593.0, stdev=259.2, avg_strikes=2.97, first_out_rate=0.193
Contestant 3: win_rate=0.069, avg_score=1322.3, median_score=1314.0, stdev=240.3, avg_strikes=2.97, first_out_rate=0.732
Last survivor but lost rate: 0.117
Solo started behind rate: 0.256
Solo started behind and lost rate: 0.457
Avg solo start deficit: 100.8
Avg solo turns taken: 3.22
Solo had winning answer rate: 0.124
Solo had winning answer given started behind rate: 0.486
Solo start deficit buckets: 1-75: 0.501, 76-150: 0.278, 151-250: 0.145, 251+: 0.076
Avg final board read: 0.844
Avg absolute final board read: 0.282
Strong harsh board rate: 0.000
Strong generous board rate: 0.978

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.808, avg_score=2312.7, median_score=2573.0, stdev=797.3, avg_strikes=3.00, first_out_rate=0.000
Contestant 2: win_rate=0.079, avg_score=874.7, median_score=862.0, stdev=202.3, avg_strikes=3.00, first_out_rate=0.821
Contestant 3: win_rate=0.113, avg_score=939.1, median_score=914.0, stdev=247.9, avg_strikes=3.00, first_out_rate=0.179
Last survivor but lost rate: 0.185
Solo started behind rate: 0.388
Solo started behind and lost rate: 0.478
Avg solo start deficit: 130.5
Avg solo turns taken: 14.62
Solo had winning answer rate: 0.172
Solo had winning answer given started behind rate: 0.444
Solo start deficit buckets: 1-75: 0.356, 76-150: 0.273, 151-250: 0.247, 251+: 0.124
Avg final board read: 0.769
Avg absolute final board read: 0.258
Strong harsh board rate: 0.001
Strong generous board rate: 0.896

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.684, avg_score=1782.4, median_score=1763.0, stdev=107.7, avg_strikes=0.90, first_out_rate=0.001
Contestant 2: win_rate=0.258, avg_score=1637.0, median_score=1675.0, stdev=145.4, avg_strikes=2.02, first_out_rate=0.333
Contestant 3: win_rate=0.058, avg_score=1622.8, median_score=1635.0, stdev=130.9, avg_strikes=1.07, first_out_rate=0.167
Last survivor but lost rate: 0.046
Solo started behind rate: 0.062
Solo started behind and lost rate: 0.746
Avg solo start deficit: 128.7
Avg solo turns taken: 1.55
Solo had winning answer rate: 0.015
Solo had winning answer given started behind rate: 0.243
Solo start deficit buckets: 1-75: 0.199, 76-150: 0.444, 151-250: 0.320, 251+: 0.037
Avg final board read: 0.846
Avg absolute final board read: 0.282
Strong harsh board rate: 0.000
Strong generous board rate: 0.985

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.690, avg_score=1811.4, median_score=1782.0, stdev=188.6, avg_strikes=2.31, first_out_rate=0.088
Contestant 2: win_rate=0.183, avg_score=1605.4, median_score=1638.0, stdev=186.1, avg_strikes=2.68, first_out_rate=0.406
Contestant 3: win_rate=0.127, avg_score=1552.8, median_score=1585.0, stdev=191.4, avg_strikes=2.46, first_out_rate=0.394
Last survivor but lost rate: 0.167
Solo started behind rate: 0.247
Solo started behind and lost rate: 0.676
Avg solo start deficit: 118.6
Avg solo turns taken: 1.89
Solo had winning answer rate: 0.069
Solo had winning answer given started behind rate: 0.281
Solo start deficit buckets: 1-75: 0.344, 76-150: 0.345, 151-250: 0.226, 251+: 0.085
Avg final board read: 0.817
Avg absolute final board read: 0.273
Strong harsh board rate: 0.000
Strong generous board rate: 0.974

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.618, avg_score=1833.3, median_score=2151.5, stdev=810.5, avg_strikes=3.00, first_out_rate=0.014
Contestant 2: win_rate=0.369, avg_score=1429.3, median_score=1069.0, stdev=736.6, avg_strikes=3.00, first_out_rate=0.040
Contestant 3: win_rate=0.013, avg_score=622.0, median_score=592.0, stdev=231.4, avg_strikes=3.00, first_out_rate=0.947
Last survivor but lost rate: 0.112
Solo started behind rate: 0.341
Solo started behind and lost rate: 0.328
Avg solo start deficit: 96.9
Avg solo turns taken: 18.23
Solo had winning answer rate: 0.204
Solo had winning answer given started behind rate: 0.598
Solo start deficit buckets: 1-75: 0.492, 76-150: 0.296, 151-250: 0.156, 251+: 0.056
Avg final board read: 0.538
Avg absolute final board read: 0.199
Strong harsh board rate: 0.019
Strong generous board rate: 0.699

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.694, avg_score=1916.9, avg_median_score=2013.5, avg_stdev=440.6, avg_strikes=2.43, avg_first_out_rate=0.035
Contestant 2: avg_win_rate=0.230, avg_score=1432.6, avg_median_score=1367.4, avg_stdev=305.9, avg_strikes=2.73, avg_first_out_rate=0.358
Contestant 3: avg_win_rate=0.076, avg_score=1211.8, avg_median_score=1208.0, avg_stdev=208.4, avg_strikes=2.50, avg_first_out_rate=0.484
Last survivor but lost rate: 0.126
Solo started behind rate: 0.259
Solo started behind and lost rate: 0.537
Avg solo start deficit: 115.1
Avg solo turns taken: 7.90
Solo had winning answer rate: 0.117
Solo had winning answer given started behind rate: 0.410
Solo start deficit buckets: 1-75: 0.379, 76-150: 0.327, 151-250: 0.219, 251+: 0.075
Avg final board read: 0.763
Avg absolute final board read: 0.259
Avg strong harsh board rate: 0.004
```

### M4 Final (Final V2 Run):

```
=== Category: All-Time OPS+ ===
Contestant 1: win_rate=0.665, avg_score=1844.9, median_score=1789.0, stdev=301.9, avg_strikes=2.97, first_out_rate=0.045
Contestant 2: win_rate=0.285, avg_score=1649.7, median_score=1600.0, stdev=250.4, avg_strikes=2.98, first_out_rate=0.178
Contestant 3: win_rate=0.050, avg_score=1283.7, median_score=1287.0, stdev=216.9, avg_strikes=2.98, first_out_rate=0.772
Last survivor but lost rate: 0.066
Solo started behind rate: 0.208
Solo started behind and lost rate: 0.315
Avg solo start deficit: 65.4
Avg solo turns taken: 3.83
Solo had winning answer rate: 0.133
Solo had winning answer given started behind rate: 0.640
Solo start deficit buckets: 1-75: 0.652, 76-150: 0.260, 151-250: 0.082, 251+: 0.005
Avg final board read: 0.256
Avg absolute final board read: 0.257
Strong harsh board rate: 0.000
Strong generous board rate: 0.908

=== Category: All-Time bWAR ===
Contestant 1: win_rate=0.871, avg_score=2543.2, median_score=2752.0, stdev=752.3, avg_strikes=3.00, first_out_rate=0.000
Contestant 2: win_rate=0.071, avg_score=812.0, median_score=811.0, stdev=165.4, avg_strikes=3.00, first_out_rate=0.843
Contestant 3: win_rate=0.059, avg_score=837.6, median_score=831.0, stdev=190.7, avg_strikes=3.00, first_out_rate=0.157
Last survivor but lost rate: 0.124
Solo started behind rate: 0.469
Solo started behind and lost rate: 0.265
Avg solo start deficit: 102.8
Avg solo turns taken: 23.01
Solo had winning answer rate: 0.264
Solo had winning answer given started behind rate: 0.562
Solo start deficit buckets: 1-75: 0.463, 76-150: 0.286, 151-250: 0.192, 251+: 0.059
Avg final board read: 0.007
Avg absolute final board read: 0.131
Strong harsh board rate: 0.138
Strong generous board rate: 0.237

=== Category: Home Runs since 2000 ===
Contestant 1: win_rate=0.623, avg_score=1752.6, median_score=1739.0, stdev=100.0, avg_strikes=0.86, first_out_rate=0.001
Contestant 2: win_rate=0.293, avg_score=1671.0, median_score=1676.0, stdev=91.7, avg_strikes=1.96, first_out_rate=0.285
Contestant 3: win_rate=0.084, avg_score=1617.6, median_score=1639.0, stdev=105.8, avg_strikes=1.18, first_out_rate=0.168
Last survivor but lost rate: 0.051
Solo started behind rate: 0.068
Solo started behind and lost rate: 0.756
Avg solo start deficit: 114.9
Avg solo turns taken: 1.45
Solo had winning answer rate: 0.016
Solo had winning answer given started behind rate: 0.235
Solo start deficit buckets: 1-75: 0.206, 76-150: 0.537, 151-250: 0.247, 251+: 0.010
Avg final board read: 0.278
Avg absolute final board read: 0.278
Strong harsh board rate: 0.000
Strong generous board rate: 0.985

=== Category: Hits since 1900 ===
Contestant 1: win_rate=0.692, avg_score=1798.8, median_score=1759.0, stdev=180.7, avg_strikes=2.39, first_out_rate=0.063
Contestant 2: win_rate=0.209, avg_score=1649.4, median_score=1644.0, stdev=136.1, avg_strikes=2.70, first_out_rate=0.379
Contestant 3: win_rate=0.099, avg_score=1515.5, median_score=1558.0, stdev=166.9, avg_strikes=2.58, first_out_rate=0.439
Last survivor but lost rate: 0.134
Solo started behind rate: 0.213
Solo started behind and lost rate: 0.628
Avg solo start deficit: 96.2
Avg solo turns taken: 1.84
Solo had winning answer rate: 0.072
Solo had winning answer given started behind rate: 0.337
Solo start deficit buckets: 1-75: 0.398, 76-150: 0.390, 151-250: 0.203, 251+: 0.008
Avg final board read: 0.263
Avg absolute final board read: 0.263
Strong harsh board rate: 0.000
Strong generous board rate: 0.951

=== Category: Every MVP Winner ===
Contestant 1: win_rate=0.596, avg_score=1888.9, median_score=2362.0, stdev=900.9, avg_strikes=3.00, first_out_rate=0.004
Contestant 2: win_rate=0.402, avg_score=1494.0, median_score=1024.0, stdev=827.2, avg_strikes=3.00, first_out_rate=0.014
Contestant 3: win_rate=0.002, avg_score=486.0, median_score=472.0, stdev=143.7, avg_strikes=3.00, first_out_rate=0.983
Last survivor but lost rate: 0.079
Solo started behind rate: 0.365
Solo started behind and lost rate: 0.216
Avg solo start deficit: 86.8
Avg solo turns taken: 23.88
Solo had winning answer rate: 0.234
Solo had winning answer given started behind rate: 0.640
Solo start deficit buckets: 1-75: 0.525, 76-150: 0.303, 151-250: 0.145, 251+: 0.028
Avg final board read: -0.082
Avg absolute final board read: 0.128
Strong harsh board rate: 0.333
Strong generous board rate: 0.052

 === Aggregate Summary Across Validation Suite ===
Contestant 1: avg_win_rate=0.689, avg_score=1965.6, avg_median_score=2080.2, avg_stdev=447.2, avg_strikes=2.44, avg_first_out_rate=0.023
Contestant 2: avg_win_rate=0.252, avg_score=1455.2, avg_median_score=1351.0, avg_stdev=294.2, avg_strikes=2.73, avg_first_out_rate=0.340
Contestant 3: avg_win_rate=0.059, avg_score=1148.1, avg_median_score=1157.4, avg_stdev=164.8, avg_strikes=2.55, avg_first_out_rate=0.504
Last survivor but lost rate: 0.091
Solo started behind rate: 0.265
Solo started behind and lost rate: 0.436
Avg solo start deficit: 93.2
Avg solo turns taken: 10.80
Solo had winning answer rate: 0.144
Solo had winning answer given started behind rate: 0.483
Solo start deficit buckets: 1-75: 0.449, 76-150: 0.355, 151-250: 0.174, 251+: 0.022
Avg final board read: 0.144
Avg absolute final board read: 0.211
Avg strong harsh board rate: 0.094
Avg strong generous board rate: 0.627
Avg strong generous board rate: 0.907
```

### Milestone 4 Outcomes

- Further reduced solo deficits (~135 → ~93)
- Increased winning-answer availability (~10% → ~14%)
- Improved solo win rate (~0.60 → ~0.43 loss rate)

- Board inference introduced measurable behavioral shifts
- Players became more adaptive to category conditions

Remaining Issues:
- Some categories still produce extreme dominance
- Board read skew (often overly "generous")
- Opponent modeling still absent