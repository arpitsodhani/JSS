import sys
from math import gcd
from collections import deque, Counter

def get_g(values):
    g = 0
    for i in range(4):
        for j in range(i + 1, 4):
            g = gcd(g, abs(values[i] - values[j]))
    return g

def residues(values, g):
    return sorted(x % (2 * g) for x in values)

def normalize(values, base, g):
    return tuple(sorted((x - base) // g for x in values))

def neighbors(state, limit):
    arr = list(state)
    result = []
    for i in range(4):
        x = arr[i]
        for j in range(4):
            if i == j:
                continue
            y = arr[j]
            if x == y:
                continue
            z = 2 * y - x
            if abs(z) > limit:
                continue
            nxt = arr[:]
            nxt[i] = z
            result.append((tuple(sorted(nxt)), (x, y)))
    return result

def build_path(meet, parent_a, parent_b):
    first = []
    cur = meet
    while parent_a[cur] is not None:
        prev, op = parent_a[cur]
        first.append(op)
        cur = prev
    first.reverse()

    second = []
    cur = meet
    while parent_b[cur] is not None:
        prev, op = parent_b[cur]
        x, y = op
        second.append((2 * y - x, y))
        cur = prev

    return first + second

def bidirectional(start, target):
    if start == target:
        return []

    mx = max(max(map(abs, start)), max(map(abs, target)), 10)
    limit = max(80, mx * 2 + 20)

    qa = deque([start])
    qb = deque([target])
    pa = {start: None}
    pb = {target: None}

    while qa and qb and len(pa) + len(pb) <= 250000:
        if len(qa) <= len(qb):
            for _ in range(len(qa)):
                cur = qa.popleft()
                for nxt, op in neighbors(cur, limit):
                    if nxt in pa:
                        continue
                    pa[nxt] = (cur, op)
                    if nxt in pb:
                        return build_path(nxt, pa, pb)
                    qa.append(nxt)
        else:
            for _ in range(len(qb)):
                cur = qb.popleft()
                for nxt, op in neighbors(cur, limit):
                    if nxt in pb:
                        continue
                    pb[nxt] = (cur, op)
                    if nxt in pa:
                        return build_path(nxt, pa, pb)
                    qb.append(nxt)

    return None

def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) != 8:
        return

    a = data[:4]
    b = data[4:]

    if Counter(a) == Counter(b):
        print(0)
        return

    ga = get_g(a)
    gb = get_g(b)

    if ga == 0 or gb == 0:
        print(-1)
        return

    if ga != gb:
        print(-1)
        return

    g = ga
    if residues(a, g) != residues(b, g):
        print(-1)
        return

    base = a[0] % g
    if any(x % g != base for x in b):
        print(-1)
        return

    start = normalize(a, base, g)
    target = normalize(b, base, g)

    ops = bidirectional(start, target)
    if ops is None or len(ops) > 1000:
        print(-1)
        return

    print(len(ops))
    for x, y in ops:
        print(base + x * g, base + y * g)

if __name__ == "__main__":
    main()
