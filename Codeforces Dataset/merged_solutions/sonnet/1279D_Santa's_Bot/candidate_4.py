import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    cursor = 1
    kids = []
    for _ in range(n):
        k = numbers[cursor]
        cursor += 1
        kids.append(numbers[cursor:cursor + k])
        cursor += k
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
    shares = {}
    total = 0
    for wants in kids:
        size = len(wants)
        if size not in shares:
            shares[size] = pow(size, mod - 2, mod)
        share = shares[size]
        here = 0
        for item in wants:
            here += tally[item]
        total = (total + here % mod * share) % mod
    square = pow(n * n % mod, mod - 2, mod)
    return total * square % mod


# --- clause: main :: () -> None ---
def main():
    kids = read_input()
    sys.stdout.write("%d\n" % valid_chance(kids, item_counts(kids)))


if __name__ == "__main__":
    main()
