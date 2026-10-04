# CLAUSE: setup_environment
import sys

def emit_question(values):
    print(values[0], values[1], values[2], flush=True)
    return sys.stdin.readline().strip()

def same_branch(base_a, base_b, item):
    response = emit_question((base_a, base_b, item))
    return response != "Y"

# CLAUSE: solve_logic
def attach(x, y):
    tree_edges.append((x, y))
    return leaf_count + len(tree_edges)

def split_block(block):
    if len(block) == 1:
        return block[0]
    if len(block) == 2:
        return attach(block[0], block[1])

    a, b = block[0], block[1]
    a_block = [a]
    b_block = [b]

    for item in block:
        if item == a or item == b:
            continue
        if same_branch(a, b, item):
            a_block.append(item)
        else:
            b_block.append(item)

    return attach(split_block(a_block), split_block(b_block))

def compute_answer():
    global leaf_count, tree_edges
    leaf_count = int(sys.stdin.readline())
    tree_edges = []
    root_node = split_block(tuple(range(1, leaf_count + 1)))

    parents = [0 for _ in range(2 * leaf_count)]
    for offset, edge in enumerate(tree_edges):
        node_id = leaf_count + offset + 1
        left_child, right_child = edge
        parents[left_child] = node_id
        parents[right_child] = node_id
    parents[root_node] = -1
    return parents

# CLAUSE: finish_program
parents = compute_answer()
print(-1, flush=True)
print(*parents[1:], flush=True)
