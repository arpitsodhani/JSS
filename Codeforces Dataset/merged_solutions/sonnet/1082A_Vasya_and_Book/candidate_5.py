import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    cases = []
    pos = 1
    for _ in range(t):
        cases.append((data[pos], data[pos + 1], data[pos + 2], data[pos + 3]))
        pos += 4
    return cases

# --- clause: solve_case :: (n: int, x: int, y: int, d: int) -> int ---
def solve_case(n, x, y, d):
    best = -1
    if abs(y - x) % d == 0:
        best = abs(y - x) // d
    from_top = (x - 1 + d - 1) // d
    from_bottom = (n - x + d - 1) // d
    if (y - 1) % d == 0:
        cost = from_top + (y - 1) // d
        if best < 0 or cost < best:
            best = cost
    if (n - y) % d == 0:
        cost = from_bottom + (n - y) // d
        if best < 0 or cost < best:
            best = cost
    return best

# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, y, d in read_input():
        out.append(str(solve_case(n, x, y, d)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
