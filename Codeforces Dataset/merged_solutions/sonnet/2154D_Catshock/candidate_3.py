# CLAUSE: setup_environment
import sys
from collections import deque

def solve_case(n, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

# CLAUSE: solve_logic
    parent = [-2] * (n + 1)
    parent[n] = -1
    queue = deque([n])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            if parent[nxt] == -2:
                parent[nxt] = node
                queue.append(nxt)

    path = set()
    node = 1
    while True:
        path.add(node)
        if node == n:
            break
        node = parent[node]

    commands = []
    for node in order:
        if node not in path:
            commands.extend(((2, node), (1, 0)))

    node = 1
    while node != n:
        commands.extend(((2, node), (1, 0)))
        node = parent[node]

    return commands

# CLAUSE: finish_program
def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    at = 0
    t = nums[at]
    at += 1
    out = []
    for _ in range(t):
        n = nums[at]
        at += 1
        edges = []
        for _ in range(n - 1):
            edges.append((nums[at], nums[at + 1]))
            at += 2
        commands = solve_case(n, edges)
        out.append(str(len(commands)))
        for typ, value in commands:
            out.append("1" if typ == 1 else "2 " + str(value))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
