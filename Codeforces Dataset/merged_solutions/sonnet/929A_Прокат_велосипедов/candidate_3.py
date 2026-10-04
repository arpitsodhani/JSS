import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    return k, fields[2:2 + n]


# --- clause: fewest_bikes :: (k: int, x: list[int]) -> int ---
def fewest_bikes(k, x):
    n = len(x)
    at = 0
    taken = 0
    while at < n - 1:
        reach = x[at] + k
        delta = at
        for j in range(at + 1, n):
            if x[j] <= reach:
                delta = j
            else:
                break
        if delta == at:
            return -1
        at = delta
        taken += 1
    return taken


# --- clause: main :: () -> None ---
def main():
    k, x = read_input()
    sys.stdout.write("%d\n" % fewest_bikes(k, x))


if __name__ == "__main__":
    main()
