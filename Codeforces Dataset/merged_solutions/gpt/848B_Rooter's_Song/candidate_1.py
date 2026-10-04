# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit()

n, w, h = data[0], data[1], data[2]
groups = defaultdict(lambda: [[], []])

idx = 3
for i in range(n):
    g, p, t = data[idx], data[idx + 1], data[idx + 2]
    idx += 3
    groups[p - t][g - 1].append((p, i))

ans = [None] * n

for verticals, horizontals in groups.values():
    verticals.sort()
    horizontals.sort(reverse=True)

    order = [i for _, i in horizontals] + [i for _, i in verticals]
    exits = [(p, h) for p, _ in verticals] + [(w, p) for p, _ in horizontals]

    for dancer, pos in zip(order, exits):
        ans[dancer] = pos

sys.stdout.write("\n".join(f"{x} {y}" for x, y in ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
