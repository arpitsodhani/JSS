# Clause setup_environment [Confidence: 0.60]
import sys

def ask(a, b):
    print(f"? 2 {a} {b}")
    sys.stdout.flush()
    return int(sys.stdin.readline())


# Clause solve_logic [Confidence: 0.60]
def solve():
    n = int(input())
    if n == 1:
        print("!")
        sys.stdout.flush()
        return

    m = n - 1
    if m == 1:
        print("!")
        print("1 2")
        sys.stdout.flush()
        return

    edge_to_vertices = {}
    vertex_to_edges = {}
    next_vertex_id = 1

    def add_vertex():
        nonlocal next_vertex_id
        v = next_vertex_id
        next_vertex_id += 1
        vertex_to_edges[v] = []
        return v

    u = add_vertex()
    v = add_vertex()
    edge_to_vertices[0] = (u, v)
    vertex_to_edges[u].append(0)
    vertex_to_edges[v].append(0)

    for next_edge in range(1, m):
        adjacent_edge = None
        for placed_edge in range(next_edge):
            d = query_type2(next_edge + 1, placed_edge + 1)
            if d == 0:
                adjacent_edge = placed_edge
                break

        u, v = edge_to_vertices[adjacent_edge]
        shared = u

        other_edge_u = None
        for e in vertex_to_edges[u]:
            if e != adjacent_edge:
                other_edge_u = e
                break

        if other_edge_u is not None:
            d2 = query_type2(next_edge + 1, other_edge_u + 1)
            shared = u if d2 == 0 else v
        else:
            other_edge_v = None
            for e in vertex_to_edges[v]:
                if e != adjacent_edge:
                    other_edge_v = e
                    break

            if other_edge_v is not None:
                d2 = query_type2(next_edge + 1, other_edge_v + 1)
                shared = v if d2 == 0 else u

        new_vertex = add_vertex()
        edge_to_vertices[next_edge] = (shared, new_vertex)
        vertex_to_edges[shared].append(next_edge)
        vertex_to_edges[new_vertex].append(next_edge)

    print("!")
    for i in range(m):
        u, v = edge_to_vertices[i]
        print(f"{u} {v}")
    sys.stdout.flush()


# Clause finish_program [Confidence: 0.80]
solve()


