import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    spots = [int(token) for token in data[2:2 + 2 * m]]
    return n, m, spots


# --- clause: free_cells :: (n: int, m: int, spots: list[int]) -> list[str] ---
def free_cells(n, m, spots):
    rows = set()
    cols = set()
    out = []
    for i in range(m):
        r = spots[2 * i]
        c = spots[2 * i + 1]
        rows.add(r)
        cols.add(c)
        out.append(str((n - len(rows)) * (n - len(cols))))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, spots = read_input()
    sys.stdout.write(" ".join(free_cells(n, m, spots)) + "\n")


if __name__ == "__main__":
    main()
