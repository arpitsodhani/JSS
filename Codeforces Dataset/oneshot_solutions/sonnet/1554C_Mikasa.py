import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        answer = 1 << 31
        
        for bit in range(31, -1, -1):
            if (m >> bit) & 1:
                continue
            
            x = 0
            for high in range(31, bit, -1):
                if ((n >> high) & 1) != ((m >> high) & 1):
                    x |= 1 << high
            
            if ((n >> bit) & 1) == 0:
                x |= 1 << bit
            
            answer = min(answer, x)
        
        out.append(str(answer))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
