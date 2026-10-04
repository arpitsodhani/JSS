# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def build_path(n, edges):
    degree = [0] * n
    nexts = [[-1, -1] for _ in range(n)]
    for a, b in edges:
        ia = degree[a]
        ib = degree[b]
        if ia >= 2 or ib >= 2:
            return None
        nexts[a][ia] = b
        nexts[b][ib] = a
        degree[a] += 1
        degree[b] += 1
    for d in degree:
        if d > 2:
            return None
    start = 0
    for i, d in enumerate(degree):
        if d == 1:
            start = i
            break
    path = []
    parent = -1
    cur = start
    for _ in range(n):
        path.append(cur)
        a, b = nexts[cur]
        cur, parent = (a if a != parent else b), cur
    return path

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    costs = []
    at = 1
    for _ in range(3):
        costs.append(data[at:at + n])
        at += n
    edges = []
    for _ in range(n - 1):
        edges.append((data[at] - 1, data[at + 1] - 1))
        at += 2

    if n == 1:
        color = 0
        if costs[1][0] < costs[color][0]:
            color = 1
        if costs[2][0] < costs[color][0]:
            color = 2
        print(costs[color][0])
        print(color + 1)
        return

    if n == 2:
        c0 = min((costs[c][0], c) for c in range(3))[1]
        c1 = min((costs[c][1], c) for c in range(3))[1]
        print(costs[c0][0] + costs[c1][1])
        print(c0 + 1, c1 + 1)
        return

    path = build_path(n, edges)
    if path is None:
        print(-1)
        return

    choices = ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0))
    best_value = 10 ** 40
    best_choice = choices[0]
    for choice in choices:
        value = sum(costs[choice[i % 3]][vertex] for i, vertex in enumerate(path))
        if value < best_value:
            best_value = value
            best_choice = choice

    colors = [0] * n
    for i, vertex in enumerate(path):
        colors[vertex] = best_choice[i % 3] + 1

    print(best_value)
    print(*colors)

# CLAUSE: finish_program
main()
