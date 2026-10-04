# Clause program [Confidence: 0.60]
import sys
from collections import deque

values = list(map(int, sys.stdin.buffer.read().split()))
idx = 0
t = values[idx]
idx += 1
printed = []

for _ in range(t):
    n = values[idx]
    idx += 1

    # CLAUSE: build_child_adjacency
    kids = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    for v in range(2, n + 1):
        p = values[idx]
        idx += 1
        parent[v] = p
        kids[p].append(v)

    l = [0] * (n + 1)
    r = [0] * (n + 1)
    for v in range(1, n + 1):
        l[v] = values[idx]
        r[v] = values[idx + 1]
        idx += 2

    # CLAUSE: traverse_subtree_postorder
    remaining = [0] * (n + 1)
    q = deque()
    for v in range(1, n + 1):
        remaining[v] = len(kids[v])
        if remaining[v] == 0:
            q.append(v)

    child_sum = [0] * (n + 1)
    contribution = [0] * (n + 1)
    ops = 0

    while q:
        v = q.popleft()

        # CLAUSE: aggregate_child_capacity
        total = child_sum[v]

        # CLAUSE: enforce_vertex_lower_bound
        if total < l[v]:
            ops += 1

            # CLAUSE: cap_vertex_contribution
            contribution[v] = r[v]
        else:
            # CLAUSE: cap_vertex_contribution
            contribution[v] = min(total, r[v])

        p = parent[v]
        if p:
            child_sum[p] += contribution[v]
            remaining[p] -= 1
            if remaining[p] == 0:
                q.append(p)

    # CLAUSE: count_required_operations
    printed.append(str(ops))

sys.stdout.write("\n".join(printed))


