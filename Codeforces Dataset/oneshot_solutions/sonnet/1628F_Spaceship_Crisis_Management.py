import sys
import heapq
from math import gcd

EPS = 1e-10

def norm_dir(x, y):
    g = gcd(abs(x), abs(y))
    x //= g
    y //= g
    return (x, y)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    segments = []
    directions = set()
    
    for _ in range(n):
        ax, ay, bx, by = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
        idx += 4
        segments.append((ax, ay, bx, by))
        directions.add(norm_dir(ax, ay))
        directions.add(norm_dir(bx, by))
    
    q = data[idx]
    idx += 1
    
    queries = []
    for _ in range(q):
        x, y = data[idx], data[idx + 1]
        idx += 2
        queries.append((x, y))
        directions.add(norm_dir(x, y))
    
    answer = [False] * q
    
    for ux, uy in directions:
        transformed_segments = []
        y_values = {0}
        
        for ax, ay, bx, by in segments:
            x1 = ux * ax + uy * ay
            y1 = ux * ay - uy * ax
            x2 = ux * bx + uy * by
            y2 = ux * by - uy * bx
            
            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            
            transformed_segments.append((x1, y1, x2, y2))
            y_values.add(y1)
            y_values.add(y2)
        
        transformed_queries = []
        for qi, (x, y) in enumerate(queries):
            tx = ux * x + uy * y
            ty = ux * y - uy * x
            transformed_queries.append((tx, ty, qi))
            y_values.add(ty)
        
        y_list = sorted(y_values)
        y_id = {v: i for i, v in enumerate(y_list)}
        reachable = [False] * len(y_list)
        reachable[y_id[0]] = True
        
        starts = []
        for x1, y1, x2, y2 in transformed_segments:
            starts.append((x1, y1, x2, y2))
        starts.sort()
        
        events = []
        for tx, ty, qi in transformed_queries:
            if tx >= 0:
                events.append((tx, ty, qi))
        events.sort()
        
        heap = []
        si = 0
        ei = 0
        
        def apply_until(limit):
            while heap and heap[0][0] <= limit + EPS:
                _, yi, value = heapq.heappop(heap)
                reachable[yi] = value
        
        all_x = sorted(set([x for x, _, _ in events] + [s[0] for s in starts]))
        
        for current_x in all_x:
            apply_until(current_x)
            
            while si < len(starts) and starts[si][0] == current_x:
                x1, y1, x2, y2 = starts[si]
                si += 1
                
                dy = abs(y2 - y1)
                dx = x2 - x1
                can_slide = dx > dy
                active = can_slide and reachable[y_id[y1]]
                
                lo, hi = sorted((y1, y2))
                left = lower_bound(y_list, lo)
                right = upper_bound(y_list, hi)
                
                if y1 == y2:
                    for pos in range(left, right):
                        heapq.heappush(heap, (float(x1), pos, active))
                else:
                    for pos in range(left, right):
                        y = y_list[pos]
                        cross_x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
                        if cross_x >= current_x - EPS:
                            heapq.heappush(heap, (cross_x, pos, active))
            
            apply_until(current_x)
            
            while ei < len(events) and events[ei][0] == current_x:
                _, ty, qi = events[ei]
                ei += 1
                if reachable[y_id[ty]]:
                    answer[qi] = True
    
    print('\n'.join("YES" if x else "NO" for x in answer))

def lower_bound(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m
    return l

if __name__ == "__main__":
    main()
