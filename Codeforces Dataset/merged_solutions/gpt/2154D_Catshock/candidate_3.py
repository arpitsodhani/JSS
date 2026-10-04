# CLAUSE: root_target_tree
import sys
from collections import deque

def construct(n, edges):
    graph = [[] for _ in range(n + 1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)
    parent[n] = 0
    q = deque([n])
    bfs = []
    while q:
        v = q.popleft()
        bfs.append(v)
        for u in graph[v]:
            if parent[u] == -1:
                parent[u] = v
                depth[u] = depth[v] + 1
                q.append(u)

# CLAUSE: derive_escape_path
    in_corridor = [0] * (n + 1)
    node = 1
    while node != 0:
        in_corridor[node] = 1
        if node == n:
            break
        node = parent[node]

# CLAUSE: partition_side_subtrees
    side_by_depth = {}
    path_by_depth = {}
    for v in bfs:
        if v == n:
            continue
        if in_corridor[v]:
            path_by_depth.setdefault(depth[v], []).append(v)
        else:
            side_by_depth.setdefault(depth[v], []).append(v)

    removable = []
    for d in range(max(depth), -1, -1):
        removable.extend(side_by_depth.get(d, ()))
        removable.extend(path_by_depth.get(d, ()))

# CLAUSE: schedule_safe_deletions
    program = []
    frontier_parity = depth[1] & 1
    for v in removable:
        if frontier_parity == (depth[v] & 1):

# CLAUSE: enforce_walk_progress
            program.append("1")
            frontier_parity ^= 1
        else:
            program.extend(("1", "1"))

# CLAUSE: maintain_reachable_frontier
        program.append("2 %d" % v)

# CLAUSE: finalize_target_arrival
    return program

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = nums[idx]
    idx += 1
    output = []
    for _ in range(t):
        n = nums[idx]
        idx += 1
        edges = []
        for _ in range(n - 1):
            edges.append((nums[idx], nums[idx + 1]))
            idx += 2
        ans = construct(n, edges)
        output.append(str(len(ans)))
        output.extend(ans)
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
