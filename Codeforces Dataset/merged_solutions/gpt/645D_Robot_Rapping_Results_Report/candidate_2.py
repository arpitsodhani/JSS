import sys

# CLAUSE: normalize_match_constraints
tokens = list(map(int, sys.stdin.buffer.read().split()))
if tokens:
    n = tokens[0]
    m = tokens[1]
    battles = []
    p = 2
    for _ in range(m):
        battles.append((tokens[p], tokens[p + 1]))
        p += 2
else:
    n = m = 0
    battles = []

# CLAUSE: test_unique_order_prefix
def forced_after(k):
    adj, indegree = make_prefix_graph(k)
    return has_single_topological_order(adj, indegree)

# CLAUSE: build_prefix_graph
def make_prefix_graph(k):
    adj = [set() for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for u, v in battles[:k]:
        if v not in adj[u]:
            adj[u].add(v)
            indegree[v] += 1
    return adj, indegree

# CLAUSE: maintain_indegree_counts
def zero_indegree_list(indegree):
    zeros = []
    for x in range(1, n + 1):
        if indegree[x] == 0:
            zeros.append(x)
    return zeros

# CLAUSE: perform_topological_uniqueness_check
def has_single_topological_order(adj, indegree):
    zeros = zero_indegree_list(indegree)
    done = 0
    while len(zeros) == 1:
        u = zeros.pop()
        done += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                zeros.append(v)
    return done == n

# CLAUSE: binary_search_minimum_prefix
def search_answer():
    left = 0
    right = m + 1
    while right - left > 1:
        mid = (left + right) // 2
        if forced_after(mid):
            right = mid
        else:
            left = mid
    return right

# CLAUSE: validate_final_possibility
if n:
    answer = search_answer()
    print(answer if answer <= m else -1)
