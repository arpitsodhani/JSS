import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    r = int(data[1])
    x = list(map(int, data[2:2 + n]))
    
    y = []
    diameter = 2 * r
    
    for i in range(n):
        cur_y = float(r)
        
        for j in range(i):
            dx = abs(x[i] - x[j])
            if dx <= diameter:
                cur_y = max(cur_y, y[j] + math.sqrt(diameter * diameter - dx * dx))
        
        y.append(cur_y)
    
    print(' '.join(map(str, y)))

if __name__ == "__main__":
    main()
