import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = data[idx:idx + n]
        idx += n
        
        seen = set(a)
        mex = 0
        while mex in seen:
            mex += 1
        
        if mex == 0:
            out.append("YES" if n == 1 else "NO")
            continue
        
        count = [0] * mex
        for x in a:
            if x < mex:
                count[x] += 1
        
        if min(count) == 1:
            out.append("YES")
        else:
            out.append("NO")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
