import sys
from collections import Counter

def solve():
    data = sys.stdin.read().split()
    idx = 0
    q = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        
        candies = list(map(int, data[idx:idx + n]))
        idx += n
        
        frequencies = sorted(Counter(candies).values(), reverse=True)
        
        total = 0
        limit = n + 1
        for freq in frequencies:
            take = min(freq, limit - 1)
            if take <= 0:
                break
            total += take
            limit = take
        
        answers.append(str(total))
    
    print('\n'.join(answers))

solve()
