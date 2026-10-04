import sys
from collections import defaultdict

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        a = data[idx:idx + n]
        idx += n
        b = data[idx:idx + n]
        idx += n
        
        by_a = [[] for _ in range(n + 1)]
        for x, y in zip(a, b):
            by_a[x].append(y)
        
        freqs = {}
        values = []
        for x in range(1, n + 1):
            if by_a[x]:
                values.append(x)
                cur = defaultdict(int)
                for y in by_a[x]:
                    cur[y] += 1
                freqs[x] = cur
        
        result = 0
        
        for x in values:
            fx = freqs[x]
            limit = min(n, (2 * n) // x)
            
            for y in values:
                if y < x:
                    continue
                if y > limit:
                    break
                
                fy = freqs[y]
                target_sum = x * y
                
                if x == y:
                    for p, count_p in fx.items():
                        q = target_sum - p
                        if q not in fx:
                            continue
                        if p < q:
                            result += count_p * fx[q]
                        elif p == q:
                            result += count_p * (count_p - 1) // 2
                else:
                    for p, count_p in fx.items():
                        result += count_p * fy.get(target_sum - p, 0)
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
