import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    x = tokens[1]
    return x, tokens[2:2 + n]


# --- clause: teaching_time :: (x: int, chapters: list[int]) -> int ---
def teaching_time(x, chapters):
    amount = 0
    for count in sorted(chapters):
        amount += count * x
        if x > 1:
            x -= 1
    return amount


# --- clause: main :: () -> None ---
def main():
    x, chapters = read_input()
    sys.stdout.write("%d\n" % teaching_time(x, chapters))


if __name__ == "__main__":
    main()
