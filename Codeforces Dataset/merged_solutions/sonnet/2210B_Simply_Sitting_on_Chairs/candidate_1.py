import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: solve_case :: (p: list[int]) -> int ---
def solve_case(p):
    n = len(p)
    where = [0] * (n + 2)
    for i in range(1, n + 1):
        where[p[i - 1]] = i
    best = 0
    below = 0
    above = 0
    for h in range(1, n + 2):
        if h > 1:
            below += 1 if p[h - 2] <= h - 1 else 0
            above -= 1 if where[h - 1] < h - 1 else 0
            above += 1 if p[h - 2] >= h else 0
        if below + above > best:
            best = below + above
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for p in read_input():
        out.append(str(solve_case(p)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
