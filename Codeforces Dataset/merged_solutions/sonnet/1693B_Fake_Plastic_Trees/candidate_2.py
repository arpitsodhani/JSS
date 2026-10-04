import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int], list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    ptr = 0
    tests = data[ptr]
    ptr += 1
    cases = []
    for _ in range(tests):
        n = data[ptr]
        ptr += 1
        par = [0] * (n + 1)
        for v in range(2, n + 1):
            par[v] = data[ptr]
            ptr += 1
        lo = [0] * (n + 1)
        hi = [0] * (n + 1)
        for v in range(1, n + 1):
            lo[v] = data[ptr]
            hi[v] = data[ptr + 1]
            ptr += 2
        cases.append((n, par, lo, hi))
    return cases


# --- clause: solve_case :: (n: int, parent: list[int], low: list[int], high: list[int]) -> int ---
def solve_case(n, parent, low, high):
    gathered = [0] * (n + 2)
    ops = 0
    for v in range(n, 0, -1):
        got = gathered[v]
        if got >= low[v]:
            give = got if got < high[v] else high[v]
        else:
            ops += 1
            give = high[v]
        gathered[parent[v]] += give
    return ops


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    answers = []
    for case in cases:
        answers.append(str(solve_case(case[0], case[1], case[2], case[3])))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
