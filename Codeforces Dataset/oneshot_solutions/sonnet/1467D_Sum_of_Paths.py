import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    k = int(input_data[idx + 1])
    q = int(input_data[idx + 2])
    idx += 3
    
    a = [0] + [int(input_data[idx + i]) for i in range(n)]  # 1-indexed
    idx += n
    
    MOD = 10**9 + 7
    
    # left[t][i] = number of ways to reach position i in exactly t moves
    left = [[0] * (n + 2) for _ in range(k + 1)]
    for i in range(1, n + 1):
        left[0][i] = 1
    
    for t in range(1, k + 1):
        for i in range(1, n + 1):
            if i > 1:
                left[t][i] = (left[t][i] + left[t-1][i-1]) % MOD
            if i < n:
                left[t][i] = (left[t][i] + left[t-1][i+1]) % MOD
    
    # right[t][i] = number of ways to complete t moves starting from position i
    right = [[0] * (n + 2) for _ in range(k + 1)]
    for i in range(1, n + 1):
        right[0][i] = 1
    
    for t in range(1, k + 1):
        for i in range(1, n + 1):
            if i > 1:
                right[t][i] = (right[t][i] + right[t-1][i-1]) % MOD
            if i < n:
                right[t][i] = (right[t][i] + right[t-1][i+1]) % MOD
    
    # count[i] = total number of times cell i appears across all paths
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        for t in range(k + 1):
            count[i] = (count[i] + left[t][i] * right[k - t][i] % MOD) % MOD
    
    # Initial sum
    total = 0
    for i in range(1, n + 1):
        total = (total + a[i] * count[i] % MOD) % MOD
    
    # Process queries
    for _ in range(q):
        pos = int(input_data[idx])
        val = int(input_data[idx + 1])
        idx += 2
        
        # Update sum: remove old contribution, add new contribution
        total = (total - a[pos] * count[pos] % MOD + MOD) % MOD
        a[pos] = val
        total = (total + a[pos] * count[pos] % MOD) % MOD
        
        print(total)

solve()
