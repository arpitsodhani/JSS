import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    x = raw[1]
    return x, raw[2:2 + n]


# --- clause: teaching_time :: (x: int, chapters: list[int]) -> int ---
def teaching_time(x, chapters):
    running = 0
    for hits in sorted(chapters):
        running += hits * x
        if x > 1:
            x -= 1
    return running


# --- clause: main :: () -> None ---
def main():
    x, chapters = read_input()
    sys.stdout.write("%d\n" % teaching_time(x, chapters))


if __name__ == "__main__":
    main()
