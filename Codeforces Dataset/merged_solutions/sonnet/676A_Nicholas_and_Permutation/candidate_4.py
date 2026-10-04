import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: best_distance :: (n: int, a: list[int]) -> int ---
def best_distance(n, a):
    low = a.index(1)
    high = a.index(n)
    return max(max(low, high), n - 1 - min(low, high))


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(best_distance(n, a)) + "\n")


if __name__ == "__main__":
    main()
