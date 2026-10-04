import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        out.append(str(k + (k - 1) // (n - 1)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
