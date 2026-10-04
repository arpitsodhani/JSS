# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from array import array

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    T = data[idx + 2]
    idx += 3
    
    edges = []
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        w = data[idx + 2]
        idx += 3
        edges.append((u, v, w))
    
    inf = 10 ** 30
    prev = [inf] * (n + 1)
    prev[1] = 0
    
    parent = [array('H', [0]) * (n + 1) for _ in range(n + 1)]
    
    best_len = 1 if n == 1 else 0
    
    for length in range(1, n):
        cur = [inf] * (n + 1)
        
        for u, v, w in edges:
            if prev[u] + w < cur[v]:
                cur[v] = prev[u] + w
                parent[length + 1][v] = u
        
        if cur[n] <= T:
            best_len = length + 1
        
        prev = cur
    
    path = [0] * best_len
    v = n
    for length in range(best_len, 0, -1):
        path[length - 1] = v
        v = parent[length][v]
    
    print(best_len)
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
