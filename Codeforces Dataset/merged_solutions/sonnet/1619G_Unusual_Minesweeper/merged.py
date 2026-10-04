import sys

# Clause read_input [Confidence: 1.00]
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

# Clause component_timers [Confidence: 1.00]
def component_timers(n, k, mines):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[ra] = rb

    rows = sorted(range(n), key=lambda i: (mines[i][1], mines[i][0]))
    for i in range(1, n):
        first = rows[i - 1]
        second = rows[i]
        if mines[first][1] == mines[second][1] and mines[second][0] - mines[first][0] <= k:
            union(first, second)
    columns = sorted(range(n), key=lambda i: (mines[i][0], mines[i][1]))
    for i in range(1, n):
        first = columns[i - 1]
        second = columns[i]
        if mines[first][0] == mines[second][0] and mines[second][1] - mines[first][1] <= k:
            union(first, second)
    lowest = {}
    for i in range(n):
        root = find(i)
        timer = mines[i][2]
        if root not in lowest or timer < lowest[root]:
            lowest[root] = timer
    return sorted(lowest.values())

# Clause solve_case [Confidence: 0.60]
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

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, k, mines in read_input():
        out.append(str(solve_case(n, k, mines)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

