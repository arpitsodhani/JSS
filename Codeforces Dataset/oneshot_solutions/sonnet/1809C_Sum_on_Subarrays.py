import sys

def solve(n, k):
    # Find the largest m such that m*(m+1)/2 <= k
    m = 0
    while m * (m + 1) // 2 < k:
        m += 1
    if m * (m + 1) // 2 > k:
        m -= 1
    
    r = k - m * (m + 1) // 2
    
    result = [1] * m
    
    if r > 0 and len(result) < n:
        result.append(-m + r)
    
    while len(result) < n:
        result.append(-1000)
    
    return result

def main():
    data = sys.stdin.read().strip().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        result = solve(n, k)
        print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()
