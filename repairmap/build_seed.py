"""Write the seed trial table for RepairMap.

Every row was taken from one research pass on 2026-11-23. The sources were
fetched then, mostly as abstracts, registry records and conference reports.
No row has been checked a second time, so `second_check` is "no" throughout.
Run: python repairmap/build_seed.py
"""

from __future__ import annotations

import csv
from pathlib import Path

OUT = Path(__file__).parent / "data" / "trials.csv"

FIELDS = [
    "id", "agent", "trial", "mechanism", "phase", "n", "population",
    "primary_outcome", "outcome_class", "result", "effect",
    "source", "source_type", "source_date", "second_check",
]

# outcome_class: biomarker | functional | safety | target_engagement
# result: positive | negative | mixed | harm | ongoing | not_started | stopped | safety_only
# source_type: paper | registry | conference | company | review
# n is the enrolled or planned number as reported; empty when not reported.
ROWS = [
    ("clemastine-rebuild", "clemastine", "ReBUILD", "M1 muscarinic antagonist", "2", "50",
     "relapsing MS, chronic optic neuropathy", "full-field VEP P100 latency", "biomarker", "positive",
     "latency delay reduced 1.7 ms/eye (95% CI 0.5 to 2.9); no functional gain",
     "PMID 29029896", "paper", "2017"),
    ("clemastine-trapms", "clemastine", "TRAP-MS arm", "M1 muscarinic antagonist", "1/2", "16",
     "progressive MS", "safety, CSF biomarkers", "safety", "harm",
     "3 of 9 exceeded 5x baseline progression slope; arm stopped 2022; contested",
     "PMID 40371642", "paper", "2025-05"),
    ("clemastine-recover", "clemastine", "ReCOVER", "M1 muscarinic antagonist", "2", "90",
     "acute optic neuritis", "VEP latency, low-contrast acuity", "biomarker", "ongoing",
     "primary completion 2028-08", "NCT02521311", "registry", "2026-03-11"),
    ("clemastine-restore", "clemastine", "RESTORE", "M1 muscarinic antagonist", "3", "47",
     "internuclear ophthalmoplegia", "versional dysconjugacy index", "functional", "stopped",
     "terminated, no results posted, reason unknown", "NCT05338450", "registry", "2026-05-06"),
    ("clemastine-revive", "clemastine", "ReVIVE", "M1 muscarinic antagonist", "1/2", "74",
     "MS", "myelin water fraction and other quantitative MRI", "biomarker", "ongoing",
     "primary completion 2027-06", "NCT05359653", "registry", ""),
    ("clemastine-reinforce", "clemastine", "ReINFORCE", "M1 muscarinic antagonist", "1/2", "44",
     "MS", "myelin water fraction and other quantitative MRI", "biomarker", "ongoing",
     "primary completion 2028-10", "NCT06065670", "registry", ""),
    ("metformin-clemastine-ccmr2", "metformin + clemastine", "CCMR-Two",
     "AMPK activation + M1 antagonism", "2a", "70",
     "relapsing MS on DMT, VEP latency >= 118 ms", "full-field VEP P100 latency", "biomarker", "positive",
     "adjusted difference -1.2 ms (95% CI -2.4 to -0.1); no EDSS or visual effect",
     "ECTRIMS 2025 report; protocol PMID 41361285", "conference", "2025-09-26"),
    ("metformin-octopus", "metformin", "Octopus arm", "AMPK activation", "2/3", "375",
     "progressive MS", "interim: atrophy, EDSS, timed walk, peg test", "functional", "negative",
     "dropped at interim for no evidence of promise",
     "ms-octopus.mrcctu.ucl.ac.uk decision-point FAQ", "company", "2026-09-17"),
    ("metformin-macsimise", "metformin", "MACSiMiSE-BRAIN", "AMPK activation", "2", "120",
     "progressive MS", "timed 25-foot walk", "functional", "ongoing",
     "primary completion 2027-02", "NCT05893225", "registry", ""),
    ("bexarotene-ccmr1", "bexarotene", "CCMR-One", "RXR agonist", "2a", "52",
     "relapsing MS on dimethyl fumarate", "lesional MTR", "biomarker", "negative",
     "MTR difference 0.16 pu (95% CI -0.39 to 0.71); exploratory VEP positive; not tolerated",
     "PMID 34418398", "paper", "2021"),
    ("bexarotene-followup", "bexarotene", "CCMR-One follow-up", "RXR agonist", "2a", "20",
     "CCMR-One participants about 27 months later", "VEP latency", "biomarker", "positive",
     "VEP difference -7.79 ms (95% CI -14.76 to -0.82); mostly under age 42",
     "PMID 38426437; PMID 41048166", "paper", "2024"),
    ("opicinumab-renew", "opicinumab", "RENEW", "anti-LINGO-1 antibody", "2", "82",
     "first acute optic neuritis", "VEP latency at week 24", "biomarker", "negative",
     "ITT negative; 2-year follow-up -4.5 ms, p=0.274", "PMID 39662163", "paper", "2025-01"),
    ("opicinumab-synergy", "opicinumab", "SYNERGY", "anti-LINGO-1 antibody", "2", "419",
     "relapsing MS on interferon", "confirmed disability improvement", "functional", "negative",
     "no dose-linear response (p=0.89)", "PMID 31285147", "paper", "2019"),
    ("opicinumab-affinity", "opicinumab", "AFFINITY", "anti-LINGO-1 antibody", "2", "263",
     "relapsing MS on DMT", "Overall Disability Response Score", "functional", "negative",
     "difference 0.15 (95% CI -0.05 to 0.35); programme discontinued",
     "PMID 41454463", "paper", "2026-01"),
    ("pipe307-vista", "PIPE-307", "VISTA", "selective M1 antagonist", "2", "168",
     "relapsing MS", "binocular 2.5% low-contrast letter acuity", "functional", "negative",
     "missed primary and all secondary endpoints; n is 168 in news, 182 in registry",
     "Contineum press release; NCT06083753", "company", "2025-11-20"),
    ("pipe791-pet", "PIPE-791", "phase 1b PET", "LPA1 antagonist", "1b", "16",
     "12 healthy volunteers, 4 progressive MS", "receptor occupancy", "target_engagement", "stopped",
     "target engaged; MS programme deferred 2025-10-30",
     "Contineum quarterly reports", "company", "2025-10-30"),
    ("bazedoxifene-rewrap", "bazedoxifene", "ReWRAP", "selective oestrogen receptor modulator", "2", "65",
     "women 40 to 60 with relapsing MS", "myelin water fraction, corpus callosum", "biomarker", "negative",
     "no MWF difference at 3 or 6 months", "ACTRIMS 2026 reports", "conference", "2026-02"),
    ("elezanumab-radius-r", "elezanumab", "RADIUS-R", "anti-RGMa antibody", "2", "208",
     "relapsing MS", "Overall Response Score", "functional", "negative",
     "effect size -0.2", "PMID 40698976", "paper", "2025-09"),
    ("elezanumab-radius-p", "elezanumab", "RADIUS-P", "anti-RGMa antibody", "2", "123",
     "progressive MS", "Overall Response Score", "functional", "negative",
     "effect size 0.0 to 0.1", "PMID 40698976", "paper", "2025-09"),
    ("gsk239512", "GSK239512", "", "histamine H3 inverse agonist", "2", "131",
     "relapsing MS on interferon or glatiramer", "MTR recovery in new lesions", "biomarker", "mixed",
     "effect size 0.344 (90% CI 0.018 to 0.671) in enhancing lesions; no clinical benefit",
     "PMID 27888416", "paper", "2017"),
    ("domperidone-rrms", "domperidone", "", "D2/D3 antagonist, raises prolactin", "2", "17",
     "relapsing MS with enhancing lesion", "MRI repair measures", "biomarker", "negative",
     "no MRI differences", "PMID 40956548", "review", "2025"),
    ("domperidone-spms", "domperidone", "", "D2/D3 antagonist, raises prolactin", "2", "81",
     "secondary progressive MS", "timed walk worsening", "functional", "negative",
     "35% worsened against a 25% target", "PMID 40956548", "review", "2025"),
    ("biotin-phase3", "high-dose biotin (MD1003)", "", "carboxylase cofactor", "3", "642",
     "progressive MS", "disability improvement", "functional", "negative",
     "failed at phase 3 after a positive phase 2 (n=154)", "PMID 40956548", "review", "2025"),
    ("cnmau8-visionary", "CNM-Au8", "VISIONARY-MS", "gold nanocrystal catalyst", "2", "73",
     "stable relapsing MS, chronic optic neuropathy", "low-contrast letter acuity", "functional", "mixed",
     "+3.13 letters per eye pooled; stopped early; conference data only; practice effects flagged",
     "PMID 40956548", "review", "2025-05"),
    ("liothyronine-phase1", "liothyronine (T3)", "", "thyroid receptor agonist", "1", "35",
     "MS", "safety", "safety", "safety_only",
     "tolerated; no VEP effect over one week; two studies, n=15 and n=20",
     "PMID 32120028; PMID 37460763", "paper", "2023"),
    ("testosterone-totem", "testosterone", "TOTEM-RRMS", "androgen receptor agonist", "2", "40",
     "hypogonadal men with relapsing MS", "thalamic atrophy, lesional diffusivity", "biomarker", "ongoing",
     "primary completion 2027-12", "NCT03910738", "registry", "2025-06-29"),
    ("ifenprodil-modif", "ifenprodil", "MODIF-MS", "NMDA antagonist", "2", "60",
     "MS", "VEP latency", "biomarker", "not_started",
     "registry record last updated 2024-03-26", "NCT06330077", "registry", "2024-03-26"),
    ("biib061", "BIIB061", "", "oral OPC differentiation agent", "2", "",
     "MS", "disability response", "functional", "stopped",
     "withdrawn before enrolment", "PMID 40956548", "review", "2025"),
    ("nsc-stems", "human fetal neural precursor cells", "STEMS", "intrathecal cell therapy", "1", "12",
     "progressive MS", "safety", "safety", "safety_only",
     "safe; exploratory lower atrophy at highest dose", "PMID 36624312", "paper", "2023"),
]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(FIELDS)
        for row in ROWS:
            w.writerow([*row, "no"])
    print(f"{len(ROWS)} rows -> {OUT}")


if __name__ == "__main__":
    main()
