import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    return x, data[2:2 + n]


# --- clause: teaching_time :: (x: int, chapters: list[int]) -> int ---
def teaching_time(x, chapters):
    total = 0
    for count in sorted(chapters):
        total += count * x
        if x > 1:
            x -= 1
    return total


# --- clause: main :: () -> None ---
def main():
    x, chapters = read_input()
    sys.stdout.write("%d\n" % teaching_time(x, chapters))


if __name__ == "__main__":
    main()
