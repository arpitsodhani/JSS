import sys

tokens = list(map(int, sys.stdin.buffer.read().split()))
i = 0
tests = tokens[i]
i += 1
answers = []

for _ in range(tests):
    n = tokens[i]
    i += 1

    # CLAUSE: build_child_adjacency
    child = [[] for _ in range(n + 1)]
    for node in range(2, n + 1):
        parent = tokens[i]
        i += 1
        child[parent].append(node)

    low = [0] * (n + 1)
    high = [0] * (n + 1)
    for node in range(1, n + 1):
        low[node] = tokens[i]
        high[node] = tokens[i + 1]
        i += 2

    # CLAUSE: traverse_subtree_postorder
    stack = [1]
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        stack.extend(child[v])

    value = [0] * (n + 1)
    operations = 0

    for v in reversed(order):
        # CLAUSE: aggregate_child_capacity
        subtotal = 0
        for u in child[v]:
            subtotal += value[u]

        # CLAUSE: enforce_vertex_lower_bound
        if subtotal < low[v]:
            operations += 1

            # CLAUSE: cap_vertex_contribution
            value[v] = high[v]
        else:
            # CLAUSE: cap_vertex_contribution
            value[v] = subtotal if subtotal < high[v] else high[v]

    # CLAUSE: count_required_operations
    answers.append(str(operations))

sys.stdout.write("\n".join(answers))
