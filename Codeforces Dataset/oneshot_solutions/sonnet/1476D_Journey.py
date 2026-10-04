import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        left = [0] * (n + 1)
        for i in range(1, n + 1):
            if s[i - 1] == 'L':
                left[i] = 1
                if i >= 2 and s[i - 2] == 'R':
                    left[i] += left[i - 2]
        
        right = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if s[i] == 'R':
                right[i] = 1
                if i + 1 < n and s[i + 1] == 'L':
                    right[i] += right[i + 2]
        
        ans = [left[i] + right[i] + 1 for i in range(n + 1)]
        out.append(' '.join(map(str, ans)))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
