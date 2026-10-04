import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    t = int(data[0])
    cases = []
    for _ in range(t):
        n, g, b = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        cases.append((n, g, b))
    return cases


# --- clause: solve_case :: (n: int, g: int, b: int) -> int ---
def solve_case(n, g, b):
    need = (n + 1) // 2
    cycles = (need + g - 1) // g
    days = (cycles - 1) * (g + b) + need - (cycles - 1) * g
    if days >= n:
        return days
    return n


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, g, b in read_input():
        out.append(str(solve_case(n, g, b)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
