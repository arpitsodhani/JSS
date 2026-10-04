import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    idx = 1
    
    current = {}
    positions = set()
    
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        
        va = current.get(a, a)
        vb = current.get(b, b)
        current[a] = vb
        current[b] = va
        
        positions.add(a)
        positions.add(b)
    
    coords = sorted(positions)
    m = len(coords)
    
    values = [current.get(x, x) for x in coords]
    
    bit = [0] * (m + 2)
    
    def add(pos, val):
        while pos <= m:
            bit[pos] += val
            pos += pos & -pos
    
    def query(pos):
        total = 0
        while pos > 0:
            total += bit[pos]
            pos -= pos & -pos
        return total
    
    answer = 0
    
    for i, val in enumerate(values):
        rank = bisect_left(coords, val) + 1
        answer += i - query(rank)
        add(rank, 1)
    
    for x, val in zip(coords, values):
        if x < val:
            touched_between = bisect_left(coords, val) - bisect_left(coords, x) - 1
            answer += val - x - 1 - touched_between
        elif val < x:
            touched_between = bisect_left(coords, x) - bisect_left(coords, val) - 1
            answer += x - val - 1 - touched_between
    
    print(answer)

if __name__ == "__main__":
    main()
