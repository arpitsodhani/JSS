import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        graph = [[] for _ in range(n)]
        for _ in range(m):
            v = data[idx] - 1
            u = data[idx + 1] - 1
            idx += 2
            graph[v].append(u)
            graph[u].append(v)
        
        color = [-1] * n
        result = 0
        
        for start in range(n):
            if color[start] != -1:
                continue
            
            queue = deque([start])
            color[start] = 0
            count = [1, 0]
            good = True
            
            while queue:
                v = queue.popleft()
                for u in graph[v]:
                    if color[u] == -1:
                        color[u] = color[v] ^ 1
                        count[color[u]] += 1
                        queue.append(u)
                    elif color[u] == color[v]:
                        good = False
            
            if good:
                result += max(count)
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
