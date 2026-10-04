import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    k = int(input_data[idx])
    idx += 1
    
    f = []
    for i in range(n):
        f.append(int(input_data[idx]))
        idx += 1
    
    w = []
    for i in range(n):
        w.append(int(input_data[idx]))
        idx += 1
    
    # Binary lifting
    # dp[i][j] = (next_vertex, sum, min_weight) after 2^j steps from vertex i
    max_log = k.bit_length()
    INF = 10**18
    dp = [[(0, 0, INF) for _ in range(max_log + 1)] for _ in range(n)]
    
    # Base case: 2^0 = 1 step
    for i in range(n):
        dp[i][0] = (f[i], w[i], w[i])
    
    # Fill the table
    for j in range(1, max_log + 1):
        for i in range(n):
            next_v, sum1, min1 = dp[i][j-1]
            next_v2, sum2, min2 = dp[next_v][j-1]
            dp[i][j] = (next_v2, sum1 + sum2, min(min1, min2))
    
    # For each vertex, compute path of length k
    result = []
    for i in range(n):
        curr_v = i
        total_sum = 0
        total_min = INF
        
        for j in range(max_log + 1):
            if k & (1 << j):
                next_v, sum_val, min_val = dp[curr_v][j]
                total_sum += sum_val
                total_min = min(total_min, min_val)
                curr_v = next_v
        
        result.append(str(total_sum))
        result.append(str(total_min))
    
    print(' '.join(result))

solve()
