import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    r1, c1 = int(data[1]) - 1, int(data[2]) - 1
    r2, c2 = int(data[3]) - 1, int(data[4]) - 1
    grid = data[5:5 + n]

    def bfs(sr, sc):
        seen = [[False] * n for _ in range(n)]
        q = deque([(sr, sc)])
        seen[sr][sc] = True
        cells = []

        while q:
            r, c = q.popleft()
            cells.append((r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc] and grid[nr][nc] == '0':
                    seen[nr][nc] = True
                    q.append((nr, nc))

        return cells, seen

    comp1, seen1 = bfs(r1, c1)
    if seen1[r2][c2]:
        print(0)
        return

    comp2, _ = bfs(r2, c2)

    ans = 10 ** 9
    for a, b in comp1:
        for x, y in comp2:
            cost = (a - x) * (a - x) + (b - y) * (b - y)
            if cost < ans:
                ans = cost

    print(ans)

if __name__ == "__main__":
    main()
