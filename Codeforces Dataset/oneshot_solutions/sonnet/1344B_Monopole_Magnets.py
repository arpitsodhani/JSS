import sys
from collections import deque

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    n, m = map(int, input_lines[0].split())
    grid = [input_lines[i+1] for i in range(n)]
    
    # Check if every row has at least one black cell
    for r in range(n):
        if '#' not in grid[r]:
            print(-1)
            return
    
    # Check if every column has at least one black cell
    for c in range(m):
        has_black = any(grid[r][c] == '#' for r in range(n))
        if not has_black:
            print(-1)
            return
    
    # Check contiguity in rows
    for r in range(n):
        first = -1
        last = -1
        for c in range(m):
            if grid[r][c] == '#':
                if first == -1:
                    first = c
                last = c
        if first != -1:
            for c in range(first, last + 1):
                if grid[r][c] == '.':
                    print(-1)
                    return
    
    # Check contiguity in columns
    for c in range(m):
        first = -1
        last = -1
        for r in range(n):
            if grid[r][c] == '#':
                if first == -1:
                    first = r
                last = r
        if first != -1:
            for r in range(first, last + 1):
                if grid[r][c] == '.':
                    print(-1)
                    return
    
    # Count connected components using BFS
    visited = [[False] * m for _ in range(n)]
    components = 0
    
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '#' and not visited[r][c]:
                components += 1
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '#' and not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    
    print(components)

if __name__ == "__main__":
    main()
