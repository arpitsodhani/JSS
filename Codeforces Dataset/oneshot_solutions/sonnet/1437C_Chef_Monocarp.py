def solve():
    n = int(input())
    t = list(map(int, input().split()))
    t.sort()
    
    MAX_TIME = 600
    INF = 10**9
    
    prev = [INF] * (MAX_TIME + 1)
    prev[0] = 0
    
    for i in range(n):
        curr = [INF] * (MAX_TIME + 1)
        min_prev = INF
        for j in range(1, MAX_TIME + 1):
            min_prev = min(min_prev, prev[j-1])
            curr[j] = min_prev + abs(t[i] - j)
        prev = curr
    
    return min(prev)

T = int(input())
for _ in range(T):
    print(solve())
