# CLAUSE: root_target_tree
import sys

def answer_one(n, edge_list):
    adj = [[] for _ in range(n + 1)]
    for u, v in edge_list:
        adj[u].append(v)
        adj[v].append(u)

    parent = [0] * (n + 1)
    depth = [-1] * (n + 1)
    depth[n] = 0
    stack = [n]
    preorder = []
    for v in stack:
        preorder.append(v)
        for u in adj[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                parent[u] = v
                stack.append(u)

# CLAUSE: derive_escape_path
    corridor_mark = bytearray(n + 1)
    v = 1
    while v:
        corridor_mark[v] = 1
        if v == n:
            break
        v = parent[v]

# CLAUSE: partition_side_subtrees
    removed_later = []
    removed_on_path = []
    for v in preorder:
        if v == n:
            continue
        if corridor_mark[v]:
            removed_on_path.append(v)
        else:
            removed_later.append(v)
    removed_later.sort(key=depth.__getitem__, reverse=True)
    removed_on_path.sort(key=depth.__getitem__, reverse=True)
    sequence = removed_later + removed_on_path

# CLAUSE: schedule_safe_deletions
    operations = []
    reachable_parity = depth[1] & 1
    for v in sequence:
        vertex_parity = depth[v] & 1
        move_count = 1 + (reachable_parity != vertex_parity)

# CLAUSE: enforce_walk_progress
        while move_count:
            operations.append("1")
            reachable_parity ^= 1
            move_count -= 1

# CLAUSE: maintain_reachable_frontier
        operations.append("2 " + repr(v))

# CLAUSE: finalize_target_arrival
    return operations

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    lines = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        edges = []
        for _ in range(n - 1):
            u = int(data[pos])
            v = int(data[pos + 1])
            pos += 2
            edges.append((u, v))
        ops = answer_one(n, edges)
        lines.append(str(len(ops)))
        lines.extend(ops)
    sys.stdout.write("\n".join(lines))

main()
