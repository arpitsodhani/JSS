import sys
import heapq

def solve_case(n, m, a):
    ans = 0
    
    total = 0
    positives = []
    for i in range(m - 1, 0, -1):
        total += a[i]
        if a[i] > 0:
            heapq.heappush(positives, -a[i])
        
        while total > 0:
            x = -heapq.heappop(positives)
            total -= 2 * x
            ans += 1
    
    total = 0
    negatives = []
    for i in range(m, n):
        total += a[i]
        if a[i] < 0:
            heapq.heappush(negatives, a[i])
        
        while total < 0:
            x = heapq.heappop(negatives)
            total -= 2 * x
            ans += 1
    
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        out.append(str(solve_case(n, m, a)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
