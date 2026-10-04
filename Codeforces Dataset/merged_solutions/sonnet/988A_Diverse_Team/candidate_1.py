import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]


# --- clause: pick_team :: (k: int, ratings: list[int]) -> list[int] | None ---
def pick_team(k, ratings):
    seen = set()
    team = []
    for i in range(len(ratings)):
        if ratings[i] in seen:
            continue
        seen.add(ratings[i])
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
