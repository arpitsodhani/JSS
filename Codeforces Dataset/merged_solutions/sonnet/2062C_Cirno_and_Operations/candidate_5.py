import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = raw[p]
    p += 1
    cases = []
    for _ in range(t):
        n = raw[p]
        p += 1
        values = raw[p:p + n]
        p += n
        cases.append(values)
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    row = list(a)
    best = sum(row)
    while len(row) > 1:
        row = [row[j + 1] - row[j] for j in range(len(row) - 1)]
        s = sum(row)
        if s < 0:
            s = 0 - s
        if best < s:
            best = s
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(solve_case(values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
