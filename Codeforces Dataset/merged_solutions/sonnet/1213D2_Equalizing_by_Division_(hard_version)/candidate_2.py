import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return n, k, data[2:2 + n]


# --- clause: fewest_moves :: (n: int, k: int, a: list[int]) -> int ---
def fewest_moves(n, k, a):
    limit = max(a) + 1
    buckets = [[] for _ in range(limit)]
    for value in a:
        current = value
        steps = 0
        while current:
            buckets[current].append(steps)
            current >>= 1
            steps += 1
        buckets[0].append(steps)
    best = -1
    for group in buckets:
        if len(group) < k:
            continue
        group.sort()
        total = sum(group[:k])
        if best < 0 or total < best:
            best = total
    return best


# --- clause: main :: () -> None ---
def main():
    n, k, a = read_input()
    sys.stdout.write(str(fewest_moves(n, k, a)) + "\n")


if __name__ == "__main__":
    main()
