import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: failed_exams :: (n: int, k: int) -> int ---
def failed_exams(n, k):
    short = 3 * n - k
    return short if short > 0 else 0


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    sys.stdout.write("%d\n" % failed_exams(n, k))


if __name__ == "__main__":
    main()
