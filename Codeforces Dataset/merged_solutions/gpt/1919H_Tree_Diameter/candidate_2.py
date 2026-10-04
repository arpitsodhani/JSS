import sys

def q1(arr):
    sys.stdout.write("? 1 " + " ".join(map(str, arr)) + "\n")
    sys.stdout.flush()
    return int(sys.stdin.readline())

def q2(x, y):
    sys.stdout.write(f"? 2 {x} {y}\n")
    sys.stdout.flush()
    return int(sys.stdin.readline())

def emit(ans):
    sys.stdout.write("!\n")
    for a, b in ans:
        sys.stdout.write(f"{a} {b}\n")
    sys.stdout.flush()

def main():
    s = sys.stdin.readline().strip()
    if not s:
        return
    n = int(s)
    if n <= 1:
        emit([])
        return

    edges_count = n - 1

    # CLAUSE: choose_root_edge
    root_edge = 1
    owner = {root_edge: 2}
    tree_edges = [(1, 2)]

    # CLAUSE: measure_edge_depths
    dist = {root_edge: 0}
    deepest = 0
    for label in range(2, edges_count + 1):
        val = q2(root_edge, label)
        dist[label] = val
        deepest = max(deepest, val)

    # CLAUSE: bucket_edges_by_depth
    by_depth = {}
    for label, val in dist.items():
        by_depth.setdefault(val, []).append(label)
    for val in by_depth:
        by_depth[val].sort()

    # CLAUSE: encode_parent_candidates
    base = n
    heavy = n ** 4 + 17
    twin = (root_edge, root_edge)
    twin_valid = True
    anchor = None
    sons = {i: [] for i in range(1, edges_count + 1)}

    def encode(new_label, prev):
        arr = [1 for _ in range(edges_count)]
        arr[new_label - 1] = heavy
        if anchor is not None:
            arr[anchor - 1] = heavy - base
        same_twin = twin_valid and len(prev) == 2 and tuple(prev) == twin
        if same_twin:
            arr[prev[0] - 1] = base
            arr[prev[1] - 1] = base
        else:
            mult = 1
            for label in prev:
                arr[label - 1] = mult * base
                mult += 1
        return arr, same_twin

    # CLAUSE: decode_parent_from_diameter
    def decode(total, prev, was_twin):
        if was_twin:
            return None
        idx = (total - heavy) // base
        if idx < 1:
            idx = 1
        elif idx > len(prev):
            idx = len(prev)
        return prev[idx - 1]

    # CLAUSE: maintain_isomorphic_pair
    def record(new_label, parent, was_twin):
        nonlocal twin_valid, twin
        if was_twin:
            a, b = twin
            sons[a].append(new_label)
            sons[b].append(new_label)
            return a
        sons[parent].append(new_label)
        if twin_valid:
            a, b = twin
            if parent == a or parent == b:
                mate = b if parent == a else a
                if len(sons[parent]) != len(sons[mate]):
                    twin_valid = False
                else:
                    twin = (parent, mate)
            else:
                twin_valid = False
        return parent

    # CLAUSE: switch_to_leaf_anchor
    def choose_anchor(prev):
        nonlocal anchor
        if anchor is not None:
            return
        for label in prev:
            if len(sons[label]) == 0:
                q2(root_edge, label)
                anchor = label
                return
        anchor = prev[0] if prev else root_edge

    # CLAUSE: reconstruct_answer_tree
    for dep in range(1, deepest + 1):
        prev = by_depth.get(dep - 1, [])
        cur = by_depth.get(dep, [])
        for label in cur:
            if not twin_valid and anchor is None:
                choose_anchor(prev)
            packet, ambiguous = encode(label, prev)
            got = q1(packet)
            par = decode(got, prev, ambiguous)
            if par is None:
                par = twin[0]
            par = record(label, par, ambiguous)
            owner[label] = len(owner) + 2
            tree_edges.append((owner[par], owner[label]))

    emit(tree_edges)

if __name__ == "__main__":
    main()
