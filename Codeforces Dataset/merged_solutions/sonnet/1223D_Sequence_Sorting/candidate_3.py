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
    lo = {}
    hi = {}
    for i in range(len(a)):
        key = a[i]
        if key not in lo:
            lo[key] = i
        hi[key] = i
    order = sorted(lo.keys())
    longest = 1
    chain = 1
    for j in range(1, len(order)):
        prev = order[j - 1]
        here = order[j]
        chain = chain + 1 if hi[prev] < lo[here] else 1
        if chain > longest:
            longest = chain
    return len(order) - longest


# --- clause: main :: () -> None ---
def main():
    lines = []
    for seq in read_input():
        lines.append(str(solve_case(seq)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
