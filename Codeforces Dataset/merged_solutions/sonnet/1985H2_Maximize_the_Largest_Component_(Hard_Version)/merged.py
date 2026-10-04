# Clause setup_environment [Confidence: 0.60]
import sys
from collections import defaultdict

def main():
    raw = sys.stdin.read().split()
    pos = 0
    cases = int(raw[pos])
    pos += 1
    answers = []


# Clause solve_logic [Confidence: 0.80]
    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        grid = [next(it) for _ in range(n)]
        comp = [[-1] * m for _ in range(n)]
        sizes = []
        boxes = []
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#' and comp[i][j] < 0:
                    cid = len(sizes)
                    q = deque([(i, j)])
                    comp[i][j] = cid
                    cnt = 0
                    lo_r = hi_r = i
                    lo_c = hi_c = j
                    while q:
                        r, c = q.popleft()
                        cnt += 1
                        if r < lo_r:
                            lo_r = r
                        if r > hi_r:
                            hi_r = r
                        if c < lo_c:
                            lo_c = c
                        if c > hi_c:
                            hi_c = c
                        for dr, dc in dirs:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '#' and comp[nr][nc] < 0:
                                comp[nr][nc] = cid
                                q.append((nr, nc))
                    sizes.append(cnt)
                    boxes.append((max(0, lo_r - 1), min(n - 1, hi_r + 1), max(0, lo_c - 1), min(m - 1, hi_c + 1)))
        row_gain = [row.count('.') for row in grid]
        col_gain = [0] * m
        for r in range(n):
            for c, ch in enumerate(grid[r]):
                if ch == '.':
                    col_gain[c] += 1
        diff = [[0] * (m + 1) for _ in range(n + 1)]
        for w, (r1, r2, c1, c2) in zip(sizes, boxes):
            diff[r1][c1] += w
            diff[r2 + 1][c1] -= w
            diff[r1][c2 + 1] -= w
            diff[r2 + 1][c2 + 1] += w
            for r in range(r1, r2 + 1):
                row_gain[r] += w
            for c in range(c1, c2 + 1):
                col_gain[c] += w
        best = max(sizes, default=0)
        for r in range(n):
            run = 0
            for c in range(m):
                run += diff[r][c]
                if r:
                    diff[r][c] += diff[r - 1][c]
                    cur_overlap = diff[r][c]
                else:
                    cur_overlap = run
                    diff[r][c] = run
                cur = row_gain[r] + col_gain[c] - cur_overlap
                if grid[r][c] == '.':
                    cur -= 1
                if cur > best:
                    best = cur
        ans.append(str(best))


# Clause finish_program [Confidence: 0.80]
    sys.stdout.write("\n".join(ans))

main()


