import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    spots = [int(data[i + 2]) for i in range(2 * m)]
    return n, m, spots


# --- clause: free_cells :: (n: int, m: int, spots: list[int]) -> list[str] ---
def free_cells(n, m, spots):
    rows = [False] * (n + 1)
    cols = [False] * (n + 1)
    used_rows = 0
    used_cols = 0
    out = []
    for i in range(m):
        r = spots[2 * i]
        c = spots[2 * i + 1]
        if not rows[r]:
            rows[r] = True
            used_rows += 1
        if not cols[c]:
            cols[c] = True
            used_cols += 1
        out.append(str((n - used_rows) * (n - used_cols)))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, spots = read_input()
    rows = free_cells(n, m, spots)
    sys.stdout.write(" ".join(rows) + "\n")


if __name__ == "__main__":
    main()
