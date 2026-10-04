import sys

def group_cost(positions, size):
    total = 0
    m = len(positions)
    
    for start in range(0, m, size):
        mid = start + size // 2
        median = positions[mid]
        
        for i in range(start, start + size):
            total += abs(positions[i] - median)
    
    return total

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    
    positions = []
    for i in range(n):
        if int(data[i + 1]) == 1:
            positions.append(i)
    
    total = len(positions)
    if total == 1:
        print(-1)
        return
    
    factors = []
    x = total
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.append(d)
            while x % d == 0:
                x //= d
        d += 1
    
    if x > 1:
        factors.append(x)
    
    answer = 10 ** 18
    for factor in factors:
        answer = min(answer, group_cost(positions, factor))
    
    print(answer)

if __name__ == "__main__":
    main()
