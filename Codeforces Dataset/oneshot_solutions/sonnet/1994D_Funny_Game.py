import sys

def solve_case(n, a):
    parent = list(range(n))
    size = [1] * n
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        size[rx] += size[ry]
        return True
    
    edges = []
    
    for mod in range(n - 1, 0, -1):
        seen = {}
        found = False
        
        for i in range(n):
            r = a[i] % mod
            if r in seen:
                j = seen[r]
                if find(i) != find(j):
                    union(i, j)
                    edges.append((i + 1, j + 1))
                    found = True
                    break
            else:
                seen[r] = i
        
        if not found:
            return None
    
    edges.reverse()
    return edges

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        edges = solve_case(n, a)
        if edges is None:
            out.append("NO")
        else:
            out.append("YES")
            for u, v in edges:
                out.append(f"{u} {v}")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
