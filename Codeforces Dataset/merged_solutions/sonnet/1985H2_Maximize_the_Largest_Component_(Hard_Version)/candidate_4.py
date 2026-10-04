# CLAUSE: setup_environment
import sys

def main():
    data = sys.stdin.buffer.read().split()
    k = 0
    t = int(data[k])
    k += 1
    res = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = int(data[k])
        m = int(data[k + 1])
        k += 2
        grid = [data[k + i].decode() for i in range(n)]
        k += n
        comp = [[-1] * m for _ in range(n)]
        sizes = []
        rects = []
        for sr in range(n):
            for sc in range(m):
                if grid[sr][sc] == '#' and comp[sr][sc] == -1:
                    cid = len(sizes)
                    stack = [(sr, sc)]
                    comp[sr][sc] = cid
                    count = 0
                    min_r = max_r = sr
                    min_c = max_c = sc
                    while stack:
                        r, c = stack.pop()
                        count += 1
                        if r < min_r:
                            min_r = r
                        elif r > max_r:
                            max_r = r
                        if c < min_c:
                            min_c = c
                        elif c > max_c:
                            max_c = c
                        nr = r - 1
                        if nr >= 0 and grid[nr][c] == '#' and comp[nr][c] == -1:
                            comp[nr][c] = cid
                            stack.append((nr, c))
                        nr = r + 1
                        if nr < n and grid[nr][c] == '#' and comp[nr][c] == -1:
                            comp[nr][c] = cid
                            stack.append((nr, c))
                        nc = c - 1
                        if nc >= 0 and grid[r][nc] == '#' and comp[r][nc] == -1:
                            comp[r][nc] = cid
                            stack.append((r, nc))
                        nc = c + 1
                        if nc < m and grid[r][nc] == '#' and comp[r][nc] == -1:
                            comp[r][nc] = cid
                            stack.append((r, nc))
                    sizes.append(count)
                    rects.append((max(0, min_r - 1), min(n - 1, max_r + 1), max(0, min_c - 1), min(m - 1, max_c + 1)))
        rows = [0] * n
        cols = [0] * m
        for r in range(n):
            row = grid[r]
            rows[r] = row.count('.')
            for c in range(m):
                if row[c] == '.':
                    cols[c] += 1
        events = [[] for _ in range(n + 1)]
        for cid, size in enumerate(sizes):
            r1, r2, c1, c2 = rects[cid]
            for r in range(r1, r2 + 1):
                rows[r] += size
            for c in range(c1, c2 + 1):
                cols[c] += size
            events[r1].append((c1, c2, size))
            events[r2 + 1].append((c1, c2, -size))
        active = [0] * m
        best = max(sizes) if sizes else 0
        for r in range(n):
            for c1, c2, delta in events[r]:
                for c in range(c1, c2 + 1):
                    active[c] += delta
            row_base = rows[r]
            row_text = grid[r]
            for c in range(m):
                total = row_base + cols[c] - active[c]
                if row_text[c] == '.':
                    total -= 1
                if total > best:
                    best = total
        res.append(str(best))

# CLAUSE: finish_program
    print("\n".join(res))

main()
