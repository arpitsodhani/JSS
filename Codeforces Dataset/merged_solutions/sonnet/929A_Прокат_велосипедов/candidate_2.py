import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    k = tokens[1]
    return k, tokens[2:2 + n]


# --- clause: fewest_bikes :: (k: int, x: list[int]) -> int ---
def fewest_bikes(k, x):
    n = len(x)
    at = 0
    taken = 0
    while at < n - 1:
        reach = x[at] + k
        stride = at
        for j in range(at + 1, n):
            if x[j] <= reach:
                stride = j
            else:
                break
        if stride == at:
            return -1
        at = stride
        taken += 1
    return taken


# --- clause: main :: () -> None ---
def main():
    k, x = read_input()
    sys.stdout.write("%d\n" % fewest_bikes(k, x))


if __name__ == "__main__":
    main()
