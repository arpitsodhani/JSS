import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    return k, numbers[2:2 + n]


# --- clause: fewest_bikes :: (k: int, x: list[int]) -> int ---
def fewest_bikes(k, x):
    n = len(x)
    for i in range(1, n):
        if x[i] - x[i - 1] > k:
            return -1
    at = 0
    taken = 0
    for i in range(1, n):
        if x[i] - x[at] > k:
            at = i - 1
            taken += 1
    return taken + 1


# --- clause: main :: () -> None ---
def main():
    k, x = read_input()
    sys.stdout.write("%d\n" % fewest_bikes(k, x))


if __name__ == "__main__":
    main()
