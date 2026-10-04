# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    if fib[-1] != n:
        print("NO")
        return
    
    graph = [[] for _ in range(n + 1)]
    idx = 1
    for edge_id in range(n - 1):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        graph[a].append((b, edge_id))
        graph[b].append((a, edge_id))
    
    removed = [False] * max(1, n - 1)
    parent = [0] * (n + 1)
    parent_edge = [-1] * (n + 1)
    subtree = [0] * (n + 1)
    
    def find_split(root, k):
        target_a = fib[k - 1]
        target_b = fib[k - 2]
        
        order = []
        stack = [root]
        parent[root] = 0
        parent_edge[root] = -1
        
        while stack:
            v = stack.pop()
            order.append(v)
            
            for to, edge_id in graph[v]:
                if removed[edge_id] or to == parent[v]:
                    continue
                parent[to] = v
                parent_edge[to] = edge_id
                stack.append(to)
        
        for v in reversed(order):
            total = 1
            for to, edge_id in graph[v]:
                if not removed[edge_id] and parent[to] == v:
                    total += subtree[to]
            
            subtree[v] = total
            
            if v != root and (total == target_a or total == target_b):
                return v
        
        return -1
    
    sys.setrecursionlimit(300000)
    
    def check(root, k):
        if k <= 1:
            return True
        
        cut_node = find_split(root, k)
        if cut_node == -1:
            return False
        
        cut_size = subtree[cut_node]
        edge_id = parent_edge[cut_node]
        removed[edge_id] = True
        
        if cut_size == fib[k - 1]:
            return check(cut_node, k - 1) and check(root, k - 2)
        else:
            return check(cut_node, k - 2) and check(root, k - 1)
    
    print("YES" if check(1, len(fib) - 1) else "NO")

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
