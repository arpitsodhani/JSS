from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    # Build adjacency list with edge types
    graph = defaultdict(list)
    
    for _ in range(m):
        parts = input().split()
        i, j = int(parts[0]), int(parts[1])
        c = parts[2]
        
        # opposite = 1 (imposter claim), same = 0 (crewmate claim)
        edge_type = 1 if c == "imposter" else 0
        graph[i].append((j, edge_type))
        graph[j].append((i, edge_type))
    
    # Color each connected component
    color = [-1] * (n + 1)
    total_imposters = 0
    
    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        
        # Check if this is an isolated node
        if not graph[start]:
            # Isolated node - can be imposter
            total_imposters += 1
            continue
        
        # BFS to color this component
        queue = deque([start])
        color[start] = 0
        component = [start]
        valid = True
        
        while queue and valid:
            u = queue.popleft()
            for v, edge_type in graph[u]:
                expected_color = (color[u] + edge_type) % 2
                
                if color[v] == -1:
                    color[v] = expected_color
                    component.append(v)
                    queue.append(v)
                elif color[v] != expected_color:
                    valid = False
                    break
        
        if not valid:
            print(-1)
            return
        
        # Count imposters for both assignments
        count0 = sum(1 for node in component if color[node] == 0)
        count1 = len(component) - count0
        
        # We want to maximize imposters
        total_imposters += max(count0, count1)
    
    print(total_imposters)

t = int(input())
for _ in range(t):
    solve()
