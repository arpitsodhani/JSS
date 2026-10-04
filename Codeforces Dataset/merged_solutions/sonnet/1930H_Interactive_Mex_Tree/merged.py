# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        
        log = (n + 1).bit_length()
        parent = [[0] * (n + 1) for _ in range(log)]
        depth = [0] * (n + 1)
        
        stack = [1]
        order = [1]
        parent[0][1] = 0
        
        while stack:
            v = stack.pop()
            for to in graph[v]:
                if to == parent[0][v]:
                    continue
                parent[0][to] = v
                depth[to] = depth[v] + 1
                stack.append(to)
                order.append(to)
        
        for j in range(1, log):
            prev = parent[j - 1]
            cur = parent[j]
            for v in range(1, n + 1):
                cur[v] = prev[prev[v]]
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            bit = 0
            while diff:
                if diff & 1:
                    u = parent[bit][u]
                diff >>= 1
                bit += 1
            
            if u == v:
                return u
            
            for j in range(log - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]
            
            return parent[0][u]
        
        seen = [0] * (n + 1)
        stamp = 0
        values = [0] * (n + 1)
        
        for _ in range(q):
            for v in range(1, n + 1):
                values[v] = data[idx]
                idx += 1
            
            u = data[idx]
            v = data[idx + 1]
            idx += 2
            
            w = lca(u, v)
            stamp += 1
            
            x = u
            while x != w:
                seen[values[x]] = stamp
                x = parent[0][x]
            
            seen[values[w]] = stamp
            
            x = v
            while x != w:
                seen[values[x]] = stamp
                x = parent[0][x]
            
            mex = 0
            while mex <= n and seen[mex] == stamp:
                mex += 1
            
            out.append(str(mex))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
