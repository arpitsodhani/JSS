import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        m = int(data[pos])
        pos += 1
        size = n * m
        first = [int(token) for token in data[pos:pos + size]]
        pos += size
        second = [int(token) for token in data[pos:pos + size]]
        pos += size
        cases.append((n, m, first, second))
    return cases


# --- clause: consistent :: (n: int, m: int, first: list[int], second: list[int]) -> str ---
def consistent(n, m, first, second):
    size = n * m
    row_of = [0] * (size + 1)
    col_of = [0] * (size + 1)
    for i in range(size):
        row_of[first[i]] = i // m
        col_of[first[i]] = i % m
    for r in range(n):
        base = row_of[second[r * m]]
        for c in range(m):
            if row_of[second[r * m + c]] != base:
                return "NO"
    for c in range(m):
        base = col_of[second[c]]
        for r in range(n):
            if col_of[second[r * m + c]] != base:
                return "NO"
    rows = {row_of[second[r * m]] for r in range(n)}
    if len(rows) != n:
        return "NO"
    cols = set()
    for c in range(m):
        cols.add(col_of[second[c]])
    if len(cols) != m:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, m, first, second in read_input():
        out.append(consistent(n, m, first, second))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
