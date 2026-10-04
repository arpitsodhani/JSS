import sys

def read_distances(n):
    values = []
    while len(values) < n:
        values += [int(x) for x in sys.stdin.readline().split()]
    return values

def request(v, n):
    print("?", v)
    sys.stdout.flush()
    return read_distances(n)

def main():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)

    # CLAUSE: initialize_root_distances
    first = 1
    distances_from_first = request(first, n)

    # CLAUSE: partition_tree_by_parity
    even_vertices = []
    odd_vertices = []
    for v in range(1, n + 1):
        if distances_from_first[v - 1] % 2 == 0:
            even_vertices.append(v)
        else:
            odd_vertices.append(v)

    # CLAUSE: select_query_partition
    if len(even_vertices) <= len(odd_vertices):
        chosen_vertices = even_vertices
    else:
        chosen_vertices = odd_vertices

    # CLAUSE: collect_neighbor_distances
    result_edges = []
    cached_root_response = {first: distances_from_first}
    for v in chosen_vertices:
        answer = cached_root_response.get(v)
        if answer is None:
            answer = request(v, n)

        # CLAUSE: infer_cross_partition_edges
        result_edges.extend((v, u) for u in range(1, n + 1) if answer[u - 1] == 1)

    # CLAUSE: deduplicate_edge_set
    edge_set = set()
    for x, y in result_edges:
        edge_set.add((x, y) if x < y else (y, x))

    # CLAUSE: emit_final_tree
    print("!")
    for x, y in edge_set:
        print(x, y)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
