import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: best_distance :: (n: int, a: list[int]) -> int ---
def best_distance(n, a):
    low = 0
    high = 0
    for i, value in enumerate(a):
        if value == 1:
            low = i
        elif value == n:
            high = i
    best = 0
    for spot in (low, high):
        if spot > best:
            best = spot
        if n - 1 - spot > best:
            best = n - 1 - spot
    return best


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    sys.stdout.write(str(best_distance(n, a)) + "\n")


if __name__ == "__main__":
    main()
