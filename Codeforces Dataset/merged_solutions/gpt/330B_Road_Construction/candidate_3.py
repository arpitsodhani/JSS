import sys

# CLAUSE: parse_forbidden_pairs
raw = sys.stdin.buffer.read().split()
n = int(raw[0])
m = int(raw[1])
forbidden_pairs = [(int(raw[i]), int(raw[i + 1])) for i in range(2, 2 + 2 * m, 2)]

# CLAUSE: mark_blocked_endpoints
endpoint_seen = [0] * (n + 1)
for a, b in forbidden_pairs:
    endpoint_seen[a] = 1
    endpoint_seen[b] = 1

# CLAUSE: select_unrestricted_center
center = 0
for city in range(1, n + 1):
    if endpoint_seen[city] == 0:
        center = city
        break

# CLAUSE: prove_star_minimality
roads_needed = n - 1

# CLAUSE: generate_star_edges
constructed = [(center, city) for city in range(1, n + 1) if city != center]

# CLAUSE: format_construction_output
print(roads_needed)
for a, b in constructed:
    print(a, b)
