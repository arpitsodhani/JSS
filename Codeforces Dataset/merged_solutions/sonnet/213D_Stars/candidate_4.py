# CLAUSE: setup_environment
import math
import sys

# CLAUSE: solve_logic
def solve():
    n = int(sys.stdin.buffer.readline())
    r = 5.0 / math.sin(math.pi / 5.0)
    unit = []
    for k in range(5):
        t = 2.0 * math.pi * k / 5.0
        unit.append((r * math.cos(t), r * math.sin(t)))

    points = []
    stars = []
    center_x = 0.0
    center_y = 0.0
    previous_shared = 0
    for star in range(n):
        ids = []
        begin = 0
        if star > 0:
            ids.append(previous_shared)
            sx, sy = points[previous_shared - 1]
            center_x = sx - r
            center_y = sy
            begin = 1
        while begin < 5:
            dx, dy = unit[begin]
            points.append((center_x + dx, center_y + dy))
            ids.append(len(points))
            begin += 1
        previous_shared = ids[-1]
        stars.append(ids)

    edges = []
    for ids in stars:
        for i in range(5):
            for j in range(i + 1, 5):
                edges.append((ids[i], ids[j]))

    adjacency = [[] for _ in range(len(points) + 1)]
    for index, pair in enumerate(edges):
        a, b = pair
        adjacency[a].append((b, index))
        adjacency[b].append((a, index))

    used = [False] * len(edges)
    stack = [1]
    trail = []
    while stack:
        v = stack[-1]
        while adjacency[v] and used[adjacency[v][-1][1]]:
            adjacency[v].pop()
        if adjacency[v]:
            to, edge_id = adjacency[v].pop()
            if not used[edge_id]:
                used[edge_id] = True
                stack.append(to)
        else:
            trail.append(stack.pop())
    trail = trail[::-1]

# CLAUSE: finish_program
    lines = [str(len(points))]
    lines += [f"{point[0]:.15f} {point[1]:.15f}" for point in points]
    lines += [" ".join(map(str, trail))]
    print("\n".join(lines))

solve()
