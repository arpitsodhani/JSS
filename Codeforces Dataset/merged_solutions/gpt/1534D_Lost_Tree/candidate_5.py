import sys

def query_vertex(v, n):
    sys.stdout.write("? " + str(v) + "\n")
    sys.stdout.flush()
    row = []
    while len(row) != n:
        row.extend(int(part) for part in sys.stdin.readline().split())
    return row

def main():
    n_text = sys.stdin.readline().strip()
    if not n_text:
        return
    n = int(n_text)

    # CLAUSE: initialize_root_distances
    root_vertex = 1
    root_row = query_vertex(root_vertex, n)
    known_rows = {root_vertex: root_row}

    # CLAUSE: partition_tree_by_parity
    parity_lists = [[], []]
    for node, dist in zip(range(1, n + 1), root_row):
        parity_lists[dist % 2].append(node)

    # CLAUSE: select_query_partition
    chosen_parity = 0
    if len(parity_lists[1]) < len(parity_lists[0]):
        chosen_parity = 1
    nodes_to_query = parity_lists[chosen_parity]

    # CLAUSE: collect_neighbor_distances
    raw_edges = []
    for node in nodes_to_query:
        distances = known_rows[node] if node in known_rows else query_vertex(node, n)

        # CLAUSE: infer_cross_partition_edges
        position = 0
        while position < n:
            if distances[position] == 1:
                raw_edges.append((node, position + 1))
            position += 1

    # CLAUSE: deduplicate_edge_set
    final_edges = set()
    for u, v in raw_edges:
        if u < v:
            final_edges.add((u, v))
        else:
            final_edges.add((v, u))

    # CLAUSE: emit_final_tree
    sys.stdout.write("!\n")
    for u, v in final_edges:
        sys.stdout.write(str(u) + " " + str(v) + "\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
