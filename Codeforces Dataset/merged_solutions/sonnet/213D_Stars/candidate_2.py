# CLAUSE: setup_environment
import math
import sys

# CLAUSE: solve_logic
def solve():
    data = sys.stdin.read().strip().split()
    n = int(data[0])
    side = 10.0
    radius = side / (2.0 * math.sin(math.pi / 5.0))
    vertices = []
    pentagons = []
    for p in range(n):
        current = []
        if p == 0:
            cx = 0.0
            cy = 0.0
            start = 0
        else:
            current.append(pentagons[-1][-1])
            sx, sy = vertices[current[0] - 1]
            cx = sx - radius
            cy = sy
            start = 1
        for i in range(start, 5):
            a = 2.0 * math.pi * i / 5.0
            vertices.append((cx + radius * math.cos(a), cy + radius * math.sin(a)))
            current.append(len(vertices))
        pentagons.append(current)

    graph = {i: [] for i in range(1, len(vertices) + 1)}
    for pentagon in pentagons:
        for i in range(5):
            u = pentagon[i]
            for j in range(i + 1, 5):
                v = pentagon[j]
                graph[u].append(v)
                graph[v].append(u)

    stack = [1]
    route = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            route.append(stack.pop())
    route.reverse()

# CLAUSE: finish_program
    out = [str(len(vertices))]
    out.extend(f"{x:.15f} {y:.15f}" for x, y in vertices)
    out.append(" ".join(str(x) for x in route))
    sys.stdout.write("\n".join(out))

solve()
