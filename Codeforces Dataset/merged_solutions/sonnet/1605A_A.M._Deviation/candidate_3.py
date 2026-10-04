import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    while len(cases) < t:
        cases.append((int(data[pos]), int(data[pos + 1]), int(data[pos + 2])))
        pos += 3
    return cases


# --- clause: solve_case :: (a: int, b: int, c: int) -> int ---
def solve_case(a, b, c):
    total = a + b + c
    best = total
    for middle in (total // 3, total // 3 + 1):
        gap = total - 3 * middle
        if gap < 0:
            gap = -gap
        if gap < best:
            best = gap
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, c in read_input():
        out.append(str(solve_case(a, b, c)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
