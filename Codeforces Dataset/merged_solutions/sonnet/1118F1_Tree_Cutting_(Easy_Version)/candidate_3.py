import sys


# --- clause: read_input :: () -> tuple[list[int], list[tuple[int, int]]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    colours = fields[1:1 + n]
    edges = []
    offset = 1 + n
    for _ in range(n - 1):
        edges.append((fields[offset], fields[offset + 1]))
        offset += 2
    return colours, edges


# --- clause: subtree_counts :: (colours: list[int], edges: list[tuple[int, int]]) -> tuple[list[int], list[int], list[int], list[int]] ---
def subtree_counts(colours, edges):
    n = len(colours)
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    parent = [0] * (n + 1)
    parent[1] = 1
    order = [1]
    seen = [False] * (n + 1)
    seen[1] = True
    front = 0
    while front < len(order):
        v = order[front]
        front += 1
        for u in adj[v]:
            if not seen[u]:
                seen[u] = True
                parent[u] = v
                order.append(u)
    red = [0] * (n + 1)
    blue = [0] * (n + 1)
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
    total_red = red[1]
    total_blue = blue[1]
    count = 0
    for v in order[1:]:
        inside_red = red[v]
        inside_blue = blue[v]
        outside_red = total_red - inside_red
        outside_blue = total_blue - inside_blue
        if (inside_red == 0 and outside_blue == 0) or (inside_blue == 0 and outside_red == 0):
            count += 1
    return count


# --- clause: main :: () -> None ---
def main():
    colours, edges = read_input()
    order, parent, red, blue = subtree_counts(colours, edges)
    sys.stdout.write("%d\n" % nice_edges(order, parent, red, blue))


if __name__ == "__main__":
    main()
