#!/usr/bin/env python3
"""Run self-contained, assistant-origin verification checks (not human peer review)."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKS = (
    "review_four_thresholds_and_equality",
    "review_quartic_root",
    "review_14_event_bands",
)


def main():
    if sys.version_info < (3, 9):
        raise SystemExit("Python 3.9 or later required")
    for name in CHECKS:
        script = ROOT / "checks" / (name + ".py")
        expected = json.loads((ROOT / "receipts" / (name + "_result.json")).read_text(encoding="utf-8"))
        for opts in ((), ("-O",)):
            args = [sys.executable, *opts, str(script)]
            result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=120)
            if result.returncode:
                raise RuntimeError(f"{name} {opts}: exit {result.returncode}: {result.stderr[-1400:]}")
            observed = json.loads(result.stdout)
            if observed != expected:
                raise AssertionError(f"{name} {opts}: parsed JSON differs from pinned expected receipt")
        print("PASS", name, flush=True)
    print("VERIFIED 3 checks x 2 modes = 6 runs", flush=True)


if __name__ == "__main__":
    main()
