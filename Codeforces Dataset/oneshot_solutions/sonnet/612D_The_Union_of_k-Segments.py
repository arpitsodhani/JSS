import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    
    events = []
    idx = 2
    for _ in range(n):
        l = data[idx]
        r = data[idx + 1]
        idx += 2
        events.append((l, 1))
        events.append((r, -1))
    
    events.sort(key=lambda x: (x[0], -x[1]))
    
    result = []
    active = 0
    start = None
    
    for x, delta in events:
        if active < k and active + delta >= k:
            start = x
        
        if active >= k and active + delta < k:
            result.append((start, x))
            start = None
        
        active += delta
    
    out = [str(len(result))]
    for l, r in result:
        out.append(f"{l} {r}")
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
