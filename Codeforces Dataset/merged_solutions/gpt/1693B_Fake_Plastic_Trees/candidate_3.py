import sys

arr = list(map(int, sys.stdin.buffer.read().split()))
pos = 0
tc = arr[pos]
pos += 1
res = []

for _ in range(tc):
    n = arr[pos]
    pos += 1

    # CLAUSE: build_child_adjacency
    head = [-1] * (n + 1)
    to = [0] * max(1, n - 1)
    nxt = [0] * max(1, n - 1)
    edge = 0
    for v in range(2, n + 1):
        p = arr[pos]
        pos += 1
        to[edge] = v
        nxt[edge] = head[p]
        head[p] = edge
        edge += 1

    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for v in range(1, n + 1):
        left[v] = arr[pos]
        right[v] = arr[pos + 1]
        pos += 2

    # CLAUSE: traverse_subtree_postorder
    order = []
    stack = [1]
    while stack:
        v = stack.pop()
        order.append(v)
        e = head[v]
        while e != -1:
            stack.append(to[e])
            e = nxt[e]

    dp = [0] * (n + 1)
    need = 0

    for v in order[::-1]:
        # CLAUSE: aggregate_child_capacity
        s = 0
        e = head[v]
        while e != -1:
            s += dp[to[e]]
            e = nxt[e]

        # CLAUSE: enforce_vertex_lower_bound
        if s < left[v]:
            need += 1

            # CLAUSE: cap_vertex_contribution
            dp[v] = right[v]
        else:
            # CLAUSE: cap_vertex_contribution
            dp[v] = min(s, right[v])

    # CLAUSE: count_required_operations
    res.append(str(need))

print("\n".join(res))
