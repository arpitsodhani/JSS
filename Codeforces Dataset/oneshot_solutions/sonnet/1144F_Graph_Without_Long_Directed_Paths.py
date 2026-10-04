import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().decode().strip().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    edges = []
    graph = [[] for _ in range(n + 1)]
    
    for i in range(m):
        u = int(input_data[idx])
        idx += 1
        v = int(input_data[idx])
        idx += 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
    
    # BFS to check bipartiteness and assign colors
    color = [-1] * (n + 1)
    color[1] = 0
    queue = deque([1])
    is_bipartite = True
    
    while queue and is_bipartite:
        u = queue.popleft()
        for v in graph[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                is_bipartite = False
                break
    
    if not is_bipartite:
        print("NO")
    else:
        print("YES")
        result = []
        for u, v in edges:
            if color[u] == 0:
                result.append('1')
            else:
                result.append('0')
        print(''.join(result))

if __name__ == "__main__":
    main()
