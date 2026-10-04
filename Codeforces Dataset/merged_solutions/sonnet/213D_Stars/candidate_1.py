# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import math
from collections import defaultdict

def solve():
    n = int(input())
    
    side = 10.0
    R = side / (2 * math.sin(math.pi / 5))
    
    all_vertices = []
    pentagon_vertex_indices = []
    
    for pent_idx in range(n):
        vertices_for_this_pentagon = []
        
        if pent_idx == 0:
            # First pentagon centered at origin
            center_x, center_y = 0, 0
            for i in range(5):
                angle = 2 * math.pi * i / 5
                x = center_x + R * math.cos(angle)
                y = center_y + R * math.sin(angle)
                all_vertices.append((x, y))
                vertices_for_this_pentagon.append(len(all_vertices))
        else:
            # Share last vertex of previous pentagon
            shared_vertex_idx = pentagon_vertex_indices[-1][-1]
            vertices_for_this_pentagon.append(shared_vertex_idx)
            
            # Position new pentagon using shared vertex
            shared_x, shared_y = all_vertices[shared_vertex_idx - 1]
            
            # Center positioned so first vertex is at shared location
            center_x = shared_x - R
            center_y = shared_y
            
            for i in range(1, 5):
                angle = 2 * math.pi * i / 5
                x = center_x + R * math.cos(angle)
                y = center_y + R * math.sin(angle)
                all_vertices.append((x, y))
                vertices_for_this_pentagon.append(len(all_vertices))
        
        pentagon_vertex_indices.append(vertices_for_this_pentagon)
    
    # Build K5 graph for each pentagon
    graph = defaultdict(list)
    
    for pentagon_indices in pentagon_vertex_indices:
        for i in range(5):
            for j in range(i + 1, 5):
                u = pentagon_indices[i]
                v = pentagon_indices[j]
                graph[u].append(v)
                graph[v].append(u)
    
    # Find Eulerian circuit using Hierholzer's algorithm
    start = 1
    stack = [start]
    path = []
    
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    
    path.reverse()
    
    # Output
    print(len(all_vertices))
    for x, y in all_vertices:
        print(f"{x:.15f} {y:.15f}")
    print(' '.join(map(str, path)))

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
