# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import deque

def assign_colors(nodes, parent_color, k):
    m = len(nodes)
    colors = list(range(1, m + 1))
    forbidden = [parent_color[v] for v in nodes]
    
    if m < k:
        spare = m + 1
        for i in range(m):
            if colors[i] == forbidden[i]:
                colors[i] = spare
                spare = forbidden[i]
        return colors
    
    first = 0
    second = -1
    for i in range(1, m):
        if forbidden[i] != forbidden[first]:
            second = i
            break
    
    for i in range(m):
        if colors[i] == forbidden[i]:
            if forbidden[first] != forbidden[i]:
                j = first
            else:
                j = second
            colors[i], colors[j] = colors[j], colors[i]
    
    return colors

def solve_case(n, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    levels = []
    
    queue = deque([1])
    parent[1] = -1
    
    while queue:
        v = queue.popleft()
        if depth[v] == len(levels):
            levels.append([])
        levels[depth[v]].append(v)
        
        for to in graph[v]:
            if to == parent[v]:
                continue
            parent[to] = v
            depth[to] = depth[v] + 1
            queue.append(to)
    
    max_width = max(len(level) for level in levels)
    operations = max_width
    
    for d in range(1, len(levels)):
        if len(levels[d]) == max_width:
            p = parent[levels[d][0]]
            same_parent = True
            for v in levels[d]:
                if parent[v] != p:
                    same_parent = False
                    break
            if same_parent:
                operations += 1
                break
    
    color = [0] * (n + 1)
    color[1] = 1
    
    by_color = [[] for _ in range(operations + 1)]
    by_color[1].append(1)
    
    for d in range(1, len(levels)):
        parent_color = [0] * (n + 1)
        for v in levels[d]:
            parent_color[v] = color[parent[v]]
        
        assigned = assign_colors(levels[d], parent_color, operations)
        for v, c in zip(levels[d], assigned):
            color[v] = c
            by_color[c].append(v)
    
    result = [str(operations)]
    for c in range(1, operations + 1):
        group = by_color[c]
        result.append(str(len(group)) + " " + " ".join(map(str, group)))
    
    return result

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    output = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        edges = []
        for _ in range(n - 1):
            a = data[idx]
            b = data[idx + 1]
            idx += 2
            edges.append((a, b))
        
        output.extend(solve_case(n, edges))
    
    print("\n".join(output))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
