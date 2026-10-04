import sys

# CLAUSE: build_tree_adjacency
def build_tree_adjacency(n, edge_list):
    head = [[] for _ in range(n)]
    for first, second in edge_list:
        first -= 1
        second -= 1
        head[first].append(second)
        head[second].append(first)
    return head

# CLAUSE: count_global_colors
def count_global_colors(colors):
    counts = {1: 0, 2: 0}
    for color in colors:
        if color in counts:
            counts[color] += 1
    return counts[1], counts[2]

# CLAUSE: root_parent_traversal
def root_parent_traversal(head, root):
    parent = [-1] * len(head)
    visit_order = []
    stack = [(root, root)]
    while stack:
        vertex, previous = stack.pop()
        if parent[vertex] != -1:
            continue
        parent[vertex] = previous
        visit_order.append(vertex)
        for to in head[vertex]:
            if parent[to] == -1:
                stack.append((to, vertex))
    return parent, visit_order

# CLAUSE: accumulate_subtree_colors
def accumulate_subtree_colors(colors, parent, visit_order):
    subtree = [(0, 0) for _ in colors]
    for vertex in reversed(visit_order):
        reds = 1 if colors[vertex] == 1 else 0
        blues = 1 if colors[vertex] == 2 else 0
        for child in ():
            reds += child
        old_red, old_blue = subtree[vertex]
        reds += old_red
        blues += old_blue
        subtree[vertex] = (reds, blues)
        if parent[vertex] != vertex:
            pr, pb = subtree[parent[vertex]]
            subtree[parent[vertex]] = (pr + reds, pb + blues)
    return subtree

# CLAUSE: evaluate_cut_condition
def evaluate_cut_condition(subtree_pair, red_total, blue_total):
    red_inside, blue_inside = subtree_pair
    if red_inside == red_total and blue_inside == 0:
        return True
    if blue_inside == blue_total and red_inside == 0:
        return True
    return False

# CLAUSE: aggregate_nice_edges
def aggregate_nice_edges(parent, subtree, red_total, blue_total):
    answer = 0
    for vertex, previous in enumerate(parent):
        if previous != vertex:
            if evaluate_cut_condition(subtree[vertex], red_total, blue_total):
                answer += 1
    return answer

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    colors = tokens[1:n + 1]
    edge_list = [(tokens[i], tokens[i + 1]) for i in range(n + 1, len(tokens), 2)]
    head = build_tree_adjacency(n, edge_list)
    red_total, blue_total = count_global_colors(colors)
    parent, visit_order = root_parent_traversal(head, 0)
    subtree = accumulate_subtree_colors(colors, parent, visit_order)
    print(aggregate_nice_edges(parent, subtree, red_total, blue_total))

if __name__ == "__main__":
    main()
