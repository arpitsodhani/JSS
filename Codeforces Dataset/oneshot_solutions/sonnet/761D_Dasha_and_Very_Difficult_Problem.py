import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    idx = 0
    n = data[idx]
    l = data[idx + 1]
    r = data[idx + 2]
    idx += 3
    
    a = data[idx:idx + n]
    idx += n
    
    p = data[idx:idx + n]
    
    order = sorted(range(n), key=lambda i: p[i])
    c = [0] * n
    
    previous = -10**30
    for i in order:
        low = l - a[i]
        high = r - a[i]
        
        value = max(low, previous + 1)
        if value > high:
            print(-1)
            return
        
        c[i] = value
        previous = value
    
    b = [a[i] + c[i] for i in range(n)]
    print(' '.join(map(str, b)))

if __name__ == "__main__":
    main()
