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
        
        ones = k - 3
        remaining = n - ones
        
        result = [1] * ones
        
        if remaining % 2 == 1:
            result += [1, remaining // 2, remaining // 2]
        elif remaining % 4 == 0:
            result += [remaining // 2, remaining // 4, remaining // 4]
        else:
            result += [2, remaining // 2 - 1, remaining // 2 - 1]
        
        out.append(' '.join(map(str, result)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
