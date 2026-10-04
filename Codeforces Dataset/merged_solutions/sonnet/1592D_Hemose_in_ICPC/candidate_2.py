# CLAUSE: setup_environment
import sys

def query(nodes):
    print("?", len(nodes), *nodes)
    sys.stdout.flush()
    return int(input())

# CLAUSE: solve_logic
def solve(nodes, target):
    if len(nodes) == 2:
        return nodes

    mid = len(nodes) // 2
    left = nodes[:mid]
    right = nodes[mid:]

    if query(left) == target:
        return solve(left, target)

    if query(right) == target:
        return solve(right, target)

    left_pool = left[:]
    while len(left_pool) > 1:
        cut = len(left_pool) // 2
        probe = left_pool[:cut]
        if query(probe + right) == target:
            left_pool = probe
        else:
            left_pool = left_pool[cut:]

    fixed_left = left_pool[0]
    right_pool = right[:]
    while len(right_pool) > 1:
        cut = len(right_pool) // 2
        probe = right_pool[:cut]
        if query([fixed_left] + probe) == target:
            right_pool = probe
        else:
            right_pool = right_pool[cut:]

    return [fixed_left, right_pool[0]]

n = int(input())
for _ in range(n - 1):
    input()

nodes = list(range(1, n + 1))
maximum = query(nodes)
answer = solve(nodes, maximum)

# CLAUSE: finish_program
print("!", answer[0], answer[1])
sys.stdout.flush()
