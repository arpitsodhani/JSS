import sys

# CLAUSE: build_tree_adjacency
def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    values = [0] + tokens[1:n + 1]
    adj = [[] for _ in range(n + 1)]
    edges = tokens[n + 1:]
    for i in range(0, len(edges), 2):
        a, b = edges[i], edges[i + 1]
        adj[a].append(b)
        adj[b].append(a)

# CLAUSE: orient_parent_child_order
    sys.setrecursionlimit(max(300000, n * 2 + 10))
    parent = [0] * (n + 1)
    postorder = []
    kids = [[] for _ in range(n + 1)]

    def root_tree(v, p):
        parent[v] = p
        for to in adj[v]:
            if to != p:
                kids[v].append(to)
                root_tree(to, v)
        postorder.append(v)

    root_tree(1, 0)

# CLAUSE: accumulate_subtree_sums
    total = [0] * (n + 1)
    for v in postorder:
        s = values[v]
        for to in kids[v]:
            s += total[to]
        total[v] = s

# CLAUSE: propagate_best_subtree
    best = [0] * (n + 1)

# CLAUSE: combine_disjoint_branches
    answer = None
    for v in postorder:
        candidates = [best[to] for to in kids[v]]
        if len(candidates) >= 2:
            candidates.sort(reverse=True)

# CLAUSE: track_global_answer
            score = candidates[0] + candidates[1]
            answer = score if answer is None or score > answer else answer
        best[v] = total[v]
        for to in kids[v]:
            if best[to] > best[v]:
                best[v] = best[to]

# CLAUSE: emit_impossible_or_score
    sys.stdout.write("Impossible\n" if answer is None else str(answer) + "\n")

if __name__ == "__main__":
    main()
