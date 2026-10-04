import sys

def solve(n, k):
    # Check if it's possible
    if n < 2**(k-1):
        return -1
    
    # Construction: [m, m-1, ..., 1, m+1, ..., n]
    m = n - 2**(k-1) + 1
    
    # First part: [m, m-1, ..., 1] (decreasing)
    # Second part: [m+1, ..., n] (increasing)
    result = list(range(m, 0, -1)) + list(range(m+1, n+1))
    
    return result

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        result = solve(n, k)
        if result == -1:
            print(-1)
        else:
            print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
