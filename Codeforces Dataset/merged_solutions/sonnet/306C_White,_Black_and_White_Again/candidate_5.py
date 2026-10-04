import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[0], raw[1], raw[2]


# --- clause: binomials :: (limit: int, mod: int) -> list[list[int]] ---
def binomials(limit, mod):
    table = []
    for i in range(limit + 1):
        band = [1] * (i + 1)
        for j in range(1, i):
            band[j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
        table.append(band)
    return table


# --- clause: count_ways :: (n: int, w: int, b: int, choose: list[list[int]]) -> int ---
def count_ways(n, w, b, choose):
    mod = 1000000009
    total = 0
    for dark in range(1, n - 1):
        light = n - dark
        if light > w or dark > b:
            continue
        ways = choose[w - 1][light - 1] * choose[b - 1][dark - 1] % mod
        total = (total + ways * (light - 1)) % mod
    for number in range(1, w + 1):
        total = total * number % mod
    for number in range(1, b + 1):
        total = total * number % mod
    return total


# --- clause: main :: () -> None ---
def main():
    n, w, b = read_input()
    choose = binomials(max(w, b), 1000000009)
    sys.stdout.write("%d\n" % count_ways(n, w, b, choose))


if __name__ == "__main__":
    main()
