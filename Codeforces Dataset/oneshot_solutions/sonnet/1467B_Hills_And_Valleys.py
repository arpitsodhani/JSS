import sys

def is_bad(a, i):
    return (a[i] > a[i - 1] and a[i] > a[i + 1]) or (a[i] < a[i - 1] and a[i] < a[i + 1])

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    out = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        
        bad = [0] * n
        total = 0
        for i in range(1, n - 1):
            if is_bad(a, i):
                bad[i] = 1
                total += 1
        
        answer = total
        
        for i in range(n):
            candidates = []
            if i > 0:
                candidates.append(a[i - 1])
            if i + 1 < n:
                candidates.append(a[i + 1])
            
            old = a[i]
            before = 0
            for j in range(max(1, i - 1), min(n - 1, i + 2)):
                before += bad[j]
            
            for value in candidates:
                a[i] = value
                after = 0
                for j in range(max(1, i - 1), min(n - 1, i + 2)):
                    if is_bad(a, j):
                        after += 1
                answer = min(answer, total - before + after)
            
            a[i] = old
        
        out.append(str(answer))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
