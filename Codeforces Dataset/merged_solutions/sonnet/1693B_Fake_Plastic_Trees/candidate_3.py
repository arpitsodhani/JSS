import sys


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int], list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    q = tokens[idx]
    idx += 1
    cases = []
    for _ in range(q):
        n = tokens[idx]
        idx += 1
        upward = [0] * (n + 1)
        for v in range(2, n + 1):
            upward[v] = tokens[idx]
            idx += 1
        need = [0] * (n + 1)
        cap = [0] * (n + 1)
        for v in range(1, n + 1):
            need[v] = tokens[idx]
            cap[v] = tokens[idx + 1]
            idx += 2
        cases.append((n, upward, need, cap))
    return cases


# --- clause: solve_case :: (n: int, parent: list[int], low: list[int], high: list[int]) -> int ---
def solve_case(n, parent, low, high):
    pool = [0] * (n + 2)
    count = 0
    for v in range(n, 0, -1):
        supplied = pool[v]
        if supplied < low[v]:
            count += 1
            value = high[v]
        else:
            value = min(supplied, high[v])
        pool[parent[v]] += value
    return count


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, upward, need, cap in read_input():
        lines.append(str(solve_case(n, upward, need, cap)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
