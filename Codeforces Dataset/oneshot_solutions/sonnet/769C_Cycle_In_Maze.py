import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    grid = data[3:3 + n]
    
    start_r = start_c = -1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                start_r, start_c = i, j
    
    if k % 2 == 1:
        print("IMPOSSIBLE")
        return
    
    dist = [[-1] * m for _ in range(n)]
    q = deque([(start_r, start_c)])
    dist[start_r][start_c] = 0
    
    moves = [
        ('D', 1, 0),
        ('L', 0, -1),
        ('R', 0, 1),
        ('U', -1, 0),
    ]
    
    while q:
        r, c = q.popleft()
        for _, dr, dc in moves:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '*' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    
    r, c = start_r, start_c
    result = []
    
    for step in range(k):
        remaining = k - step - 1
        chosen = False
        
        for ch, dr, dc in moves:
            nr = r + dr
            nc = c + dc
            
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if grid[nr][nc] == '*' or dist[nr][nc] == -1:
                continue
            if dist[nr][nc] <= remaining and (remaining - dist[nr][nc]) % 2 == 0:
                result.append(ch)
                r, c = nr, nc
                chosen = True
                break
        
        if not chosen:
            print("IMPOSSIBLE")
            return
    
    print(''.join(result))

if __name__ == "__main__":
    main()
