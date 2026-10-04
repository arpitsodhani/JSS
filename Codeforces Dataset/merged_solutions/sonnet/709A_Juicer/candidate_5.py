import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    b = raw[1]
    d = raw[2]
    return b, d, raw[3:3 + n]


# --- clause: count_empties :: (b: int, d: int, sizes: list[int]) -> int ---
def count_empties(b, d, sizes):
    waste = 0
    times = 0
    for number in sizes:
        if number > b:
            continue
        waste += number
        if waste > d:
            waste = 0
            times += 1
    return times


# --- clause: main :: () -> None ---
def main():
    b, d, sizes = read_input()
    sys.stdout.write("%d\n" % count_empties(b, d, sizes))


if __name__ == "__main__":
    main()
