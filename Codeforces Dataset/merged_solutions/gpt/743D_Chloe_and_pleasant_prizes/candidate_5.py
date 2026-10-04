import sys
from collections import deque

# CLAUSE: build_tree_adjacency
def main():
    ints = list(map(int, sys.stdin.buffer.read().split()))
    n = ints[0]
    val = [0] + ints[1:1 + n]
    adj = [[] for _ in range(n + 1)]
    edge_data = ints[1 + n:]
    for i in range(n - 1):
        u = edge_data[2 * i]
        v = edge_data[2 * i + 1]
        adj[u].append(v)
        adj[v].append(u)

# CLAUSE: orient_parent_child_order
    parent = [0] * (n + 1)
    child_lists = [[] for _ in range(n + 1)]
    preorder = []
    q = deque([1])
    parent[1] = -1
    while q:
        v = q.pop()
        preorder.append(v)
        for u in adj[v]:
            if u == parent[v]:
                continue
            parent[u] = v
            child_lists[v].append(u)
            q.append(u)
    post = list(reversed(preorder))

# CLAUSE: accumulate_subtree_sums
    sums = [0] * (n + 1)
    for v in post:
        acc = val[v]
        for u in child_lists[v]:
            acc += sums[u]
        sums[v] = acc

# CLAUSE: propagate_best_subtree
    best_inside = sums[:]

# CLAUSE: combine_disjoint_branches
    possible = False
    best_pair = None
    for v in post:
        first = None
        second = None
        for u in child_lists[v]:
            x = best_inside[u]
            if first is None or x > first:
                second = first
                first = x
            elif second is None or x > second:
                second = x

# CLAUSE: track_global_answer
        if second is not None:
            combined = first + second
            if best_pair is None or combined > best_pair:
                best_pair = combined
                possible = True
        for u in child_lists[v]:
            best_inside[v] = max(best_inside[v], best_inside[u])

# CLAUSE: emit_impossible_or_score
    if possible:
        print(best_pair)
    else:
        print("Impossible")

if __name__ == "__main__":
    main()
