"""Independent exact verification of 14 supplied dyadic event enclosures at rational endpoints."""
from fractions import Fraction as F
import json
L, M, H = (F(1, 100), F(1, 8), F(6, 25))
palette = (L, M, H)
taus = (F(23921081755, 10 ** 11), F(23921081756, 10 ** 11))
rows = [(0, 'r', 2, 2, 0, 295824159954572162, 295824163585612420), (1, 'r', 1, 2, 0, 611934895323245289, 611934902023543845), (2, 'r', 0, 2, 0, 2203113667312937766, 2203113676295398233), (2, 's', 1, 1, 3, 2203113675028454476, 2203113675228388048), (3, 's', 0, 0, 3, 4359906488806314711, 4359906489007818734), (4, 'r', 0, 1, 2, 12978762333437047866, 12978762335679642826), (5, 'r', 2, 2, 1, 14638828740941917956, 14638828746240993431), (6, 'r', 1, 1, 2, 16667856700365241303, 16667856704251603855), (7, 'r', 1, 2, 1, 20415484303638146330, 20415484308398324865), (8, 'r', 2, 1, 2, 23245190774454362566, 23245190782868834961), (9, 'r', 0, 2, 1, 26218398805676205243, 26218398810206471497), (10, 'r', 0, 0, 2, 154455201555070674368, 154455202184810193675), (11, 'r', 1, 0, 2, 556076088805678703623, 556076094894358795229), (12, 'r', 2, 0, 2, 1150285909022640415417, 1150285923141617185905)]
if not len(rows) == 14:
    raise AssertionError('Reviewer check failed')
D = 2 ** 64
P2 = []
for grp, kind, c, a, b, li, hi in rows:
    if not li < hi:
        raise AssertionError('Reviewer check failed')
    l, h = (F(li, D), F(hi, D))
    aa = palette[a]
    bb = F(1) if kind == 's' else palette[b]
    cc = palette[c]

    def q(t, tau):
        return (aa + bb * t) ** 2 - tau * tau * (1 + 2 * cc * t + t * t)
    for tau in taus:
        if not q(l, tau) * q(h, tau) < 0:
            raise AssertionError((grp, kind, tau))
    P2.append((grp, l, h, kind))
for left, right in zip(P2, P2[1:]):
    if left[0] != right[0]:
        if not left[2] < right[1]:
            raise AssertionError((left, right))
for g in range(12):
    end = max((h for gg, l, h, _ in P2 if gg == g))
    begin = min((l for gg, l, h, _ in P2 if gg == g + 1))
    if not end < begin:
        raise AssertionError((g, end, begin))
if not (P2[2][1] < P2[3][2] and P2[3][1] < P2[2][2]):
    raise AssertionError('Reviewer check failed')
print(json.dumps({'verified_bands': len(P2), 'separated_groups': 13, 'internal_group_2_overlap': True, 'uniform_all_tau_from_Q_affine_decreasing_in_tau2': True}, indent=2))
