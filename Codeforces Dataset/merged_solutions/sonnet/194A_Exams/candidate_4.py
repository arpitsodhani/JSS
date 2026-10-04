import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1]


# --- clause: failed_exams :: (n: int, k: int) -> int ---
def failed_exams(n, k):
    twos = 0
    left = k
    for i in range(n):
        if left - 3 * (n - i - 1) < 3:
            twos += 1
            left -= 2
        else:
            left -= 3
    return twos


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % failed_exams(n, k))


if __name__ == "__main__":
    main()
