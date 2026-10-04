import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input().strip())
    
    # Extract the four critical cells (0-indexed)
    a = grid[0][1]
    b = grid[1][0]
    c = grid[n-2][n-1]
    d = grid[n-1][n-2]
    
    changes = []
    
    if a == b and c == d:
        if a == c:
            # Only one path type exists, block it
            changes.append((1, 2))
            changes.append((2, 1))
    elif a == b:
        # Only a-paths can exist, block at finish
        if c == a:
            changes.append((n-1, n))
        else:
            changes.append((n, n-1))
    elif c == d:
        # Only c-paths can exist, block at start
        if a == c:
            changes.append((1, 2))
        else:
            changes.append((2, 1))
    else:
        # Both path types exist, make start all 0 and finish all 1
        if a == '1':
            changes.append((1, 2))
        else:
            changes.append((2, 1))
        
        if c == '0':
            changes.append((n-1, n))
        else:
            changes.append((n, n-1))
    
    print(len(changes))
    for r, col in changes:
        print(r, col)

t = int(input())
for _ in range(t):
    solve()
