import sys
from collections import deque

def operation_a(perm):
    result = perm[:]
    for i in range(0, len(perm), 2):
        result[i], result[i+1] = result[i+1], result[i]
    return result

def operation_b(perm, n):
    result = perm[:]
    for i in range(n):
        result[i], result[i+n] = result[i+n], result[i]
    return result

def solve(n, perm):
    target = tuple(range(1, 2*n + 1))
    perm_tuple = tuple(perm)
    
    if perm_tuple == target:
        return 0
    
    queue = deque([(perm_tuple, 0)])
    visited = {perm_tuple}
    
    while queue:
        current, steps = queue.popleft()
        current_list = list(current)
        
        # Try operation A
        next_a = tuple(operation_a(current_list))
        if next_a == target:
            return steps + 1
        if next_a not in visited:
            visited.add(next_a)
            queue.append((next_a, steps + 1))
        
        # Try operation B
        next_b = tuple(operation_b(current_list, n))
        if next_b == target:
            return steps + 1
        if next_b not in visited:
            visited.add(next_b)
            queue.append((next_b, steps + 1))
    
    return -1

data = sys.stdin.read().split()
n = int(data[0])
perm = list(map(int, data[1:]))
print(solve(n, perm))
