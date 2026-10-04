import sys

def main():
    k = int(sys.stdin.readline())
    
    if k % 2 == 0:
        print("NO")
        return
    
    half = k + 2
    n = 2 * half
    edges = []
    
    for base in (0, half):
        special = base + 1
        
        for i in range(base + 1, base + half + 1):
            for j in range(i + 1, base + half + 1):
                edges.append((i, j))
        
        remove = set()
        remove.add((special, base + 2))
        remove.add((special, base + 3))
        
        cur = base + 4
        while cur <= base + half:
            remove.add((cur, cur + 1))
            cur += 2
        
        edges = [e for e in edges if e not in remove]
    
    edges.append((1, half + 1))
    
    print("YES")
    print(n, len(edges))
    for u, v in edges:
        print(u, v)

if __name__ == "__main__":
    main()
