import sys


# --- clause: read_input :: () -> list[tuple[str, int, int]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    friends = []
    for i in range(n):
        friends.append((raw[1 + 3 * i].decode(), int(raw[2 + 3 * i]), int(raw[3 + 3 * i])))
    return friends


# --- clause: best_day :: (friends: list[tuple[str, int, int]]) -> int ---
def best_day(friends):
    men = [0] * 370
    women = [0] * 370
    for gender, head_pos, end in friends:
        table = men if gender == "M" else women
        for day in range(head_pos, end + 1):
            table[day] += 1
    top = 0
    for day in range(1, 367):
        pairs = men[day] if men[day] < women[day] else women[day]
        if pairs > top:
            top = pairs
    return 2 * top


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_day(read_input()))


if __name__ == "__main__":
    main()
