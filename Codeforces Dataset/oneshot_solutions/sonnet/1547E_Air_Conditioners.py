import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    q = int(input_data[idx])
    idx += 1
    
    for _ in range(q):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        a = []
        for i in range(k):
            a.append(int(input_data[idx]))
            idx += 1
        
        t = []
        for i in range(k):
            t.append(int(input_data[idx]))
            idx += 1
        
        # Initialize result array
        INF = 10**18
        result = [INF] * (n + 1)
        
        # Place air conditioners
        for i in range(k):
            result[a[i]] = min(result[a[i]], t[i])
        
        # Left to right pass
        for i in range(2, n + 1):
            result[i] = min(result[i], result[i-1] + 1)
        
        # Right to left pass
        for i in range(n - 1, 0, -1):
            result[i] = min(result[i], result[i+1] + 1)
        
        print(' '.join(map(str, result[1:])))

main()
