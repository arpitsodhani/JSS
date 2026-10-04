import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))
    
    # Find positions of each value in both matrices
    pos_a = {}
    pos_b = {}
    for i in range(n):
        for j in range(m):
            pos_a[a[i][j]] = (i, j)
            pos_b[b[i][j]] = (i, j)
    
    # Build row and column mappings
    row_map = {}
    col_map = {}
    
    for val in range(1, n * m + 1):
        r_a, c_a = pos_a[val]
        r_b, c_b = pos_b[val]
        
        # Check consistency for row mapping
        if r_a in row_map:
            if row_map[r_a] != r_b:
                return "NO"
        else:
            row_map[r_a] = r_b
        
        # Check consistency for column mapping
        if c_a in col_map:
            if col_map[c_a] != c_b:
                return "NO"
        else:
            col_map[c_a] = c_b
    
    # Check if mappings are bijections (permutations)
    if len(set(row_map.values())) != n:
        return "NO"
    if len(set(col_map.values())) != m:
        return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    print(solve())
