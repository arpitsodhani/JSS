import sys

def query(node, size):
    sys.stdout.write(f"? {node}\n")
    sys.stdout.flush()
    response = []
    while len(response) < size:
        response.extend(map(int, sys.stdin.readline().split()))
    return response

def main():
    n = int(sys.stdin.readline().strip())

    # CLAUSE: initialize_root_distances
    base_node = 1
    base_distances = query(base_node, n)

    # CLAUSE: partition_tree_by_parity
    by_parity = {0: [], 1: []}
    for index in range(n):
        by_parity[base_distances[index] % 2].append(index + 1)

    # CLAUSE: select_query_partition
    base_side = base_distances[base_node - 1] % 2
    candidate_sides = []
    for side in (0, 1):
        extra_queries = len(by_parity[side]) - int(side == base_side)
        candidate_sides.append((extra_queries, side))
    selected_side = min(candidate_sides)[1]
    selected_vertices = by_parity[selected_side]

    # CLAUSE: collect_neighbor_distances
    discovered = set()
    for source in selected_vertices:
        current = base_distances if source == base_node else query(source, n)

        # CLAUSE: infer_cross_partition_edges
        for target in range(1, n + 1):
            if current[target - 1] == 1:
                discovered.add((source, target))

    # CLAUSE: deduplicate_edge_set
    normalized = sorted((min(a, b), max(a, b)) for a, b in discovered)

    # CLAUSE: emit_final_tree
    sys.stdout.write("!\n")
    for a, b in normalized[:n - 1]:
        sys.stdout.write(f"{a} {b}\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
