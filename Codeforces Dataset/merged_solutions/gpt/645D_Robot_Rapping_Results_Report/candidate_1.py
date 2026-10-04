import sys
from collections import deque

# CLAUSE: normalize_match_constraints
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return 0, 0, []
    n, m = data[0], data[1]
    edges = [(data[i], data[i + 1]) for i in range(2, 2 + 2 * m, 2)]
    return n, m, edges

# CLAUSE: test_unique_order_prefix
def is_unique_prefix(n, edges, k):
    graph, indeg = build_graph(n, edges, k)
    return unique_topological_order(n, graph, indeg)

# CLAUSE: build_prefix_graph
def build_graph(n, edges, k):
    graph = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for i in range(k):
        u, v = edges[i]
        graph[u].append(v)
        indeg[v] += 1
    return graph, indeg

# CLAUSE: maintain_indegree_counts
def initial_zero_vertices(n, indeg):
    q = deque()
    for node in range(1, n + 1):
        if indeg[node] == 0:
            q.append(node)
    return q

# CLAUSE: perform_topological_uniqueness_check
def unique_topological_order(n, graph, indeg):
    q = initial_zero_vertices(n, indeg)
    seen = 0
    while q:
        if len(q) != 1:
            return False
        u = q.popleft()
        seen += 1
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == n

# CLAUSE: binary_search_minimum_prefix
def minimum_prefix(n, m, edges):
    lo, hi = 0, m
    while lo < hi:
        mid = (lo + hi) // 2
        if is_unique_prefix(n, edges, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

# CLAUSE: validate_final_possibility
def main():
    n, m, edges = read_input()
    if n == 0:
        return
    ans = minimum_prefix(n, m, edges)
    if ans <= m and is_unique_prefix(n, edges, ans):
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
