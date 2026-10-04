# CLAUSE: root_target_tree
import sys

def solve_case(n, edges):
    g = [[] for _ in range(n + 1)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)

    parent = [0] * (n + 1)
    depth = [-1] * (n + 1)
    order = []
    stack = [n]
    depth[n] = 0
    while stack:
        v = stack.pop()
        order.append(v)
        for to in g[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            depth[to] = depth[v] + 1
            stack.append(to)

# CLAUSE: derive_escape_path
    corridor = []
    x = 1
    while x:
        corridor.append(x)
        if x == n:
            break
        x = parent[x]
    on_path = [False] * (n + 1)
    for v in corridor:
        on_path[v] = True

# CLAUSE: partition_side_subtrees
    side_nodes = []
    path_nodes = []
    for v in order:
        if v == n:
            continue
        if on_path[v]:
            path_nodes.append(v)
        else:
            side_nodes.append(v)
    deletion_order = sorted(side_nodes + path_nodes, key=lambda z: depth[z], reverse=True)

# CLAUSE: schedule_safe_deletions
    ops = []
    cat_parity = depth[1] & 1
    for v in deletion_order:
        target_parity = depth[v] & 1
        if cat_parity == target_parity:
            ops.append("1")
            cat_parity ^= 1

# CLAUSE: enforce_walk_progress
        else:
            ops.append("1")
            cat_parity ^= 1
            ops.append("1")
            cat_parity ^= 1

# CLAUSE: maintain_reachable_frontier
        ops.append("2 " + str(v))

# CLAUSE: finalize_target_arrival
    return ops

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        p += 1
        edges = []
        for _ in range(n - 1):
            edges.append((data[p], data[p + 1]))
            p += 2
        ans = solve_case(n, edges)
        out.append(str(len(ans)))
        out.extend(ans)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
