def solve():
    x, n = map(int, input().split())
    min_rollbacks = float('inf')
    
    for _ in range(n):
        a, b, c = map(int, input().split())
        
        # Check if this jump type is usable (won't go negative on first rollback)
        if (b - 1) * a < c:
            continue
        
        # Check if we can reach x with 0 rollbacks
        if x <= (b - 1) * a:
            min_rollbacks = 0
            continue
        
        # Calculate D = b*a - c (net progress per b jumps)
        D = b * a - c
        
        # If D <= 0, we can't make progress beyond (b-1)*a
        if D <= 0:
            continue
        
        # Calculate minimum rollbacks needed
        # We need: r * D + (b-1) * a >= x
        # So: r >= (x - (b-1)*a) / D
        numerator = x - (b - 1) * a
        r = (numerator + D - 1) // D  # Ceiling division
        min_rollbacks = min(min_rollbacks, r)
    
    if min_rollbacks == float('inf'):
        print(-1)
    else:
        print(min_rollbacks)

t = int(input())
for _ in range(t):
    solve()
