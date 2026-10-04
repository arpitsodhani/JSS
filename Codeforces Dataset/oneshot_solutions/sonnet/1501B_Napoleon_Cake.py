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
        
        result = [0] * n
        cream = 0
        
        for i in range(n - 1, -1, -1):
            cream = max(cream, a[i])
            if cream > 0:
                result[i] = 1
                cream -= 1
        
        out.append(' '.join(map(str, result)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
