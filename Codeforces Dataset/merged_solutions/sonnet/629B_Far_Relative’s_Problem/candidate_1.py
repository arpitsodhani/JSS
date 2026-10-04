import sys


# --- clause: read_input :: () -> list[tuple[str, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    friends = []
    for i in range(n):
        friends.append((data[1 + 3 * i].decode(), int(data[2 + 3 * i]), int(data[3 + 3 * i])))
    return friends


# --- clause: best_day :: (friends: list[tuple[str, int, int]]) -> int ---
def best_day(friends):
    men = [0] * 370
    women = [0] * 370
    for gender, start, end in friends:
        table = men if gender == "M" else women
        for day in range(start, end + 1):
            table[day] += 1
    best = 0
    for day in range(1, 367):
        pairs = men[day] if men[day] < women[day] else women[day]
        if pairs > best:
            best = pairs
    return 2 * best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_day(read_input()))


if __name__ == "__main__":
    main()
