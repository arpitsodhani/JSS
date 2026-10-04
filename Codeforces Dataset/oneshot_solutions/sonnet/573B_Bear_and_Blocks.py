import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    h = data[1:1 + n]
    
    if n == 1:
        print(1)
        return
    
    h[0] = 1
    h[-1] = 1
    
    for i in range(1, n):
        h[i] = min(h[i], h[i - 1] + 1)
    
    for i in range(n - 2, -1, -1):
        h[i] = min(h[i], h[i + 1] + 1)
    
    print(max(h))

if __name__ == "__main__":
    main()
