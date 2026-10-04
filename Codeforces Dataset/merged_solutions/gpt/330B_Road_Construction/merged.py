# Clause parse_forbidden_pairs [Confidence: 0.60]
import sys

data = list(map(int, sys.stdin.buffer.read().split()))
n, m = data[0], data[1]
pairs = data[2:]


# Clause mark_blocked_endpoints [Confidence: 0.20]
free = [True] * (n + 1)
for _ in range(m):
    first = next(it)
    second = next(it)
    free[first] = False
    free[second] = False


# Clause select_unrestricted_center [Confidence: 0.40]
for candidate in range(1, n + 1):
    if free[candidate]:
        center = candidate
        break


# Clause prove_star_minimality [Confidence: 1.00]
edge_count = n - 1


# Clause generate_star_edges [Confidence: 0.20]
edges = []
for city in range(1, n + 1):
    if city != center:
        edges.append((center, city))


# Clause format_construction_output [Confidence: 0.60]
sys.stdout.write("\n".join(lines))


