# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from collections import deque

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        sys.exit()

    w, h, n = data[0], data[1], data[2]
    segments = []
    xs = [0, w]
    ys = [0, h]

    p = 3
    for _ in range(n):
        x1, y1, x2, y2 = data[p], data[p + 1], data[p + 2], data[p + 3]
        p += 4
        if x1 > x2 or y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        segments.append((x1, y1, x2, y2))
        xs.append(x1)
        xs.append(x2)
        ys.append(y1)
        ys.append(y2)

    xs = sorted(set(xs))
    ys = sorted(set(ys))
    xi = {x: i for i, x in enumerate(xs)}
    yi = {y: i for i, y in enumerate(ys)}

    cx = len(xs) - 1
    cy = len(ys) - 1

    vertical = [[False] * cy for _ in range(len(xs))]
    horizontal = [[False] * len(ys) for _ in range(cx)]

    for x1, y1, x2, y2 in segments:
        if x1 == x2:
            x = xi[x1]
            a = yi[y1]
            b = yi[y2]
            for j in range(a, b):
                vertical[x][j] = True
        else:
            y = yi[y1]
            a = xi[x1]
            b = xi[x2]
            for i in range(a, b):
                horizontal[i][y] = True

    visited = [[False] * cy for _ in range(cx)]
    areas = []

    for sx in range(cx):
        for sy in range(cy):
            if visited[sx][sy]:
                continue

            q = deque([(sx, sy)])
            visited[sx][sy] = True
            area = 0

            while q:
                x, y = q.popleft()
                area += (xs[x + 1] - xs[x]) * (ys[y + 1] - ys[y])

                if x > 0 and not vertical[x][y] and not visited[x - 1][y]:
                    visited[x - 1][y] = True
                    q.append((x - 1, y))
                if x + 1 < cx and not vertical[x + 1][y] and not visited[x + 1][y]:
                    visited[x + 1][y] = True
                    q.append((x + 1, y))
                if y > 0 and not horizontal[x][y] and not visited[x][y - 1]:
                    visited[x][y - 1] = True
                    q.append((x, y - 1))
                if y + 1 < cy and not horizontal[x][y + 1] and not visited[x][y + 1]:
                    visited[x][y + 1] = True
                    q.append((x, y + 1))

            areas.append(area)

    areas.sort()
    print(*areas)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
