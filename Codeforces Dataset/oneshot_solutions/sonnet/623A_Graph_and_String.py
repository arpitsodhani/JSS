import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    edge = [[False] * n for _ in range(n)]
    for i in range(n):
        edge[i][i] = True
    
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2
        edge[u][v] = True
        edge[v][u] = True
    
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        
        color[start] = 0
        q = deque([start])
        
        while q:
            v = q.popleft()
            for u in range(n):
                if u == v:
                    continue
                
                if not edge[v][u]:
                    if color[u] == -1:
                        color[u] = color[v] ^ 1
                        q.append(u)
                    elif color[u] == color[v]:
                        print("No")
                        return
    
    ans = ['b'] * n
    for i in range(n):
        has_missing = False
        for j in range(n):
            if i != j and not edge[i][j]:
                has_missing = True
                break
        
        if has_missing:
            ans[i] = 'a' if color[i] == 0 else 'c'
    
    for i in range(n):
        for j in range(i + 1, n):
            expected = not (ans[i] == 'a' and ans[j] == 'c') and not (ans[i] == 'c' and ans[j] == 'a')
            if edge[i][j] != expected:
                print("No")
                return
    
    print("Yes")
    print(''.join(ans))

if __name__ == "__main__":
    main()
