def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Find left and right positions for each value
    left = {}
    right = {}
    for i in range(n):
        v = a[i]
        if v not in left:
            left[v] = i
        right[v] = i
    
    # Get distinct values in sorted order
    distinct = sorted(left.keys())
    k = len(distinct)
    
    if k == 0:
        return 0
    
    # DP to find longest chain
    dp = [1] * k
    for i in range(1, k):
        for j in range(i):
            if right[distinct[j]] < left[distinct[i]]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    max_chain = max(dp)
    return k - max_chain

q = int(input())
for _ in range(q):
    print(solve())
