# Canon 13.0 ledger report
Generated: 2026-08-29

## Ledger size
| table | rows |
|---|---|
| claims | 19 |
| vintages | 3 |
| rules | 3 |
| sources | 13 |
| calculations | 6 |
| conlog | 6 |
| tests | 0 |
| characters | 12 |
| corpusmap | 126 |

## Claim status
| status | count |
|---|---|
| FACT—VERIFIED | 10 |
| FACT—VINTAGE-SENSITIVE | 1 |
| NOT YET VALIDATED | 2 |
| UNREVIEWED | 6 |

## Engine detections
- VALUE collisions: 2
  - canon_band_45_59_action (CLM-0004, CLM-0005)
  - canon_hemisphere2_max_points (CLM-0001, CLM-0014, CLM-0015, CLM-0016)
- RULE collisions (open): 1
  - RUL-0001 <-> RUL-0003
- TEMPORAL due (as-of before 2026-08-29): 1
  - CLM-0007 (as_of 2026-08-25)

## Contradiction log (conlog)
| id | type | status | description |
|---|---|---|---|
| CON-0001 | A | open | Hemisphere 2 denominator printed as 40 in three case studies vs canonical 60 |
| CON-0002 | B | open | ch-64 '55-69 Adequate - investable' vs ch-66 '45-59 no fresh capital' - overlap 55-59 |
| CON-0003 | C | open | Credit-cycle 6-18 month lead asserted without test (ch-0-1) |
| CON-0004 | D | open | Chilime 62/100 pre-flood; rescore pending |
| CON-0005 | B | open | Two band systems for one 0-100 score: ch-64 bands vs ch-66 screening tiers |
| CON-0006 | A | open | Book self-describes as 118 chapters; TOC has 121 chapter pages |

## Duplicate-quantity hotspots (top 10 by occurrences)
| qkey | occurrences |
|---|---|
| canon_hemisphere2_max_points | 20 |
| canon_band_45_59_action | 8 |
| credit_to_nepse_lead_lag | 7 |
| canon_band_55_69 | 6 |
| canon_weight_vector_v1 | 5 |
| canon_hemisphere1_max_points | 3 |
| canon_score_chilime | 3 |
| nrb_bank_roe_q3_fy2425 | 3 |
| canon_band_vocabulary | 3 |
| canon_score_max | 3 |

## Corpus crawl state
- pages fetched: 126 / 126

## Unreviewed candidates
- 6 claim row(s) still UNREVIEWED (triage pending, 03)
