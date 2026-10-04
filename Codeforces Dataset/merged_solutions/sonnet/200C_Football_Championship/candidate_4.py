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

# --- clause: search_score :: (games: list, rival: str, teams: list[str]) -> str ---
def search_score(games, rival, teams):
    winning = []
    for scored in range(1, 102):
        for lost in range(scored):
            trial = games + [("BERLAND", rival, scored, lost)]
            if berland_place(trial, teams) < 2:
                winning.append((scored - lost, lost, scored))
    if not winning:
        return "IMPOSSIBLE"
    _diff, lost, scored = min(winning)
    return "%d:%d" % (scored, lost)

# --- clause: main :: () -> None ---
def main():
    games = read_input()
    rival, teams = find_opponent(games)
    sys.stdout.write(search_score(games, rival, teams) + "\n")


if __name__ == "__main__":
    main()
