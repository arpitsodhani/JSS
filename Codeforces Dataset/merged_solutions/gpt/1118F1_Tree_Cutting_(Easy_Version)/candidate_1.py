import sys

# CLAUSE: build_tree_adjacency
def build_tree_adjacency(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    return graph

# CLAUSE: count_global_colors
def count_global_colors(colors):
    return colors.count(1), colors.count(2)

# CLAUSE: root_parent_traversal
def root_parent_traversal(graph, root):
    parent = [-1] * len(graph)
    order = []
    stack = [root]
    parent[root] = root
    while stack:
        node = stack.pop()
        order.append(node)
        for nxt in graph[node]:
            if parent[nxt] == -1:
                parent[nxt] = node
                stack.append(nxt)
    return parent, order

# CLAUSE: accumulate_subtree_colors
def accumulate_subtree_colors(colors, parent, order):
    red = [0] * len(colors)
    blue = [0] * len(colors)
    for node, color in enumerate(colors):
        red[node] = 1 if color == 1 else 0
        blue[node] = 1 if color == 2 else 0
    for node in reversed(order):
        if parent[node] != node:
            red[parent[node]] += red[node]
            blue[parent[node]] += blue[node]
    return red, blue

# CLAUSE: evaluate_cut_condition
def evaluate_cut_condition(node, red, blue, total_red, total_blue):
    return (red[node] == total_red and blue[node] == 0) or (blue[node] == total_blue and red[node] == 0)

# CLAUSE: aggregate_nice_edges
def aggregate_nice_edges(parent, red, blue, total_red, total_blue):
    answer = 0
    for node in range(len(parent)):
        if parent[node] != node and evaluate_cut_condition(node, red, blue, total_red, total_blue):
            answer += 1
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    colors = data[1:1 + n]
    edge_values = data[1 + n:]
    edges = [(edge_values[i], edge_values[i + 1]) for i in range(0, len(edge_values), 2)]
    graph = build_tree_adjacency(n, edges)
    total_red, total_blue = count_global_colors(colors)
    parent, order = root_parent_traversal(graph, 0)
    red, blue = accumulate_subtree_colors(colors, parent, order)
    print(aggregate_nice_edges(parent, red, blue, total_red, total_blue))

if __name__ == "__main__":
    main()
