# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
from collections import deque

def solve():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    
    # Find connected components
    component = [[-1] * m for _ in range(n)]
    comp_size = []
    comp_id = 0
    
    def bfs(sr, sc):
        q = deque([(sr, sc)])
        component[sr][sc] = comp_id
        size = 1
        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '#' and component[nr][nc] == -1:
                    component[nr][nc] = comp_id
                    q.append((nr, nc))
                    size += 1
        return size
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and component[i][j] == -1:
                size = bfs(i, j)
                comp_size.append(size)
                comp_id += 1
    
    # For each row, find components that touch it
    row_comps = []
    row_dots = []
    for r in range(n):
        comps = set()
        dots = 0
        for c in range(m):
            if grid[r][c] == '#':
                comps.add(component[r][c])
            else:
                dots += 1
            # Check cells above and below
            for dr in [-1, 1]:
                nr = r + dr
                if 0 <= nr < n and grid[nr][c] == '#':
                    comps.add(component[nr][c])
        row_comps.append(comps)
        row_dots.append(dots)
    
    # For each column, find components that touch it
    col_comps = []
    col_dots = []
    for c in range(m):
        comps = set()
        dots = 0
        for r in range(n):
            if grid[r][c] == '#':
                comps.add(component[r][c])
            else:
                dots += 1
            # Check cells left and right
            for dc in [-1, 1]:
                nc = c + dc
                if 0 <= nc < m and grid[r][nc] == '#':
                    comps.add(component[r][nc])
        col_comps.append(comps)
        col_dots.append(dots)
    
    # Find maximum
    max_size = max(comp_size) if comp_size else 0
    
    for r in range(n):
        for c in range(m):
            # Union of components
            comps = row_comps[r] | col_comps[c]
            size = sum(comp_size[cid] for cid in comps)
            size += row_dots[r] + col_dots[c]
            # Subtract 1 if grid[r][c] is '.' (counted twice)
            if grid[r][c] == '.':
                size -= 1
            max_size = max(max_size, size)
    
    print(max_size)

t = int(input())
for _ in range(t):
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
