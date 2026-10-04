import sys

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    
    if n == 1:
        print("1")
        return
    
    # Build tree
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    # Compute all pairwise distances
    dist = [[0] * (n + 1) for _ in range(n + 1)]
    max_dist = 0
    for start in range(1, n + 1):
        queue = [start]
        visited = [False] * (n + 1)
        visited[start] = True
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[start][v] = dist[start][u] + 1
                    max_dist = max(max_dist, dist[start][v])
                    queue.append(v)
    
    # For each k, count connected components in G_k
    result = []
    for k in range(1, n + 1):
        if k > max_dist:
            result.append(str(n))
        else:
            # Union-find
            parent = list(range(n + 1))
            
            def find(x):
                root = x
                while parent[root] != root:
                    root = parent[root]
                while parent[x] != x:
                    next_x = parent[x]
                    parent[x] = root
                    x = next_x
                return root
            
            # Add edges where distance >= k
            for u in range(1, n + 1):
                for v in range(u + 1, n + 1):
                    if dist[u][v] >= k:
                        pu, pv = find(u), find(v)
                        if pu != pv:
                            parent[pu] = pv
            
            # Count components
            comp_count = len(set(find(i) for i in range(1, n + 1)))
            result.append(str(comp_count))
    
    print(' '.join(result))

if __name__ == '__main__':
    main()
