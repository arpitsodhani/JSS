import sys
from math import gcd

def solve(n, p, s):
    # Condition 1: p[i+1] divides p[i] for all i
    for i in range(n - 1):
        if p[i] % p[i + 1] != 0:
            return "NO"
    
    # Condition 2: s[i] divides s[i+1] for all i
    for i in range(n - 1):
        if s[i + 1] % s[i] != 0:
            return "NO"
    
    # Condition 3: gcd(p[i], s[i]) is constant for all i
    g = gcd(p[0], s[0])
    for i in range(1, n):
        if gcd(p[i], s[i]) != g:
            return "NO"
    
    # Condition 4: s[0] divides p[0]
    if p[0] % s[0] != 0:
        return "NO"
    
    # Condition 5: p[n-1] divides s[n-1]
    if s[n - 1] % p[n - 1] != 0:
        return "NO"
    
    return "YES"

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        p = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        s = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        results.append(solve(n, p, s))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
