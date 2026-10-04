import sys
from collections import deque

# CLAUSE: normalize_match_constraints
def normalize_match_constraints():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return 0, []
    count = raw[1]
    pairs = [None] * count
    at = 2
    for i in range(count):
        pairs[i] = (raw[at], raw[at + 1])
        at += 2
    return raw[0], pairs

# CLAUSE: test_unique_order_prefix
def test_unique_order_prefix(robot_count, ordered_edges, prefix_len):
    heads, indeg = build_prefix_graph(robot_count, ordered_edges, prefix_len)
    return perform_topological_uniqueness_check(robot_count, heads, indeg)

# CLAUSE: build_prefix_graph
def build_prefix_graph(robot_count, ordered_edges, prefix_len):
    heads = [[] for _ in range(robot_count + 1)]
    incoming = [0] * (robot_count + 1)
    for idx in range(prefix_len):
        a, b = ordered_edges[idx]
        heads[a].append(b)
        incoming[b] += 1
    return heads, incoming

# CLAUSE: maintain_indegree_counts
def collect_sources(robot_count, incoming):
    sources = deque()
    for robot in range(1, robot_count + 1):
        if incoming[robot] == 0:
            sources.append(robot)
    return sources

# CLAUSE: perform_topological_uniqueness_check
def perform_topological_uniqueness_check(robot_count, heads, incoming):
    sources = collect_sources(robot_count, incoming)
    placed = 0
    while sources:
        if len(sources) > 1:
            return False
        cur = sources.popleft()
        placed += 1
        for nxt in heads[cur]:
            incoming[nxt] -= 1
            if incoming[nxt] == 0:
                sources.append(nxt)
    return placed == robot_count

# CLAUSE: binary_search_minimum_prefix
def binary_search_minimum_prefix(robot_count, ordered_edges):
    low = 0
    high = len(ordered_edges)
    while low < high:
        middle = low + (high - low) // 2
        if test_unique_order_prefix(robot_count, ordered_edges, middle):
            high = middle
        else:
            low = middle + 1
    return low

# CLAUSE: validate_final_possibility
def validate_final_possibility():
    robot_count, ordered_edges = normalize_match_constraints()
    if robot_count == 0:
        return
    candidate = binary_search_minimum_prefix(robot_count, ordered_edges)
    if candidate == len(ordered_edges) and not test_unique_order_prefix(robot_count, ordered_edges, candidate):
        print(-1)
    else:
        print(candidate)

validate_final_possibility()
