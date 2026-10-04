import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    out = []
    for _ in range(t):
        n = data[idx]
        x = data[idx + 1]
        idx += 2
        
        total = 0
        max_beauty = 0
        
        for _ in range(n):
            a = data[idx]
            idx += 1
            total += a
            max_beauty += (a + x - 1) // x
        
        min_beauty = (total + x - 1) // x
        out.append(f"{min_beauty} {max_beauty}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
