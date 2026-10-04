import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    colours = numbers[1:1 + n]
    edges = []
    cursor = 1 + n
    for _ in range(n - 1):
        edges.append((numbers[cursor], numbers[cursor + 1]))
        cursor += 2
    return colours, edges


# --- clause: subtree_counts :: (colours: list[int], edges: list[tuple[int, int]]) -> tuple[list[int], list[int], list[int], list[int]] ---
def subtree_counts(colours, edges):
    n = len(colours)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = [0 for _ in range(n + 1)]
    parent[1] = 1
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    head = 0
    while head < len(order):
        v = order[head]
        head += 1
        for u in adj[v]:
            if not seen[u]:
                seen[u] = True
                parent[u] = v
                order.append(u)
    red = [0 for _ in range(n + 1)]
    blue = [0 for _ in range(n + 1)]
    for v in range(1, n + 1):
        if colours[v - 1] == 1:
            red[v] = 1
        elif colours[v - 1] == 2:
            blue[v] = 1
    for i in range(len(order) - 1, 0, -1):
        v = order[i]
        red[parent[v]] += red[v]
        blue[parent[v]] += blue[v]
    return order, parent, red, blue


# --- clause: nice_edges :: (order: list[int], parent: list[int], red: list[int], blue: list[int]) -> int ---
def nice_edges(order, parent, red, blue):
    whole_red = red[1]
    whole_blue = blue[1]
    count = 0
    for spot in range(1, len(order)):
        v = order[spot]
        pair = (red[v], blue[v])
        rest = (whole_red - pair[0], whole_blue - pair[1])
        clean_inside = pair[0] == 0 or pair[1] == 0
        clean_outside = rest[0] == 0 or rest[1] == 0
        if not clean_inside or not clean_outside:
            continue
        if pair[0] == 0 and rest[1] == 0:
            count += 1
        elif pair[1] == 0 and rest[0] == 0:
            count += 1
    return count


# --- clause: main :: () -> None ---
def main():
    colours, edges = read_input()
    order, parent, red, blue = subtree_counts(colours, edges)
    sys.stdout.write("%d\n" % nice_edges(order, parent, red, blue))


if __name__ == "__main__":
    main()
