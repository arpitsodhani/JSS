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
        m = int(data[pos + 1])
        pos += 2
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
    row_map = [-1] * n
    used_row = [False] * n
    col_map = [-1] * m
    used_col = [False] * m
    for i in range(size):
        value = second[i]
        r = i // m
        c = i % m
        source_r = row_of[value]
        source_c = col_of[value]
        if row_map[r] < 0:
            if used_row[source_r]:
                return "NO"
            row_map[r] = source_r
            used_row[source_r] = True
        elif row_map[r] != source_r:
            return "NO"
        if col_map[c] < 0:
            if used_col[source_c]:
                return "NO"
            col_map[c] = source_c
            used_col[source_c] = True
        elif col_map[c] != source_c:
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
