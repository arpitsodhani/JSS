import sys
from math import gcd

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        a.sort(key=lambda x: x % 2)
        
        good = 0
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(a[i], 2 * a[j]) > 1:
                    good += 1
        
        answers.append(str(good))
    
    print('\n'.join(answers))

solve()
