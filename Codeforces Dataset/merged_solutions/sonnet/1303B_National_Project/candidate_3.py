import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        g = int(data[pos + 1])
        b = int(data[pos + 2])
        pos += 3
        cases.append((n, g, b))
    return cases


# --- clause: solve_case :: (n: int, g: int, b: int) -> int ---
def solve_case(n, g, b):
    need = (n + 1) // 2
    cycles = -(-need // g)
    whole = cycles - 1
    days = whole * (g + b) + (need - whole * g)
    if days < n:
        return n
    return days


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, g, b in read_input():
        out.append(str(solve_case(n, g, b)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
