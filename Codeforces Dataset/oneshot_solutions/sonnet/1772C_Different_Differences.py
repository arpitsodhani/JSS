import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    
    out = []
    for _ in range(t):
        k = data[idx]
        n = data[idx + 1]
        idx += 2
        
        result = [1]
        current = 1
        diff = 1
        
        for pos in range(2, k + 1):
            remaining = k - pos
            
            if current + diff + remaining <= n:
                current += diff
                diff += 1
            else:
                current += 1
            
            result.append(current)
        
        out.append(' '.join(map(str, result)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
