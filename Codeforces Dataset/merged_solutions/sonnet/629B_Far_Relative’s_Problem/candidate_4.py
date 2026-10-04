import sys


# --- clause: read_input :: () -> list[tuple[str, int, int]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    friends = []
    for i in range(n):
        friends.append((numbers[1 + 3 * i].decode(), int(numbers[2 + 3 * i]), int(numbers[3 + 3 * i])))
    return friends


# --- clause: best_day :: (friends: list[tuple[str, int, int]]) -> int ---
def best_day(friends):
    men = [0] * 372
    women = [0] * 372
    for gender, start, end in friends:
        table = men if gender == "M" else women
        table[start] += 1
        table[end + 1] -= 1
    best = 0
    here = 0
    there = 0
    for day in range(1, 367):
        here += men[day]
        there += women[day]
        pairs = here if here < there else there
        if pairs > best:
            best = pairs
    return 2 * best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % best_day(read_input()))


if __name__ == "__main__":
    main()
