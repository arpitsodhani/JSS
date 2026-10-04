import sys
from collections import defaultdict

def solve_case(n, a):
    positions = defaultdict(list)
    for i, value in enumerate(a):
        positions[value].append(i)
    
    groups = sorted(positions.values(), key=len, reverse=True)
    order = []
    for group in groups:
        order.extend(group)
    
    shift = len(groups[0])
    b = [0] * n
    
    for i in range(n):
        b[order[i]] = a[order[(i + shift) % n]]
    
    return b

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        b = solve_case(n, a)
        out.append(' '.join(map(str, b)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
