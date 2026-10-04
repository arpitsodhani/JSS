import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    m = data[0]
    counts = data[1:1 + m]
    return counts, data[1 + m], data[2 + m]


# --- clause: best_rate :: (counts: list[int], low: int, high: int) -> int ---
def best_rate(counts, low, high):
    m = len(counts)
    best = 0
    gap = -1
    for k in range(1, m + 1):
        beginners = 0
        for value in range(k - 1):
            beginners += counts[value]
        rest = 0
        for value in range(k - 1, m):
            rest += counts[value]
        if beginners < low or beginners > high or rest < low or rest > high:
            continue
        here = beginners - rest
        if here < 0:
            here = -here
        if gap < 0 or here < gap:
            gap = here
            best = k
    return best if gap >= 0 else 0


# --- clause: main :: () -> None ---
def main():
    counts, low, high = read_input()
    sys.stdout.write("%d\n" % best_rate(counts, low, high))


if __name__ == "__main__":
    main()
