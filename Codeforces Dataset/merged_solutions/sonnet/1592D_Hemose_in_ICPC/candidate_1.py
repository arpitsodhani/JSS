# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def query(nodes):
    print("?", len(nodes), *nodes)
    sys.stdout.flush()
    return int(input())

def solve(nodes, target):
    if len(nodes) == 2:
        return nodes
    
    mid = len(nodes) // 2
    left = nodes[:mid]
    right = nodes[mid:]
    
    val_left = query(left)
    if val_left == target:
        return solve(left, target)
    
    val_right = query(right)
    if val_right == target:
        return solve(right, target)
    
    # Target is between left and right
    cand_left = left[:]
    while len(cand_left) > 1:
        m = len(cand_left) // 2
        if query(cand_left[:m] + right) == target:
            cand_left = cand_left[:m]
        else:
            cand_left = cand_left[m:]
    
    node_left = cand_left[0]
    
    cand_right = right[:]
    while len(cand_right) > 1:
        m = len(cand_right) // 2
        if query([node_left] + cand_right[:m]) == target:
            cand_right = cand_right[:m]
        else:
            cand_right = cand_right[m:]
    
    return [node_left, cand_right[0]]

n = int(input())
for _ in range(n - 1):
    input()

all_nodes = list(range(1, n + 1))
M = query(all_nodes)

result = solve(all_nodes, M)
print("!", result[0], result[1])
sys.stdout.flush()

# CLAUSE: finish_program
RESULT_SENTINEL = None
