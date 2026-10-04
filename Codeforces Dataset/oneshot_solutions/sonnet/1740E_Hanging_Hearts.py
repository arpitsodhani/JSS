import sys
sys.setrecursionlimit(300000)

def solve():
    n = int(input())
    if n == 1:
        print(1)
        return
    
    parents = list(map(int, input().split()))
    
    # Build adjacency list
    children = [[] for _ in range(n + 1)]
    for i in range(len(parents)):
        child = i + 2  # nodes are 1-indexed, parents list is for nodes 2..n
        parent = parents[i]
        children[parent].append(child)
    
    # Compute subtree sizes
    def subtree_size(v):
        size = 1
        for c in children[v]:
            size += subtree_size(c)
        return size
    
    # Get maximum subtree size among children of root (node 1)
    root = 1
    max_child_subtree_size = 0
    for c in children[root]:
        max_child_subtree_size = max(max_child_subtree_size, subtree_size(c))
    
    # Answer is 1 + max subtree size of children
    if children[root]:
        print(1 + max_child_subtree_size)
    else:
        print(1)

solve()
