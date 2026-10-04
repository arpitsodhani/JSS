import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    out = []
    for i in range(1, t + 1):
        n = int(data[i])
        
        if n % 3 == 0:
            if n >= 12:
                out.append("YES")
                out.append(f"1 4 {n - 5}")
            else:
                out.append("NO")
        else:
            if n >= 7:
                out.append("YES")
                out.append(f"1 2 {n - 3}")
            else:
                out.append("NO")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
