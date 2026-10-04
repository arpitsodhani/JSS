import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    
    p = data[0]
    q = data[1]
    n = data[2]
    a = data[3:]
    
    for i in range(n):
        if q == 0:
            print("NO")
            return
        
        whole = p // q
        if whole != a[i]:
            print("NO")
            return
        
        p %= q
        
        if i == n - 1:
            print("YES" if p == 0 else "NO")
            return
        
        if p == 0:
            print("NO")
            return
        
        p, q = q, p

if __name__ == "__main__":
    main()
