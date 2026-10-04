import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[list[int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    x = fields[1]
    y = fields[2]
    links = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = fields[3 + 2 * i]
        b = fields[4 + 2 * i]
        links[a].append(b)
        links[b].append(a)
    return n, x, y, links


# --- clause: subtree_sizes :: (n: int, root: int, links: list[list[int]]) -> tuple[list[int], list[int]] ---
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


# --- clause: count_routes :: (n: int, x: int, y: int, links: list[list[int]]) -> int ---
def count_routes(n, x, y, links):
    parent, size = subtree_sizes(n, x, links)
    node = y
    while parent[node] != x:
        node = parent[node]
    return n * (n - 1) - (n - size[node]) * size[y]


# --- clause: main :: () -> None ---
def main():
    n, x, y, links = read_input()
    sys.stdout.write("%d\n" % count_routes(n, x, y, links))


if __name__ == "__main__":
    main()
