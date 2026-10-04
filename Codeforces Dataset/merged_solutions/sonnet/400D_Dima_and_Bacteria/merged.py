import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    k = data[2]
    counts = data[3:3 + k]
    edges = []
    pos = 3 + k
    for _ in range(m):
        edges.append((data[pos], data[pos + 1], data[pos + 2]))
        pos += 3
    return n, m, k, counts, edges

# Clause type_of [Confidence: 0.80]
def type_of(n, counts):
    kind = [0] * (n + 1)
    node = 1
    for index, amount in enumerate(counts):
        for _ in range(amount):
            kind[node] = index
            node += 1
    return kind

# Clause zero_components [Confidence: 1.00]
def zero_components(n, edges):
    parent = list(range(n + 1))
    for u, v, cost in edges:
        if cost:
            continue
        ra = u
        while parent[ra] != ra:
            parent[ra] = parent[parent[ra]]
            ra = parent[ra]
        rb = v
        while parent[rb] != rb:
            parent[rb] = parent[parent[rb]]
            rb = parent[rb]
        if ra != rb:
            parent[ra] = rb
    root = [0] * (n + 1)
    for node in range(1, n + 1):
        spot = node
        while parent[spot] != spot:
            parent[spot] = parent[parent[spot]]
            spot = parent[spot]
        root[node] = spot
    return root

# Clause shortest_matrix [Confidence: 1.00]
def shortest_matrix(k, kind, root, edges, n):
    big = 1 << 40
    anchor = {}
    for node in range(1, n + 1):
        group = kind[node]
        if group in anchor:
            if anchor[group] != root[node]:
                return None
        else:
            anchor[group] = root[node]
    dist = [[big] * k for _ in range(k)]
    for index in range(k):
        dist[index][index] = 0
    for u, v, cost in edges:
        a = kind[u]
        b = kind[v]
        if cost < dist[a][b]:
            dist[a][b] = cost
            dist[b][a] = cost
    for middle in range(k):
        row = dist[middle]
        for i in range(k):
            step = dist[i][middle]
            if step >= big:
                continue
            line = dist[i]
            dist[i] = [here if here <= step + there else step + there
                       for here, there in zip(line, row)]
    return dist

# Clause main [Confidence: 1.00]
def main():
    n, m, k, counts, edges = read_input()
    kind = type_of(n, counts)
    root = zero_components(n, edges)
    dist = shortest_matrix(k, kind, root, edges, n)
    if dist is None:
        sys.stdout.write("No\n")
        return
    big = 1 << 40
    lines = ["Yes"]
    for row in dist:
        lines.append(" ".join(str(value if value < big else -1) for value in row))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()

