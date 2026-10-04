import sys


# --- clause: read_input :: () -> list[list[str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    cursor = 1
    cases = []
    for _ in range(t):
        n = int(fields[cursor])
        cursor += 2
        rows = [fields[cursor + i].decode() for i in range(n)]
        cursor += n
        cases.append(rows)
    return cases


# --- clause: best_cell :: (rows: list[str]) -> tuple[int, int] ---
def best_cell(rows):
    n = len(rows)
    m = len(rows[0])
    lower = -(10 ** 9)
    corners = [lower, lower, lower, lower]
    for i in range(n):
        row = rows[i]
        for j in range(m):
            if row[j] != "B":
                continue
            if i + j > corners[0]:
                corners[0] = i + j
            if i - j > corners[1]:
                corners[1] = i - j
            if j - i > corners[2]:
                corners[2] = j - i
            if -i - j > corners[3]:
                corners[3] = -i - j
    best = None
    spot = (1, 1)
    for i in range(n):
        for j in range(m):
            far = corners[0] - i - j
            other = corners[1] - i + j
            if other > far:
                far = other
            other = corners[2] + i - j
            if other > far:
                far = other
            other = corners[3] + i + j
            if other > far:
                far = other
            if best is None or far < best:
                best = far
                spot = (i + 1, j + 1)
    return spot


# --- clause: main :: () -> None ---
def main():
    out = []
    for rows in read_input():
        out.append("%d %d" % best_cell(rows))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
