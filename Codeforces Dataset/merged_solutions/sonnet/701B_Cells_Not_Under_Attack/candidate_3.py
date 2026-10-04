import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    spots = [int(token) for token in data[2:2 + 2 * m]]
    return n, m, spots


# --- clause: free_cells :: (n: int, m: int, spots: list[int]) -> list[str] ---
def free_cells(n, m, spots):
    rows = set()
    cols = set()
    out = []
    for r, c in zip(spots[0::2], spots[1::2]):
        rows.add(r)
        cols.add(c)
        out.append(str((n - len(rows)) * (n - len(cols))))
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, spots = read_input()
    print(" ".join(free_cells(n, m, spots)))


if __name__ == "__main__":
    main()
