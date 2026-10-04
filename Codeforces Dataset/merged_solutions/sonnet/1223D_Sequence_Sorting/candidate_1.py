import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    q = data[pos]
    pos += 1
    cases = []
    for _ in range(q):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    n = len(a)
    first = {}
    last = {}
    for i in range(n):
        v = a[i]
        if v not in first:
            first[v] = i
        last[v] = i
    vals = sorted(first)
    best = 1
    cur = 1
    for j in range(1, len(vals)):
        if last[vals[j - 1]] < first[vals[j]]:
            cur += 1
        else:
            cur = 1
        if cur > best:
            best = cur
    return len(vals) - best


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
