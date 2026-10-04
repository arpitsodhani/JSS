import sys

def ask_type1(weights):
    print("? 1", *weights, flush=True)
    return int(sys.stdin.readline())

def ask_type2(a, b):
    print("? 2", a, b, flush=True)
    return int(sys.stdin.readline())

def answer(edges):
    print("!", flush=True)
    for u, v in edges:
        print(u, v, flush=True)

def main():
    line = sys.stdin.readline().strip()
    if not line:
        return
    n = int(line)
    if n == 1:
        answer([])
        return

    m = n - 1
    root = 1

    # CLAUSE: choose_root_edge
    edge_vertex = [0] * (m + 1)
    edge_parent = [0] * (m + 1)
    edge_vertex[root] = 2
    out_edges = [(1, 2)]

    # CLAUSE: measure_edge_depths
    depth = [0] * (m + 1)
    max_depth = 0
    for e in range(2, m + 1):
        depth[e] = ask_type2(root, e)
        if depth[e] > max_depth:
            max_depth = depth[e]

    # CLAUSE: bucket_edges_by_depth
    layers = [[] for _ in range(max_depth + 1)]
    layers[0].append(root)
    for e in range(2, m + 1):
        layers[depth[e]].append(e)

    # CLAUSE: encode_parent_candidates
    big = n * n * n + n * n + 7
    pair = [root, root]
    pair_live = True
    leaf_anchor = 0
    children = [[] for _ in range(m + 1)]

    def make_weights(cur, candidates):
        w = [1] * m
        w[cur - 1] = big
        if leaf_anchor:
            w[leaf_anchor - 1] = big - n
        used_pair = pair_live and len(candidates) == 2 and candidates[0] == pair[0] and candidates[1] == pair[1]
        for i, e in enumerate(candidates, 1):
            if used_pair:
                w[e - 1] = n
            else:
                w[e - 1] = i * n
        return w, used_pair

    # CLAUSE: decode_parent_from_diameter
    def decode(got, candidates, duplicate):
        if duplicate:
            return -1
        k = (got - big) // n
        if k < 1:
            k = 1
        if k > len(candidates):
            k = len(candidates)
        return candidates[k - 1]

    # CLAUSE: maintain_isomorphic_pair
    def keep_pair(child, decoded, ambiguous, candidates):
        nonlocal pair_live, pair
        if ambiguous:
            children[pair[0]].append(child)
            children[pair[1]].append(child)
            return pair[0]
        children[decoded].append(child)
        if pair_live and decoded in pair:
            other = pair[0] ^ pair[1] ^ decoded
            if len(children[decoded]) == len(children[other]):
                pair = [decoded, other]
            else:
                pair_live = False
        elif pair_live and len(candidates) != 2:
            pair_live = False
        return decoded

    # CLAUSE: switch_to_leaf_anchor
    def ensure_anchor(prev_layer):
        nonlocal leaf_anchor
        if leaf_anchor:
            return
        for e in prev_layer:
            if not children[e] and ask_type2(root, e) == depth[e]:
                leaf_anchor = e
                return
        leaf_anchor = prev_layer[0] if prev_layer else root

    # CLAUSE: reconstruct_answer_tree
    for d in range(1, max_depth + 1):
        candidates = layers[d - 1]
        for e in layers[d]:
            if not pair_live and not leaf_anchor:
                ensure_anchor(candidates)
            weights, dup = make_weights(e, candidates)
            res = ask_type1(weights)
            parent = decode(res, candidates, dup)
            if parent == -1:
                parent = pair[0]
            parent = keep_pair(e, parent, dup, candidates)
            edge_parent[e] = parent
            edge_vertex[e] = len(out_edges) + 2
            out_edges.append((edge_vertex[parent], edge_vertex[e]))

    answer(out_edges)

if __name__ == "__main__":
    main()
