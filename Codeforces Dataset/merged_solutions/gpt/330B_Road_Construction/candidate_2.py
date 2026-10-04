import sys

# CLAUSE: parse_forbidden_pairs
tokens = sys.stdin.buffer.read().split()
n = int(tokens[0])
m = int(tokens[1])

# CLAUSE: mark_blocked_endpoints
restricted = set()
pos = 2
for _ in range(m):
    a = int(tokens[pos])
    b = int(tokens[pos + 1])
    restricted.add(a)
    restricted.add(b)
    pos += 2

# CLAUSE: select_unrestricted_center
center = next(city for city in range(1, n + 1) if city not in restricted)

# CLAUSE: prove_star_minimality
minimum_roads = n - 1

# CLAUSE: generate_star_edges
answer_lines = []
for city in range(1, center):
    answer_lines.append(f"{center} {city}")
for city in range(center + 1, n + 1):
    answer_lines.append(f"{center} {city}")

# CLAUSE: format_construction_output
sys.stdout.write(str(minimum_roads) + "\n" + "\n".join(answer_lines))
