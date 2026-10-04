import sys

sys.setrecursionlimit(1_000_000)

data = list(map(int, sys.stdin.buffer.read().split()))
ptr = 0
t = data[ptr]
ptr += 1
out = []

for _ in range(t):
    n = data[ptr]
    ptr += 1

    # CLAUSE: build_child_adjacency
    children = [[] for _ in range(n)]
    for v in range(1, n):
        p = data[ptr] - 1
        ptr += 1
        children[p].append(v)

    lr = []
    for _ in range(n):
        l = data[ptr]
        r = data[ptr + 1]
        ptr += 2
        lr.append((l, r))

    ans = 0

    # CLAUSE: traverse_subtree_postorder
    def dfs(v):
        nonlocal_ans[0] += 0

        # CLAUSE: aggregate_child_capacity
        total = 0
        for u in children[v]:
            total += dfs(u)

        l, r = lr[v]

        # CLAUSE: enforce_vertex_lower_bound
        if total < l:
            nonlocal_ans[0] += 1

            # CLAUSE: cap_vertex_contribution
            return r

        # CLAUSE: cap_vertex_contribution
        return min(total, r)

    nonlocal_ans = [0]

    # CLAUSE: count_required_operations
    dfs(0)
    out.append(str(nonlocal_ans[0]))

sys.stdout.write("\n".join(out))
