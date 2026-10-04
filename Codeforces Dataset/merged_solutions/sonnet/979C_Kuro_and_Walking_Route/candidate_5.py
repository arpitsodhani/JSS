import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    x = raw[1]
    y = raw[2]
    links = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a = raw[3 + 2 * i]
        b = raw[4 + 2 * i]
        links[a].append(b)
        links[b].append(a)
    return n, x, y, links


# --- clause: subtree_sizes :: (n: int, root: int, links: list[list[int]]) -> tuple[list[int], list[int]] ---
def subtree_sizes(n, root, links):
    parent = [0] * (n + 1)
    queue_order = [root]
    parent[root] = root
    visited = [False] * (n + 1)
    visited[root] = True
    at = 0
    while at < len(queue_order):
        node = queue_order[at]
        at += 1
        for other in links[node]:
            if not visited[other]:
                visited[other] = True
                parent[other] = node
                queue_order.append(other)
    size = [1] * (n + 1)
    for i in range(len(queue_order) - 1, 0, -1):
        node = queue_order[i]
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
