# CLAUSE: setup_environment
import sys

def read_line():
    return sys.stdin.readline().strip()

def query(a, b, c):
    print(a, b, c, flush=True)
    answer = read_line()
    if answer == "X":
        return a, b
    if answer == "Y":
        return b, c
    return c, a

# CLAUSE: solve_logic
def make_tree(items):
    count = len(items)
    if count == 1:
        return items[0]
    if count == 2:
        edges.append((items[0], items[1]))
        return n + len(edges)

    first = items[0]
    second = items[1]
    left_side = [first]
    right_side = [second]

    for value in items[2:]:
        u, v = query(first, second, value)
        if u == first or v == first:
            left_side.append(value)
        elif u == second or v == second:
            right_side.append(value)
        else:
            left_side.append(value)

    left_root = make_tree(left_side)
    right_root = make_tree(right_side)
    edges.append((left_root, right_root))
    return n + len(edges)

def solve():
    global n, edges
    n = int(read_line())
    edges = []
    root = make_tree([i for i in range(1, n + 1)])

    parent = [0] * (2 * n)
    index = n + 1
    for left, right in edges:
        parent[left] = index
        parent[right] = index
        index += 1
    parent[root] = -1
    return parent

# CLAUSE: finish_program
result = solve()
print(-1, flush=True)
print(" ".join(str(x) for x in result[1:]), flush=True)
