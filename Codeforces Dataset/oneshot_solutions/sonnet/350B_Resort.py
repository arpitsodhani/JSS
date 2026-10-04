import sys
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().strip().split('\n')
    n = int(input_data[0])
    types = list(map(int, input_data[1].split()))
    parents = list(map(int, input_data[2].split()))
    
    # Build adjacency list (children of each node)
    children = [[] for _ in range(n + 1)]
    for i in range(n):
        node = i + 1
        parent = parents[i]
        if parent != 0:
            children[parent].append(node)
    
    # DP to find longest path length from each node
    dp = [-1] * (n + 1)
    visiting = [False] * (n + 1)
    
    def compute_length(v):
        if dp[v] != -1:
            return dp[v]
        
        if visiting[v]:
            # Cycle detected
            dp[v] = 0
            return 0
        
        visiting[v] = True
        
        is_hotel = types[v - 1] == 1
        
        if is_hotel:
            dp[v] = 1
        elif len(children[v]) == 1:
            child = children[v][0]
            child_length = compute_length(child)
            if child_length > 0:
                dp[v] = 1 + child_length
            else:
                dp[v] = 0
        else:
            dp[v] = 0
        
        visiting[v] = False
        return dp[v]
    
    # Compute paths for all nodes
    best_length = 0
    best_start = 0
    for v in range(1, n + 1):
        length = compute_length(v)
        if length > best_length:
            best_length = length
            best_start = v
    
    # Reconstruct the path
    path = []
    current = best_start
    while current != 0:
        path.append(current)
        if len(children[current]) == 1:
            current = children[current][0]
        else:
            break
    
    # Output
    print(best_length)
    print(' '.join(map(str, path)))

solve()
