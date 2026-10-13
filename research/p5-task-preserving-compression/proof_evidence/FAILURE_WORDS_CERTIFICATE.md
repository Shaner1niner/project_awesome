> **Publication-reading copy - link adjustments only.** This file is not byte-identical to its private source. The source Git blob is `e6509d1b09e39efa7eeb0a0b1c1d47da17384d58`; the scientific statements, data tables, and numerical constants are preserved. See `PROVENANCE_AND_LINK_MAP.md` at the archive root.

# Complete 15 failure-pattern finite certificate

**Evidence:** source-independent *assistant-local* exact event-word/cut computation, not a distinct external review. Frozen mathematical source/test at `17020db2a507fb6123ed051a69ac94072cf934c0` remains original-source authority (source code itself reports equality NOT_CERTIFIED). The original algorithm's source is `verify_eventword_p5.py`, which is **not included** here. The bundled [separately implemented four-threshold and equality checker](../checks/review_four_thresholds_and_equality.py) checks its own finite-family invariants; it does not reproduce every assertion in the original algorithm.

**Input family** 55,980 labeled P5 palette states, all colors L=1/100,M=1/8,H=6/25 present, source=0/receiver=1, inclusive z>=tau, all-finite-time whole-graph connectivity, exact binary C(t) oracle. Independent connectivity uses all 15 graph cuts and reproduces 728 connected/296 disconnected simple five-vertex graph masks.

**Output:** 10,864 Y-positive states, 45,116 Y-negative states; unchanged state-label SHA256 `ffe6e5f4ef1ef8d70b195538d70fa3b962c28b09524d071ed4cd807014245123` in left, equality, right local phases. The 45,116 negative states collapse into exactly 15 distinct failure words in each phase, with identical multiplicities across phases.

| Row | Multiplicity | Left failed open cells | Equality failed open cells | Right failed open cells |
|---:|---:|---|---|---|
| 1 | 558 | 2 | 2 | 2,3 |
| 2 | 1570 | 0,1,2 | 0,1,2 | 0,1,2,3 |
| 3 | 504 | 4 | 3 | 3,4 |
| 4 | 1570 | 0-4 | 0-3 | 0-4 |
| 5 | 528 | 11-14 | 10-13 | 11-14 |
| 6 | 48 | 4,11-14 | 3,10-13 | 3,4,11-14 |
| 7 | 1425 | 0-4,11-14 | 0-3,10-13 | 0-4,11-14 |
| 8 | 480 | 9-14 | 8-13 | 9-14 |
| 9 | 48 | 2,9-14 | 2,8-13 | 2,3,9-14 |
| 10 | 1363 | 0-2,9-14 | 0-2,8-13 | 0-3,9-14 |
| 11 | 1891 | 7-14 | 6-13 | 7-14 |
| 12 | 552 | 4-14 | 3-13 | 3-14 |
| 13 | 600 | 2-14 | 2-13 | 2-14 |
| 14 | 2017 | 1-14 | 1-13 | 1-14 |
| 15 | 31962 | 0-14 | 0-13 | 0-14 |

All multiplicities add to 45,116. Any deterministic adaptive zero-error strategy run on a persistent state follows an all-True path, which must hit each negative word. A finite hitting set gives a fixed schedule. Thus `K_adaptive = K_fixed = min hitting-set cardinality` under this restricted oracle and persistence target.

At tau_minus, the words {2}, {4}, {11,12,13,14} force >=3, and exactly four three-covers exist: (2,4,k) for k=11..14. At algebraic tau*, {2}, {3}, {10,11,12,13} force >=3; four three-covers exist: (2,3,k) for k=10..13. At tau_plus, exactly four two-covers exist: (3,11),(3,12),(3,13),(3,14). The event-band proof ensures these combinatorial regimes persist in their respective open threshold chambers throughout the frozen local tau interval. At exact event time the inclusive rule excludes root-only improvements.

The four-state witness is a human-readable subset of these rows and proves *necessity*, not universal full-family sufficiency. A human-independent mathematical audit remains outstanding; the private review issue is intentionally not linked in this public-reading copy.

**Original-source replay (original verifier not included):** `python verify_eventword_p5.py > receipt.json` and `python -O verify_eventword_p5.py > receipt_optimized.json`. These commands cannot be executed with this minimal archive. **Packaged alternative replay:** from the archive root run `python run_checks.py`; this compares three separately implemented checks with their saved structured JSON receipts in normal and optimized modes. The alternative reports must not be represented as byte-identical output of the unbundled original verifier. The original assistant-local transcript gives SHA256 `8464e6cb5194020724283da7f6853f95c9611a5665966278c11889e1cb835b5c` for both; this hash is not evidence of a repo-head run unless reproduced. Exact 14 root bands in [EVENT_BRANCH_CERTIFICATE.md](EVENT_BRANCH_CERTIFICATE.md).
