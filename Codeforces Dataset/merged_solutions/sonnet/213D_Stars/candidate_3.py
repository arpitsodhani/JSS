# CLAUSE: setup_environment
from math import cos, pi, sin
import sys

# CLAUSE: solve_logic
def make_vertices(count):
    r = 10.0 / (2.0 * sin(pi / 5.0))
    angles = [2.0 * pi * k / 5.0 for k in range(5)]
    points = []
    groups = []
    cx = 0.0
    cy = 0.0
    for idx in range(count):
        group = []
        first_angle = 0
        if idx:
            group.append(groups[-1][4])
            px, py = points[group[0] - 1]
            cx = px - r
            cy = py
            first_angle = 1
        for k in range(first_angle, 5):
            points.append((cx + r * cos(angles[k]), cy + r * sin(angles[k])))
            group.append(len(points))
        groups.append(group)
    return points, groups

def solve():
    n = int(sys.stdin.readline())
    points, groups = make_vertices(n)
    order = [0, 1, 2, 3, 4, 0, 2, 4, 1, 3, 0]
    walk = []
    for group in groups:
        if walk:
            walk.extend(group[i] for i in order[1:])
        else:
            walk.extend(group[i] for i in order)

# CLAUSE: finish_program
    answer = [str(len(points))]
    for x, y in points:
        answer.append("{:.15f} {:.15f}".format(x, y))
    answer.append(" ".join(map(str, walk)))
    sys.stdout.write("\n".join(answer))

solve()
