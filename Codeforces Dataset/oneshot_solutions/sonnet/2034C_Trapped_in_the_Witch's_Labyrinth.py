import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1),
    }
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        grid = []
        for _ in range(n):
            grid.append(data[idx])
            idx += 1
        
        alive = [[True] * m for _ in range(n)]
        need = [[0] * m for _ in range(n)]
        reverse = [[[] for _ in range(m)] for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                c = grid[i][j]
                if c == '?':
                    cnt = 0
                    for di, dj in directions.values():
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            cnt += 1
                    need[i][j] = cnt
                    if cnt == 0:
                        alive[i][j] = False
                        q.append((i, j))
                else:
                    di, dj = directions[c]
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m:
                        reverse[ni][nj].append((i, j))
                    else:
                        alive[i][j] = False
                        q.append((i, j))
        
        while q:
            x, y = q.popleft()
            
            for px, py in reverse[x][y]:
                if alive[px][py]:
                    alive[px][py] = False
                    q.append((px, py))
            
            for di, dj in directions.values():
                px, py = x + di, y + dj
                if 0 <= px < n and 0 <= py < m and alive[px][py] and grid[px][py] == '?':
                    need[px][py] -= 1
                    if need[px][py] == 0:
                        alive[px][py] = False
                        q.append((px, py))
        
        ans = 0
        for i in range(n):
            ans += sum(alive[i])
        
        out.append(str(ans))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
