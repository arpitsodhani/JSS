import sys
input = sys.stdin.readline

def solve(n, p):
    p = [x - 1 for x in p]  # Convert to 0-indexed
    memo = {}
    
    def dp(pos, marked):
        if pos >= n:
            return 0
        if marked & (1 << pos):  # Current chair is marked
            return 0
        if (pos, marked) in memo:
            return memo[(pos, marked)]
        
        # Option 1: Skip this chair
        res = dp(pos + 1, marked)
        # Option 2: Sit on this chair (mark p[pos])
        res = max(res, 1 + dp(pos + 1, marked | (1 << p[pos])))
        
        memo[(pos, marked)] = res
        return res
    
    return dp(0, 0)

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))
