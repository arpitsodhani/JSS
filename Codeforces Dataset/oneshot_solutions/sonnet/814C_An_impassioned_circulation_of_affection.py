import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    idx += 1
    s = data[idx]
    idx += 1
    
    best = [[0] * (n + 1) for _ in range(26)]
    
    for letter in range(26):
        target = chr(ord('a') + letter)
        row = best[letter]
        
        for left in range(n):
            changes = 0
            for right in range(left, n):
                if s[right] != target:
                    changes += 1
                length = right - left + 1
                if length > row[changes]:
                    row[changes] = length
        
        for m in range(1, n + 1):
            if row[m - 1] > row[m]:
                row[m] = row[m - 1]
    
    q = int(data[idx])
    idx += 1
    
    out = []
    for _ in range(q):
        m = int(data[idx])
        c = data[idx + 1]
        idx += 2
        
        if m > n:
            m = n
        out.append(str(best[ord(c) - ord('a')][m]))
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
