import sys


# --- clause: read_input :: () -> tuple[int, list[int], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    parents = [0, 0] + tokens[1:n]
    sums = tokens[n:2 * n]
    return n, parents, sums


# --- clause: restore :: (n: int, parents: list[int], sums: list[int]) -> int ---
def restore(n, parents, sums):
    depth = [0] * (n + 1)
    depth[1] = 1
    children = [0] * (n + 1)
    known = [0] * (n + 1)
    for v in range(2, n + 1):
        depth[v] = depth[parents[v]] + 1
        children[parents[v]] += 1
    for v in range(1, n + 1):
        known[v] = sums[v - 1]
    for v in range(n, 1, -1):
        if depth[v] % 2 == 0:
            continue
        p = parents[v]
        if known[p] == -1 or known[v] < known[p]:
            known[p] = known[v]
    amount = 0
    for v in range(1, n + 1):
        if depth[v] % 2 == 0 and known[v] == -1:
            known[v] = known[parents[v]]
        if v == 1:
            amount += known[v]
        else:
            gap = known[v] - known[parents[v]]
            if gap < 0:
                return -1
            amount += gap
    return amount


# --- clause: main :: () -> None ---
def main():
    n, parents, sums = read_input()
    sys.stdout.write("%d\n" % restore(n, parents, sums))


if __name__ == "__main__":
    main()
