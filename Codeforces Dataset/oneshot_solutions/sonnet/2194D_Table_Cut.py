import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        table = []
        total = 0
        
        for _ in range(n):
            token = data[idx]
            if len(token) == m and m > 1:
                row = [c - 48 for c in token]
                idx += 1
            else:
                row = [int(data[idx + j]) for j in range(m)]
                idx += m
            
            total += sum(row)
            table.append(row)
        
        need = total // 2
        
        if need == 0:
            cuts = [0] * n
        else:
            seen = 0
            cuts = None
            
            for col in range(m):
                if cuts is not None:
                    break
                
                for row in range(n - 1, -1, -1):
                    if table[row][col] == 1:
                        seen += 1
                    
                    if seen == need:
                        cuts = [col] * row + [col + 1] * (n - row)
                        break
        
        path = []
        current_col = 0
        for row in range(n):
            while current_col < cuts[row]:
                path.append('R')
                current_col += 1
            path.append('D')
        
        while current_col < m:
            path.append('R')
            current_col += 1
        
        out.append(str(need * (total - need)))
        out.append(''.join(path))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
