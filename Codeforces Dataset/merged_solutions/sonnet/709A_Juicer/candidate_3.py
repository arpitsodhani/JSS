import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    b = fields[1]
    d = fields[2]
    return b, d, fields[3:3 + n]


# --- clause: count_empties :: (b: int, d: int, sizes: list[int]) -> int ---
def count_empties(b, d, sizes):
    waste = 0
    times = 0
    for element in sizes:
        if element > b:
            continue
        waste += element
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
