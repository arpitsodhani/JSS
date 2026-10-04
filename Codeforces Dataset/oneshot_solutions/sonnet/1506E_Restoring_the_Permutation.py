import sys
from bisect import bisect_left

input_data = sys.stdin.read().split()
idx = 0
t = int(input_data[idx])
idx += 1

for _ in range(t):
    n = int(input_data[idx])
    idx += 1
    q = list(map(int, input_data[idx:idx+n]))
    idx += n
    
    # Find positions where we must use q[i]
    used = set()
    p_min = [0] * n
    p_max = [0] * n
    
    # Mark positions where p[i] = q[i]
    for i in range(n):
        if i == 0 or q[i] != q[i-1]:
            p_min[i] = q[i]
            p_max[i] = q[i]
            used.add(q[i])
    
    # For lexicographically minimal
    available = [x for x in range(1, n+1) if x not in used]
    j = 0
    for i in range(n):
        if p_min[i] == 0:
            p_min[i] = available[j]
            j += 1
    
    # For lexicographically maximal
    available = sorted([x for x in range(1, n+1) if x not in used])
    for i in range(n):
        if p_max[i] == 0:
            # Find largest available < q[i] using binary search
            pos = bisect_left(available, q[i]) - 1
            p_max[i] = available[pos]
            available.pop(pos)
    
    print(' '.join(map(str, p_min)))
    print(' '.join(map(str, p_max)))
