"""Check the RepairMap trial table and print the headline counts.

Exit code 1 if a row breaks the schema. Run: python repairmap/check.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

TABLE = Path(__file__).parent / "data" / "trials.csv"

OUTCOME_CLASSES = {"biomarker", "functional", "safety", "target_engagement"}
RESULTS = {"positive", "negative", "mixed", "harm", "ongoing", "not_started", "stopped", "safety_only"}
SOURCE_TYPES = {"paper", "registry", "conference", "company", "review"}
REQUIRED = ("id", "agent", "mechanism", "phase", "primary_outcome", "result", "source")


def load(path: Path = TABLE) -> list[dict[str, str]]:
    with path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def problems(rows: list[dict[str, str]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for i, r in enumerate(rows, start=2):
        tag = f"line {i} ({r.get('id', '?')})"
        for key in REQUIRED:
            if not r.get(key, "").strip():
                out.append(f"{tag}: empty {key}")
        if r["id"] in seen:
            out.append(f"{tag}: duplicate id")
        seen.add(r["id"])
        if r["outcome_class"] not in OUTCOME_CLASSES:
            out.append(f"{tag}: outcome_class {r['outcome_class']!r}")
        if r["result"] not in RESULTS:
            out.append(f"{tag}: result {r['result']!r}")
        if r["source_type"] not in SOURCE_TYPES:
            out.append(f"{tag}: source_type {r['source_type']!r}")
        if r["n"] and not r["n"].isdigit():
            out.append(f"{tag}: n {r['n']!r}")
        if r["second_check"] not in {"yes", "no"}:
            out.append(f"{tag}: second_check {r['second_check']!r}")
    return out


def summary(rows: list[dict[str, str]]) -> str:
    done = [r for r in rows if r["result"] in {"positive", "negative", "mixed", "harm"}]
    by = Counter((r["outcome_class"], r["result"]) for r in done)
    lines = [
        f"rows: {len(rows)}   agents: {len({r['agent'] for r in rows})}",
        f"with an efficacy or harm result: {len(done)}",
    ]
    for cls in ("biomarker", "functional", "safety"):
        parts = [f"{res} {by[(cls, res)]}" for res in ("positive", "mixed", "negative", "harm") if by[(cls, res)]]
        if parts:
            lines.append(f"  {cls} primary: " + ", ".join(parts))
    lines.append(f"checked a second time: {sum(r['second_check'] == 'yes' for r in rows)} of {len(rows)}")
    return "\n".join(lines)


def main() -> int:
    rows = load()
    bad = problems(rows)
    for line in bad:
        print(line, file=sys.stderr)
    print(summary(rows))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
