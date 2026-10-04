import sys

def main():
    n, d, h = map(int, sys.stdin.read().split())
    
    if d < h or d > 2 * h:
        print(-1)
        return
    
    if d == 1:
        if n == 2 and h == 1:
            print(1, 2)
        else:
            print(-1)
        return
    
    edges = []
    current = 2
    
    last = 1
    for _ in range(h):
        edges.append((last, current))
        last = current
        current += 1
    
    if d > h:
        last = 1
        for _ in range(d - h):
            edges.append((last, current))
            last = current
            current += 1
        
        while current <= n:
            edges.append((1, current))
            current += 1
    else:
        while current <= n:
            edges.append((2, current))
            current += 1
    
    if len(edges) != n - 1:
        print(-1)
        return
    
    print('\n'.join(f"{a} {b}" for a, b in edges))

if __name__ == "__main__":
    main()
