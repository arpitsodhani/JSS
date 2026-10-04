import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return sorted(raw[1:1 + raw[0]])


# --- clause: split_point :: (values: list[int], low: int, high: int, bit: int) -> int ---
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


# --- clause: cheapest_link :: (values: list[int], a_low: int, a_high: int, b_low: int, b_high: int, bit: int) -> int ---
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


# --- clause: tree_weight :: (values: list[int], low: int, high: int, bit: int) -> int ---
def tree_weight(values, low, high, bit):
    if bit < 0 or high - low <= 1:
        return 0
    cut = split_point(values, low, high, bit)
    if cut == low or cut == high:
        return tree_weight(values, low, high, bit - 1)
    total = tree_weight(values, low, cut, bit - 1) + tree_weight(values, cut, high, bit - 1)
    return total + cheapest_link(values, low, cut, cut, high, bit - 1) + (1 << bit)


# --- clause: main :: () -> None ---
def main():
    values = read_input()
    sys.setrecursionlimit(10000)
    sys.stdout.write("%d\n" % tree_weight(values, 0, len(values), 29))


if __name__ == "__main__":
    main()
