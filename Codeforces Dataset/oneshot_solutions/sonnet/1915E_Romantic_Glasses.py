def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    seen = {0}  # Track seen prefix differences
    diff = 0
    
    for i in range(n):
        if i % 2 == 0:  # i+1 is odd (1-indexed)
            diff += a[i]
        else:  # i+1 is even (1-indexed)
            diff -= a[i]
        
        if diff in seen:
            return "YES"
        seen.add(diff)
    
    return "NO"

t = int(input())
for _ in range(t):
    print(solve())
