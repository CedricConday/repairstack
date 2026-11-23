# RepairStack

Working name. Open tools aimed at one question: which already-approved drug has the best case for a myelin repair trial in multiple sclerosis, and how would that trial know it worked?

Started 2026-11-23. Nothing here is medical advice.

## The four parts

| Part | Folder | What it is | State on 2026-11-23 |
|---|---|---|---|
| RepairMap | `repairmap/` | Every repair trial in MS in one table: drug, mechanism, who was tested, what was measured, what happened, where it is written down. | Seed table, 29 rows, not yet checked a second time |
| RepairGauge | `repairgauge/` | An open MRI measure of repair, tested on images where the right answer is known. | Not started |
| RepairSplit | `repairsplit/` | Re-analysis of the small positive trials: who responded and who did not. | Not started |
| RepairCase | `repaircase/` | The written case for one candidate drug, built from the three parts above, for a clinic to read. | Not started |

Each part is useful alone. The order is map, gauge, split, case.

## RepairMap

```
python repairmap/build_seed.py   # writes repairmap/data/trials.csv
python repairmap/check.py        # checks the table, prints the counts
```

The seed rows come from one research pass on 2026-11-23. Sources were read then, mostly as abstracts, registry records and conference reports. The `second_check` column is "no" on every row until someone reads the source again and confirms the row.

Columns: `id`, `agent`, `trial`, `mechanism`, `phase`, `n`, `population`, `primary_outcome`, `outcome_class`, `result`, `effect`, `source`, `source_type`, `source_date`, `second_check`.

Known gaps in the seed: rHIgM22, phenytoin, repetitive TMS, temelimab, quetiapine, thyromimetics, other cell therapies, and the phase 1 company programmes. The biotin and domperidone rows cite a review, not the trial papers.
