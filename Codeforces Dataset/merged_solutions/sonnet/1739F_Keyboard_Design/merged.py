# Clause setup_environment [Confidence: 0.60]
import sys
from functools import lru_cache

def extract_path(raw):
    seq = [b - 97 for b in raw]
    if len(seq) <= 1:
        return None
    adj = [set() for _ in range(12)]
    present = set(seq)
    for a, b in zip(seq, seq[1:]):
        if a == b:
            return None
        adj[a].add(b)
        adj[b].add(a)
    vertices = [x for x in range(12) if x in present or adj[x]]
    if sum(len(adj[x]) for x in range(12)) // 2 != len(vertices) - 1:
        return None
    for x in vertices:
        if len(adj[x]) > 2:
            return None
    if len(vertices) == 2:
        route = vertices[:]
    else:
        ends = [x for x in vertices if len(adj[x]) == 1]
        if len(ends) != 2:
            return None
        route = []
        parent = -1
        node = ends[0]
        while node >= 0:
            route.append(node)
            candidates = [x for x in adj[node] if x != parent]
            parent, node = node, candidates[0] if candidates else -1
    route = tuple(route)
    other = route[::-1]
    return route if route < other else other


# Clause solve_logic [Confidence: 0.60]
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    m = int(data[0])
    totals = {}
    j = 1
    for _ in range(m):
        cost = int(data[j])
        pattern = canonical_pattern(data[j + 1])
        j += 2
        if pattern:
            totals[pattern] = totals.get(pattern, 0) + cost

    nxt = [[-1] * 12]
    score = [0]

    def node():
        nxt.append([-1] * 12)
        score.append(0)
        return len(nxt) - 1

    for pattern, cost in totals.items():
        for seq in (pattern, pattern[::-1]):
            p = 0
            for letter in seq:
                q = nxt[p][letter]
                if q < 0:
                    q = node()
                    nxt[p][letter] = q
                p = q
            score[p] += cost

    target = (1 << 12) - 1
    memo = {}
    parent = {}

    def best(mask, active):
        if mask == target:
            return 0
        key = (mask, active)
        stored = memo.get(key)
        if stored is not None:
            return stored
        opt = -1
        opt_ch = 0
        for letter in range(12):
            if mask >> letter & 1:
                continue
            coming = []
            gain = 0
            root = nxt[0][letter]
            if root >= 0:
                coming.append(root)
                gain += score[root]
            for p in active:
                q = nxt[p][letter]
                if q >= 0:
                    coming.append(q)
                    gain += score[q]
            got = gain + best(mask | (1 << letter), tuple(coming))
            if got > opt:
                opt = got
                opt_ch = letter
        memo[key] = opt
        parent[key] = opt_ch
        return opt

    mask = 0
    active = ()
    out = []
    for _ in range(12):
        best(mask, active)
        letter = parent[(mask, active)]
        out.append(chr(97 + letter))
        coming = []
        root = nxt[0][letter]
        if root >= 0:
            coming.append(root)
        for p in active:
            q = nxt[p][letter]
            if q >= 0:
                coming.append(q)
        active = tuple(coming)
        mask |= 1 << letter


# Clause finish_program [Confidence: 0.80]
    print("".join(answer))

if __name__ == "__main__":
    main()


