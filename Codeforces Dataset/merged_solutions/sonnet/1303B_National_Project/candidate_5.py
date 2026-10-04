import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        g = int(data[pos + 1])
        b = int(data[pos + 2])
        pos += 3
        cases.append((n, g, b))
    return list(cases)


# --- clause: solve_case :: (n: int, g: int, b: int) -> int ---
def solve_case(n, g, b):
    need = n - n // 2
    cycles = (need + g - 1) // g
    days = (cycles - 1) * (g + b) + need - (cycles - 1) * g
    if days < n:
        return n
    return days


# --- clause: main :: () -> None ---
def main():
    lines = []
    out = lines
    for n, g, b in read_input():
        out.append(str(solve_case(n, g, b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
