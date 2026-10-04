import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[tuple[int, int, int]]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        mines = []
        for _ in range(n):
            mines.append((data[pos], data[pos + 1], data[pos + 2]))
            pos += 3
        cases.append((n, k, mines))
    return cases

# --- clause: component_timers :: (n: int, k: int, mines: list[tuple[int, int, int]]) -> list[int] ---
def component_timers(n, k, mines):
    parent = list(range(n))

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[ra] = rb

    by_row = {}
    by_column = {}
    for i, (x, y, _timer) in enumerate(mines):
        by_row.setdefault(y, []).append((x, i))
        by_column.setdefault(x, []).append((y, i))
    for line in by_row.values():
        line.sort()
        for j in range(1, len(line)):
            if line[j][0] - line[j - 1][0] <= k:
                union(line[j - 1][1], line[j][1])
    for line in by_column.values():
        line.sort()
        for j in range(1, len(line)):
            if line[j][0] - line[j - 1][0] <= k:
                union(line[j - 1][1], line[j][1])
    lowest = {}
    for i in range(n):
        root = find(i)
        timer = mines[i][2]
        if root not in lowest or timer < lowest[root]:
            lowest[root] = timer
    return sorted(lowest.values())

# --- clause: solve_case :: (n: int, k: int, mines: list[tuple[int, int, int]]) -> int ---
def solve_case(n, k, mines):
    timers = component_timers(n, k, mines)
    total = len(timers)
    idx = 0
    for seconds in range(total):
        while idx < total and timers[idx] <= seconds:
            idx += 1
        if total - idx <= seconds + 1:
            return seconds
    return total - 1

# --- clause: main :: () -> None ---
def main():
    out = []
    for n, k, mines in read_input():
        out.append(str(solve_case(n, k, mines)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
