import sys

def query(kind, data):
    if kind == 1:
        print("? 1", *data, flush=True)
    else:
        print("? 2", data[0], data[1], flush=True)
    return int(sys.stdin.readline())

def main():
    raw = sys.stdin.readline().strip()
    if not raw:
        return
    n = int(raw)
    last_edge = n - 1
    if last_edge == 0:
        print("!", flush=True)
        return

    # CLAUSE: choose_root_edge
    root = 1
    vertex_of = [0] * (last_edge + 1)
    vertex_of[root] = 2
    produced = [(1, 2)]

    # CLAUSE: measure_edge_depths
    level = [0] * (last_edge + 1)
    limit = 0
    for edge in range(2, last_edge + 1):
        level[edge] = query(2, (root, edge))
        limit = max(limit, level[edge])

    # CLAUSE: bucket_edges_by_depth
    levels = [[] for _ in range(limit + 1)]
    edge = 1
    while edge <= last_edge:
        levels[level[edge]].append(edge)
        edge += 1

    # CLAUSE: encode_parent_candidates
    unit = n
    dominant = n * n * n * n * n + 31
    mirror = [root, root]
    mirror_alive = True
    extra_leaf = -1
    descendants = [[] for _ in range(last_edge + 1)]

    def build(edge, parents):
        weights = [1] * last_edge
        weights[edge - 1] = dominant
        if extra_leaf != -1:
            weights[extra_leaf - 1] = dominant - unit
        shared_code = mirror_alive and len(parents) == 2 and parents[0] == mirror[0] and parents[1] == mirror[1]
        if shared_code:
            for p in parents:
                weights[p - 1] = unit
        else:
            code = unit
            for p in parents:
                weights[p - 1] = code
                code += unit
        return weights, shared_code

    # CLAUSE: decode_parent_from_diameter
    def parent_from(value, parents, shared_code):
        if shared_code:
            return parents[0]
        number = (value - dominant) // unit
        number = min(max(number, 1), len(parents))
        return parents[number - 1]

    # CLAUSE: maintain_isomorphic_pair
    def update_mirror(edge, parent, shared_code):
        nonlocal mirror_alive, mirror
        if shared_code:
            descendants[mirror[0]].append(edge)
            descendants[mirror[1]].append(edge)
            return mirror[0]
        descendants[parent].append(edge)
        if mirror_alive:
            x, y = mirror
            if parent == x:
                mirror_alive = len(descendants[x]) == len(descendants[y])
            elif parent == y:
                mirror_alive = len(descendants[x]) == len(descendants[y])
                if mirror_alive:
                    mirror = [y, x]
            else:
                mirror_alive = False
        return parent

    # CLAUSE: switch_to_leaf_anchor
    def activate_leaf(parents):
        nonlocal extra_leaf
        if extra_leaf != -1:
            return
        pick = root
        for p in parents:
            if not descendants[p]:
                query(2, (root, p))
                pick = p
                break
        else:
            if parents:
                pick = parents[-1]
        extra_leaf = pick

    # CLAUSE: reconstruct_answer_tree
    for depth in range(1, limit + 1):
        parents = levels[depth - 1]
        current = levels[depth]
        idx = 0
        while idx < len(current):
            edge = current[idx]
            if not mirror_alive and extra_leaf == -1:
                activate_leaf(parents)
            weights, shared_code = build(edge, parents)
            value = query(1, weights)
            parent = parent_from(value, parents, shared_code)
            parent = update_mirror(edge, parent, shared_code)
            vertex_of[edge] = len(produced) + 2
            produced.append((vertex_of[parent], vertex_of[edge]))
            idx += 1

    print("!", flush=True)
    for a, b in produced:
        print(a, b, flush=True)

if __name__ == "__main__":
    main()
