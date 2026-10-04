import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int], list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    t = raw[p]
    p += 1
    cases = []
    for _ in range(t):
        n = raw[p]
        p += 1
        up = [0] * (n + 1)
        for v in range(2, n + 1):
            up[v] = raw[p]
            p += 1
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for v in range(1, n + 1):
            left[v] = raw[p]
            right[v] = raw[p + 1]
            p += 2
        cases.append((n, up, left, right))
    return cases


# --- clause: solve_case :: (n: int, parent: list[int], low: list[int], high: list[int]) -> int ---
def solve_case(n, parent, low, high):
    stored = [0] * (n + 2)
    used = 0
    for v in range(n, 0, -1):
        have = stored[v]
        if have < low[v]:
            used += 1
            have = high[v]
        else:
            have = min(have, high[v])
        stored[parent[v]] += have
    return used


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2], case[3])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
