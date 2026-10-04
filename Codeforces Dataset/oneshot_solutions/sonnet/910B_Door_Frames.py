import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, a, b = data[0], data[1], data[2]
    
    pieces = [a, a, a, a, b, b]
    m = len(pieces)
    
    feasible = [False] * (1 << m)
    for mask in range(1 << m):
        total = 0
        for i in range(m):
            if (mask >> i) & 1:
                total += pieces[i]
        feasible[mask] = total <= n
    
    dp = [10**9] * (1 << m)
    dp[0] = 0
    
    for mask in range(1 << m):
        remaining = ((1 << m) - 1) ^ mask
        sub = remaining
        while sub:
            if feasible[sub]:
                dp[mask | sub] = min(dp[mask | sub], dp[mask] + 1)
            sub = (sub - 1) & remaining
    
    print(dp[(1 << m) - 1])

main()
