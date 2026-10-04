import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:]
    
    by_height = {}
    for i, h in enumerate(a):
        by_height.setdefault(h, []).append(i)
    
    active = [False] * n
    parent = list(range(n))
    size = [1] * n
    
    odd_segments = 0
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        nonlocal odd_segments
        
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return
        
        if size[rx] < size[ry]:
            rx, ry = ry, rx
        
        if size[rx] % 2 == 1:
            odd_segments -= 1
        if size[ry] % 2 == 1:
            odd_segments -= 1
        
        parent[ry] = rx
        size[rx] += size[ry]
        
        if size[rx] % 2 == 1:
            odd_segments += 1
    
    heights = sorted(by_height)
    
    for h in heights[:-1]:
        for pos in by_height[h]:
            active[pos] = True
            odd_segments += 1
            
            if pos > 0 and active[pos - 1]:
                union(pos, pos - 1)
            if pos + 1 < n and active[pos + 1]:
                union(pos, pos + 1)
        
        if odd_segments > 0:
            print("NO")
            return
    
    print("YES")

if __name__ == "__main__":
    main()
