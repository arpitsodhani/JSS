import sys

def t1(weights):
    print("? 1 " + " ".join(map(str, weights)), flush=True)
    return int(sys.stdin.readline().strip())

def t2(a, b):
    print(f"? 2 {a} {b}", flush=True)
    return int(sys.stdin.readline().strip())

def main():
    text = sys.stdin.readline().strip()
    if not text:
        return
    n = int(text)
    m = n - 1

    # CLAUSE: choose_root_edge
    if m == 0:
        print("!", flush=True)
        return
    root_edge = 1
    attach_vertex = [0 for _ in range(m + 1)]
    attach_vertex[root_edge] = 2
    result_edges = [(1, 2)]

    # CLAUSE: measure_edge_depths
    depths = [0 for _ in range(m + 1)]
    top = 0
    for edge_label in range(2, m + 1):
        depths[edge_label] = t2(root_edge, edge_label)
        if depths[edge_label] > top:
            top = depths[edge_label]

    # CLAUSE: bucket_edges_by_depth
    groups = [[] for _ in range(top + 1)]
    for edge_label in range(1, m + 1):
        groups[depths[edge_label]].append(edge_label)

    # CLAUSE: encode_parent_candidates
    step = n
    forced_weight = n * n * n * (n + 3)
    candidate_pair = [root_edge, root_edge]
    pair_state = True
    fixed_leaf = 0
    child_lists = [[] for _ in range(m + 1)]

    def coded_weights(edge_label, parents):
        weights = [1] * m
        weights[edge_label - 1] = forced_weight
        if fixed_leaf:
            weights[fixed_leaf - 1] = forced_weight - step
        twin_case = pair_state and len(parents) == 2 and parents == candidate_pair
        if twin_case:
            weights[parents[0] - 1] = step
            weights[parents[1] - 1] = step
        else:
            for offset, parent in enumerate(parents):
                weights[parent - 1] = (offset + 1) * step
        return weights, twin_case

    # CLAUSE: decode_parent_from_diameter
    def decoded_parent(diameter, parents, twin_case):
        if twin_case:
            return candidate_pair[0]
        slot = (diameter - forced_weight) // step
        if slot <= 0:
            slot = 1
        if slot > len(parents):
            slot = len(parents)
        return parents[slot - 1]

    # CLAUSE: maintain_isomorphic_pair
    def commit_child(edge_label, parent, twin_case):
        nonlocal pair_state, candidate_pair
        if twin_case:
            left, right = candidate_pair
            child_lists[left].append(edge_label)
            child_lists[right].append(edge_label)
            return left
        child_lists[parent].append(edge_label)
        if pair_state:
            left, right = candidate_pair
            if parent == left or parent == right:
                other = right if parent == left else left
                if len(child_lists[parent]) == len(child_lists[other]):
                    candidate_pair = [parent, other]
                else:
                    pair_state = False
            else:
                pair_state = False
        return parent

    # CLAUSE: switch_to_leaf_anchor
    def set_leaf_anchor(parents):
        nonlocal fixed_leaf
        if fixed_leaf:
            return
        for parent in parents:
            if len(child_lists[parent]) == 0:
                t2(root_edge, parent)
                fixed_leaf = parent
                return
        fixed_leaf = parents[0] if parents else root_edge

    # CLAUSE: reconstruct_answer_tree
    for depth_value, current_group in enumerate(groups):
        if depth_value == 0:
            continue
        parent_group = groups[depth_value - 1]
        for edge_label in current_group:
            if not pair_state and not fixed_leaf:
                set_leaf_anchor(parent_group)
            weights, twin_case = coded_weights(edge_label, parent_group)
            diameter = t1(weights)
            parent = decoded_parent(diameter, parent_group, twin_case)
            parent = commit_child(edge_label, parent, twin_case)
            attach_vertex[edge_label] = len(result_edges) + 2
            result_edges.append((attach_vertex[parent], attach_vertex[edge_label]))

    print("!", flush=True)
    for u, v in result_edges:
        print(u, v, flush=True)

if __name__ == "__main__":
    main()
