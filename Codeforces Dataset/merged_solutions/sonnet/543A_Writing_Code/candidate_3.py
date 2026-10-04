import sys


# --- clause: read_input :: () -> tuple[int, int, int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m, b, mod = (int(v) for v in data[:4])
    bugs = [int(token) for token in data[4:n + 4]]
    return n, m, b, mod, bugs


# --- clause: count_plans :: (n: int, m: int, b: int, mod: int, bugs: list[int]) -> int ---
def count_plans(n, m, b, mod, bugs):
    width = b + 1
    table = [[0] * width for _ in range(m + 1)]
    table[0][0] = 1 % mod
    for rate in bugs:
        if rate > b:
            continue
        for lines in range(1, m + 1):
            row = table[lines]
            prev = table[lines - 1]
            for cost in range(rate, b + 1):
                value = prev[cost - rate]
                if value:
                    row[cost] = (row[cost] + value) % mod
    return sum(table[m]) % mod


# --- clause: main :: () -> None ---
def main():
    n, m, b, mod, bugs = read_input()
    print(count_plans(n, m, b, mod, bugs))


if __name__ == "__main__":
    main()
