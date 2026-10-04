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
        
        a.sort(reverse=True)
        out.append(' '.join(map(str, a)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
