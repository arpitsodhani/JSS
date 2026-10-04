import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return sorted(data[1:1 + data[0]])

# Clause split_point [Confidence: 1.00]
def split_point(values, low, high, bit):
    bits = 1 << bit
    start = low
    right = high
    while start < right:
        mid = (start + right) // 2
        if values[mid] & bits:
            right = mid
        else:
            start = mid + 1
    return start

# Clause cheapest_link [Confidence: 1.00]
def cheapest_link(values, a_low, a_high, b_low, b_high, bit):
    if bit < 0:
        return 0
    a_cut = split_point(values, a_low, a_high, bit)
    b_cut = split_point(values, b_low, b_high, bit)
    best = 1 << 62
    if a_low < a_cut and b_low < b_cut:
        here = cheapest_link(values, a_low, a_cut, b_low, b_cut, bit - 1)
        if here < best:
            best = here
    if a_cut < a_high and b_cut < b_high:
        here = cheapest_link(values, a_cut, a_high, b_cut, b_high, bit - 1)
        if here < best:
            best = here
    if best < (1 << 62):
        return best
    if a_low < a_cut and b_cut < b_high:
        here = cheapest_link(values, a_low, a_cut, b_cut, b_high, bit - 1) + (1 << bit)
        if here < best:
            best = here
    if a_cut < a_high and b_low < b_cut:
        here = cheapest_link(values, a_cut, a_high, b_low, b_cut, bit - 1) + (1 << bit)
        if here < best:
            best = here
    return best

# Clause tree_weight [Confidence: 1.00]
def tree_weight(values, low, high, bit):
    if bit < 0 or high - low <= 1:
        return 0
    cut = split_point(values, low, high, bit)
    if cut == low or cut == high:
        return tree_weight(values, low, high, bit - 1)
    total = tree_weight(values, low, cut, bit - 1) + tree_weight(values, cut, high, bit - 1)
    return total + cheapest_link(values, low, cut, cut, high, bit - 1) + (1 << bit)

# Clause main [Confidence: 1.00]
def main():
    values = read_input()
    sys.setrecursionlimit(10000)
    sys.stdout.write("%d\n" % tree_weight(values, 0, len(values), 29))


if __name__ == "__main__":
    main()

