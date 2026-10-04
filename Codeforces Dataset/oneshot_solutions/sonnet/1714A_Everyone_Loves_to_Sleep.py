import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        H = int(data[idx + 1])
        M = int(data[idx + 2])
        idx += 3
        
        current = H * 60 + M
        best = 24 * 60
        
        for _ in range(n):
            h = int(data[idx])
            m = int(data[idx + 1])
            idx += 2
            
            alarm = h * 60 + m
            wait = (alarm - current) % (24 * 60)
            best = min(best, wait)
        
        out.append(f"{best // 60} {best % 60}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
