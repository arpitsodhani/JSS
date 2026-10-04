import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    b = numbers[1]
    d = numbers[2]
    return b, d, numbers[3:3 + n]


# --- clause: count_empties :: (b: int, d: int, sizes: list[int]) -> int ---
def count_empties(b, d, sizes):
    waste = 0
    times = 0
    spot = 0
    while spot < len(sizes):
        value = sizes[spot]
        spot += 1
        if value > b:
            continue
        waste += value
        if waste <= d:
            continue
        waste = 0
        times += 1
    return times


# --- clause: main :: () -> None ---
def main():
    b, d, sizes = read_input()
    sys.stdout.write("%d\n" % count_empties(b, d, sizes))


if __name__ == "__main__":
    main()
