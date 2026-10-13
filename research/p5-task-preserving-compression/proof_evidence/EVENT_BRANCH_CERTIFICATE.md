> **Publication-reading copy - link adjustments only.** This file is not byte-identical to its private source. The source Git blob is `199d14ec24b436dbcdbeba1e34392f39ebf06822`; the scientific statements, data tables, and numerical constants are preserved. See `PROVENANCE_AND_LINK_MAP.md` at the archive root.

# Event-order certificate | frozen narrow P5 interval

**Status:** assistant-local exact rational evidence; not an external referee signoff. Original execution source (not distributed in this minimal archive): `verify_eventword_p5.py`, Git blob `75920bbef5374f9653bd832dd071ec5bc4cdf44b` (original local SHA256 `0a0706ca20795b31fd01864ffff572cf2cfc90960daca948028568dd1e2c9536`). A separate, **nonidentical** check of the narrow root bands is included as [review_14_event_bands.py](../checks/review_14_event_bands.py).

For u=tau^2, every dynamic receiver edge has sign Q_(a,b,c)(t,u)=(a+bt)^2-u(1+2ct+t^2); one source edge has (a,b,c)=(c,1,c). Three palette choices give 27 receiver and 3 source templates.

## Sixteen analytic exclusions
- Twelve receiver low/low choices: a,b <= M=1/8, c in {L,M,H}. Since 2(1+2ct+t^2)-(1+c)(1+t)^2=(1-c)(t-1)^2 >= 0 for t>=0, the square of each contact never exceeds 2*M^2/(1+L) < tau_min^2.
- Three high/high receiver choices: a=b=H=6/25 and c in palette. Because sqrt(1+2ct+t^2) <= 1+t, similarity >= H>tau_max.
- One high source edge c=H starts at H and monotonically increases. Thus 16 of 30 templates never switch.

The other 14 (source c=L,M; and 12 mixed H vs L/M receiver templates) each have opposite strict signs at t=0 and infinity and therefore exactly one simple positive root.

## Uniform bands and sole coalescence
Use rational bisection for positive roots at both u endpoints, rounded outwards to integer ticks divided by 2^64. For each tick band [ell,r], verify Q(ell,u) and Q(r,u) have the requisite opposite signs at u_lo and u_hi. Since Q is strictly affine decreasing in u at fixed nonnegative t, the signs persist for **every** u in between. By the intermediate value theorem and the single-positive-root proof, every event remains in its band throughout the interval.

| Group | Template (0=L,1=M,2=H) | low tick / 2^64 | high tick / 2^64 |
|---:|---|---:|---:|
| 0 | r,2,2,0 | 295824159954572162 | 295824163585612420 |
| 1 | r,1,2,0 | 611934895323245289 | 611934902023543845 |
| 2 | r,0,2,0 | 2203113667312937766 | 2203113676295398233 |
| 2 | s,1 | 2203113675028454476 | 2203113675228388048 |
| 3 | s,0 | 4359906488806314711 | 4359906489007818734 |
| 4 | r,0,1,2 | 12978762333437047866 | 12978762335679642826 |
| 5 | r,2,2,1 | 14638828740941917956 | 14638828746240993431 |
| 6 | r,1,1,2 | 16667856700365241303 | 16667856704251603855 |
| 7 | r,1,2,1 | 20415484303638146330 | 20415484308398324865 |
| 8 | r,2,1,2 | 23245190774454362566 | 23245190782868834961 |
| 9 | r,0,2,1 | 26218398805676205243 | 26218398810206471497 |
| 10 | r,0,0,2 | 154455201555070674368 | 154455202184810193675 |
| 11 | r,1,0,2 | 556076088805678703623 | 556076094894358795229 |
| 12 | r,2,0,2 | 1150285909022640415417 | 1150285923141617185905 |

All 13 bands are pairwise disjoint except the intended two templates in group 2. Source (M,1,M) and receiver (H,L,L) coalesce exactly once: the difference between their squared contact laws equals P(t)/80000 after cross-multiplication, where P(t)=79992t^4+21214t^3+76938t^2+18489t-3358. P has exactly one positive root. The crossing is bracketed by 119431031636/10^12 and 119431031637/10^12; the corresponding tau* is in the frozen local interval. Endpoint signs determine the exchange of event order.

The event order gives 15 open time cells on each strict side, 14 at equality. Exact algebraic root-time observations do not create extra failures: at an event, inclusive threshold edges are a superset of either one-sided graph, so disconnected-at-root states form a subset of disconnected-in-either-adjacent-cell states. This is one-way domination, not an equivalence.

The original executable certifier, **not included in this archive**, contains those assertions and generated its original receipt. The included alternative check covers the narrow root bands rather than reproducing every assertion in the original verifier. **No timing-jitter, strict-threshold, publication or universal generalization claim follows.**
