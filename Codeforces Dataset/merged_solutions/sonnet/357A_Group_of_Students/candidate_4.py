import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    m = numbers[0]
    counts = numbers[1:1 + m]
    return counts, numbers[1 + m], numbers[2 + m]


# --- clause: best_rate :: (counts: list[int], low: int, high: int) -> int ---
def best_rate(counts, low, high):
    m = len(counts)
    prefix = [0] * (m + 1)
    for i in range(m):
        prefix[i + 1] = prefix[i] + counts[i]
    total = prefix[m]
    best = 0
    gap = -1
    k = 1
    while k <= m:
        beginners = prefix[k - 1]
        rest = total - beginners
        k += 1
        if beginners < low or beginners > high:
            continue
        if rest < low or rest > high:
            continue
        here = abs(beginners - rest)
        if gap < 0 or here < gap:
            gap = here
            best = k - 1
    return best if gap >= 0 else 0


# --- clause: main :: () -> None ---
def main():
    counts, low, high = read_input()
    sys.stdout.write("%d\n" % best_rate(counts, low, high))


if __name__ == "__main__":
    main()
