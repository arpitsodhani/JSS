# CLAUSE: setup_environment
import sys

def ask(a, b):
    print(f"? 2 {a} {b}")
    sys.stdout.flush()
    return int(sys.stdin.readline())

# CLAUSE: solve_logic
def solve():
    n = int(sys.stdin.readline())
    if n == 1:
        print("!")
        sys.stdout.flush()
        return

    edge_count = n - 1
    if edge_count == 1:
        print("!")
        print("1 2")
        sys.stdout.flush()
        return

    edge_vertices = {0: (1, 2)}
    vertex_edges = {1: [0], 2: [0]}
    next_vertex = 3

    for edge in range(1, edge_count):
        neighbor = 0
        for old in range(edge):
            if ask(edge + 1, old + 1) == 0:
                neighbor = old
                break

        a, b = edge_vertices[neighbor]
        shared = a

        witness = next((x for x in vertex_edges[a] if x != neighbor), None)
        if witness is not None:
            shared = a if ask(edge + 1, witness + 1) == 0 else b
        else:
            witness = next((x for x in vertex_edges[b] if x != neighbor), None)
            if witness is not None:
                shared = b if ask(edge + 1, witness + 1) == 0 else a

        new_vertex = next_vertex
        next_vertex += 1
        edge_vertices[edge] = (shared, new_vertex)
        vertex_edges[shared].append(edge)
        vertex_edges[new_vertex] = [edge]

    lines = ["!"]
    for i in range(edge_count):
        a, b = edge_vertices[i]
        lines.append(f"{a} {b}")
    print("\n".join(lines))
    sys.stdout.flush()

# CLAUSE: finish_program
solve()
