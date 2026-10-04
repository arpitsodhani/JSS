import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: best_distance :: (n: int, a: list[int]) -> int ---
def best_distance(n, a):
    where = [0] * (n + 1)
    for i, value in enumerate(a):
        where[value] = i
    low = where[1]
    high = where[n]
    return max(low, high, n - 1 - low, n - 1 - high)


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(best_distance(n, a)) + "\n")


if __name__ == "__main__":
    main()
