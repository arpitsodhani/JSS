import sys

# CLAUSE: normalize_match_constraints
def parse():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return 0, 0, []
    n, m = nums[:2]
    edges = []
    for i in range(m):
        base = 2 + 2 * i
        edges.append((nums[base], nums[base + 1]))
    return n, m, edges

# CLAUSE: test_unique_order_prefix
def prefix_defines_order(n, edges, length):
    children, indegree = prefix_graph(n, edges, length)
    return kahn_is_unique(n, children, indegree)

# CLAUSE: build_prefix_graph
def prefix_graph(n, edges, length):
    children = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    i = 0
    while i < length:
        winner, loser = edges[i]
        children[winner].append(loser)
        indegree[loser] += 1
        i += 1
    return children, indegree

# CLAUSE: maintain_indegree_counts
def make_frontier(n, indegree):
    frontier = []
    node = 1
    while node <= n:
        if indegree[node] == 0:
            frontier.append(node)
        node += 1
    return frontier

# CLAUSE: perform_topological_uniqueness_check
def kahn_is_unique(n, children, indegree):
    frontier = make_frontier(n, indegree)
    used = 0
    while frontier:
        if len(frontier) != 1:
            return False
        node = frontier.pop()
        used += 1
        for child in children[node]:
            new_value = indegree[child] - 1
            indegree[child] = new_value
            if new_value == 0:
                frontier.append(child)
    return used == n

# CLAUSE: binary_search_minimum_prefix
def find_minimum(n, m, edges):
    left = 0
    right = m
    answer = m + 1
    while left <= right:
        mid = (left + right) // 2
        if prefix_defines_order(n, edges, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

# CLAUSE: validate_final_possibility
def run():
    n, m, edges = parse()
    if n == 0:
        return
    result = find_minimum(n, m, edges)
    print(result if result <= m else -1)

run()
