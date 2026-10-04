# CLAUSE: setup_environment
import sys
from collections import defaultdict

def main():
    raw = sys.stdin.read().split()
    pos = 0
    cases = int(raw[pos])
    pos += 1
    answers = []

# CLAUSE: solve_logic
    for _ in range(cases):
        n = int(raw[pos])
        m = int(raw[pos + 1])
        pos += 2
        grid = raw[pos:pos + n]
        pos += n
        seen = [[False] * m for _ in range(n)]
        components = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '#' and not seen[r][c]:
                    q = [(r, c)]
                    seen[r][c] = True
                    head = 0
                    size = 0
                    rlo = rhi = r
                    clo = chi = c
                    while head < len(q):
                        x, y = q[head]
                        head += 1
                        size += 1
                        rlo = min(rlo, x)
                        rhi = max(rhi, x)
                        clo = min(clo, y)
                        chi = max(chi, y)
                        for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '#' and not seen[nx][ny]:
                                seen[nx][ny] = True
                                q.append((nx, ny))
                    components.append((size, max(0, rlo - 1), min(n - 1, rhi + 1), max(0, clo - 1), min(m - 1, chi + 1)))
        row_score = [sum(ch == '.' for ch in grid[r]) for r in range(n)]
        col_score = [sum(grid[r][c] == '.' for r in range(n)) for c in range(m)]
        row_add = defaultdict(int)
        col_add = defaultdict(int)
        rect_add = [[0] * (m + 1) for _ in range(n + 1)]
        answer = 0
        for size, a, b, l, rr in components:
            answer = max(answer, size)
            row_add[a] += size
            row_add[b + 1] -= size
            col_add[l] += size
            col_add[rr + 1] -= size
            rect_add[a][l] += size
            rect_add[b + 1][l] -= size
            rect_add[a][rr + 1] -= size
            rect_add[b + 1][rr + 1] += size
        cur = 0
        for r in range(n):
            cur += row_add[r]
            row_score[r] += cur
        cur = 0
        for c in range(m):
            cur += col_add[c]
            col_score[c] += cur
        vertical = [0] * m
        for r in range(n):
            horizontal = 0
            for c in range(m):
                horizontal += rect_add[r][c]
                vertical[c] += horizontal
                value = row_score[r] + col_score[c] - vertical[c]
                if grid[r][c] == '.':
                    value -= 1
                if value > answer:
                    answer = value
        answers.append(str(answer))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(answers))

main()
