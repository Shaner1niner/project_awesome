# P5 — Task-Preserving Compression of Optimal Observations

**Public mathematical reproducibility supplement** · Shane Corrie · 2026

This directory accompanies the manuscript *Task-Preserving Compression of Optimal Observations in Finite Gram Dynamics*. It is a **narrow, standalone evidence subset**, not a mirror of the private `SETA_Research` repository and not evidence of human peer review or public arXiv submission.

## What is here

The three finite mathematical certificates are [`proof_evidence/`](proof_evidence/): the rational contact-event band, the exact 15-pattern failure-word census, and the statewise kernel audit. The three separately implemented standard-library verification programs are in [`checks/`](checks/); their pinned JSON receipts are in [`receipts/`](receipts/). Run the included [`run_checks.py`](run_checks.py) to check all three in normal and optimized mode.

The **mathematical scope** is one five-vertex labeled Gram family (55,980 states), exact one-bit whole-network connectivity observations, the narrow algebraic crossing and equality case, wider rational endpoint checks, and the task-preserving AND map. The scripts do **not** establish the separate adversarial clock-jitter claims, broader model families, real-world sensor costs, or priority over other literature. The rigorous extension between checked threshold values also uses analytic/monotonicity arguments in the manuscript.

## Reproduce (Python 3.9+; standard library)

From this directory:

```sh
python run_checks.py
```

The runner checks each program in normal and `-O` mode and verifies outputs against stored structured JSON. For byte-level package integrity, compare files against [`MANIFEST_SHA256.txt`](MANIFEST_SHA256.txt) (`sha256sum -c MANIFEST_SHA256.txt` on compatible systems).

## Provenance and precise limitations

The three readable certificates were adapted from private-repository documents **only to fix inaccessible references and identify omitted verifiers**; they are not byte-identical to the private source. Their original and published Git blob/byte hashes appear in [`PROVENANCE_SOURCE_AND_PUBLIC_COPY_HASHES.json`](PROVENANCE_SOURCE_AND_PUBLIC_COPY_HASHES.json). [`PROVENANCE_AND_LINK_MAP.md`](PROVENANCE_AND_LINK_MAP.md) shows the source-to-public editorial changes, with private reviewer URLs redacted. Original private verifier scripts are **not** distributed. The three public checker scripts are alternative, assistant-origin implementations; they are not a separately authored human review.

A source-independent computer implementation can catch programming mistakes but is not the same as independent human proof/novelty assessment, both of which remain open. The published certificate copies and receipts are archival evidence of the reported finite model, not an endorsement of physical sensor designs.

## Licenses and scope

The three checker scripts and replay runner are MIT-licensed; certificates, documentation and JSON receipts are CC BY 4.0-licensed, as enumerated in [`LICENSE_SCOPE.md`](LICENSE_SCOPE.md). The license scope applies only to named materials and only to rights held by the licensor; it does **not** change licensing for other contents of `project_awesome`, the private SETA project, or the paper's planned separate arXiv distribution license.

Please cite the paper title, author and this directory URL when using the supplement; retain the adaptation notice when quoting the link-adjusted certificates. No DOI is assigned to this supporting material.
