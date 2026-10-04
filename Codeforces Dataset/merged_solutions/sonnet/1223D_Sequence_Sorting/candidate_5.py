import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    q = raw[p]
    p += 1
    cases = []
    for _ in range(q):
        n = raw[p]
        p += 1
        values = raw[p:p + n]
        p += n
        cases.append(values)
    return cases


# --- clause: solve_case :: (a: list[int]) -> int ---
def solve_case(a):
    head = {}
    tail = {}
    for i in range(len(a)):
        x = a[i]
        head.setdefault(x, i)
        tail[x] = i
    uniq = sorted(head)
    best = 1
    window = 1
    for j in range(1, len(uniq)):
        if tail[uniq[j - 1]] < head[uniq[j]]:
            window += 1
        else:
            window = 1
        if best < window:
            best = window
    return len(uniq) - best


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(str(solve_case(values)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
