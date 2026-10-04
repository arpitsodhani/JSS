# CLAUSE: root_target_tree
import sys

def make_program(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [n]
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for to in adj[v]:
            if to != parent[v]:
                parent[to] = v
                depth[to] = depth[v] + 1
                order.append(to)

# CLAUSE: derive_escape_path
    path_flag = [False] * (n + 1)
    path = []
    x = 1
    while True:
        path.append(x)
        path_flag[x] = True
        if x == n:
            break
        x = parent[x]

# CLAUSE: partition_side_subtrees
    by_depth = [[] for _ in range(n)]
    for v in range(1, n + 1):
        if v != n:
            by_depth[depth[v]].append(v)

    deletion = []
    for d in range(n - 1, -1, -1):
        if not by_depth[d]:
            continue
        for v in by_depth[d]:
            if not path_flag[v]:
                deletion.append(v)
        for v in by_depth[d]:
            if path_flag[v]:
                deletion.append(v)

# CLAUSE: schedule_safe_deletions
    ops = []
    parity = depth[1] % 2
    for v in deletion:
        safe_now = parity != (depth[v] % 2)

# CLAUSE: enforce_walk_progress
        ops.append("1")
        parity ^= 1
        if safe_now:
            ops.append("1")
            parity ^= 1

# CLAUSE: maintain_reachable_frontier
        ops.append("2 " + str(v))

# CLAUSE: finalize_target_arrival
    return ops

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 1
    out = []
    for _ in range(values[0]):
        n = values[ptr]
        ptr += 1
        edges = [(values[i], values[i + 1]) for i in range(ptr, ptr + 2 * (n - 1), 2)]
        ptr += 2 * (n - 1)
        ops = make_program(n, edges)
        out.append(str(len(ops)))
        out.extend(ops)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
