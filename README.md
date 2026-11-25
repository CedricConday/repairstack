# RepairStack

Working name. Four open tools aimed at one question: which already-approved drug has the best case for a myelin repair trial in multiple sclerosis, and how would that trial know it worked?

Started 2026-11-23. Nothing here is medical advice.

## Why

Several drugs slow multiple sclerosis. None has been shown to repair the damage. As of November 2026 no drug has a repeated, clinically meaningful repair result in people, and trial groups say the first obstacle is that there is no agreed way to measure repair. These tools work on that obstacle first and on the choice of drug second.

## The four parts

| Part | Repo | What it is |
|---|---|---|
| RepairMap | [repairmap](https://github.com/CedricConday/repairmap) | Every repair trial in MS in one checked table: drug, mechanism, who was tested, what was measured, what happened, where it is written down. |
| RepairGauge | [repairgauge](https://github.com/CedricConday/repairgauge) | Measures, lesion by lesion, whether a myelin-sensitive MRI value recovered between two scans, and is tested on images where the right answer is known. |
| RepairSplit | [repairsplit](https://github.com/CedricConday/repairsplit) | Asks whether some trial participants responded and others did not, and shows what trials of a given size can detect. |
| RepairCase | [repaircase](https://github.com/CedricConday/repaircase) | Scores each approved drug against a rubric fixed in advance and writes the case for the top one. |

Each part is useful alone. They feed each other in the order map, gauge, split, case.

## Where it stands on 2026-11-25

| Part | Version | Result |
|---|---|---|
| RepairMap | v0.1.0 | 64 trials of 39 agents; 63 rows checked against their source, most against the abstract only. On a biomarker main outcome: 4 positive, 1 mixed, 8 negative. On a functional main outcome: 1 positive, 1 mixed, 9 negative. |
| RepairSplit | v0.1.0 | In simulation, none of the three published positive trial designs can tell "some people responded" from "everyone shifted a little": 5 to 36 percent power for an even split at the reported effect. Not yet run on patient data, which is available on request only. |
| RepairCase | v0.1.0 | No approved drug reaches the bar of 4 of 7 points set in advance. Best available: metformin plus clemastine at 3 points, not cleared. |
| RepairGauge | v0.1.0 | On planted recovery in same-day healthy MTR scans (MIRROR, four held-out subjects): 95 percent of fully recovered lesions called repaired, no false "repaired" among judged lesions. ihMTR is too noisy to judge 9 lesions in 10. A one-voxel misalignment between visits gives 35 percent false repair calls on the phantom. No patient data yet. |

Each repo's README has the detail and the limits.

## Scope

Drugs that are already approved for another use, tested for a new one. Designing new molecules is out of scope.

## Related work

`docs/oss_survey_2026-11-23.md` lists the open software and data that already exist for the first three parts, and the gap each part fills.
