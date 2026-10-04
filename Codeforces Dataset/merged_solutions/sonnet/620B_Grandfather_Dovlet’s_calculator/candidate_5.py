import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: total_segments :: (a: int, b: int) -> int ---
def total_segments(a, b):
    per_digit = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
    running = [0] * (b + 1)
    for number in range(1, b + 1):
        running[number] = running[number // 10] + per_digit[number % 10]
    return sum(running[a:b + 1])


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(str(total_segments(a, b)) + "\n")


if __name__ == "__main__":
    main()
