import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().strip().split()
    idx = 0
    
    n = int(data[idx]); idx += 1
    a = int(data[idx]); idx += 1
    b = int(data[idx]); idx += 1
    
    Ax, Ay = int(data[idx]), int(data[idx+1]); idx += 2
    Bx, By = int(data[idx]), int(data[idx+1]); idx += 2
    
    trenches = []
    for _ in range(n):
        x1, y1, x2, y2 = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        trenches.append(((x1, y1), (x2, y2)))
    
    A, B = (Ax, Ay), (Bx, By)
    
    def dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def in_trench(p):
        for (p1, p2) in trenches:
            if p1[0] == p2[0]:  # vertical
                if p[0] == p1[0] and min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1]):
                    return True
            else:  # horizontal
                if p[1] == p1[1] and min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]):
                    return True
        return False
    
    # Collect key points
    points = [A, B]
    for t in trenches:
        points.append(t[0])
        points.append(t[1])
    
    # Dijkstra
    pq = [(0.0, A)]
    best = {}
    MAX_CYCLES = 2000
    
    while pq:
        time, pos = heappop(pq)
        
        if pos == B:
            print(f"{time:.10f}")
            return
        
        cycle = int(time // (a + b))
        if cycle > MAX_CYCLES:
            break
        
        state = (pos, cycle)
        if state in best:
            continue
        best[state] = time
        
        phase_time = time % (a + b)
        
        if phase_time < a:
            # Charging phase - can move
            remaining = a - phase_time
            
            for npos in points:
                if npos == pos:
                    continue
                
                d = dist(pos, npos)
                if d <= remaining:
                    heappush(pq, (time + d, npos))
            
            # If in trench, can wait through shooting
            if in_trench(pos):
                heappush(pq, (time + remaining + b, pos))
        else:
            # Shooting phase - can only wait if in trench
            if in_trench(pos):
                remaining = (a + b) - phase_time
                heappush(pq, (time + remaining, pos))
    
    print(-1)

solve()
