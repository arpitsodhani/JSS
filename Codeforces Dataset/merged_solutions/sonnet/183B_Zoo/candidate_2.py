import sys
from math import gcd


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    birds = []
    pos = 2
    for _ in range(m):
        birds.append((data[pos], data[pos + 1]))
        pos += 2
    return n, m, birds


# --- clause: line_counts :: (n: int, birds: list[tuple[int, int]]) -> dict ---
def line_counts(n, birds):
    m = len(birds)
    pairs = {}
    for i in range(m - 1):
        x1, y1 = birds[i]
        for j in range(i + 1, m):
            x2, y2 = birds[j]
            den = y2 - y1
            if den == 0:
                continue
            num = x1 * y2 - x2 * y1
            spot, rest = divmod(num, den)
            if rest:
                continue
            if not 1 <= spot <= n:
                continue
            dx = x1 - spot
            step = gcd(dx if dx >= 0 else -dx, y1)
            key = (spot, dx // step, y1 // step)
            if key in pairs:
                pairs[key] += 1
            else:
                pairs[key] = 1
    return pairs


# --- clause: total_seen :: (n: int, m: int, birds: list[tuple[int, int]]) -> int ---
def total_seen(n, m, birds):
    pairs = line_counts(n, birds)
    best = {}
    for key, count in pairs.items():
        size = 2
        while size * (size - 1) // 2 < count:
            size += 1
        spot = key[0]
        if best.get(spot, 0) < size:
            best[spot] = size
    total = n
    for spot, size in best.items():
        total += size - 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, birds = read_input()
    sys.stdout.write(str(total_seen(n, m, birds)) + "\n")


if __name__ == "__main__":
    main()
