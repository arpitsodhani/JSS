import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        
        edges = []
        max_edge = [0] * (n + 1)
        
        for _ in range(m):
            u, v, w = data[idx], data[idx + 1], data[idx + 2]
            idx += 3
            edges.append((u, v, w))
            max_edge[u] = max(max_edge[u], w)
            max_edge[v] = max(max_edge[v], w)
        
        # Check if solution is valid
        valid = True
        for u, v, w in edges:
            if max_edge[u] != w and max_edge[v] != w:
                valid = False
                break
        
        if valid:
            print("YES")
            print(' '.join(map(str, max_edge[1:])))
        else:
            print("NO")

if __name__ == "__main__":
    main()
