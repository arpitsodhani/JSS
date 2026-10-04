import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    grid = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
    
    # Precompute whether there's an actor in each direction
    left = [[False] * m for _ in range(n)]
    right = [[False] * m for _ in range(n)]
    up = [[False] * m for _ in range(n)]
    down = [[False] * m for _ in range(n)]
    
    # Compute left: is there any actor to the left?
    for i in range(n):
        for j in range(1, m):
            left[i][j] = left[i][j-1] or (grid[i][j-1] == 1)
    
    # Compute right: is there any actor to the right?
    for i in range(n):
        for j in range(m-2, -1, -1):
            right[i][j] = right[i][j+1] or (grid[i][j+1] == 1)
    
    # Compute up: is there any actor above?
    for j in range(m):
        for i in range(1, n):
            up[i][j] = up[i-1][j] or (grid[i-1][j] == 1)
    
    # Compute down: is there any actor below?
    for j in range(m):
        for i in range(n-2, -1, -1):
            down[i][j] = down[i+1][j] or (grid[i+1][j] == 1)
    
    # Count good positions
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                count += left[i][j] + right[i][j] + up[i][j] + down[i][j]
    
    print(count)

main()
