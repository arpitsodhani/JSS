# CLAUSE: setup_environment
import sys
from bisect import bisect_left, insort

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
        
        parent = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        for v in range(2, n + 1):
            parent[v] = data[idx]
            idx += 1
            children[parent[v]].append(v)
        
        order = [0] + data[idx:idx + n]
        idx += n
        
        pos = [0] * (n + 1)
        for i in range(1, n + 1):
            pos[order[i]] = i
        
        size = [1] * (n + 1)
        stack = [1]
        traversal = []
        while stack:
            v = stack.pop()
            traversal.append(v)
            for c in children[v]:
                stack.append(c)
        
        for v in reversed(traversal):
            for c in children[v]:
                size[v] += size[c]
        
        child_pos = [[] for _ in range(n + 1)]
        for v in range(2, n + 1):
            child_pos[parent[v]].append(pos[v])
        for v in range(1, n + 1):
            child_pos[v].sort()
        
        bad = 0
        
        def node_bad(v):
            arr = child_pos[v]
            if arr and arr[0] < pos[v]:
                return 1
            
            for i in range(len(arr) - 1):
                left = order[arr[i]]
                if arr[i] + size[left] > arr[i + 1]:
                    return 1
            
            return 0
        
        bad_nodes = [0] * (n + 1)
        for v in range(1, n + 1):
            bad_nodes[v] = node_bad(v)
            bad += bad_nodes[v]
        
        def refresh(v):
            nonlocal bad
            if v <= 0:
                return
            bad -= bad_nodes[v]
            bad_nodes[v] = node_bad(v)
            bad += bad_nodes[v]
        
        for _ in range(q):
            x = data[idx]
            y = data[idx + 1]
            idx += 2
            
            if x == y:
                out.append("YES" if bad == 0 else "NO")
                continue
            
            a = order[x]
            b = order[y]
            affected = {a, b, parent[a], parent[b]}
            
            for v in affected:
                if v > 0:
                    refresh(v)
            
            if parent[a]:
                arr = child_pos[parent[a]]
                arr.pop(bisect_left(arr, x))
                insort(arr, y)
            
            if parent[b]:
                arr = child_pos[parent[b]]
                arr.pop(bisect_left(arr, y))
                insort(arr, x)
            
            order[x], order[y] = order[y], order[x]
            pos[a], pos[b] = y, x
            
            for v in affected:
                if v > 0:
                    refresh(v)
            
            out.append("YES" if bad == 0 else "NO")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
