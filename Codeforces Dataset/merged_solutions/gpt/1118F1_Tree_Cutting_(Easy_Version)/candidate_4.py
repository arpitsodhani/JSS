import sys

# CLAUSE: build_tree_adjacency
def build_tree_adjacency(n, edges):
    neighbors = [[] for _ in range(n + 1)]
    for left, right in edges:
        neighbors[left].append(right)
        neighbors[right].append(left)
    return neighbors

# CLAUSE: count_global_colors
def count_global_colors(colors):
    red_total = sum(1 for color in colors if color == 1)
    blue_total = sum(1 for color in colors if color == 2)
    return red_total, blue_total

# CLAUSE: root_parent_traversal
def root_parent_traversal(neighbors, root):
    parent = [-1] * len(neighbors)
    sequence = []
    stack = [root]
    parent[root] = 0
    while stack:
        vertex = stack.pop()
        sequence.append(vertex)
        for nxt in neighbors[vertex]:
            if nxt != parent[vertex]:
                parent[nxt] = vertex
                stack.append(nxt)
    return parent, sequence

# CLAUSE: accumulate_subtree_colors
def accumulate_subtree_colors(colors, parent, sequence):
    red = [0] * len(parent)
    blue = [0] * len(parent)
    for vertex in reversed(sequence):
        color = colors[vertex - 1]
        red[vertex] += 1 if color == 1 else 0
        blue[vertex] += 1 if color == 2 else 0
        if parent[vertex] != 0:
            red[parent[vertex]] += red[vertex]
            blue[parent[vertex]] += blue[vertex]
    return red, blue

# CLAUSE: evaluate_cut_condition
def evaluate_cut_condition(vertex, red, blue, all_red, all_blue):
    has_all_red_only = red[vertex] == all_red and blue[vertex] == 0
    has_all_blue_only = blue[vertex] == all_blue and red[vertex] == 0
    return has_all_red_only or has_all_blue_only

# CLAUSE: aggregate_nice_edges
def aggregate_nice_edges(parent, red, blue, all_red, all_blue):
    result = 0
    for vertex in range(1, len(parent)):
        if parent[vertex] > 0:
            result += evaluate_cut_condition(vertex, red, blue, all_red, all_blue)
    return result

def main():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    colors = raw[1:n + 1]
    edges = []
    position = n + 1
    while position < len(raw):
        edges.append((raw[position], raw[position + 1]))
        position += 2
    neighbors = build_tree_adjacency(n, edges)
    all_red, all_blue = count_global_colors(colors)
    parent, sequence = root_parent_traversal(neighbors, 1)
    red, blue = accumulate_subtree_colors(colors, parent, sequence)
    print(aggregate_nice_edges(parent, red, blue, all_red, all_blue))

if __name__ == "__main__":
    main()
