import sys

def solve():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    T = int(data[idx])
    idx += 1
    
    for _ in range(T):
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        
        x = [int(data[idx+i]) for i in range(n)]
        idx += n
        
        a = [data[idx+i] for i in range(n)]
        idx += n
        
        best_p = None
        best_surprise = -1
        
        # Try all 2^n strategies (maximize/minimize for each student)
        for mask in range(1 << n):
            s = [(1 if (mask >> i) & 1 else -1) for i in range(n)]
            
            # Calculate weight for each question
            w = []
            for j in range(m):
                weight = sum(s[i] for i in range(n) if a[i][j] == '1')
                w.append((weight, j))
            
            # Sort by weight descending, then by index ascending
            w.sort(key=lambda x: (-x[0], x[1]))
            
            # Assign values: highest value to highest weight
            p = [0] * m
            for rank, (_, j) in enumerate(w):
                p[j] = m - rank
            
            # Calculate actual surprise value
            surprise = 0
            for i in range(n):
                r = sum(p[j] for j in range(m) if a[i][j] == '1')
                surprise += abs(x[i] - r)
            
            if surprise > best_surprise:
                best_surprise = surprise
                best_p = p[:]
        
        print(' '.join(map(str, best_p)))

solve()
