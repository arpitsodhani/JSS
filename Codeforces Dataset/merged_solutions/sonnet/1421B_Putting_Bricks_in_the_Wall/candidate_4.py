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
    a = grid[0][1]
    b = grid[1][0]
    c = grid[n - 2][n - 1]
    d = grid[n - 1][n - 2]
    zero_plan = []
    if a != "0":
        zero_plan.append((1, 2))
    if b != "0":
        zero_plan.append((2, 1))
    if c != "1":
        zero_plan.append((n - 1, n))
    if d != "1":
        zero_plan.append((n, n - 1))
    if len(zero_plan) <= 2:
        return zero_plan
    one_plan = []
    if a != "1":
        one_plan.append((1, 2))
    if b != "1":
        one_plan.append((2, 1))
    if c != "0":
        one_plan.append((n - 1, n))
    if d != "0":
        one_plan.append((n, n - 1))
    return one_plan


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
