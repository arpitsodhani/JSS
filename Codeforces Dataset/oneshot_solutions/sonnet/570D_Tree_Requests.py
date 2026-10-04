import sys
from bisect import bisect_left, bisect_right

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    head = [-1] * (n + 1)
    to = [0] * (n + 1)
    nxt = [0] * (n + 1)
    depth = [0] * (n + 1)
    depth[1] = 1
    
    for v in range(2, n + 1):
        p = int(data[idx])
        idx += 1
        depth[v] = depth[p] + 1
        to[v] = v
        nxt[v] = head[p]
        head[p] = v
    
    letters = data[idx]
    idx += 1
    
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    by_depth = [None] * (n + 2)
    pref = [None] * (n + 2)
    
    timer = 0
    stack = [(1, 0)]
    
    while stack:
        v, state = stack.pop()
        
        if state == 0:
            timer += 1
            tin[v] = timer
            
            d = depth[v]
            if by_depth[d] is None:
                by_depth[d] = []
                pref[d] = [0]
            
            by_depth[d].append(timer)
            mask = 1 << (letters[v - 1] - 97)
            pref[d].append(pref[d][-1] ^ mask)
            
            stack.append((v, 1))
            child = head[v]
            while child != -1:
                stack.append((to[child], 0))
                child = nxt[child]
        else:
            tout[v] = timer
    
    ans = []
    for _ in range(m):
        v = int(data[idx])
        h = int(data[idx + 1])
        idx += 2
        
        if h > n or by_depth[h] is None:
            ans.append("Yes")
            continue
        
        arr = by_depth[h]
        left = bisect_left(arr, tin[v])
        right = bisect_right(arr, tout[v])
        mask = pref[h][right] ^ pref[h][left]
        
        if mask & (mask - 1):
            ans.append("No")
        else:
            ans.append("Yes")
    
    sys.stdout.write('\n'.join(ans))

if __name__ == "__main__":
    main()
