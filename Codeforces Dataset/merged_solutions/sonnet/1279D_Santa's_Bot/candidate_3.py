import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    offset = 1
    kids = []
    for _ in range(n):
        k = fields[offset]
        offset += 1
        kids.append(fields[offset:offset + k])
        offset += k
    return kids


# --- clause: item_counts :: (kids: list[list[int]]) -> dict[int, int] ---
def item_counts(kids):
    tally = {}
    for wants in kids:
        for item in wants:
            tally[item] = tally.get(item, 0) + 1
    return tally


# --- clause: valid_chance :: (kids: list[list[int]], tally: dict[int, int]) -> int ---
def valid_chance(kids, tally):
    mod = 998244353
    n = len(kids)
    inverse_n = pow(n, mod - 2, mod)
    summed = 0
    for wants in kids:
        share = pow(len(wants), mod - 2, mod)
        for item in wants:
            summed = (summed + share * tally[item]) % mod
    return summed * inverse_n % mod * inverse_n % mod


# --- clause: main :: () -> None ---
def main():
    kids = read_input()
    sys.stdout.write("%d\n" % valid_chance(kids, item_counts(kids)))


if __name__ == "__main__":
    main()
