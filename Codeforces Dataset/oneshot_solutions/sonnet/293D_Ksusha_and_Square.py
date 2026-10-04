import sys
from array import array

def ceil_div(a, b):
    return -((-a) // b)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    
    points = []
    idx = 1
    for _ in range(n):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        points.append((x, y))
    
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    offset = -min_x
    width = max_x - min_x + 1
    
    inf = 10 ** 9
    low = array('i', [inf]) * width
    high = array('i', [-inf]) * width
    
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        
        if x1 == x2:
            pos = x1 + offset
            a, b = sorted((y1, y2))
            if a < low[pos]:
                low[pos] = a
            if b > high[pos]:
                high[pos] = b
            continue
        
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        
        dx = x2 - x1
        dy = y2 - y1
        
        for x in range(x1, x2 + 1):
            num = y1 * dx + dy * (x - x1)
            pos = x + offset
            
            bottom = ceil_div(num, dx)
            top = num // dx
            
            if bottom < low[pos]:
                low[pos] = bottom
            if top > high[pos]:
                high[pos] = top
    
    count = 0
    sum_x = 0
    sum_y = 0
    sum_sq = 0
    
    for pos in range(width):
        lo = low[pos]
        hi = high[pos]
        if lo > hi:
            continue
        
        x = pos - offset
        c = hi - lo + 1
        k = c - 1
        
        sy = (lo + hi) * c // 2
        sy2 = c * lo * lo + lo * c * k + k * c * (2 * k + 1) // 6
        
        count += c
        sum_x += x * c
        sum_y += sy
        sum_sq += x * x * c + sy2
    
    total_dist_sq = count * sum_sq - sum_x * sum_x - sum_y * sum_y
    answer = total_dist_sq / (count * (count - 1))
    
    print("{:.10f}".format(answer))

if __name__ == "__main__":
    main()
