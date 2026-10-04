import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    n = int(input_data[0])
    k = int(input_data[1])
    a = list(map(int, input_data[2:2+n]))
    
    # For each possible target, store the operations needed to reach it from each element
    target_ops = defaultdict(list)
    
    for num in a:
        ops = 0
        current = num
        while True:
            target_ops[current].append(ops)
            if current == 0:
                break
            current //= 2
            ops += 1
    
    min_operations = float('inf')
    
    for target, ops_list in target_ops.items():
        if len(ops_list) >= k:
            # Sort and take the k smallest
            ops_list.sort()
            total = sum(ops_list[:k])
            min_operations = min(min_operations, total)
    
    print(min_operations)

solve()
