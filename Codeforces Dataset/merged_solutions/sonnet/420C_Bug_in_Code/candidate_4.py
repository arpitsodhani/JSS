import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    p = numbers[1]
    claims = [(numbers[2 + 2 * i], numbers[3 + 2 * i]) for i in range(n)]
    return n, p, claims


# --- clause: count_sets :: (n: int, p: int, claims: list[tuple[int, int]]) -> int ---
def count_sets(n, p, claims):
    import bisect

    votes = [0] * (n + 1)
    pairs = {}
    for x, y in claims:
        votes[x] += 1
        votes[y] += 1
        key = (x, y) if x < y else (y, x)
        pairs[key] = pairs.get(key, 0) + 1
    order = sorted(votes[1:])
    total = 0
    for i in range(n):
        at = bisect.bisect_left(order, p - order[i])
        if at <= i:
            at = i + 1
        total += n - at
    for key in pairs:
        x = key[0]
        y = key[1]
        if votes[x] + votes[y] >= p > votes[x] + votes[y] - pairs[key]:
            total -= 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, p, claims = read_input()
    sys.stdout.write("%d\n" % count_sets(n, p, claims))


if __name__ == "__main__":
    main()
