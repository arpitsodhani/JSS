import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    MOD = 998244353
    
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx + 1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
        
        # Color array: -1 = unvisited, 0 or 1 = bipartite coloring
        color = [-1] * (n + 1)
        
        result = 1
        is_beautiful = True
        
        for start in range(1, n + 1):
            if color[start] != -1:
                continue
            
            # BFS to check bipartiteness and count partition sizes
            queue = deque([start])
            color[start] = 0
            count = [1, 0]
            
            component_bipartite = True
            
            while queue and component_bipartite:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        count[color[v]] += 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        component_bipartite = False
                        is_beautiful = False
                        break
            
            if not component_bipartite:
                break
            
            # This component is bipartite with partitions of sizes count[0] and count[1]
            ways = (pow(2, count[0], MOD) + pow(2, count[1], MOD)) % MOD
            result = (result * ways) % MOD
        
        if is_beautiful:
            print(result)
        else:
            print(0)

if __name__ == "__main__":
    main()
