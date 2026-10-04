import sys
sys.setrecursionlimit(300000)

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2
        
        directed = []
        undirected = []
        dir_adj = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            edge_type = int(input_data[idx])
            u = int(input_data[idx + 1])
            v = int(input_data[idx + 2])
            idx += 3
            
            if edge_type == 1:
                directed.append((u, v))
                dir_adj[u].append(v)
            else:
                undirected.append((u, v))
        
        # DFS to check for cycles and compute topological order
        color = [0] * (n + 1)
        has_cycle = [False]
        topo_order = []
        
        def dfs(u):
            if has_cycle[0]:
                return
            color[u] = 1
            for v in dir_adj[u]:
                if color[v] == 1:
                    has_cycle[0] = True
                    return
                if color[v] == 0:
                    dfs(v)
            color[u] = 2
            topo_order.append(u)
        
        for i in range(1, n + 1):
            if color[i] == 0:
                dfs(i)
        
        if has_cycle[0]:
            print("NO")
        else:
            topo_order.reverse()
            pos = {}
            for i, v in enumerate(topo_order):
                pos[v] = i
            
            print("YES")
            for u, v in directed:
                print(u, v)
            for u, v in undirected:
                if pos[u] < pos[v]:
                    print(u, v)
                else:
                    print(v, u)

if __name__ == "__main__":
    main()
