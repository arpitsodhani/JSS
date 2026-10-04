import sys
from collections import Counter

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        count = Counter(a)
        values = sorted(count)
        
        left = 0
        current = 0
        best = 0
        
        for right, value in enumerate(values):
            if right > 0 and value != values[right - 1] + 1:
                left = right
                current = 0
            
            current += count[value]
            
            while right - left + 1 > k:
                current -= count[values[left]]
                left += 1
            
            best = max(best, current)
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
