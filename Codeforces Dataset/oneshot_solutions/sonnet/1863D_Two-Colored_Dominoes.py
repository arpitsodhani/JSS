import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        grid = []
        for _ in range(n):
            grid.append(list(data[idx]))
            idx += 1
        
        ans = [['.' for _ in range(m)] for _ in range(n)]
        possible = True
        
        for i in range(n):
            starts = []
            for j in range(m):
                if grid[i][j] == 'U':
                    starts.append(j)
            
            if len(starts) % 2:
                possible = False
                break
            
            for k, j in enumerate(starts):
                if k % 2 == 0:
                    ans[i][j] = 'W'
                    ans[i + 1][j] = 'B'
                else:
                    ans[i][j] = 'B'
                    ans[i + 1][j] = 'W'
        
        if possible:
            for j in range(m):
                starts = []
                for i in range(n):
                    if grid[i][j] == 'L':
                        starts.append(i)
                
                if len(starts) % 2:
                    possible = False
                    break
                
                for k, i in enumerate(starts):
                    if k % 2 == 0:
                        ans[i][j] = 'W'
                        ans[i][j + 1] = 'B'
                    else:
                        ans[i][j] = 'B'
                        ans[i][j + 1] = 'W'
        
        if not possible:
            out.append("-1")
        else:
            out.extend(''.join(row) for row in ans)
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
