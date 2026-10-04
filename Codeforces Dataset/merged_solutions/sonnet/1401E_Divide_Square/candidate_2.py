import sys


# --- clause: read_input :: () -> tuple[list[tuple[int, int, int]], list[tuple[int, int, int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    pos = 2
    flat = []
    for _ in range(n):
        flat.append((tokens[pos], tokens[pos + 1], tokens[pos + 2]))
        pos += 3
    tall = []
    for _ in range(m):
        tall.append((tokens[pos], tokens[pos + 1], tokens[pos + 2]))
        pos += 3
    return flat, tall


# --- clause: full_spans :: (flat: list[tuple[int, int, int]], tall: list[tuple[int, int, int]]) -> int ---
def full_spans(flat, tall):
    side = 1000000
    total = 0
    for y, low, top_value in flat:
        if low == 0 and top_value == side:
            total += 1
    for x, low, top_value in tall:
        if low == 0 and top_value == side:
            total += 1
    return total


# --- clause: count_crossings :: (flat: list[tuple[int, int, int]], tall: list[tuple[int, int, int]]) -> int ---
def count_crossings(flat, tall):
    side = 1000000
    starts = [[] for _ in range(side + 2)]
    stops = [[] for _ in range(side + 2)]
    for y, low, top_value in flat:
        starts[low].append(y)
        stops[top_value].append(y)
    asked = [[] for _ in range(side + 2)]
    for x, low, top_value in tall:
        asked[x].append((low, top_value))
    tree = [0] * (side + 2)
    total = 0
    for x in range(side + 1):
        for y in starts[x]:
            spot = y + 1
            while spot <= side + 1:
                tree[spot] += 1
                spot += spot & (-spot)
        for low, top_value in asked[x]:
            upper = 0
            spot = top_value + 1
            while spot > 0:
                upper += tree[spot]
                spot -= spot & (-spot)
            lower = 0
            spot = low
            while spot > 0:
                lower += tree[spot]
                spot -= spot & (-spot)
            total += upper - lower
        for y in stops[x]:
            spot = y + 1
            while spot <= side + 1:
                tree[spot] -= 1
                spot += spot & (-spot)
    return total


# --- clause: main :: () -> None ---
def main():
    flat, tall = read_input()
    pieces = 1 + full_spans(flat, tall) + count_crossings(flat, tall)
    sys.stdout.write("%d\n" % pieces)


if __name__ == "__main__":
    main()
