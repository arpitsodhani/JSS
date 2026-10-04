import sys

def read_int():
    return int(sys.stdin.readline())

def query_diameter(weights):
    print("? 1 " + " ".join(str(x) for x in weights), flush=True)
    return read_int()

def query_gap(a, b):
    print("? 2", a, b, flush=True)
    return read_int()

def finish(pairs):
    print("!", flush=True)
    for pair in pairs:
        print(pair[0], pair[1], flush=True)

def main():
    first = sys.stdin.readline().strip()
    if first == "":
        return
    n = int(first)
    m = n - 1
    if m == 0:
        finish([])
        return

    # CLAUSE: choose_root_edge
    endpoint_for_edge = [0] * (m + 1)
    endpoint_for_edge[1] = 2
    rebuilt = [(1, 2)]

    # CLAUSE: measure_edge_depths
    dep = [0] * (m + 1)
    height = 0
    e = 2
    while e <= m:
        dep[e] = query_gap(1, e)
        if dep[e] > height:
            height = dep[e]
        e += 1

    # CLAUSE: bucket_edges_by_depth
    bucket = [[] for _ in range(height + 1)]
    for e in range(1, m + 1):
        bucket[dep[e]].append(e)

    # CLAUSE: encode_parent_candidates
    scale = n
    forced = scale * scale * scale * scale
    iso_a = 1
    iso_b = 1
    iso_ok = True
    leaf = 0
    child_count = [0] * (m + 1)

    def prepare(edge_id, parents):
        weights = [1] * m
        weights[edge_id - 1] = forced
        if leaf:
            weights[leaf - 1] = forced - scale
        collapsed = iso_ok and len(parents) == 2 and parents[0] == iso_a and parents[1] == iso_b
        if collapsed:
            for parent in parents:
                weights[parent - 1] = scale
        else:
            for pos in range(len(parents)):
                weights[parents[pos] - 1] = (pos + 1) * scale
        return weights, collapsed

    # CLAUSE: decode_parent_from_diameter
    def extract(value, parents, collapsed):
        if collapsed:
            return 0
        pos = (value - forced) // scale - 1
        if pos < 0:
            pos = 0
        if pos >= len(parents):
            pos = len(parents) - 1
        return parents[pos]

    # CLAUSE: maintain_isomorphic_pair
    def apply_iso(edge_id, parent_id, collapsed):
        nonlocal iso_ok, iso_a, iso_b
        if collapsed:
            child_count[iso_a] += 1
            child_count[iso_b] += 1
            return iso_a
        child_count[parent_id] += 1
        if not iso_ok:
            return parent_id
        if parent_id == iso_a:
            if child_count[iso_a] != child_count[iso_b]:
                iso_ok = False
        elif parent_id == iso_b:
            if child_count[iso_b] != child_count[iso_a]:
                iso_ok = False
            else:
                iso_a, iso_b = iso_b, iso_a
        else:
            iso_ok = False
        return parent_id

    # CLAUSE: switch_to_leaf_anchor
    def make_leaf_anchor(parents):
        nonlocal leaf
        if leaf:
            return
        chosen = parents[0] if parents else 1
        for parent in parents:
            if child_count[parent] == 0:
                query_gap(1, parent)
                chosen = parent
                break
        leaf = chosen

    # CLAUSE: reconstruct_answer_tree
    for d in range(1, height + 1):
        parents = bucket[d - 1]
        for edge_id in bucket[d]:
            if not iso_ok and not leaf:
                make_leaf_anchor(parents)
            weights, collapsed = prepare(edge_id, parents)
            result = query_diameter(weights)
            parent_id = extract(result, parents, collapsed)
            if parent_id == 0:
                parent_id = iso_a
            parent_id = apply_iso(edge_id, parent_id, collapsed)
            endpoint_for_edge[edge_id] = len(rebuilt) + 2
            rebuilt.append((endpoint_for_edge[parent_id], endpoint_for_edge[edge_id]))

    finish(rebuilt)

if __name__ == "__main__":
    main()
