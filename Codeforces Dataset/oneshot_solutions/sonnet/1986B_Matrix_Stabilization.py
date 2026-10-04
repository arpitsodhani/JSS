import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(m):
                # Find all neighbors
                neighbors = []
                if i > 0:
                    neighbors.append(a[i-1][j])
                if i < n-1:
                    neighbors.append(a[i+1][j])
                if j > 0:
                    neighbors.append(a[i][j-1])
                if j < m-1:
                    neighbors.append(a[i][j+1])
                
                if neighbors and all(a[i][j] > nb for nb in neighbors):
                    a[i][j] = max(neighbors)
                    changed = True
    
    for row in a:
        print(' '.join(map(str, row)))

t = int(input())
for _ in range(t):
    solve()
