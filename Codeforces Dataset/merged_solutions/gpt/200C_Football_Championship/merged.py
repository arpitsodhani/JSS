# CLAUSE: setup_environment
import sys
from itertools import combinations

# CLAUSE: solve_logic
data = sys.stdin.read().split()

games = []
teams = set()

for i in range(0, len(data), 3):
    a = data[i]
    b = data[i + 1]
    x, y = map(int, data[i + 2].split(":"))
    games.append((a, b, x, y))
    teams.add(a)
    teams.add(b)

stats0 = {t: [0, 0, 0] for t in teams}

played = set()
for a, b, x, y in games:
    played.add(tuple(sorted((a, b))))
    stats0[a][1] += x
    stats0[a][2] += y
    stats0[b][1] += y
    stats0[b][2] += x
    if x > y:
        stats0[a][0] += 3
    elif x < y:
        stats0[b][0] += 3
    else:
        stats0[a][0] += 1
        stats0[b][0] += 1

opponent = None
for a, b in combinations(teams, 2):
    if tuple(sorted((a, b))) not in played:
        if a == "BERLAND":
            opponent = b
        elif b == "BERLAND":
            opponent = a
        break

def qualifies(bg, og):
    stats = {t: stats0[t][:] for t in teams}

    stats["BERLAND"][1] += bg
    stats["BERLAND"][2] += og
    stats[opponent][1] += og
    stats[opponent][2] += bg

    if bg > og:
        stats["BERLAND"][0] += 3
    elif bg < og:
        stats[opponent][0] += 3
    else:
        stats["BERLAND"][0] += 1
        stats[opponent][0] += 1

    order = sorted(
        teams,
        key=lambda t: (-stats[t][0], -(stats[t][1] - stats[t][2]), -stats[t][1], t)
    )
    return order.index("BERLAND") < 2

for bg in range(101):
    for og in range(101):
        if qualifies(bg, og):
            print(f"{bg}:{og}")
            sys.exit()

print("IMPOSSIBLE")

# CLAUSE: finish_program
RESULT_SENTINEL = None
