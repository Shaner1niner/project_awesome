> **Publication-reading copy - link adjustments only.** This file is not byte-identical to its private source. The source Git blob is `6262276e6dabe615762c9ef5101786a3df802a52`; the scientific statements, data tables, and numerical constants are preserved. See `PROVENANCE_AND_LINK_MAP.md` at the archive root.

# Manuscript V0.2 — three-word kernel and exact statewise comparison

**Internal supplemental check, 2026-10-13.** This is assistant-local, not an independent external mathematical proof. Frozen original `verify_eventword_p5.py` source is unchanged; this V0.2 check imports its exact root/order/cut routines.

- Original supplemental source (not bundled here): `verify_kernel_and_statewise_equality_v02.py`. The [bundled separate finite-family checker](../checks/review_four_thresholds_and_equality.py) uses different logic and must not be misidentified as the original V0.2 helper.
- Local source SHA256: `b07b9867eac2016c3675e0e218afd49e7b2e037aa663e5c521f4e18b7fdf9525` (verify separately against GitHub source, since remote newline normalization is possible)
- Canonical normal output SHA256: `28e91e494820a32f97b8266b7bd46d00e1410ae791ca49f966c481aa8a65d494`
- Canonical `python -O` output SHA256: `28e91e494820a32f97b8266b7bd46d00e1410ae791ca49f966c481aa8a65d494`
- Full ordered statewise persistent vectors materialized as 6,998-byte bytearrays (55,980 bits), compared **by exact bytes**, equality `True`. Their identical SHA256 is `ffe6e5f4ef1ef8d70b195538d70fa3b962c28b09524d071ed4cd807014245123`.
- All 55,980 distinct *labeled* palette assignments visited on each phase. Persistent count 10,864. Nonpersistent count 45,116.
- All 15 nonzero failure-word patterns remain in each phase; **exactly rows 1, 3, 5 are inclusion-minimal**. All 15 rows contain one or more of those rows, and the three have no subset relationship to one another.
- Left: kernel `{2}`, `{4}`, `{11,12,13,14}`; no two-query covers.
- Equality: kernel `{2}`, `{3}`, `{10,11,12,13}`; no two-query covers.
- Right: kernel `{2,3}`, `{3,4}`, `{11,12,13,14}`; exactly four two-query covers `(3,11)`, `(3,12)`, `(3,13)`, `(3,14)`.

## Inclusion dominance certificate

The row-to-minimal-row incidence map (1-based) is **the same across phases**:

```text
1 -> 1           2 -> 1           3 -> 3
4 -> 1,3         5 -> 5           6 -> 3,5
7 -> 1,3,5       8 -> 5           9 -> 1,5
10 -> 1,5        11 -> 5          12 -> 3,5
13 -> 1,3,5      14 -> 1,3,5      15 -> 1,3,5
```

**Mathematical meaning:** for any family of sets, a query-time hitting set for all inclusion-minimal members hits every superset member; conversely the minimal members themselves occur in the full family, so the *entire family of winning query schedules* is identical to that for the kernel. Consequently the P5 full-family upper bound can be presented as an explicit finite dominance certificate, not an inference from four example states alone.

**Provenance boundary:** the script reuses previous event-order and cut-table functions and compares direct bytevectors with original digest, so this is stronger internal regression evidence but *not* algorithmically independent external review. The original P5 equality label remains source-level `NOT_CERTIFIED`; the local theorem rests on subsequent exact assistant-local sources. No claim of full publication qualification or novel universal transversal theory.
