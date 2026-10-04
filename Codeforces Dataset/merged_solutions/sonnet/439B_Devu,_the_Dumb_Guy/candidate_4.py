import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    x = numbers[1]
    return x, numbers[2:2 + n]


# --- clause: teaching_time :: (x: int, chapters: list[int]) -> int ---
def teaching_time(x, chapters):
    order = sorted(chapters)
    total = 0
    for i in range(len(order)):
        rate = x - i
        if rate < 1:
            rate = 1
        total += order[i] * rate
    return total


# --- clause: main :: () -> None ---
def main():
    x, chapters = read_input()
    sys.stdout.write("%d\n" % teaching_time(x, chapters))


if __name__ == "__main__":
    main()
