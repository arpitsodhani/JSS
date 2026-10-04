import sys

def ask_distance_array(node_count, node):
    print("?", node, flush=True)
    data = list(map(int, sys.stdin.readline().split()))
    while len(data) < node_count:
        data.extend(map(int, sys.stdin.readline().split()))
    return data

def main():
    n = int(sys.stdin.readline())

    # CLAUSE: initialize_root_distances
    root = 1
    depth = ask_distance_array(n, root)

    # CLAUSE: partition_tree_by_parity
    partitions = [[], []]
    for node in range(1, n + 1):
        partitions[depth[node - 1] & 1].append(node)

    # CLAUSE: select_query_partition
    selected = min(partitions, key=len)

    # CLAUSE: collect_neighbor_distances
    edge_candidates = []
    for node in selected:
        if node == root:
            dist = depth
        else:
            dist = ask_distance_array(n, node)

        # CLAUSE: infer_cross_partition_edges
        neighbors = [idx + 1 for idx, value in enumerate(dist) if value == 1]
        for neighbor in neighbors:
            edge_candidates.append((node, neighbor))

    # CLAUSE: deduplicate_edge_set
    answer = []
    seen = set()
    for left, right in edge_candidates:
        edge = tuple(sorted((left, right)))
        if edge not in seen:
            seen.add(edge)
            answer.append(edge)

    # CLAUSE: emit_final_tree
    print("!", flush=True)
    for left, right in answer[:n - 1]:
        print(left, right, flush=True)

if __name__ == "__main__":
    main()
