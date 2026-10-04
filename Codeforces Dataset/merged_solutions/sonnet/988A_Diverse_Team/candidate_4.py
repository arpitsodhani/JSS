import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: pick_team :: (k: int, ratings: list[int]) -> list[int] | None ---
def pick_team(k, ratings):
    first = {}
    for i in range(len(ratings) - 1, -1, -1):
        first[ratings[i]] = i + 1
    if len(first) < k:
        return None
    team = sorted(first.values())
    return team[:k]


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
