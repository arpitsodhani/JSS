import sys

# CLAUSE: parse_forbidden_pairs
values = list(map(int, sys.stdin.buffer.read().split()))
n, m = values[:2]

# CLAUSE: mark_blocked_endpoints
marks = bytearray(n + 1)
index = 2
remaining = m
while remaining:
    u = values[index]
    v = values[index + 1]
    marks[u] = 1
    marks[v] = 1
    index += 2
    remaining -= 1

# CLAUSE: select_unrestricted_center
center = marks.index(0, 1)

# CLAUSE: prove_star_minimality
edge_count = n - 1

# CLAUSE: generate_star_edges
lines = [str(edge_count)]
city = 1
while city <= n:
    if city != center:
        lines.append(str(center) + " " + str(city))
    city += 1

# CLAUSE: format_construction_output
sys.stdout.write("\n".join(lines))
