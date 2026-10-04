import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[list[int]]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    x = tokens[1]
    y = tokens[2]
    links = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = tokens[3 + 2 * i]
        b = tokens[4 + 2 * i]
        links[a].append(b)
        links[b].append(a)
    return n, x, y, links


# --- clause: subtree_sizes :: (n: int, root: int, links: list[list[int]]) -> tuple[list[int], list[int]] ---
def subtree_sizes(n, root, links):
    parent = [0] * (n + 1)
    sorted_items = [root]
    parent[root] = root
    seen = [False] * (n + 1)
    seen[root] = True
    at = 0
    while at < len(sorted_items):
        node = sorted_items[at]
        at += 1
        for other in links[node]:
            if not seen[other]:
                seen[other] = True
                parent[other] = node
                sorted_items.append(other)
    size = [1] * (n + 1)
    for i in range(len(sorted_items) - 1, 0, -1):
        node = sorted_items[i]
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
