import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        seen = [False] * (n + 1)
        for x in a:
            seen[x] = True
        
        mex = 0
        while seen[mex]:
            mex += 1
        
        cycle = [mex] + a
        shift = k % (n + 1)
        
        if shift:
            cycle = cycle[-shift:] + cycle[:-shift]
        
        out.append(' '.join(map(str, cycle[1:])))
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
