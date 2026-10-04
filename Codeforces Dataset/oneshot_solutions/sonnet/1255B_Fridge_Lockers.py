import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    if n < 3 or m < n:
        print(-1)
        return
    
    # Find indices of two smallest weights
    indexed_a = [(a[i], i) for i in range(n)]
    indexed_a.sort()
    
    min1_idx = indexed_a[0][1]
    min2_idx = indexed_a[1][1]
    
    # Calculate cost
    total_sum = sum(a)
    cost = 2 * total_sum + (m - n) * (indexed_a[0][0] + indexed_a[1][0])
    
    print(cost)
    
    # Create cycle 1-2-3-...-n-1
    for i in range(1, n + 1):
        next_i = i % n + 1
        print(i, next_i)
    
    # Add m - n additional chains connecting min1_idx and min2_idx (1-indexed)
    for _ in range(m - n):
        print(min1_idx + 1, min2_idx + 1)

t = int(input())
for _ in range(t):
    solve()
