import sys
from math import gcd
from collections import defaultdict

def normalize_direction(dy, dx):
    if dx == 0:
        return (1, 0)  # Vertical line
    if dx < 0:
        dx = -dx
        dy = -dy
    g = gcd(abs(dy), abs(dx))
    return (dy // g, dx // g)

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    flamingos = []
    for _ in range(m):
        x = int(input_data[idx])
        idx += 1
        y = int(input_data[idx])
        idx += 1
        flamingos.append((x, y))
    
    total = 0
    
    for i in range(1, n + 1):
        direction_count = defaultdict(int)
        
        for x, y in flamingos:
            dx = x - i
            dy = y
            direction = normalize_direction(dy, dx)
            direction_count[direction] += 1
        
        if direction_count:
            total += max(direction_count.values())
    
    print(total)

if __name__ == "__main__":
    main()
