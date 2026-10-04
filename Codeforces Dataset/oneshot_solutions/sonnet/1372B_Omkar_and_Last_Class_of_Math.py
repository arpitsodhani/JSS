import sys

def smallest_factor(n):
    if n % 2 == 0:
        return 2
    
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    
    return n

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    
    result = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        p = smallest_factor(n)
        a = n // p
        b = n - a
        result.append(f"{a} {b}")
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
