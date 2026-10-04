import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, k = data[0], data[1], data[2]
    idx = 3
    
    grid = [[False] * (m + 2) for _ in range(n + 2)]
    
    for move in range(1, k + 1):
        r, c = data[idx], data[idx + 1]
        idx += 2
        
        grid[r][c] = True
        
        for dr in (0, -1):
            for dc in (0, -1):
                x = r + dr
                y = c + dc
                if 1 <= x < n and 1 <= y < m:
                    if grid[x][y] and grid[x + 1][y] and grid[x][y + 1] and grid[x + 1][y + 1]:
                        print(move)
                        return
    
    print(0)

if __name__ == "__main__":
    main()
