import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        b = data[idx:idx + m]
        idx += m
        b.sort()
        
        prev = -10**30
        possible = True
        
        for x in a:
            best = 10**30
            
            if x >= prev:
                best = x
            
            pos = bisect_left(b, prev + x)
            if pos < m:
                best = min(best, b[pos] - x)
            
            if best == 10**30:
                possible = False
                break
            
            prev = best
        
        answers.append("YES" if possible else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
