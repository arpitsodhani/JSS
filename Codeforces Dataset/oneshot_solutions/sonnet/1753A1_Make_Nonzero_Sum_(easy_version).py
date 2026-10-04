import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        if n % 2 == 1:
            out.append("-1")
            continue
        
        segments = []
        for i in range(0, n, 2):
            if a[i] == a[i + 1]:
                segments.append((i + 1, i + 2))
            else:
                segments.append((i + 1, i + 1))
                segments.append((i + 2, i + 2))
        
        out.append(str(len(segments)))
        for l, r in segments:
            out.append(f"{l} {r}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
