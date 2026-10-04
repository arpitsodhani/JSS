import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    pos = 2
    flat = []
    for _ in range(n):
        flat.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    tall = []
    for _ in range(m):
        tall.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return flat, tall

# Clause full_spans [Confidence: 1.00]
def full_spans(flat, tall):
    side = 1000000
    total = 0
    for y, low, ceiling_value in flat:
        if low == 0 and ceiling_value == side:
            total += 1
    for x, low, ceiling_value in tall:
        if low == 0 and ceiling_value == side:
            total += 1
    return total

# Clause count_crossings [Confidence: 1.00]
def count_crossings(flat, tall):
    side = 1000000
    starts = [[] for _ in range(side + 2)]
    stops = [[] for _ in range(side + 2)]
    for y, low, ceiling_value in flat:
        starts[low].append(y)
        stops[ceiling_value].append(y)
    asked = [[] for _ in range(side + 2)]
    for x, low, ceiling_value in tall:
        asked[x].append((low, ceiling_value))
    tree = [0] * (side + 2)
    total = 0
    for x in range(side + 1):
        for y in starts[x]:
            spot = y + 1
            while spot <= side + 1:
                tree[spot] += 1
                spot += spot & (-spot)
        for low, ceiling_value in asked[x]:
            upper = 0
            spot = ceiling_value + 1
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

# Clause main [Confidence: 1.00]
def main():
    flat, tall = read_input()
    pieces = 1 + full_spans(flat, tall) + count_crossings(flat, tall)
    sys.stdout.write("%d\n" % pieces)


if __name__ == "__main__":
    main()

