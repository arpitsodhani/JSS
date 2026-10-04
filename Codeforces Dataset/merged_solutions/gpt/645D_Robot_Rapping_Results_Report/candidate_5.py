import sys
from collections import deque

# CLAUSE: normalize_match_constraints
def normalize_match_constraints():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return 0, []
    total_edges = values[1]
    reports = [(values[j], values[j + 1]) for j in range(2, 2 + total_edges * 2, 2)]
    return values[0], reports

# CLAUSE: test_unique_order_prefix
def test_unique_order_prefix(n, reports, end):
    graph, indeg = build_prefix_graph(n, reports, end)
    zeros = maintain_indegree_counts(n, indeg)
    return perform_topological_uniqueness_check(n, graph, indeg, zeros)

# CLAUSE: build_prefix_graph
def build_prefix_graph(n, reports, end):
    graph = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    for winner, loser in reports[:end]:
        graph[winner].append(loser)
        indeg[loser] += 1
    return graph, indeg

# CLAUSE: maintain_indegree_counts
def maintain_indegree_counts(n, indeg):
    return deque(i for i in range(1, n + 1) if indeg[i] == 0)

# CLAUSE: perform_topological_uniqueness_check
def perform_topological_uniqueness_check(n, graph, indeg, zeros):
    taken = 0
    while True:
        if not zeros:
            break
        if len(zeros) != 1:
            return False
        u = zeros.popleft()
        taken += 1
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                zeros.append(v)
    return taken == n

# CLAUSE: binary_search_minimum_prefix
def binary_search_minimum_prefix(n, reports):
    lo = 0
    hi = len(reports) + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if test_unique_order_prefix(n, reports, mid):
            hi = mid
        else:
            lo = mid
    return hi

# CLAUSE: validate_final_possibility
def validate_final_possibility():
    n, reports = normalize_match_constraints()
    if n == 0:
        return
    answer = binary_search_minimum_prefix(n, reports)
    if answer == len(reports) + 1:
        print(-1)
    else:
        print(answer)

validate_final_possibility()
