import sys

# CLAUSE: parse_forbidden_pairs
it = iter(map(int, sys.stdin.buffer.read().split()))
n = next(it)
m = next(it)

# CLAUSE: mark_blocked_endpoints
free = [True] * (n + 1)
for _ in range(m):
    first = next(it)
    second = next(it)
    free[first] = False
    free[second] = False

# CLAUSE: select_unrestricted_center
for candidate in range(1, n + 1):
    if free[candidate]:
        center = candidate
        break

# CLAUSE: prove_star_minimality
total_edges = n - 1

# CLAUSE: generate_star_edges
def star_lines(center_city, city_count):
    for other in range(1, city_count + 1):
        if other == center_city:
            continue
        yield f"{center_city} {other}"

# CLAUSE: format_construction_output
sys.stdout.write("\n".join([str(total_edges), *star_lines(center, n)]))
