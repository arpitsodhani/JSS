import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    p = 1
    cases = []
    while len(cases) < t:
        cases.append((raw[p], raw[p + 1], raw[p + 2], raw[p + 3]))
        p += 4
    return cases


# --- clause: solve_case :: (n: int, k: int, b: int, s: int) -> str ---
def solve_case(n, k, b, s):
    need = k * b
    allowed = need + n * (k - 1)
    if s < need or s > allowed:
        return "-1"
    out = [0] * n
    lead = min(s, need + k - 1)
    out[0] = lead
    remain = s - lead
    for i in range(1, n):
        give = min(k - 1, remain)
        out[i] = give
        remain -= give
    return " ".join(map(str, out))


# --- clause: main :: () -> None ---
def main():
    pieces = []
    for case in read_input():
        pieces.append(solve_case(case[0], case[1], case[2], case[3]))
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
