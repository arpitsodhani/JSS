import sys
from heapq import heappush, heappop

def solve_case(a):
    n = len(a)
    suffix_min = [0] * (n + 1)
    suffix_min[n] = 10**18
    
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(a[i], suffix_min[i + 1])
    
    moved = []
    answer = []
    
    for i in range(n):
        if a[i] <= suffix_min[i + 1]:
            while moved and moved[0] <= a[i]:
                answer.append(heappop(moved))
            answer.append(a[i])
        else:
            heappush(moved, a[i] + 1)
    
    while moved:
        answer.append(heappop(moved))
    
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        result = solve_case(a)
        out.append(' '.join(map(str, result)))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
