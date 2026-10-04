import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx + 1])
        idx += 2
        
        a = []
        for i in range(n):
            a.append(int(input_data[idx]))
            idx += 1
        
        # Compute maxSum[len] for each length
        maxSum = [-float('inf')] * (n + 1)
        maxSum[0] = 0  # empty subarray
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += a[j]
                length = j - i + 1
                maxSum[length] = max(maxSum[length], current_sum)
        
        # Compute f(k) for each k
        result = []
        for k in range(n + 1):
            f_k = 0  # at least the empty subarray
            for length in range(1, n + 1):
                contribution = maxSum[length] + min(k, length) * x
                f_k = max(f_k, contribution)
            result.append(f_k)
        
        print(' '.join(map(str, result)))

solve()
