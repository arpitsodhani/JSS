import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    games = []
    for line in sys.stdin.read().split("\n"):
        line = line.strip()
        if not line:
            continue
        first, second, score = line.split()
        left, right = score.split(":")
        games.append((first, second, int(left), int(right)))
        if len(games) == 5:
            break
    return games

# Clause find_opponent [Confidence: 1.00]
def find_opponent(games):
    appearances = {}
    for first, second, _, _ in games:
        appearances[first] = appearances.get(first, 0) + 1
        appearances[second] = appearances.get(second, 0) + 1
    teams = sorted(appearances)
    rival = ""
    for team in teams:
        if team != "BERLAND" and appearances[team] == 2:
            rival = team
    return rival, teams

# Clause berland_place [Confidence: 1.00]
def berland_place(games, teams):
    points = dict.fromkeys(teams, 0)
    scored = dict.fromkeys(teams, 0)
    missed = dict.fromkeys(teams, 0)
    for host, guest, goals1, goals2 in games:
        scored[host] += goals1
        missed[host] += goals2
        scored[guest] += goals2
        missed[guest] += goals1
        if goals1 == goals2:
            points[host] += 1
            points[guest] += 1
        elif goals1 > goals2:
            points[host] += 3
        else:
            points[guest] += 3
    table = sorted(teams, key=lambda t: (-points[t], missed[t] - scored[t], -scored[t], t))
    return table.index("BERLAND")

# Clause search_score [Confidence: 1.00]
def search_score(games, rival, teams):
    for diff in range(1, 101):
        for lost in range(0, 101):
            trial = games + [("BERLAND", rival, lost + diff, lost)]
            if berland_place(trial, teams) < 2:
                return "%d:%d" % (lost + diff, lost)
    return "IMPOSSIBLE"

# Clause main [Confidence: 1.00]
def main():
    games = read_input()
    rival, teams = find_opponent(games)
    sys.stdout.write(search_score(games, rival, teams) + "\n")


if __name__ == "__main__":
    main()

