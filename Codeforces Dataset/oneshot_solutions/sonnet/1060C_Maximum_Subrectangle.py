import sys

def solve():
    lines = sys.stdin.read().strip().split('\n')
    
    n, m = map(int, lines[0].split())
    a = list(map(int, lines[1].split()))
    b = list(map(int, lines[2].split()))
    x = int(lines[3])
    
    # Compute prefix sums
    prefix_a = [0] * (n + 1)
    for i in range(n):
        prefix_a[i + 1] = prefix_a[i] + a[i]
    
    prefix_b = [0] * (m + 1)
    for i in range(m):
        prefix_b[i + 1] = prefix_b[i] + b[i]
    
    # Compute min_sum_a: minimum sum of subarray of each length
    min_sum_a = [float('inf')] * (n + 1)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            s = prefix_a[start + length] - prefix_a[start]
            min_sum_a[length] = min(min_sum_a[length], s)
    
    # Compute min_sum_b: minimum sum of subarray of each length
    min_sum_b = [float('inf')] * (m + 1)
    for length in range(1, m + 1):
        for start in range(m - length + 1):
            s = prefix_b[start + length] - prefix_b[start]
            min_sum_b[length] = min(min_sum_b[length], s)
    
    # Find maximum area
    max_area = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if min_sum_a[i] * min_sum_b[j] <= x:
                max_area = max(max_area, i * j)
    
    print(max_area)

solve()
