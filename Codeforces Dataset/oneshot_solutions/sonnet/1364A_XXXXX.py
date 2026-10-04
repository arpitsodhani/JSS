import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        idx += 2
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        total = sum(a)
        if total % x != 0:
            results.append(str(n))
            continue
        
        first = -1
        last = -1
        
        for i in range(n):
            if a[i] % x != 0:
                if first == -1:
                    first = i
                last = i
        
        if first == -1:
            results.append("-1")
        else:
            results.append(str(max(n - first - 1, last)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
