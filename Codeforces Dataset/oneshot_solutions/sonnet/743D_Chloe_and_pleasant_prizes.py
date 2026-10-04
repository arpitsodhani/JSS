import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

def solve():
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    
    if n == 1:
        print("Impossible")
        return
    
    a = [0] + list(map(int, lines[1].split()))
    
    adj = defaultdict(list)
    for i in range(2, n + 1):
        u, v = map(int, lines[i].split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Build rooted tree
    children = defaultdict(list)
    
    def build_tree(node, parent):
        for neighbor in adj[node]:
            if neighbor != parent:
                children[node].append(neighbor)
                build_tree(neighbor, node)
    
    build_tree(1, -1)
    
    # DFS to compute answer
    subtree_sum = [0] * (n + 1)
    max_subtree = [float('-inf')] * (n + 1)
    max_pair = [float('-inf')] * (n + 1)
    
    def dfs(node):
        subtree_sum[node] = a[node]
        max_subtree[node] = a[node]
        
        child_maxes = []
        
        for child in children[node]:
            dfs(child)
            subtree_sum[node] += subtree_sum[child]
            max_subtree[node] = max(max_subtree[node], max_subtree[child])
            max_pair[node] = max(max_pair[node], max_pair[child])
            child_maxes.append(max_subtree[child])
        
        # Consider taking entire subtree rooted at node
        max_subtree[node] = max(max_subtree[node], subtree_sum[node])
        
        # Consider taking two subtrees from different children
        if len(child_maxes) >= 2:
            child_maxes.sort(reverse=True)
            max_pair[node] = max(max_pair[node], child_maxes[0] + child_maxes[1])
    
    dfs(1)
    
    if max_pair[1] == float('-inf'):
        print("Impossible")
    else:
        print(max_pair[1])

solve()
