import sys
from bisect import bisect_left, bisect_right

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    m = data[idx + 1]
    k = data[idx + 2]
    idx += 3
    
    roads = []
    for _ in range(m):
        a = data[idx]
        b = data[idx + 1]
        c = data[idx + 2]
        idx += 3
        roads.append((a, b, c))
    
    queries = data[idx:idx + k]
    queries.sort()
    
    total = 0
    for a, b, c in roads:
        left = bisect_left(queries, a)
        right = bisect_right(queries, b)
        
        for i in range(left, right):
            total += c + queries[i] - a
    
    print(total)

if __name__ == "__main__":
    main()
