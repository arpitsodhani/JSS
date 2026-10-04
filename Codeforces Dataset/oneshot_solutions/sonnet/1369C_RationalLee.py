import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    out = []
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        w = data[idx:idx + k]
        idx += k
        
        a.sort()
        w.sort()
        
        ans = 0
        right = n - 1
        groups = []
        
        for need in w:
            ans += a[right]
            if need == 1:
                ans += a[right]
            else:
                groups.append(need)
            right -= 1
        
        left = 0
        for need in reversed(groups):
            ans += a[left]
            left += need - 1
        
        out.append(str(ans))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
