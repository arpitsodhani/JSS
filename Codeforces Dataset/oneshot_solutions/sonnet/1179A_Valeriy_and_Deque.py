import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().decode('utf-8').split()
    idx = 0
    
    n = int(input_data[idx])
    q = int(input_data[idx + 1])
    idx += 2
    
    a = []
    for i in range(n):
        a.append(int(input_data[idx]))
        idx += 1
    
    queries = []
    for i in range(q):
        queries.append(int(input_data[idx]))
        idx += 1
    
    if q == 0:
        return
    
    # Store operations until max reaches front
    operations = []
    dq = deque(a)
    max_val = max(a)
    
    # Simulate until max is at front
    while dq[0] != max_val:
        A = dq.popleft()
        B = dq.popleft()
        operations.append((A, B))
        
        if A > B:
            dq.appendleft(A)
            dq.append(B)
        else:
            dq.appendleft(B)
            dq.append(A)
    
    # Now the max is at front, store the cyclic pattern
    cycle = []
    first = dq[0]
    for i in range(1, n):
        cycle.append((first, dq[i]))
    
    # Answer queries
    for m in queries:
        if m <= len(operations):
            print(operations[m - 1][0], operations[m - 1][1])
        else:
            # Use cyclic pattern
            offset = m - len(operations) - 1
            idx_in_cycle = offset % (n - 1)
            print(cycle[idx_in_cycle][0], cycle[idx_in_cycle][1])

solve()
