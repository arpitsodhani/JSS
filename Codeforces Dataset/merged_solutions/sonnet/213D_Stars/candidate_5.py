# CLAUSE: setup_environment
import math
import sys
from collections import deque

# CLAUSE: solve_logic
def solve():
    n = int(sys.stdin.read())
    r = 10.0 / (2.0 * math.sin(math.pi / 5.0))
    shifts = tuple((r * math.cos(2.0 * math.pi * i / 5.0), r * math.sin(2.0 * math.pi * i / 5.0)) for i in range(5))
    points = []
    rings = []
    center = (0.0, 0.0)
    for i in range(n):
        ring = []
        first = 0
        if i:
            ring.append(rings[-1][-1])
            x, y = points[ring[0] - 1]
            center = (x - r, y)
            first = 1
        for j in range(first, 5):
            points.append((center[0] + shifts[j][0], center[1] + shifts[j][1]))
            ring.append(len(points))
        rings.append(ring)

    graph = [set() for _ in range(len(points) + 1)]
    for ring in rings:
        a, b, c, d, e = ring
        pairs = ((a, b), (a, c), (a, d), (a, e), (b, c), (b, d), (b, e), (c, d), (c, e), (d, e))
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)

    active = deque([1])
    circuit = []
    while active:
        v = active[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            active.append(u)
        else:
            circuit.append(active.pop())
    circuit.reverse()

# CLAUSE: finish_program
    result = [str(len(points))]
    result.extend("%.15f %.15f" % (x, y) for x, y in points)
    result.append(" ".join(str(v) for v in circuit))
    sys.stdout.write("\n".join(result))

solve()
