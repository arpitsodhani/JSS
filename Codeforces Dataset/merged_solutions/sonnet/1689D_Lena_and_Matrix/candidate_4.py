import sys


# --- clause: read_input :: () -> list[list[str]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    reader = 1
    cases = []
    for _ in range(t):
        n = int(numbers[reader])
        reader += 2
        rows = [numbers[reader + i].decode() for i in range(n)]
        reader += n
        cases.append(rows)
    return cases


# --- clause: best_cell :: (rows: list[str]) -> tuple[int, int] ---
def best_cell(rows):
    n = len(rows)
    m = len(rows[0])
    big = 10 ** 9
    plus_max = -big
    minus_max = -big
    plus_min = big
    minus_min = big
    for i in range(n):
        for j in range(m):
            if rows[i][j] != "B":
                continue
            if i + j > plus_max:
                plus_max = i + j
            if i + j < plus_min:
                plus_min = i + j
            if i - j > minus_max:
                minus_max = i - j
            if i - j < minus_min:
                minus_min = i - j
    best = None
    spot = (1, 1)
    for i in range(n):
        for j in range(m):
            far = max(plus_max - i - j, i + j - plus_min,
                      minus_max - i + j, i - j - minus_min)
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
