import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    speeds = list(map(int, data[1:1 + n]))
    return n, speeds


# --- clause: smallest_sum :: (n: int, speeds: list[int]) -> int ---
def smallest_sum(n, speeds):
    speeds.sort()
    if n == 1:
        return 0
    prev = [0] * n
    for width in range(1, n):
        m = n - width
        lefts = prev[1:]
        rights = prev[:m]
        sj = speeds[width:]
        si = speeds[:m]
        prev = [b - a + (l if l < r else r) for a, b, l, r in zip(si, sj, lefts, rights)]
    return prev[0]


# --- clause: main :: () -> None ---
def main():
    n, speeds = read_input()
    sys.stdout.write(str(smallest_sum(n, speeds)) + "\n")


if __name__ == "__main__":
    main()
