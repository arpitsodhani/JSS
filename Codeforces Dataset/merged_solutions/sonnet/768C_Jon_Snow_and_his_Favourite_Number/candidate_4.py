import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    k = numbers[1]
    x = numbers[2]
    return k, x, numbers[3:3 + n]


# --- clause: run_rounds :: (k: int, x: int, strengths: list[int]) -> list[int] ---
def run_rounds(k, x, strengths):
    top = 1024
    counts = [0] * top
    for value in strengths:
        counts[value] += 1
    seen = {}
    step = 0
    while step < k:
        key = tuple(counts)
        if key in seen:
            period = step - seen[key]
            begin = (k - step) % period
            for _ in range(begin):
                counts = one_round(counts, x, top)
            return counts
        seen[key] = step
        counts = one_round(counts, x, top)
        step += 1
    return counts


# --- clause: one_round :: (counts: list[int], x: int, top: int) -> list[int] ---
def one_round(counts, x, top):
    fresh = list(counts)
    seen = 0
    for value in range(top):
        here = counts[value]
        if here == 0:
            continue
        first = seen % 2 == 0
        moved = (here + 1) // 2 if first else here // 2
        seen += here
        if moved:
            fresh[value] -= moved
            fresh[value ^ x] += moved
    return fresh


# --- clause: main :: () -> None ---
def main():
    k, x, strengths = read_input()
    counts = run_rounds(k, x, strengths)
    low = -1
    high = 0
    for value in range(len(counts)):
        if counts[value]:
            if low < 0:
                low = value
            high = value
    sys.stdout.write("%d %d\n" % (high, low))


if __name__ == "__main__":
    main()
