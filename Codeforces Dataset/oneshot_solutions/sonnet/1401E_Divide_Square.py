import sys

LIMIT = 1000000

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)
    
    def add(self, idx, val):
        idx += 1
        while idx <= self.n + 1:
            self.bit[idx] += val
            idx += idx & -idx
    
    def sum(self, idx):
        idx += 1
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result
    
    def range_sum(self, left, right):
        if left > right:
            return 0
        return self.sum(right) - (self.sum(left - 1) if left > 0 else 0)

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    horizontals = []
    full_horizontal = 0
    
    for _ in range(n):
        y = int(data[idx])
        x1 = int(data[idx + 1])
        x2 = int(data[idx + 2])
        idx += 3
        
        if x1 == 0 and x2 == LIMIT:
            full_horizontal += 1
        horizontals.append((y, x1, x2))
    
    events = []
    answer = 1 + full_horizontal
    
    for _ in range(m):
        x = int(data[idx])
        y1 = int(data[idx + 1])
        y2 = int(data[idx + 2])
        idx += 3
        
        if y1 == 0 and y2 == LIMIT:
            answer += 1
            events.append((x, 0, y1, y2))
    
    for y, x1, x2 in horizontals:
        events.append((x1, 1, y, 0))
        events.append((x2, -1, y, 0))
    
    events.sort(key=lambda e: (e[0], e[1]))
    
    bit = Fenwick(LIMIT + 1)
    
    for _, typ, a, b in events:
        if typ == 1:
            bit.add(a, 1)
        elif typ == -1:
            bit.add(a, -1)
        else:
            answer += bit.range_sum(a, b)
    
    print(answer)

if __name__ == "__main__":
    main()
