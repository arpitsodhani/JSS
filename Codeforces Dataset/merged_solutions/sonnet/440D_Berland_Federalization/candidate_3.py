import sys


# --- clause: read_input :: () -> tuple[int, int, list[tuple[int, int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    edges = []
    pos = 2
    for _ in range(n - 1):
        edges.append((data[pos], data[pos + 1]))
        pos += 2
    return n, k, edges


# --- clause: root_tree :: (n: int, edges: list[tuple[int, int]]) -> tuple[list[int], list[int], list[list[int]]] ---
def root_tree(n, edges):
    adj = [[] for _ in range(n + 1)]
    for index, (u, v) in enumerate(edges):
        adj[u].append(v)
        adj[v].append(u)
    parent = [0] * (n + 1)
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    head = 0
    while head < len(order):
        node = order[head]
        head += 1
        for nxt in adj[node]:
            if not seen[nxt]:
                seen[nxt] = True
                parent[nxt] = node
                order.append(nxt)
    children = [[] for _ in range(n + 1)]
    for node in order[1:]:
        children[parent[node]].append(node)
    return parent, order, children


# --- clause: pick_component :: (n: int, k: int, order: list[int], children: list[list[int]]) -> set ---
def pick_component(n, k, order, children):
    big = 1 << 40
    table = [None] * (n + 1)
    history = [None] * (n + 1)
    size = [1] * (n + 1)
    for node in reversed(order):
        current = [big, 0]
        steps = []
        total = 1
        for child in children[node]:
            steps.append(current[:])
            sub = table[child]
            merged = [big] * (total + size[child] + 1)
            for taken in range(1, total + 1):
                here = current[taken]
                if here >= big:
                    continue
                if here + 1 < merged[taken]:
                    merged[taken] = here + 1
                for extra in range(1, size[child] + 1):
                    if sub[extra] >= big:
                        continue
                    if here + sub[extra] < merged[taken + extra]:
                        merged[taken + extra] = here + sub[extra]
            total += size[child]
            current = merged
        table[node] = current
        history[node] = steps
        size[node] = total
    best = big
    root = 1
    for node in range(1, n + 1):
        column = table[node]
        if k < len(column) and column[k] < big:
            cost = column[k] + (0 if node == 1 else 1)
            if cost < best:
                best = cost
                root = node
    chosen = set()
    stack = [(root, k)]
    while stack:
        node, want = stack.pop()
        chosen.add(node)
        current = table[node]
        kids = children[node]
        for index in range(len(kids) - 1, -1, -1):
            previous = history[node][index]
            child = kids[index]
            sub = table[child]
            if want < len(previous) and previous[want] < big and previous[want] + 1 == current[want]:
                current = previous
                continue
            for extra in range(1, min(size[child], want - 1) + 1):
                if want - extra < len(previous) and previous[want - extra] < big and sub[extra] < big:
                    if previous[want - extra] + sub[extra] == current[want]:
                        stack.append((child, extra))
                        want -= extra
                        break
            current = previous
    return chosen


# --- clause: main :: () -> None ---
def main():
    n, k, edges = read_input()
    parent, order, children = root_tree(n, edges)
    chosen = pick_component(n, k, order, children)
    cuts = []
    for index, (u, v) in enumerate(edges, start=1):
        if (u in chosen) != (v in chosen):
            cuts.append(index)
    sys.stdout.write(str(len(cuts)) + "\n" + " ".join(map(str, cuts)) + "\n")


if __name__ == "__main__":
    main()
