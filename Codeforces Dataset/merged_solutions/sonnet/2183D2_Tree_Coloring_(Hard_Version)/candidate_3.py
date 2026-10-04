# CLAUSE: setup_environment
import sys

def allocate(row, forbidden, k):
    size = len(row)
    result = [i + 1 for i in range(size)]
    if size < k:
        hold = size + 1
        for i, v in enumerate(row):
            bad = forbidden[v]
            if result[i] == bad:
                result[i] = hold
                hold = bad
        return result
    anchor = 0
    swap_with = -1
    base_bad = forbidden[row[0]]
    for i in range(1, size):
        if forbidden[row[i]] != base_bad:
            swap_with = i
            break
    for i, v in enumerate(row):
        if result[i] == forbidden[v]:
            target = anchor if base_bad != forbidden[v] else swap_with
            result[i], result[target] = result[target], result[i]
    return result

# CLAUSE: solve_logic
def solve_case(n, edges):
    adj = [[] for _ in range(n + 1)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)

    parent = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    levels = [[1]]
    parent[1] = -1
    layer = [1]

    while layer:
        nxt = []
        for v in layer:
            for u in adj[v]:
                if u != parent[v]:
                    parent[u] = v
                    children[v].append(u)
                    nxt.append(u)
        if nxt:
            levels.append(nxt)
        layer = nxt

    widest = max(map(len, levels))
    operations = widest
    for row in levels:
        if len(row) == widest and row != levels[0]:
            p = parent[row[0]]
            if all(parent[v] == p for v in row):
                operations += 1
                break

    color = [0] * (n + 1)
    color[1] = 1
    groups = [[] for _ in range(operations + 1)]
    groups[1].append(1)
    forbidden = [0] * (n + 1)

    for row in levels[1:]:
        for v in row:
            forbidden[v] = color[parent[v]]
        assigned = allocate(row, forbidden, operations)
        for i, v in enumerate(row):
            c = assigned[i]
            color[v] = c
            groups[c].append(v)

    lines = [str(operations)]
    for group in groups[1:]:
        line = [str(len(group))]
        line.extend(map(str, group))
        lines.append(" ".join(line))
    return lines

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    answer = []
    for _ in range(nums[0]):
        n = nums[at]
        at += 1
        edges = []
        for _ in range(n - 1):
            edges.append((nums[at], nums[at + 1]))
            at += 2
        answer += solve_case(n, edges)
    print("\n".join(answer))

if __name__ == "__main__":
    main()
