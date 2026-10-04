import sys

# CLAUSE: build_tree_adjacency
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    weight = [0] + data[1:1 + n]
    graph = [[] for _ in range(n + 1)]
    pos = 1 + n
    for _ in range(n - 1):
        u, v = data[pos], data[pos + 1]
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

# CLAUSE: orient_parent_child_order
    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        node = stack.pop()
        order.append(node)
        for nxt in graph[node]:
            if nxt == parent[node]:
                continue
            parent[nxt] = node
            children[node].append(nxt)
            stack.append(nxt)

# CLAUSE: accumulate_subtree_sums
    subtree_sum = weight[:]
    for node in reversed(order):
        for child in children[node]:
            subtree_sum[node] += subtree_sum[child]

# CLAUSE: propagate_best_subtree
    best_subtree = subtree_sum[:]

# CLAUSE: combine_disjoint_branches
    neg_inf = -10 ** 30
    answer = neg_inf
    for node in reversed(order):
        first = second = neg_inf
        for child in children[node]:
            candidate = best_subtree[child]
            if candidate > first:
                second = first
                first = candidate
            elif candidate > second:
                second = candidate

# CLAUSE: track_global_answer
        if second != neg_inf:
            answer = max(answer, first + second)
        for child in children[node]:
            if best_subtree[child] > best_subtree[node]:
                best_subtree[node] = best_subtree[child]

# CLAUSE: emit_impossible_or_score
    print("Impossible" if answer == neg_inf else answer)

if __name__ == "__main__":
    main()
