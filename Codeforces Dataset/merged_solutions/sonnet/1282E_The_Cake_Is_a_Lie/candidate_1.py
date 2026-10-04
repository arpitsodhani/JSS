# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
from collections import defaultdict

def solve():
    n = int(input())
    triangles = []
    for _ in range(n - 2):
        triangle = list(map(int, input().split()))
        triangles.append(triangle)
    
    if n == 3:
        # Special case: single triangle
        print(' '.join(map(str, triangles[0])))
        return
    
    # Count how many triangles contain each edge
    edge_count = defaultdict(int)
    for triangle in triangles:
        a, b, c = triangle
        edges = [(min(a,b), max(a,b)), (min(b,c), max(b,c)), (min(a,c), max(a,c))]
        for edge in edges:
            edge_count[edge] += 1
    
    # Find boundary edges (appear exactly once)
    boundary_edges = []
    for edge, count in edge_count.items():
        if count == 1:
            boundary_edges.append(edge)
    
    # Build adjacency list for boundary vertices
    adj = defaultdict(list)
    for u, v in boundary_edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Trace the boundary cycle starting from any boundary vertex
    start = boundary_edges[0][0]
    path = [start]
    prev = -1
    current = start
    
    while True:
        for next_vertex in adj[current]:
            if next_vertex != prev:
                prev = current
                current = next_vertex
                path.append(current)
                break
        if current == start:
            break
    
    # Remove the duplicate (last element equals first)
    path.pop()
    print(' '.join(map(str, path)))

t = int(input())
for _ in range(t):
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
