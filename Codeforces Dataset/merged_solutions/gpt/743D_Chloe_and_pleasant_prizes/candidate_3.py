import sys

# CLAUSE: build_tree_adjacency
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n = int(raw[0])
    pleasant = [0] + [int(x) for x in raw[1:n + 1]]
    neighbors = [[] for _ in range(n + 1)]
    idx = n + 1
    while idx < len(raw):
        u = int(raw[idx])
        v = int(raw[idx + 1])
        idx += 2
        neighbors[u].append(v)
        neighbors[v].append(u)

# CLAUSE: orient_parent_child_order
    parent = [-2] * (n + 1)
    parent[1] = 0
    order = []
    stack = [(1, 0)]
    while stack:
        v, p = stack.pop()
        order.append(v)
        for to in neighbors[v]:
            if to == p:
                continue
            parent[to] = v
            stack.append((to, v))

# CLAUSE: accumulate_subtree_sums
    sub = pleasant[:]
    for v in order[::-1]:
        p = parent[v]
        if p:
            sub[p] += sub[v]

# CLAUSE: propagate_best_subtree
    best = sub[:]

# CLAUSE: combine_disjoint_branches
    found = False
    ans = 0
    for v in order[::-1]:
        top = []
        for to in neighbors[v]:
            if parent[to] == v:
                top.append(best[to])
                if len(top) > 2:
                    top.sort(reverse=True)
                    top.pop()

# CLAUSE: track_global_answer
        if len(top) == 2:
            current = top[0] + top[1]
            if not found or current > ans:
                ans = current
                found = True
        for to in neighbors[v]:
            if parent[to] == v and best[to] > best[v]:
                best[v] = best[to]

# CLAUSE: emit_impossible_or_score
    print(ans if found else "Impossible")

if __name__ == "__main__":
    main()
