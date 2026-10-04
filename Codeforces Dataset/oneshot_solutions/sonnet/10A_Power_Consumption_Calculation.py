def solve():
    n, P1, P2, P3, T1, T2 = map(int, input().split())
    
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    
    total_power = 0
    
    # Power during active periods
    for l, r in intervals:
        total_power += (r - l) * P1
    
    # Power during idle periods between intervals
    for i in range(n - 1):
        idle_duration = intervals[i + 1][0] - intervals[i][1]
        
        if idle_duration <= T1:
            total_power += idle_duration * P1
        elif idle_duration <= T1 + T2:
            total_power += T1 * P1
            total_power += (idle_duration - T1) * P2
        else:
            total_power += T1 * P1
            total_power += T2 * P2
            total_power += (idle_duration - T1 - T2) * P3
    
    print(total_power)

solve()
