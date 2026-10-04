import sys
from bisect import bisect_right

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        a.sort()
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        
        possible = set()
        
        def add_segments(l, r):
            total = prefix[r + 1] - prefix[l]
            possible.add(total)
            
            if a[l] == a[r]:
                return
            
            mid = (a[l] + a[r]) // 2
            split = bisect_right(a, mid, l, r + 1)
            
            if split > l:
                add_segments(l, split - 1)
            if split <= r:
                add_segments(split, r)
        
        add_segments(0, n - 1)
        
        for _ in range(q):
            s = data[idx]
            idx += 1
            out.append("Yes" if s in possible else "No")
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
