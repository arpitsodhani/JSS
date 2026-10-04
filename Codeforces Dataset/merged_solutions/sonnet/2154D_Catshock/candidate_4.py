# CLAUSE: setup_environment
import sys

def build_rooted_tree(n, graph):
    parent = [0] * (n + 1)
    seen = [False] * (n + 1)
    seen[n] = True
    parent[n] = -1
    stack = [(n, 0)]
    order = []
    while stack:
        node, idx = stack[-1]
        if idx == 0:
            order.append(node)
        if idx == len(graph[node]):
            stack.pop()
            continue
        nxt = graph[node][idx]
        stack[-1] = (node, idx + 1)
        if not seen[nxt]:
            seen[nxt] = True
            parent[nxt] = node
            stack.append((nxt, 0))
    return parent, order

# CLAUSE: solve_logic
def commands_for_tree(n, graph):
    parent, order = build_rooted_tree(n, graph)

    on_path = [False] * (n + 1)
    path_nodes = []
    node = 1
    while node != n:
        path_nodes.append(node)
        on_path[node] = True
        node = parent[node]
    path_nodes.append(n)
    on_path[n] = True

    commands = []
    for node in order:
        if on_path[node]:
            continue
        commands.append("2 " + str(node))
        commands.append("1")

    for node in path_nodes[:-1]:
        commands.append("2 " + str(node))
        commands.append("1")

    return commands

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p = 0
    tests = data[p]
    p += 1
    answer = []
    for _ in range(tests):
        n = data[p]
        p += 1
        graph = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = data[p]
            v = data[p + 1]
            p += 2
            graph[u].append(v)
            graph[v].append(u)
        block = commands_for_tree(n, graph)
        answer.append(str(len(block)))
        answer.extend(block)
    sys.stdout.write("\n".join(answer))

if __name__ == "__main__":
    main()
