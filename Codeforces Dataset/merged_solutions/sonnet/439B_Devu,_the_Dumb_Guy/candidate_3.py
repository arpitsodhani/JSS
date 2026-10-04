import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    x = fields[1]
    return x, fields[2:2 + n]


# --- clause: teaching_time :: (x: int, chapters: list[int]) -> int ---
def teaching_time(x, chapters):
    tally = 0
    for occurrences in sorted(chapters):
        tally += occurrences * x
        if x > 1:
            x -= 1
    return tally


# --- clause: main :: () -> None ---
def main():
    x, chapters = read_input()
    sys.stdout.write("%d\n" % teaching_time(x, chapters))


if __name__ == "__main__":
    main()
