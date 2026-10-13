"""Isolated P5 reviewer exercise: exact-rational 4-threshold finite replay.
Written from V0.7's mathematical model; does not import the original or prior checker.
This is assistant-origin computational scrutiny, not a human referee.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
P = (Q(1, 100), Q(1, 8), Q(6, 25))
TAUS = {'a': Q(23920, 100000), 'minus': Q(23921081755, 10 ** 11), 'plus': Q(23921081756, 10 ** 11), 'b': Q(23925, 100000)}
EDGES = tuple(combinations(range(5), 2))
IX = {edge: i for i, edge in enumerate(EDGES)}
SOURCE = (IX[0, 1],)
MOVING = (IX[1, 2], IX[1, 3], IX[1, 4])
FIXED = (IX[0, 2], IX[0, 3], IX[0, 4], IX[2, 3], IX[2, 4], IX[3, 4])
TEMPLATES = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)] + [(c, 3, c) for c in range(3)]
CONNECTED = []
for mask in range(1024):
    seen = {0}
    for _ in range(4):
        seen |= {v for i, (u, v) in enumerate(EDGES) if mask >> i & 1 and u in seen}
        seen |= {u for i, (u, v) in enumerate(EDGES) if mask >> i & 1 and v in seen}
    CONNECTED.append(len(seen) == 5)
if not sum(CONNECTED) == 728:
    raise AssertionError('Reviewer check failed')

def poly(key, t, tau):
    a, b, c = key
    aa, bb, cc = (P[a], Q(1) if b == 3 else P[b], P[c])
    return (aa + bb * t) ** 2 - tau * tau * (1 + 2 * cc * t + t * t)

def get_roots_and_samples(tau):
    intervals = []
    for key in TEMPLATES:
        a, b, c = key
        if b <= 1 and a <= 1 or (a == 2 and b == 2) or (b == 3 and c == 2):
            continue
        initial = poly(key, Q(0), tau)
        if not initial != 0:
            raise AssertionError('Reviewer check failed')
        low, hi = (Q(0), Q(1))
        while (poly(key, hi, tau) > 0) == (initial > 0):
            hi *= 2
            if not hi < 2 ** 18:
                raise AssertionError('Reviewer check failed')
        for _ in range(82):
            mid = (low + hi) / 2
            if (poly(key, mid, tau) > 0) == (initial > 0):
                low = mid
            else:
                hi = mid
        if not (poly(key, low, tau) > 0) == (initial > 0):
            raise AssertionError('Reviewer check failed')
        if not (poly(key, hi, tau) > 0) != (initial > 0):
            raise AssertionError('Reviewer check failed')
        intervals.append((low, hi, key))
    intervals.sort()
    if not len(intervals) == 14:
        raise AssertionError('Reviewer check failed')
    for v, w in zip(intervals, intervals[1:]):
        if not v[1] < w[0]:
            raise AssertionError((tau, v[2], w[2]))
    times = [intervals[0][0] / 2]
    times.extend(((v[1] + w[0]) / 2 for v, w in zip(intervals, intervals[1:])))
    times.append(intervals[-1][1] + 1)
    if not len(times) == 15:
        raise AssertionError('Reviewer check failed')
    statuses = {key: tuple((poly(key, t, tau) >= 0 for t in times)) for key in TEMPLATES}
    return (intervals, times, statuses)

def enumerate_at(tau):
    intervals, times, status = get_roots_and_samples(tau)
    wordcounts = Counter()
    labelbits = []
    words = []
    for row in product(range(3), repeat=10):
        if len(set(row)) != 3:
            continue
        c = row[IX[0, 1]]
        keys = [(c, 3, c)]
        keys.extend(((row[edgeid], row[IX[0, j]], c) for edgeid, j in zip(MOVING, (2, 3, 4))))
        static = sum((1 << i for i in FIXED if row[i] == 2))
        pattern = 0
        for k in range(15):
            mask = static
            for idx, key in zip(SOURCE + MOVING, keys):
                if status[key][k]:
                    mask |= 1 << idx
            if not CONNECTED[mask]:
                pattern |= 1 << k
        words.append(pattern)
        wordcounts[pattern] += 1
        labelbits.append(1 if pattern == 0 else 0)
    if not len(words) == 55980:
        raise AssertionError('Reviewer check failed')
    packed = bytes((sum((labelbits[j + q] << q for q in range(min(8, len(labelbits) - j)))) for j in range(0, len(labelbits), 8)))
    positives = wordcounts[0]
    if not positives == 10864:
        raise AssertionError('Reviewer check failed')
    neg = [w for w in wordcounts if w]

    def cover_ok(qs):
        q = sum((1 << i for i in qs))
        return all((w & q for w in neg))
    minimum = next((k for k in range(16) if any((cover_ok(q) for q in combinations(range(15), k)))), None)
    covers = [tuple(q) for q in combinations(range(15), minimum) if cover_ok(q)]
    return {'root_keys': [key for a, b, key in intervals], 'words': words, 'positive': positives, 'negative': len(words) - positives, 'word_patterns': len(neg), 'hash': sha256(packed).hexdigest(), 'K': minimum, 'covers': covers, 'multiplicity': wordcounts}

def response_pair(left, right):
    patterns = Counter()
    errors = []
    for idx, (w1, w2) in enumerate(zip(left['words'], right['words'])):
        x, y, z = (0 if w1 >> q & 1 else 1 for q in (2, 4, 11))
        u, v = (0 if w2 >> q & 1 else 1 for q in (3, 11))
        if (u, v) != (x & y, z):
            errors.append(idx)
        patterns[x, y, z, u, v] += 1
    return (patterns, errors)
results = {name: enumerate_at(tau) for name, tau in TAUS.items()}
standard = 'ffe6e5f4ef1ef8d70b195538d70fa3b962c28b09524d071ed4cd807014245123'
if not {a['hash'] for a in results.values()} == {standard}:
    raise AssertionError('Reviewer check failed')
if not {name: a['K'] for name, a in results.items()} == {'a': 3, 'minus': 3, 'plus': 2, 'b': 2}:
    raise AssertionError('Reviewer check failed')
if not all((a['negative'] == 45116 and a['word_patterns'] == 15 for a in results.values())):
    raise AssertionError('Reviewer check failed')
if not results['minus']['covers'] == [(2, 4, i) for i in (11, 12, 13, 14)]:
    raise AssertionError('Reviewer check failed')
if not results['plus']['covers'] == [(3, i) for i in (11, 12, 13, 14)]:
    raise AssertionError('Reviewer check failed')
pat, errs = response_pair(results['minus'], results['plus'])
if not not errs:
    raise AssertionError('Reviewer check failed')
if not len({v[:3] for v in pat}) == 8:
    raise AssertionError('Reviewer check failed')
if not len({v[3:] for v in pat}) == 4:
    raise AssertionError('Reviewer check failed')
lower = Counter()
upper = Counter()
for p, n in pat.items():
    lower[''.join(map(str, p[:3]))] += n
    upper[''.join(map(str, p[3:]))] += n
if not lower == {'000': 36004, '001': 1570, '010': 1411, '011': 2128, '100': 600, '101': 504, '110': 2899, '111': 10864}:
    raise AssertionError('Reviewer check failed')
if not upper == {'00': 38015, '01': 4202, '10': 2899, '11': 10864}:
    raise AssertionError('Reviewer check failed')
fold = lambda w: w & 7 | w >> 4 << 3
eq_left = [fold(w) for w in results['minus']['words']]
eq_right = [fold(w) for w in results['plus']['words']]
if not eq_left == eq_right:
    raise AssertionError('Reviewer check failed')
equality_words = Counter(eq_left)
if not (equality_words[0] == 10864 and len(equality_words) == 16):
    raise AssertionError('Reviewer check failed')
neg_eq = [w for w in equality_words if w]

def eq_hit(cols):
    choice = sum((1 << c for c in cols))
    return all((w & choice for w in neg_eq))
if not not any((eq_hit(cols) for n in range(3) for cols in combinations(range(14), n))):
    raise AssertionError('Reviewer check failed')
eq_covers = [list(cols) for cols in combinations(range(14), 3) if eq_hit(cols)]
if not eq_covers == [[2, 3, i] for i in (10, 11, 12, 13)]:
    raise AssertionError('Reviewer check failed')
report = {name: {key: ans[key] for key in ('positive', 'negative', 'word_patterns', 'hash', 'K', 'covers')} for name, ans in results.items()}
report['and_map'] = {'errors': len(errs), 'left': dict(sorted(lower.items())), 'right': dict(sorted(upper.items()))}
report['equality_from_algebraic_collision'] = {'cells': 14, 'K': 3, 'all_optimal_3_covers': eq_covers, 'negative_patterns': len(neg_eq), 'statewise_phase_fold_agreement': len(eq_left)}
print(json.dumps(report, sort_keys=True, indent=2))
with open('p5_v07_referee_receipt.json', 'w') as fh:
    json.dump(report, fh, sort_keys=True, indent=2)
