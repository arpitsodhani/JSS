import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    values = list(map(int, data[:3]))
    return values[0], values[1], values[2]


# --- clause: binomials :: (limit: int) -> tuple[list[int], list[int]] ---
def binomials(limit):
    factorial = [1] * (limit + 1)
    for i in range(1, limit + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    inverse = [1] * (limit + 1)
    inverse[limit] = pow(factorial[limit], MOD - 2, MOD)
    i = limit
    while i > 0:
        inverse[i - 1] = inverse[i] * i % MOD
        i -= 1
    return factorial, inverse


# --- clause: arrangement_counts :: (f: int, w: int, h: int, factorial: list[int], inverse: list[int]) -> tuple[int, int] ---
def arrangement_counts(f, w, h, factorial, inverse):
    def choose(a, b):
        if b < 0 or b > a or a < 0:
            return 0
        return factorial[a] * inverse[b] % MOD * inverse[a - b] % MOD

    total = 0
    good = 0
    top_f = f if f else 0
    top_w = w if w else 0
    for boxes in range(0, top_f + 1):
        food_ways = choose(f - 1, boxes - 1) if boxes else (1 if f == 0 else 0)
        if food_ways == 0:
            continue
        for barrels in (boxes - 1, boxes, boxes + 1):
            if barrels < 0 or barrels > top_w:
                continue
            if barrels == 0 and w != 0:
                continue
            if barrels and w == 0:
                continue
            wine_ways = choose(w - 1, barrels - 1) if barrels else 1
            spots = 2 if barrels == boxes and boxes else 1
            if boxes == 0:
                spots = 1
            total = (total + food_ways * wine_ways % MOD * spots) % MOD
            tall = choose(w - barrels * h - 1, barrels - 1) if barrels else 1
            good = (good + food_ways * tall % MOD * spots) % MOD
    return good, total


# --- clause: main :: () -> None ---
def main():
    f, w, h = read_input()
    tables = binomials(f + w + 10)
    factorial, inverse = tables[0], tables[1]
    good, total = arrangement_counts(f, w, h, factorial, inverse)
    sys.stdout.write(str(good * pow(total, MOD - 2, MOD) % MOD) + "\n")


if __name__ == "__main__":
    main()
