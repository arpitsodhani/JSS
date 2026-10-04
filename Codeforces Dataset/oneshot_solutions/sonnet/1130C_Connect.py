import sys
from collections import deque

def main():
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    r1, c1 = map(int, lines[1].split())
    r2, c2 = map(int, lines[2].split())
    grid = [lines[i+3] for i in range(n)]
    
    def bfs(start_r, start_c):
        visited = [[False] * n for _ in range(n)]
        queue = deque([(start_r, start_c)])
        visited[start_r-1][start_c-1] = True
        component = [(start_r, start_c)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 1 <= nr <= n and 1 <= nc <= n and not visited[nr-1][nc-1]:
                    if grid[nr-1][nc-1] == '0':
                        visited[nr-1][nc-1] = True
                        queue.append((nr, nc))
                        component.append((nr, nc))
        
        return component
    
    comp1 = bfs(r1, c1)
    comp2 = bfs(r2, c2)
    
    # Check if already connected
    comp1_set = set(comp1)
    if any(cell in comp1_set for cell in comp2):
        print(0)
    else:
        # Find minimum cost tunnel
        min_cost = min((rs - rt) ** 2 + (cs - ct) ** 2 
                       for rs, cs in comp1 
                       for rt, ct in comp2)
        print(min_cost)

if __name__ == "__main__":
    main()
