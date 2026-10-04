import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        flat = data[pos:pos + 2 * (n - 1)]
        pos += 2 * (n - 1)
        cases.append((n, flat))
    return cases

# Clause build_tree [Confidence: 1.00]
def build_tree(n, flat):
    adj = [[] for _ in range(n + 1)]
    for i in range(0, len(flat), 2):
        adj[flat[i]].append(flat[i + 1])
        adj[flat[i + 1]].append(flat[i])
    parent = [0] * (n + 1)
    order = []
    frontier = [1]
    while frontier:
        nxt = []
        for u in frontier:
            order.append(u)
            for w in adj[u]:
                if w != parent[u]:
                    parent[w] = u
                    nxt.append(w)
        frontier = nxt
    return adj, parent, order

# Clause solve_case [Confidence: 1.00]
def solve_case(n, flat):
    adj, parent, order = build_tree(n, flat)
    size = [1] * (n + 1)
    saved = [0] * (n + 1)
    for u in reversed(order):
        kids = [w for w in adj[u] if w != parent[u]]
        if len(kids) == 1:
            saved[u] = size[kids[0]] - 1
        elif len(kids) == 2:
            first, second = kids
            cut_first = size[first] - 1 + saved[second]
            cut_second = size[second] - 1 + saved[first]
            saved[u] = cut_first if cut_first > cut_second else cut_second
        size[parent[u]] += size[u]
    return saved[1]

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, flat in read_input():
        out.append(str(solve_case(n, flat)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

