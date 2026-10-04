def solve():
    n = int(input())
    x = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    result = 0
    
    for j in range(n):
        A_j = sum(x[i] & x[j] for i in range(n)) % MOD
        B_j = sum(x[j] | x[k] for k in range(n)) % MOD
        result = (result + A_j * B_j) % MOD
    
    return result

t = int(input())
for _ in range(t):
    print(solve())
