import sys
import math

def solve():
    n, k = map(int, input().split())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    def can_cover(r):
        if r < 1e-9:
            count = sum(1 for x, y in points if x*x + y*y < 1e-18)
            return count >= k
        
        intervals = []
        for x, y in points:
            d = math.sqrt(x*x + y*y)
            if d > 2 * r + 1e-9:
                continue
            
            if d < 1e-9:
                cnt = sum(1 for x2, y2 in points if math.sqrt(x2*x2 + y2*y2) <= 2*r + 1e-9)
                return cnt >= k
            
            beta = math.atan2(y, x)
            cos_half = min(1.0, d / (2 * r))
            half_angle = math.acos(cos_half)
            
            left = beta - half_angle
            right = beta + half_angle
            
            span = right - left
            if span >= 2 * math.pi - 1e-9:
                return True
            
            left = (left % (2 * math.pi) + 2 * math.pi) % (2 * math.pi)
            right = left + span
            
            if right >= 2 * math.pi:
                intervals.append((left, 2 * math.pi))
                intervals.append((0, right - 2 * math.pi))
            else:
                intervals.append((left, right))
        
        if len(intervals) < k:
            return False
        
        events = []
        for left, right in intervals:
            events.append((left, 1))
            events.append((right, -1))
        
        events.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        for _, delta in events:
            count += delta
            if count >= k:
                return True
        
        return False
    
    left, right = 0.0, 2e5
    for _ in range(100):
        mid = (left + right) / 2
        if can_cover(mid):
            right = mid
        else:
            left = mid
    
    print(f"{right:.10f}")

solve()
