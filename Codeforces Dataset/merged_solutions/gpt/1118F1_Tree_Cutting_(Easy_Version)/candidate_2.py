import sys

# CLAUSE: build_tree_adjacency
def build_tree_adjacency(n, pairs):
    adjacency = [[] for _ in range(n + 1)]
    for u, v in pairs:
        adjacency[u].append(v)
        adjacency[v].append(u)
    return adjacency

# CLAUSE: count_global_colors
def count_global_colors(colors):
    red_total = 0
    blue_total = 0
    for color in colors[1:]:
        if color == 1:
            red_total += 1
        elif color == 2:
            blue_total += 1
    return red_total, blue_total

# CLAUSE: root_parent_traversal
def root_parent_traversal(adjacency, root):
    parent = [0] * len(adjacency)
    preorder = []
    stack = [(root, 0)]
    while stack:
        vertex, par = stack.pop()
        parent[vertex] = par
        preorder.append(vertex)
        for child in adjacency[vertex]:
            if child != par:
                stack.append((child, vertex))
    return parent, preorder

# CLAUSE: accumulate_subtree_colors
def accumulate_subtree_colors(colors, parent, preorder):
    sub = [[0, 0] for _ in range(len(colors))]
    for vertex in preorder:
        if colors[vertex] == 1:
            sub[vertex][0] = 1
        elif colors[vertex] == 2:
            sub[vertex][1] = 1
    for vertex in preorder[::-1]:
        par = parent[vertex]
        if par:
            sub[par][0] += sub[vertex][0]
            sub[par][1] += sub[vertex][1]
    return sub

# CLAUSE: evaluate_cut_condition
def evaluate_cut_condition(counts, red_total, blue_total):
    reds, blues = counts
    return (reds == red_total and blues == 0) or (blues == blue_total and reds == 0)

# CLAUSE: aggregate_nice_edges
def aggregate_nice_edges(parent, sub, red_total, blue_total):
    good = 0
    for vertex in range(1, len(parent)):
        if parent[vertex] and evaluate_cut_condition(sub[vertex], red_total, blue_total):
            good += 1
    return good

def main():
    items = list(map(int, sys.stdin.buffer.read().split()))
    n = items[0]
    colors = [0] + items[1:n + 1]
    pairs = []
    index = n + 1
    for _ in range(n - 1):
        pairs.append((items[index], items[index + 1]))
        index += 2
    adjacency = build_tree_adjacency(n, pairs)
    red_total, blue_total = count_global_colors(colors)
    parent, preorder = root_parent_traversal(adjacency, 1)
    sub = accumulate_subtree_colors(colors, parent, preorder)
    print(aggregate_nice_edges(parent, sub, red_total, blue_total))

if __name__ == "__main__":
    main()
