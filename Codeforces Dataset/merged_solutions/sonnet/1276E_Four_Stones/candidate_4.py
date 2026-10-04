# CLAUSE: setup_environment
import sys
from collections import Counter
from math import gcd

# CLAUSE: solve_logic
def invariant_g(a):
    g = 0
    n = len(a)
    for i in range(n):
        xi = a[i]
        for j in range(i + 1, n):
            g = gcd(g, abs(xi - a[j]))
    return g

def residue_signature(a, g):
    m = 2 * g
    return tuple(sorted(v % m for v in a))

def state_of(a, base, g):
    return tuple(sorted((v - base) // g for v in a))

def moves(s, limit):
    arr = list(s)
    for i in range(4):
        moved = arr[i]
        for j in range(4):
            fixed = arr[j]
            if i == j or moved == fixed:
                continue
            reflected = fixed * 2 - moved
            if abs(reflected) > limit:
                continue
            nxt = arr.copy()
            nxt[i] = reflected
            yield tuple(sorted(nxt)), (moved, fixed)

def path_from(center, left, right):
    a = []
    node = center
    while left[node] is not None:
        node, op = left[node]
        a.append(op)
    a.reverse()
    b = []
    node = center
    while right[node] is not None:
        prev, op = right[node]
        x, y = op
        b.append((2 * y - x, y))
        node = prev
    return a + b

def bidirectional_layers(start, goal):
    if start == goal:
        return []
    limit = max(80, 2 * max(10, *(abs(x) for x in start), *(abs(x) for x in goal)) + 20)
    front_a = {start}
    front_b = {goal}
    parent_a = {start: None}
    parent_b = {goal: None}
    while front_a and front_b and len(parent_a) + len(parent_b) <= 250000:
        if len(front_a) <= len(front_b):
            new_front = set()
            for cur in front_a:
                for nxt, op in moves(cur, limit):
                    if nxt in parent_a:
                        continue
                    parent_a[nxt] = (cur, op)
                    if nxt in parent_b:
                        return path_from(nxt, parent_a, parent_b)
                    new_front.add(nxt)
            front_a = new_front
        else:
            new_front = set()
            for cur in front_b:
                for nxt, op in moves(cur, limit):
                    if nxt in parent_b:
                        continue
                    parent_b[nxt] = (cur, op)
                    if nxt in parent_a:
                        return path_from(nxt, parent_a, parent_b)
                    new_front.add(nxt)
            front_b = new_front
    return None

def main():
    vals = [int(x) for x in sys.stdin.read().split()]
    if len(vals) != 8:
        return
    src = vals[:4]
    dst = vals[4:]
    if Counter(src) == Counter(dst):
        print(0)
        return
    gs = invariant_g(src)
    gt = invariant_g(dst)
    possible = gs != 0 and gs == gt and residue_signature(src, gs) == residue_signature(dst, gs)
    if not possible:
        print(-1)
        return
    base = src[0] % gs
    if any(v % gs != base for v in dst):
        print(-1)
        return
    ans = bidirectional_layers(state_of(src, base, gs), state_of(dst, base, gs))
    if ans is None or len(ans) > 1000:
        print(-1)
        return
    print(len(ans))
    for x, y in ans:
        print(base + x * gs, base + y * gs)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
