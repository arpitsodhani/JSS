import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n, q = int(data[idx]), int(data[idx + 1])
        idx += 2
        
        # Read parents (for vertices 2 to n)
        parents = [0, 0]  # parents[0] is unused, parents[1] = 0 (root has no parent)
        for i in range(n - 1):
            parents.append(int(data[idx]))
            idx += 1
        
        # Read ornaments (for vertices 1 to n)
        ornaments = [0]  # ornaments[0] is unused
        for i in range(n):
            ornaments.append(int(data[idx]))
            idx += 1
        
        # Build adjacency list for children
        children = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            children[parents[i]].append(i)
        
        # Precompute ops values
        ops = [0] * (n + 1)
        
        def compute_ops(v):
            if not children[v]:  # Leaf
                ops[v] = ornaments[v]
            else:
                child_sum = sum(compute_ops(c) for c in children[v])
                ops[v] = max(ornaments[v], child_sum)
            return ops[v]
        
        # Initial computation
        compute_ops(1)
        print(ops[1])
        
        # Process queries
        for _ in range(q):
            u, x = int(data[idx]), int(data[idx + 1])
            idx += 2
            ornaments[u] = x
            
            # Recompute ops for u and all its ancestors
            v = u
            while v != 0:
                if not children[v]:  # Leaf
                    ops[v] = ornaments[v]
                else:
                    child_sum = sum(ops[c] for c in children[v])
                    ops[v] = max(ornaments[v], child_sum)
                v = parents[v]
            
            print(ops[1])

if __name__ == "__main__":
    main()
