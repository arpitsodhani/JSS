import sys

# CLAUSE: build_tree_adjacency
def build_tree_adjacency(n, edges):
    adjacency = [[] for _ in range(n)]
    for edge in edges:
        x = edge[0] - 1
        y = edge[1] - 1
        adjacency[x].append(y)
        adjacency[y].append(x)
    return adjacency

# CLAUSE: count_global_colors
def count_global_colors(colors):
    totals = [0, 0]
    for value in colors:
        if value:
            totals[value - 1] += 1
    return totals[0], totals[1]

# CLAUSE: root_parent_traversal
def root_parent_traversal(adjacency, root):
    parent = [-2] * len(adjacency)
    parent[root] = -1
    traversal = []
    stack = [root]
    while stack:
        current = stack.pop()
        traversal.append(current)
        for neighbor in adjacency[current]:
            if parent[neighbor] == -2:
                parent[neighbor] = current
                stack.append(neighbor)
    return parent, traversal

# CLAUSE: accumulate_subtree_colors
def accumulate_subtree_colors(colors, parent, traversal):
    subtree_red = [0] * len(colors)
    subtree_blue = [0] * len(colors)
    for current in reversed(traversal):
        subtree_red[current] += colors[current] == 1
        subtree_blue[current] += colors[current] == 2
        par = parent[current]
        if par != -1:
            subtree_red[par] += subtree_red[current]
            subtree_blue[par] += subtree_blue[current]
    return subtree_red, subtree_blue

# CLAUSE: evaluate_cut_condition
def evaluate_cut_condition(red_count, blue_count, total_red, total_blue):
    red_component = red_count == total_red and blue_count == 0
    blue_component = blue_count == total_blue and red_count == 0
    return red_component or blue_component

# CLAUSE: aggregate_nice_edges
def aggregate_nice_edges(parent, subtree_red, subtree_blue, total_red, total_blue):
    total = 0
    for current, par in enumerate(parent):
        if par == -1:
            continue
        if evaluate_cut_condition(subtree_red[current], subtree_blue[current], total_red, total_blue):
            total += 1
    return total

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    colors = values[1:n + 1]
    rest = values[n + 1:]
    edges = list(zip(rest[0::2], rest[1::2]))
    adjacency = build_tree_adjacency(n, edges)
    total_red, total_blue = count_global_colors(colors)
    parent, traversal = root_parent_traversal(adjacency, 0)
    subtree_red, subtree_blue = accumulate_subtree_colors(colors, parent, traversal)
    print(aggregate_nice_edges(parent, subtree_red, subtree_blue, total_red, total_blue))

if __name__ == "__main__":
    main()
