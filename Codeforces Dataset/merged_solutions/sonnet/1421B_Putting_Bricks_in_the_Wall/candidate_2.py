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
    cells = [(1, 2, grid[0][1]), (2, 1, grid[1][0]),
             (n - 1, n, grid[n - 2][n - 1]), (n, n - 1, grid[n - 1][n - 2])]
    wanted_zero = ["0", "0", "1", "1"]
    wanted_one = ["1", "1", "0", "0"]
    first = []
    second = []
    for index in range(4):
        r, c, value = cells[index]
        if value != wanted_zero[index]:
            first.append((r, c))
        if value != wanted_one[index]:
            second.append((r, c))
    return first if len(first) <= len(second) else second


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
