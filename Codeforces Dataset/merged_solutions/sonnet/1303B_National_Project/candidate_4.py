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
        pos += 1
        g = int(data[pos])
        pos += 1
        b = int(data[pos])
        pos += 1
        cases.append((n, g, b))
    return cases


# --- clause: solve_case :: (n: int, g: int, b: int) -> int ---
def solve_case(n, g, b):
    need = (n + 1) // 2
    cycles = (need + g - 1) // g
    days = (cycles - 1) * (g + b) + need - (cycles - 1) * g
    if days < n:
        return n
    return days


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
