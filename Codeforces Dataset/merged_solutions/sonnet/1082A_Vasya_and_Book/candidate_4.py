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
    options = []
    if (y - x) % d == 0:
        options.append(abs(y - x) // d)
    if (y - 1) % d == 0:
        options.append((x - 1 + d - 1) // d + (y - 1) // d)
    if (n - y) % d == 0:
        options.append((n - x + d - 1) // d + (n - y) // d)
    if not options:
        return -1
    return min(options)

# --- clause: main :: () -> None ---
def main():
    out = []
    for n, x, y, d in read_input():
        out.append(str(solve_case(n, x, y, d)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
