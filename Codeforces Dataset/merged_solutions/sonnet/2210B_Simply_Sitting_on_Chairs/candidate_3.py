import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    q = tokens[idx]
    idx += 1
    cases = []
    for _ in range(q):
        n = tokens[idx]
        idx += 1
        seq = tokens[idx:idx + n]
        idx += n
        cases.append(seq)
    return cases


# --- clause: solve_case :: (p: list[int]) -> int ---
def solve_case(p):
    n = len(p)
    spot = [0] * (n + 2)
    for i in range(n):
        spot[p[i]] = i + 1
    best = 0
    settled = 0
    pending = 0
    for h in range(1, n + 2):
        if h > 1:
            prev = p[h - 2]
            settled = settled + 1 if prev <= h - 1 else settled
            if spot[h - 1] < h - 1:
                pending = pending - 1
            if prev >= h:
                pending = pending + 1
        best = max(best, settled + pending)
    return best


# --- clause: main :: () -> None ---
def main():
    lines = []
    for seq in read_input():
        lines.append(str(solve_case(seq)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
