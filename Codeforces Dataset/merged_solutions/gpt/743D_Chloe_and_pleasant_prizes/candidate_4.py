import sys

# CLAUSE: build_tree_adjacency
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    cost = [0] + data[1:n + 1]
    graph = [[] for _ in range(n + 1)]
    for u, v in zip(data[n + 1::2], data[n + 2::2]):
        graph[u].append(v)
        graph[v].append(u)

# CLAUSE: orient_parent_child_order
    sys.setrecursionlimit(1_000_000)
    parent = [0] * (n + 1)
    order = []

    def dfs(v, p):
        parent[v] = p
        for u in graph[v]:
            if u != p:
                dfs(u, v)
        order.append(v)

    dfs(1, -1)

# CLAUSE: accumulate_subtree_sums
    subtotal = [0] * (n + 1)
    for v in order:
        subtotal[v] = cost[v] + sum(subtotal[u] for u in graph[v] if parent[u] == v)

# CLAUSE: propagate_best_subtree
    strongest = [0] * (n + 1)

# CLAUSE: combine_disjoint_branches
    minus_inf = -10 ** 20
    result = minus_inf
    for v in order:
        largest = minus_inf
        runner_up = minus_inf
        child_best = []
        for u in graph[v]:
            if parent[u] == v:
                child_best.append(strongest[u])
        for x in child_best:
            if x >= largest:
                largest, runner_up = x, largest
            elif x > runner_up:
                runner_up = x

# CLAUSE: track_global_answer
        if runner_up != minus_inf:
            result = max(result, largest + runner_up)
        strongest[v] = subtotal[v]
        if child_best:
            strongest[v] = max(strongest[v], max(child_best))

# CLAUSE: emit_impossible_or_score
    sys.stdout.write("Impossible\n" if result == minus_inf else f"{result}\n")

if __name__ == "__main__":
    main()
