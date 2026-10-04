# CLAUSE: setup_environment
import sys

def colors_for_layer(layer, parent_color, k):
    m = len(layer)
    res = []
    for i in range(m):
        res.append(i + 1)
    if m < k:
        spare = m + 1
        for i in range(m):
            node = layer[i]
            if res[i] == parent_color[node]:
                res[i] = spare
                spare = parent_color[node]
        return res
    first = 0
    second = -1
    for i in range(1, m):
        if parent_color[layer[i]] != parent_color[layer[first]]:
            second = i
            break
    for i in range(m):
        node = layer[i]
        if res[i] == parent_color[node]:
            if parent_color[layer[first]] == parent_color[node]:
                j = second
            else:
                j = first
            res[i], res[j] = res[j], res[i]
    return res

# CLAUSE: solve_logic
def solve_tree(n, edges):
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    parent = [0] * (n + 1)
    parent[1] = -1
    stack = [(1, 0)]
    order = []
    while stack:
        v, d = stack.pop()
        order.append((v, d))
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                stack.append((u, d + 1))

    level_count = 0
    for _, d in order:
        if d + 1 > level_count:
            level_count = d + 1
    levels = [[] for _ in range(level_count)]
    for v, d in order:
        levels[d].append(v)

    width = max(len(x) for x in levels)
    operations = width
    for i in range(1, len(levels)):
        layer = levels[i]
        if len(layer) == width:
            one_parent = parent[layer[0]]
            for v in layer:
                if parent[v] != one_parent:
                    break
            else:
                operations += 1
                break

    color = [0] * (n + 1)
    color[1] = 1
    parent_color = [0] * (n + 1)
    answer_groups = [[] for _ in range(operations + 1)]
    answer_groups[1].append(1)

    for layer in levels[1:]:
        for v in layer:
            parent_color[v] = color[parent[v]]
        assigned = colors_for_layer(layer, parent_color, operations)
        for i in range(len(layer)):
            v = layer[i]
            c = assigned[i]
            color[v] = c
            answer_groups[c].append(v)

    lines = [str(operations)]
    for i in range(1, operations + 1):
        group = answer_groups[i]
        lines.append(" ".join(str(x) for x in [len(group)] + group))
    return lines

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    tests = data[index]
    index += 1
    output = []
    for _ in range(tests):
        n = data[index]
        index += 1
        edges = []
        for _ in range(n - 1):
            edges.append((data[index], data[index + 1]))
            index += 2
        output.extend(solve_tree(n, edges))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
