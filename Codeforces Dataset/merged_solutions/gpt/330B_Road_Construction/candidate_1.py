import sys

# CLAUSE: parse_forbidden_pairs
data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]
pairs = data[2:]

# CLAUSE: mark_blocked_endpoints
blocked = [False] * (n + 1)
for i in range(0, 2 * m, 2):
    blocked[pairs[i]] = True
    blocked[pairs[i + 1]] = True

# CLAUSE: select_unrestricted_center
center = 1
while blocked[center]:
    center += 1

# CLAUSE: prove_star_minimality
road_count = n - 1

# CLAUSE: generate_star_edges
edges = []
for city in range(1, n + 1):
    if city != center:
        edges.append((center, city))

# CLAUSE: format_construction_output
out = [str(road_count)]
out.extend(f"{a} {b}" for a, b in edges)
sys.stdout.write("\n".join(out))
