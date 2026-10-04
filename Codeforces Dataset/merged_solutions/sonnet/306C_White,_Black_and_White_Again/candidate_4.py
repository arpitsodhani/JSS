import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1], numbers[2]


# --- clause: binomials :: (limit: int, mod: int) -> list[list[int]] ---
def binomials(limit, mod):
    table = []
    for i in range(limit + 1):
        record = [1] * (i + 1)
        for j in range(1, i):
            record[j] = (table[i - 1][j - 1] + table[i - 1][j]) % mod
        table.append(record)
    return table


# --- clause: count_ways :: (n: int, w: int, b: int, choose: list[list[int]]) -> int ---
def count_ways(n, w, b, choose):
    mod = 1000000009
    scale = 1
    for value in range(1, w + 1):
        scale = scale * value % mod
    for value in range(1, b + 1):
        scale = scale * value % mod
    total = 0
    for light in range(2, n):
        dark = n - light
        if light > w or dark > b:
            continue
        ways = choose[w - 1][light - 1] * choose[b - 1][dark - 1] % mod
        total = (total + ways * (light - 1)) % mod
    return total * scale % mod


# --- clause: main :: () -> None ---
def main():
    n, w, b = read_input()
    choose = binomials(max(w, b), 1000000009)
    sys.stdout.write("%d\n" % count_ways(n, w, b, choose))


if __name__ == "__main__":
    main()
