import sys


# --- clause: read_input :: () -> list[tuple[str, str, int, int]] ---
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


# --- clause: find_opponent :: (games: list) -> tuple[str, list[str]] ---
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

# --- clause: berland_place :: (games: list, teams: list[str]) -> int ---
def berland_place(games, teams):
    points = dict.fromkeys(teams, 0)
    scored = dict.fromkeys(teams, 0)
    missed = dict.fromkeys(teams, 0)
    for first, second, goals1, goals2 in games:
        scored[first] += goals1
        missed[first] += goals2
        scored[second] += goals2
        missed[second] += goals1
        if goals1 > goals2:
            points[first] += 3
        elif goals1 < goals2:
            points[second] += 3
        else:
            points[first] += 1
            points[second] += 1

    keys = {}
    for team in teams:
        keys[team] = (-points[team], missed[team] - scored[team], -scored[team], team)
    mine = keys["BERLAND"]
    ahead = 0
    for team in teams:
        if keys[team] < mine:
            ahead += 1
    return ahead

# --- clause: search_score :: (games: list, rival: str, teams: list[str]) -> str ---
def search_score(games, rival, teams):
    for diff in range(1, 101):
        for lost in range(0, 101):
            trial = games + [("BERLAND", rival, lost + diff, lost)]
            if berland_place(trial, teams) < 2:
                return "%d:%d" % (lost + diff, lost)
    return "IMPOSSIBLE"

# --- clause: main :: () -> None ---
def main():
    games = read_input()
    rival, teams = find_opponent(games)
    sys.stdout.write(search_score(games, rival, teams) + "\n")


if __name__ == "__main__":
    main()
