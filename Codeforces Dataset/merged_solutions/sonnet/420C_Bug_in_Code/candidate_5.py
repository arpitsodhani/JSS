import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    p = raw[1]
    claims = [(raw[2 + 2 * i], raw[3 + 2 * i]) for i in range(n)]
    return n, p, claims


# --- clause: count_sets :: (n: int, p: int, claims: list[tuple[int, int]]) -> int ---
def count_sets(n, p, claims):
    votes = [0] * (n + 1)
    pairs = {}
    for x, y in claims:
        votes[x] += 1
        votes[y] += 1
        key = (x, y) if x < y else (y, x)
        pairs[key] = pairs.get(key, 0) + 1
    sorted_items = sorted(votes[1:])
    total = 0
    low = 0
    ceiling_value = n - 1
    while low < ceiling_value:
        if sorted_items[low] + sorted_items[ceiling_value] >= p:
            total += ceiling_value - low
            ceiling_value -= 1
        else:
            low += 1
    for (x, y), shared in pairs.items():
        if votes[x] + votes[y] >= p and votes[x] + votes[y] - shared < p:
            total -= 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, p, claims = read_input()
    sys.stdout.write("%d\n" % count_sets(n, p, claims))


if __name__ == "__main__":
    main()
