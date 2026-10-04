import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        s = list(data[idx])
        idx += 1
        
        count = 0
        i = 0
        while i <= n - m:
            # Check if s[i:i+m] is all 0s
            if all(s[j] == '0' for j in range(i, i + m)):
                # Apply Timar at position p
                p = min(i + m - 1, n - k)
                for j in range(p, min(p + k, n)):
                    s[j] = '1'
                count += 1
                i = p + k  # Skip ahead
            else:
                i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

solve()
