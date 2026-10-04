import sys


# --- clause: read_input :: () -> tuple[str, list[tuple[int, int]]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    m = int(numbers[1])
    s = numbers[2].decode()
    asked = []
    for i in range(m):
        asked.append((int(numbers[3 + 2 * i]), int(numbers[4 + 2 * i])))
    return s, asked


# --- clause: mismatch_tables :: (s: str) -> list[list[int]] ---
def mismatch_tables(s):
    orders = ["abc", "acb", "bac", "bca", "cab", "cba"]
    tables = []
    for ranked in orders:
        run = [0] * (len(s) + 1)
        for i in range(len(s)):
            run[i + 1] = run[i] + (0 if s[i] == ranked[i % 3] else 1)
        tables.append(run)
    return tables


# --- clause: cheapest :: (tables: list[list[int]], low: int, high: int) -> int ---
def cheapest(tables, low, high):
    costs = []
    for run in tables:
        costs.append(run[high] - run[low - 1])
    return min(costs)


# --- clause: main :: () -> None ---
def main():
    s, asked = read_input()
    tables = mismatch_tables(s)
    out = []
    for low, high in asked:
        out.append(cheapest(tables, low, high))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
