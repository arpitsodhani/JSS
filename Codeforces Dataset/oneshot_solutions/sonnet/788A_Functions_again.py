import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:]
    
    best = 0
    cur1 = 0
    cur2 = 0
    
    for i in range(n - 1):
        diff = abs(a[i] - a[i + 1])
        
        if i % 2 == 0:
            x1 = diff
            x2 = -diff
        else:
            x1 = -diff
            x2 = diff
        
        cur1 = max(x1, cur1 + x1)
        cur2 = max(x2, cur2 + x2)
        best = max(best, cur1, cur2)
    
    print(best)

if __name__ == "__main__":
    main()
