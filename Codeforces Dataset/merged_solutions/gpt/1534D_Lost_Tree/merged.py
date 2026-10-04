import sys

def ask(vertex, n):
    print("?", vertex, flush=True)
    return list(map(int, sys.stdin.readline().split()))

def main():
    n = int(sys.stdin.readline())

    # CLAUSE: initialize_root_distances
    root = 1
    root_dist = ask(root, n)
    queried = {root}

    # CLAUSE: partition_tree_by_parity
    groups = [[], []]
    for vertex, distance in enumerate(root_dist, 1):
        groups[distance & 1].append(vertex)

    # CLAUSE: select_query_partition
    root_parity = root_dist[root - 1] & 1
    even_cost = len(groups[0]) - (1 if root_parity == 0 else 0)
    odd_cost = len(groups[1]) - (1 if root_parity == 1 else 0)
    chosen = groups[0] if even_cost <= odd_cost else groups[1]

    # CLAUSE: collect_neighbor_distances
    edges = []
    for vertex in chosen:
        if vertex in queried:
            distances = root_dist
        else:
            distances = ask(vertex, n)
            queried.add(vertex)

        # CLAUSE: infer_cross_partition_edges
        for other, distance in enumerate(distances, 1):
            if distance == 1:
                edges.append((vertex, other))

    # CLAUSE: deduplicate_edge_set
    unique = set()
    for a, b in edges:
        if a > b:
            a, b = b, a
        unique.add((a, b))

    # CLAUSE: emit_final_tree
    print("!", flush=True)
    for a, b in list(unique)[:n - 1]:
        print(a, b, flush=True)

if __name__ == "__main__":
    main()
