import sys

def min_max_digit(x):
    mn = 9
    mx = 0
    
    while x > 0:
        d = x % 10
        mn = min(mn, d)
        mx = max(mx, d)
        x //= 10
    
    return mn, mx

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    result = []
    
    for _ in range(t):
        a = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        for _ in range(k - 1):
            mn, mx = min_max_digit(a)
            if mn == 0:
                break
            a += mn * mx
        
        result.append(str(a))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
