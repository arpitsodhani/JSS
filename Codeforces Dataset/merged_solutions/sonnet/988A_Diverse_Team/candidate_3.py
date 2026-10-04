import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    return k, fields[2:2 + n]


# --- clause: pick_team :: (k: int, ratings: list[int]) -> list[int] | None ---
def pick_team(k, ratings):
    marked = set()
    team = []
    for i in range(len(ratings)):
        if ratings[i] in marked:
            continue
        marked.add(ratings[i])
        team.append(i + 1)
        if len(team) == k:
            return team
    return None


# --- clause: main :: () -> None ---
def main():
    k, ratings = read_input()
    team = pick_team(k, ratings)
    if team is None:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n%s\n" % " ".join(map(str, team)))


if __name__ == "__main__":
    main()
