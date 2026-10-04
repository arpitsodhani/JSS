# CLAUSE: setup_environment
import sys
from collections import deque

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n, m, k = map(int, data[:3])
    grid = data[3:3 + n]

    sr = sc = 0
    for i, row in enumerate(grid):
        pos = row.find("X")
        if pos != -1:
            sr, sc = i, pos
            break

    if k % 2:
        print("IMPOSSIBLE")
        return

    dist = [[-1] * m for _ in range(n)]
    dist[sr][sc] = 0
    q = deque([(sr, sc)])
    moves = (("D", 1, 0), ("L", 0, -1), ("R", 0, 1), ("U", -1, 0))

    while q:
        r, c = q.popleft()
        nd = dist[r][c] + 1
        for _, dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != "*" and dist[nr][nc] < 0:
                dist[nr][nc] = nd
                q.append((nr, nc))

    ans = []
    r, c = sr, sc
    for step in range(k):
        left = k - step - 1
        for ch, dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] != -1 and grid[nr][nc] != "*":
                if dist[nr][nc] <= left and (left - dist[nr][nc]) % 2 == 0:
                    ans.append(ch)
                    r, c = nr, nc
                    break
        else:
            print("IMPOSSIBLE")
            return

    print("".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
