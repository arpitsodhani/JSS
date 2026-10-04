import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        ans = sum(int(c) for c in s)
        for i in range(n - 1):
            if s[i] != '0':
                ans += 1
        
        results.append(str(ans))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
