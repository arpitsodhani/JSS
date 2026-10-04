import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    x = data[1]
    y = data[2]
    links = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = data[3 + 2 * i]
        b = data[4 + 2 * i]
        links[a].append(b)
        links[b].append(a)
    return n, x, y, links

# Clause subtree_sizes [Confidence: 1.00]
def subtree_sizes(n, root, links):
    parent = [0] * (n + 1)
    arranged = [root]
    parent[root] = root
    known = [False] * (n + 1)
    known[root] = True
    at = 0
    while at < len(arranged):
        node = arranged[at]
        at += 1
        for other in links[node]:
            if not known[other]:
                known[other] = True
                parent[other] = node
                arranged.append(other)
    size = [1] * (n + 1)
    for i in range(len(arranged) - 1, 0, -1):
        node = arranged[i]
        size[parent[node]] += size[node]
    return parent, size

# Clause count_routes [Confidence: 1.00]
def count_routes(n, x, y, links):
    parent, size = subtree_sizes(n, x, links)
    node = y
    while parent[node] != x:
        node = parent[node]
    return n * (n - 1) - (n - size[node]) * size[y]

# Clause main [Confidence: 1.00]
def main():
    n, x, y, links = read_input()
    sys.stdout.write("%d\n" % count_routes(n, x, y, links))


if __name__ == "__main__":
    main()

