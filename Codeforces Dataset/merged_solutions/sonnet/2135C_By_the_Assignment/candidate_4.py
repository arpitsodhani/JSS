# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def inner():
    import sys

    MOD = 998244353

    def solve_case(n, m, V, weights, edges):
        graph = [[] for _ in range(n)]
        for eid, (u, v) in enumerate(edges):
            u -= 1
            v -= 1
            graph[u].append((v, eid))
            graph[v].append((u, eid))
    
        parent = list(range(n))
        forced_zero = [False] * n
    
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
    
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return
            parent[rb] = ra
            forced_zero[ra] |= forced_zero[rb]
    
        tin = [0] * n
        low = [0] * n
        timer = 0
        stack = []
    
        sys.setrecursionlimit(500000)
    
        def process_component(component):
            vertices = []
            for eid in component:
                u, v = edges[eid]
                u -= 1
                v -= 1
                vertices.append(u)
                vertices.append(v)
        
            vertices = list(set(vertices))
            if len(component) < len(vertices):
                return
        
            first = vertices[0]
            for v in vertices[1:]:
                union(first, v)
        
            color = {}
            odd_cycle = False
        
            for start in vertices:
                if start in color:
                    continue
            
                color[start] = 0
                dfs_stack = [start]
                while dfs_stack:
                    v = dfs_stack.pop()
                    for to, eid in graph[v]:
                        if eid not in component_set:
                            continue
                        if to not in color:
                            color[to] = color[v] ^ 1
                            dfs_stack.append(to)
                        elif color[to] == color[v]:
                            odd_cycle = True
        
            if odd_cycle:
                forced_zero[find(first)] = True
    
        def dfs(v, parent_edge):
            nonlocal timer, component_set
            timer += 1
            tin[v] = low[v] = timer
        
            for to, eid in graph[v]:
                if eid == parent_edge:
                    continue
            
                if tin[to]:
                    if tin[to] < tin[v]:
                        stack.append(eid)
                    low[v] = min(low[v], tin[to])
                else:
                    stack.append(eid)
                    dfs(to, eid)
                    low[v] = min(low[v], low[to])
                
                    if low[to] >= tin[v]:
                        component = []
                        while True:
                            last = stack.pop()
                            component.append(last)
                            if last == eid:
                                break
                    
                        component_set = set(component)
                        process_component(component)
    
        component_set = set()
        dfs(0, -1)
    
        fixed = {}
        for i, value in enumerate(weights):
            root = find(i)
            if forced_zero[root] and value not in (-1, 0):
                return 0
        
            if value != -1:
                if root in fixed and fixed[root] != value:
                    return 0
                fixed[root] = value
    
        roots = set(find(i) for i in range(n))
        free = 0
    
        for root in roots:
            if forced_zero[root]:
                continue
            if root not in fixed:
                free += 1
    
        return pow(V % MOD, free, MOD)

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        idx = 0
        t = data[idx]
        idx += 1
    
        answers = []
        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            V = data[idx + 2]
            idx += 3
        
            weights = data[idx:idx + n]
            idx += n
        
            edges = []
            for _ in range(m):
                u = data[idx]
                v = data[idx + 1]
                idx += 2
                edges.append((u, v))
        
            answers.append(str(solve_case(n, m, V, weights, edges)))
    
        print('\n'.join(answers))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    inner()

main()
