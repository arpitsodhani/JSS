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


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    work = list(a)
    best = sum(work)
    while len(work) > 1:
        work = [work[i] - work[i - 1] for i in range(1, len(work))]
        candidate = abs(sum(work))
        best = candidate if candidate > best else best
    return best


# --- clause: main :: () -> None ---
def main():
    lines = []
    for seq in read_input():
        lines.append(str(solve_case(seq)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
