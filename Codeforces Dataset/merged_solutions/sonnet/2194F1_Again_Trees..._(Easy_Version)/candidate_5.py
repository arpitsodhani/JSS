import sys

MOD = 1000000007


# --- clause: read_input :: () -> list[tuple[int, list[int], list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        k = int(data[pos])
        pos += 1
        edges = [int(token) for token in data[pos:pos + 2 * (n - 1)]]
        pos += 2 * (n - 1)
        values = [int(token) for token in data[pos:pos + n]]
        pos += n
        targets = [int(token) for token in data[pos:pos + k]]
        pos += k
        cases.append((n, edges, values, targets))
    return cases


# --- clause: build_order :: (n: int, edges: list[int]) -> tuple[list[int], list[int]] ---
def build_order(n, edges):
    head = [0] * (n + 2)
    for value in edges:
        head[value] += 1
    start = [0] * (n + 2)
    for v in range(1, n + 1):
        start[v + 1] = start[v] + head[v]
    fill = start[:]
    adj = [0] * (2 * (n - 1)) if n > 1 else []
    for i in range(0, len(edges), 2):
        u = edges[i]
        v = edges[i + 1]
        adj[fill[u]] = v
        fill[u] += 1
        adj[fill[v]] = u
        fill[v] += 1
    parent = [0] * (n + 1)
    order = []
    seen = [False] * (n + 1)
    seen[1] = True
    stack = [1]
    while stack:
        node = stack.pop()
        order.append(node)
        for idx in range(start[node], start[node + 1]):
            nxt = adj[idx]
            if not seen[nxt]:
                seen[nxt] = True
                parent[nxt] = node
                stack.append(nxt)
    return order, parent


# --- clause: count_sets :: (n: int, values: list[int], targets: list[int], order: list[int], parent: list[int]) -> int ---
def count_sets(n, values, targets, order, parent):
    goal = set(targets)
    span = {0}
    for b in targets:
        span |= {x ^ b for x in span}
    span = list(span)
    tables = [None] * (n + 1)
    for node in order:
        tables[node] = {values[node - 1]: 1}
    for i in range(len(order) - 1, 0, -1):
        node = order[i]
        up = parent[node]
        child = tables[node]
        cut = 0
        for value, ways in child.items():
            if value in goal:
                cut += ways
        cut %= MOD
        merged = {}
        parent_table = tables[up]
        for value in parent_table:
            ways = parent_table[value]
            if cut:
                merged[value] = (merged.get(value, 0) + ways * cut) % MOD
            for other in child:
                key = value ^ other
                merged[key] = (merged.get(key, 0) + ways * child[other]) % MOD
        tables[up] = merged
        tables[node] = None
    total = 0
    for value, ways in tables[order[0]].items():
        if value in goal:
            total += ways
    return total % MOD


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, edges, values, targets in read_input():
        order, parent = build_order(n, edges)
        out.append(str(count_sets(n, values, targets, order, parent)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
