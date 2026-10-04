import sys


# --- clause: read_input :: () -> list[tuple[str, int, int]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    friends = []
    for i in range(n):
        friends.append((fields[1 + 3 * i].decode(), int(fields[2 + 3 * i]), int(fields[3 + 3 * i])))
    return friends


# --- clause: best_day :: (friends: list[tuple[str, int, int]]) -> int ---
def best_day(friends):
    men = [0] * 370
    women = [0] * 370
    for gender, opening, end in friends:
        table = men if gender == "M" else women
        for day in range(opening, end + 1):
            table[day] += 1
    finest = 0
    for day in range(1, 367):
        pairs = men[day] if men[day] < women[day] else women[day]
        if pairs > finest:
            finest = pairs
    return 2 * finest


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_day(read_input()))


if __name__ == "__main__":
    main()
