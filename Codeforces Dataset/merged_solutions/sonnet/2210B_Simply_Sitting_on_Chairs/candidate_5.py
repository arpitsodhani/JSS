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


# --- clause: solve_case :: (p: list[int]) -> int ---
def solve_case(p):
    n = len(p)
    home = [0] * (n + 2)
    for i in range(n):
        home[p[i]] = i + 1
    best = 0
    kept = 0
    live = 0
    for h in range(1, n + 2):
        if h > 1:
            cur = p[h - 2]
            if cur <= h - 1:
                kept += 1
            if home[h - 1] < h - 1:
                live -= 1
            if cur >= h:
                live += 1
        score = kept + live
        if score > best:
            best = score
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(solve_case(values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
