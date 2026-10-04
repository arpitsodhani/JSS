import sys

sys.setrecursionlimit(100000)

def main():
    data = sys.stdin.read().split()
    idx = 0
    W = int(data[idx])
    idx += 1
    H = int(data[idx])
    idx += 1
    n = int(data[idx])
    idx += 1
    
    breaks = []
    for i in range(n):
        x1 = int(data[idx])
        idx += 1
        y1 = int(data[idx])
        idx += 1
        x2 = int(data[idx])
        idx += 1
        y2 = int(data[idx])
        idx += 1
        breaks.append((x1, y1, x2, y2))
    
    areas = []
    
    def process(x1, y1, x2, y2, available):
        found = False
        for i in available:
            bx1, by1, bx2, by2 = breaks[i]
            
            if bx1 == bx2:  # vertical break
                xc = bx1
                if x1 < xc < x2 and by1 == y1 and by2 == y2:
                    new_available = available - {i}
                    process(x1, y1, xc, y2, new_available)
                    process(xc, y1, x2, y2, new_available)
                    found = True
                    break
            else:  # horizontal break
                yc = by1
                if y1 < yc < y2 and bx1 == x1 and bx2 == x2:
                    new_available = available - {i}
                    process(x1, y1, x2, yc, new_available)
                    process(x1, yc, x2, y2, new_available)
                    found = True
                    break
        
        if not found:
            areas.append((x2 - x1) * (y2 - y1))
    
    process(0, 0, W, H, set(range(n)))
    
    areas.sort()
    print(' '.join(map(str, areas)))

if __name__ == '__main__':
    main()
