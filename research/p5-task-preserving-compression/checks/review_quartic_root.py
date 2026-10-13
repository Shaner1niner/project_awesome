"""Exact quartic and uniform narrow-band referee checks, independent algebra."""
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
import json
M, H, L = (F(1, 8), F(6, 25), F(1, 100))
tau_minus = F(23921081755, 10 ** 11)
tau_plus = F(23921081756, 10 ** 11)
q_tlo = F(119431031636, 10 ** 12)
q_thi = F(119431031637, 10 ** 12)
poly = lambda t: 79992 * t ** 4 + 21214 * t ** 3 + 76938 * t ** 2 + 18489 * t - 3358
if not poly(q_tlo) < 0 < poly(q_thi):
    raise AssertionError('Reviewer check failed')

def src(t):
    return (M + t) ** 2 / (1 + 2 * M * t + t * t)

def rec(t):
    return (H + L * t) ** 2 / (1 + 2 * L * t + t * t)
if not src(q_tlo) > tau_minus * tau_minus:
    raise AssertionError('Reviewer check failed')
if not src(q_thi) < tau_plus * tau_plus:
    raise AssertionError('Reviewer check failed')
cross = lambda t: (M + t) ** 2 * (1 + 2 * L * t + t * t) - (H + L * t) ** 2 * (1 + 2 * M * t + t * t)
for t in [F(i, 4) for i in range(7)]:
    if not 80000 * cross(t) == poly(t):
        raise AssertionError((t, 80000 * cross(t), poly(t)))
rf = lambda t: L - H * L + (L * L - H) * t
if not (rf(q_tlo) < 0 and rf(q_thi) < 0):
    raise AssertionError('Reviewer check failed')
out = {'quartic_identity': '80000 cross(t)=P(t)', 'unique_positive_root': "P(0)<0;P'(t)>0 for t>0", 'tlo': str(q_tlo), 'thi': str(q_thi), 'Plo': str(poly(q_tlo)), 'Phi': str(poly(q_thi)), 'tau_bracket': [str(tau_minus), str(tau_plus)], 'fs_lower_bound_gt_tau_minus': True, 'fs_upper_bound_lt_tau_plus': True, 'fr_derivative_negative_in_tstar_bracket': True}
print(json.dumps(out, indent=2))
with open('p5_v07_root_receipt.json', 'w') as f:
    json.dump(out, f, indent=2)
