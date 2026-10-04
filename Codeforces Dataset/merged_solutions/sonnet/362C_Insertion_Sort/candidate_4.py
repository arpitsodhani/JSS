import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + n]


# --- clause: smaller_before :: (n: int, a: list[int]) -> list[int] ---
def smaller_before(n, a):
    tree = [0] * (n + 2)
    counts = [0] * n
    for j in range(n):
        value = a[j]
        spot = value
        total = 0
        while spot > 0:
            total += tree[spot]
            spot -= spot & -spot
        counts[j] = total
        spot = value + 1
        while spot <= n:
            tree[spot] += 1
            spot += spot & -spot
    return counts


# --- clause: best_swap :: (n: int, a: list[int]) -> tuple[int, int] ---
def best_swap(n, a):
    less = smaller_before(n, a)
    inversions = 0
    for j in range(n):
        inversions += j - less[j]
    seen_before = [0] * n
    best = None
    ways = 0
    for i in range(n):
        value = a[i]
        for j in range(n):
            if a[j] > value:
                seen_before[j] += 1
        inside = 0
        for j in range(i + 1, n):
            if j > i + 1 and a[j - 1] < value:
                inside += 1
            below = less[j] - seen_before[j]
            if value > a[j]:
                delta = -(2 * (inside - below) + 1)
            else:
                delta = 2 * (below - inside) + 1
            if best is None or delta < best:
                best = delta
                ways = 1
            elif delta == best:
                ways += 1
    return inversions + best, ways


# --- clause: main :: () -> None ---
def main():
    n, a = read_input()
    total, ways = best_swap(n, a)
    sys.stdout.write("%d %d\n" % (total, ways))


if __name__ == "__main__":
    main()
