import sys

data = sys.stdin.buffer.read().decode().strip().split()
n = int(data[0])
a = list(map(int, data[1:n+1]))

if n == 1:
    print(0)
else:
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        max_val = a[i - 1]
        min_val = a[i - 1]
        
        for j in range(i - 1, -1, -1):
            if j < i - 1:
                max_val = max(max_val, a[j])
                min_val = min(min_val, a[j])
            
            dp[i] = max(dp[i], dp[j] + max_val - min_val)
    
    print(dp[n])
