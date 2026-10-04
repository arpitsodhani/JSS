import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        if n % 2 == 0:
            out.append("No")
            continue
        
        out.append("Yes")
        start = 3 * (n + 1) // 2
        
        left = 1
        right = n
        for s in range(start, start + n):
            if s % 2 == start % 2:
                a = left
                left += 1
            else:
                a = right
                right -= 1
            out.append(f"{a} {s - a}")
    
    print("\n".join(out))

if __name__ == "__main__":
    main()
