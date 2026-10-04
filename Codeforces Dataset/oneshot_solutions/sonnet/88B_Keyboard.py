import sys
from math import sqrt

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    x = int(data[idx + 2])
    idx += 3
    
    positions = [[] for _ in range(26)]
    shifts = []
    
    for i in range(n):
        row = data[idx]
        idx += 1
        for j, ch in enumerate(row):
            if ch == 'S':
                shifts.append((i, j))
            else:
                positions[ord(ch) - ord('a')].append((i, j))
    
    q = int(data[idx])
    text = data[idx + 1]
    
    needs_extra = [False] * 26
    limit = x * x
    
    if shifts:
        for c in range(26):
            if not positions[c]:
                continue
            
            close = False
            for i, j in positions[c]:
                for si, sj in shifts:
                    dist = (i - si) * (i - si) + (j - sj) * (j - sj)
                    if dist <= limit:
                        close = True
                        break
                if close:
                    break
            
            needs_extra[c] = not close
    
    answer = 0
    
    for ch in text:
        lower = ch.lower()
        c = ord(lower) - ord('a')
        
        if not positions[c]:
            print(-1)
            return
        
        if ch.isupper():
            if not shifts:
                print(-1)
                return
            if needs_extra[c]:
                answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()
