import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, l, r, x = (int(token) for token in data[:4])
    hardness = list(map(int, data[4:n + 4]))
    return n, l, r, x, hardness


# --- clause: count_sets :: (n: int, l: int, r: int, x: int, hardness: list[int]) -> int ---
def count_sets(n, l, r, x, hardness):
    size = 1 << n
    sums = [0] * size
    lows = [0] * size
    highs = [0] * size
    bits = [0] * size
    total = 0
    for mask in range(1, size):
        low_bit = mask & -mask
        i = low_bit.bit_length() - 1
        rest = mask ^ low_bit
        value = hardness[i]
        sums[mask] = sums[rest] + value
        bits[mask] = bits[rest] + 1
        if rest:
            lows[mask] = lows[rest] if lows[rest] < value else value
            highs[mask] = highs[rest] if highs[rest] > value else value
        else:
            lows[mask] = value
            highs[mask] = value
        if bits[mask] >= 2 and l <= sums[mask] <= r and highs[mask] - lows[mask] >= x:
            total += 1
    return total


# --- clause: main :: () -> None ---
def main():
    n, l, r, x, hardness = read_input()
    sys.stdout.write("%d\n" % count_sets(n, l, r, x, hardness))


if __name__ == "__main__":
    main()
