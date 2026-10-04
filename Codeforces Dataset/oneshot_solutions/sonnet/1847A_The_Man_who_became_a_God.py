import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    results = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        diffs = []
        total = 0
        for i in range(n - 1):
            d = abs(a[i] - a[i + 1])
            diffs.append(d)
            total += d
        
        diffs.sort(reverse=True)
        results.append(str(total - sum(diffs[:k - 1])))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
