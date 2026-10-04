import sys
from collections import Counter

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        a = []
        for i in range(n):
            a.append(int(input_data[idx]))
            idx += 1
        
        q = int(input_data[idx])
        idx += 1
        
        count = Counter(a)
        
        query_results = []
        for _ in range(q):
            x = int(input_data[idx])
            idx += 1
            y = int(input_data[idx])
            idx += 1
            
            D = x * x - 4 * y
            
            if D < 0:
                query_results.append(0)
                continue
            
            sqrt_D = int(D ** 0.5)
            if sqrt_D * sqrt_D != D:
                if (sqrt_D + 1) * (sqrt_D + 1) == D:
                    sqrt_D += 1
                else:
                    query_results.append(0)
                    continue
            
            if (x + sqrt_D) % 2 != 0:
                query_results.append(0)
                continue
            
            t1 = (x + sqrt_D) // 2
            t2 = (x - sqrt_D) // 2
            
            if t1 == t2:
                c = count.get(t1, 0)
                query_results.append(c * (c - 1) // 2)
            else:
                c1 = count.get(t1, 0)
                c2 = count.get(t2, 0)
                query_results.append(c1 * c2)
        
        results.append(' '.join(map(str, query_results)))
    
    print('\n'.join(results))

solve()
