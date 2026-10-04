#!/usr/bin/env python3
"""Randomised cross-checks for the ast_merger_sonent_sols candidates."""
import itertools
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/arpit/Desktop/cf_ast_merger_testbed")
OUT = ROOT / "ast_merger_sonent_sols"
PY = str(ROOT / ".venv/bin/python")
random.seed(20260829)


def run(path, stdin):
    r = subprocess.run([PY, str(path)], input=stdin, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    assert r.returncode == 0, f"{path} crashed: {r.stderr[-500:]}"
    return r.stdout.strip()


def cands(pid):
    return [OUT / pid / f"candidate_{i}.py" for i in range(1, 6)]


def ref(pid):
    return ROOT / "codeforces_sols" / pid / "solution.py"


# ---------------- 2051F: brute deck simulation
def brute_2051F(n, m, ops):
    decks = {tuple(range(1, n + 1))}
    joker = m
    res = []
    for a in ops:
        nxt = set()
        for d in decks:
            c = d[a - 1]
            rest = d[:a - 1] + d[a:]
            nxt.add((c,) + rest)
            nxt.add(rest + (c,))
        decks = nxt
        res.append(len({d.index(joker) + 1 for d in decks}))
    return res


def stress_2051F(rounds=200):
    for _ in range(rounds):
        n = random.randint(1, 6)
        m = random.randint(1, n)
        q = random.randint(1, 4)
        ops = [random.randint(1, n) for _ in range(q)]
        stdin = f"1\n{n} {m} {q}\n{' '.join(map(str, ops))}\n"
        want = " ".join(map(str, brute_2051F(n, m, ops)))
        for c in cands("2051F"):
            got = run(c, stdin)
            assert got == want, f"2051F {stdin!r} {c.name}: got {got!r} want {want!r}"
    return f"2051F: {rounds} random cases match brute deck simulation"


# ---------------- 1223D: BFS brute
def brute_1223D(a):
    from collections import deque
    start = tuple(a)
    if list(start) == sorted(start):
        return 0
    seen = {start}
    dq = deque([(start, 0)])
    while dq:
        cur, d = dq.popleft()
        for x in set(cur):
            keep = [v for v in cur if v != x]
            cnt = len(cur) - len(keep)
            for nxt in ((x,) * cnt + tuple(keep), tuple(keep) + (x,) * cnt):
                if nxt in seen:
                    continue
                if list(nxt) == sorted(nxt):
                    return d + 1
                seen.add(nxt)
                dq.append((nxt, d + 1))
    raise AssertionError("unreachable")


def stress_1223D(rounds=120):
    for _ in range(rounds):
        n = random.randint(1, 7)
        a = [random.randint(1, min(n, 4)) for _ in range(n)]
        stdin = f"1\n{n}\n{' '.join(map(str, a))}\n"
        want = str(brute_1223D(a))
        for c in cands("1223D"):
            got = run(c, stdin)
            assert got == want, f"1223D {a} {c.name}: got {got!r} want {want!r}"
    return f"1223D: {rounds} random cases match BFS brute force"


# ---------------- 180D: permutation brute
def brute_180D(s, t):
    best = None
    for p in set(itertools.permutations(s)):
        cand = "".join(p)
        if cand > t and (best is None or cand < best):
            best = cand
    return best if best is not None else "-1"


def stress_180D(rounds=120):
    for _ in range(rounds):
        alpha = "abc"
        s = "".join(random.choice(alpha) for _ in range(random.randint(1, 5)))
        t = "".join(random.choice(alpha) for _ in range(random.randint(1, 5)))
        stdin = f"{s}\n{t}\n"
        want = brute_180D(s, t)
        for c in cands("180D"):
            got = run(c, stdin)
            assert got == want, f"180D s={s} t={t} {c.name}: got {got!r} want {want!r}"
    return f"180D: {rounds} random cases match permutation brute force"


# ---------------- 985C: partition brute
def brute_985C(n, k, l, staves):
    best = 0
    idx = list(range(n * k))
    for perm in set(itertools.permutations(idx)):
        groups = [sorted(staves[perm[i * k + j]] for j in range(k)) for i in range(n)]
        vols = [g[0] for g in groups]
        if max(vols) - min(vols) > l:
            continue
        best = max(best, sum(vols))
    return best


def stress_985C(rounds=60):
    for _ in range(rounds):
        n = random.randint(1, 3)
        k = random.randint(1, 6 // n)
        l = random.randint(0, 3)
        staves = [random.randint(1, 6) for _ in range(n * k)]
        stdin = f"{n} {k} {l}\n{' '.join(map(str, staves))}\n"
        want = str(brute_985C(n, k, l, staves))
        for c in cands("985C"):
            got = run(c, stdin)
            assert got == want, f"985C {n} {k} {l} {staves} {c.name}: got {got!r} want {want!r}"
    return f"985C: {rounds} random cases match partition brute force"


# ---------------- 1693B: cross-check vs accepted reference
def stress_1693B(rounds=40):
    for _ in range(rounds):
        tests = random.randint(1, 3)
        parts = [str(tests)]
        for _ in range(tests):
            n = random.randint(1, 8)
            parts.append(str(n))
            if n > 1:
                parts.append(" ".join(str(random.randint(1, v - 1)) for v in range(2, n + 1)))
            for _ in range(n):
                lo = random.randint(1, 8)
                parts.append(f"{lo} {random.randint(lo, 10)}")
        stdin = "\n".join(parts) + "\n"
        want = run(ref("1693B"), stdin)
        for c in cands("1693B"):
            got = run(c, stdin)
            assert got == want, f"1693B {stdin!r} {c.name}: got {got!r} want {want!r}"
    return f"1693B: {rounds} random forests match the accepted reference solution"


# ---------------- 534B: brute over speed sequences
def brute_534B(v1, v2, t, d):
    best = [-1]

    def rec(seq):
        if len(seq) == t:
            if seq[-1] == v2:
                best[0] = max(best[0], sum(seq))
            return
        for nxt in range(max(0, seq[-1] - d), seq[-1] + d + 1):
            rec(seq + [nxt])

    rec([v1])
    return best[0]


def stress_534B(rounds=40):
    for _ in range(rounds):
        t = random.randint(2, 4)
        d = random.randint(0, 3)
        v1 = random.randint(1, 6)
        v2 = random.randint(max(1, v1 - d * (t - 1)), v1 + d * (t - 1))
        want = brute_534B(v1, v2, t, d)
        if want < 0:
            continue
        stdin = f"{v1} {v2}\n{t} {d}\n"
        for c in cands("534B"):
            got = run(c, stdin)
            assert got == str(want), f"534B {v1} {v2} {t} {d} {c.name}: got {got!r} want {want}"
    return f"534B: {rounds} random cases match exhaustive speed-sequence search"


# ---------------- 1715B / 2084A / 801B / 519C: property checks
def stress_1715B(rounds=60):
    for _ in range(rounds):
        n = random.randint(1, 6)
        k = random.randint(1, 6)
        b = random.randint(0, 5)
        s = random.randint(0, 60)
        stdin = f"1\n{n} {k} {b} {s}\n"
        feasible = k * b <= s <= k * b + n * (k - 1)
        for c in cands("1715B"):
            got = run(c, stdin)
            if not feasible:
                assert got == "-1", f"1715B {n} {k} {b} {s} {c.name}: expected -1, got {got!r}"
                continue
            arr = list(map(int, got.split()))
            assert len(arr) == n and all(v >= 0 for v in arr), f"1715B {c.name}: {got!r}"
            assert sum(arr) == s and sum(v // k for v in arr) == b, f"1715B {c.name}: {got!r}"
    return f"1715B: {rounds} random cases satisfy sum/beauty/feasibility"


def stress_2084A(rounds=1):
    ns = list(range(1, 40))
    stdin = f"{len(ns)}\n" + "\n".join(map(str, ns)) + "\n"
    for c in cands("2084A"):
        lines = run(c, stdin).splitlines()
        assert len(lines) == len(ns)
        for n, line in zip(ns, lines):
            if n % 2 == 0:
                assert line.strip() == "-1", f"2084A n={n} {c.name}: {line!r}"
                continue
            p = list(map(int, line.split()))
            assert sorted(p) == list(range(1, n + 1)), f"2084A n={n} {c.name}: {line!r}"
            for i in range(2, n + 1):
                assert max(p[i - 2], p[i - 1]) % i == i - 1, f"2084A n={n} i={i} {c.name}"
    return "2084A: n=1..39 all outputs are valid permutations (or -1 on even n)"


def stress_801B(rounds=80):
    for _ in range(rounds):
        n = random.randint(1, 6)
        x = "".join(random.choice("abc") for _ in range(n))
        y = "".join(random.choice("abc") for _ in range(n))
        stdin = f"{x}\n{y}\n"
        possible = all(b <= a for a, b in zip(x, y))
        for c in cands("801B"):
            got = run(c, stdin)
            if not possible:
                assert got == "-1", f"801B {x}/{y} {c.name}: {got!r}"
                continue
            assert len(got) == n, f"801B {x}/{y} {c.name}: {got!r}"
            assert "".join(min(a, b) for a, b in zip(x, got)) == y, f"801B {x}/{y} {c.name}: {got!r}"
    return f"801B: {rounds} random cases satisfy f(x, z) == y"


def stress_519C(rounds=1):
    for n in range(0, 30):
        for m in range(0, 30):
            if n == 0 and m == 0:
                continue
            want = run(ref("519C"), f"{n} {m}\n")
            for c in cands("519C"):
                got = run(c, f"{n} {m}\n")
                assert got == want, f"519C {n} {m} {c.name}: got {got!r} want {want!r}"
    return "519C: n,m in 0..29 match the accepted reference solution"


BATCH1 = (stress_2084A, stress_519C, stress_801B, stress_534B, stress_1715B,
          stress_985C, stress_180D, stress_1223D, stress_1693B, stress_2051F)


def _main():
    import sys as _sys
    which = _sys.argv[1] if len(_sys.argv) > 1 else "all"
    fns = BATCH1 if which == "1" else BATCH2 if which == "2" else BATCH1 + BATCH2
    for fn in fns:
        print(fn(), flush=True)
    print("\nall stress checks passed")


# ---------------- second batch (500A, 2210B, 2062C, 2070B, 203B) ----------------

def brute_2210B(p):
    n = len(p)
    best = 0

    def rec(i, marked, sat):
        nonlocal best
        if i > n:
            best = max(best, sat)
            return
        if i in marked:
            best = max(best, sat)
            return
        rec(i + 1, marked, sat)                       # skip
        rec(i + 1, marked | {p[i - 1]}, sat + 1)      # sit

    rec(1, frozenset(), 0)
    return best


def stress_2210B(rounds=120):
    import itertools as it
    for _ in range(rounds):
        n = random.randint(1, 7)
        p = list(range(1, n + 1))
        random.shuffle(p)
        stdin = f"1\n{n}\n{' '.join(map(str, p))}\n"
        want = str(brute_2210B(p))
        for c in cands("2210B"):
            got = run(c, stdin)
            assert got == want, f"2210B {p} {c.name}: got {got!r} want {want!r}"
    return f"2210B: {rounds} random permutations match exhaustive sit/skip search"


def brute_2062C(a):
    best = [None]
    seen = set()

    def rec(seq):
        key = tuple(seq)
        if key in seen:
            return
        seen.add(key)
        s = sum(seq)
        if best[0] is None or s > best[0]:
            best[0] = s
        if len(seq) == 1:
            return
        rec(seq[::-1])
        rec([seq[i + 1] - seq[i] for i in range(len(seq) - 1)])

    rec(list(a))
    return best[0]


def stress_2062C(rounds=100):
    for _ in range(rounds):
        n = random.randint(1, 6)
        a = [random.randint(-20, 20) for _ in range(n)]
        stdin = f"1\n{n}\n{' '.join(map(str, a))}\n"
        want = str(brute_2062C(a))
        for c in cands("2062C"):
            got = run(c, stdin)
            assert got == want, f"2062C {a} {c.name}: got {got!r} want {want!r}"
    return f"2062C: {rounds} random sequences match exhaustive reverse/difference search"


def brute_2070B(n, x, k, s):
    pos = x
    i = 0
    hits = 0
    for _ in range(k):
        pos += 1 if s[i] == "R" else -1
        i += 1
        if pos == 0:
            hits += 1
            i = 0
        elif i == n:
            break
    return hits


def stress_2070B(rounds=200):
    for _ in range(rounds):
        n = random.randint(1, 6)
        s = "".join(random.choice("LR") for _ in range(n))
        x = random.choice([v for v in range(-4, 5) if v != 0])
        k = random.randint(1, 40)
        stdin = f"1\n{n} {x} {k}\n{s}\n"
        want = str(brute_2070B(n, x, k, s))
        for c in cands("2070B"):
            got = run(c, stdin)
            assert got == want, f"2070B n={n} x={x} k={k} s={s} {c.name}: got {got!r} want {want!r}"
    return f"2070B: {rounds} random programs match direct simulation"


def brute_203B(n, cells):
    grid = [[0] * (n + 2) for _ in range(n + 2)]
    for step, (x, y) in enumerate(cells, 1):
        grid[x][y] = 1
        for cx in range(1, n - 1):
            for cy in range(1, n - 1):
                if all(grid[cx + dx][cy + dy] for dx in range(3) for dy in range(3)):
                    return step
    return -1


def stress_203B(rounds=80):
    for _ in range(rounds):
        n = random.randint(3, 6)
        allc = [(x, y) for x in range(1, n + 1) for y in range(1, n + 1)]
        random.shuffle(allc)
        cells = allc[:random.randint(1, len(allc))]
        stdin = f"{n} {len(cells)}\n" + "".join(f"{x} {y}\n" for x, y in cells)
        want = str(brute_203B(n, cells))
        for c in cands("203B"):
            got = run(c, stdin)
            assert got == want, f"203B n={n} {c.name}: got {got!r} want {want!r}"
    return f"203B: {rounds} random paint orders match naive full-grid scan"


def brute_500A(n, t, jumps):
    cur = 1
    while cur < t:
        cur += jumps[cur - 1]
    return "YES" if cur == t else "NO"


def stress_500A(rounds=200):
    for _ in range(rounds):
        n = random.randint(1, 8)
        jumps = [random.randint(1, n - i) for i in range(1, n)]
        t = random.randint(1, n)
        stdin = f"{n} {t}\n{' '.join(map(str, jumps))}\n"
        want = brute_500A(n, t, jumps)
        for c in cands("500A"):
            got = run(c, stdin)
            assert got == want, f"500A n={n} t={t} {jumps} {c.name}: got {got!r} want {want!r}"
    return f"500A: {rounds} random portal chains match direct walk"


BATCH2 = (stress_500A, stress_2210B, stress_2062C, stress_2070B, stress_203B)


if __name__ == "__main__":
    _main()
