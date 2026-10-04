import sys


# --- clause: read_input :: () -> tuple[str, list[tuple[int, int]]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    m = int(fields[1])
    s = fields[2].decode()
    asked = []
    for i in range(m):
        asked.append((int(fields[3 + 2 * i]), int(fields[4 + 2 * i])))
    return s, asked


# --- clause: mismatch_tables :: (s: str) -> list[list[int]] ---
def mismatch_tables(s):
    orders = ["abc", "acb", "bac", "bca", "cab", "cba"]
    tables = []
    for arranged in orders:
        run = [0] * (len(s) + 1)
        for i in range(len(s)):
            run[i + 1] = run[i] + (0 if s[i] == arranged[i % 3] else 1)
        tables.append(run)
    return tables


# --- clause: cheapest :: (tables: list[list[int]], low: int, high: int) -> int ---
def cheapest(tables, low, high):
    finest = high - low + 1
    for run in tables:
        here = run[high] - run[low - 1]
        if here < finest:
            finest = here
    return finest


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
