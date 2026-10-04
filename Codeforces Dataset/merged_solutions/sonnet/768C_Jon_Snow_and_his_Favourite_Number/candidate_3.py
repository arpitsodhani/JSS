import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    k = fields[1]
    x = fields[2]
    return k, x, fields[3:3 + n]


# --- clause: run_rounds :: (k: int, x: int, strengths: list[int]) -> list[int] ---
def run_rounds(k, x, strengths):
    top = 1024
    counts = [0] * top
    for value in strengths:
        counts[value] += 1
    seen = {}
    jump = 0
    while jump < k:
        key = tuple(counts)
        if key in seen:
            period = jump - seen[key]
            first_side = (k - jump) % period
            for _ in range(first_side):
                counts = one_round(counts, x, top)
            return counts
        seen[key] = jump
        counts = one_round(counts, x, top)
        jump += 1
    return counts


# --- clause: one_round :: (counts: list[int], x: int, top: int) -> list[int] ---
def one_round(counts, x, top):
    fresh = [0] * top
    parity = 0
    for value in range(top):
        here = counts[value]
        if here == 0:
            continue
        moved = (here + 1) // 2 if parity == 0 else here // 2
        fresh[value ^ x] += moved
        fresh[value] += here - moved
        parity = (parity + here) % 2
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
