import sys


# --- clause: read_input :: () -> list[tuple[int, list[str]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        grid = [data[pos + i].decode() for i in range(n)]
        pos += n
        cases.append((n, grid))
    return cases


# --- clause: choose_flips :: (n: int, grid: list[str]) -> list[tuple[int, int]] ---
def choose_flips(n, grid):
    start = [(1, 2), (2, 1)]
    finish = [(n - 1, n), (n, n - 1)]
    best = None
    for digit in "01":
        other = "1" if digit == "0" else "0"
        flips = []
        for r, c in start:
            if grid[r - 1][c - 1] != digit:
                flips.append((r, c))
        for r, c in finish:
            if grid[r - 1][c - 1] != other:
                flips.append((r, c))
        if best is None or len(flips) < len(best):
            best = flips
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, grid in read_input():
        flips = choose_flips(n, grid)
        out.append(str(len(flips)))
        for r, c in flips:
            out.append(str(r) + " " + str(c))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
