import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n, m, q = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        idx += 3
        
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        b = [int(data[idx + i]) for i in range(m)]
        idx += m
        
        # Sort in descending order to pick largest cards
        a.sort(reverse=True)
        b.sort(reverse=True)
        
        # Compute prefix sums for efficient range sum queries
        prefix_a = [0]
        for val in a:
            prefix_a.append(prefix_a[-1] + val)
        
        prefix_b = [0]
        for val in b:
            prefix_b.append(prefix_b[-1] + val)
        
        for _ in range(q):
            x, y, z = int(data[idx]), int(data[idx+1]), int(data[idx+2])
            idx += 3
            
            # Try all valid values of v (number of cards from Vadim)
            # We need: v + k = z, where k is cards from Kostya
            # Constraints: 0 <= v <= min(x, n, z) and 0 <= k = z - v <= min(y, m)
            # So: max(0, z - y, z - m) <= v <= min(x, n, z)
            v_min = max(0, z - y, z - m)
            v_max = min(x, n, z)
            
            max_sum = -10**18
            
            for v in range(v_min, v_max + 1):
                k = z - v
                current_sum = prefix_a[v] + prefix_b[k]
                max_sum = max(max_sum, current_sum)
            
            print(max_sum)

solve()
