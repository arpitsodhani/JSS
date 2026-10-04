import sys

def solve():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        petals = []
        for i in range(n):
            petals.append(int(data[idx]))
            idx += 1
        
        quantities = []
        for i in range(n):
            quantities.append(int(data[idx]))
            idx += 1
        
        flowers = list(zip(petals, quantities))
        flowers.sort()
        
        max_petals = 0
        
        # Try each single type
        for p, q in flowers:
            if p <= m:
                count = min(q, m // p)
                total = p * count
                max_petals = max(max_petals, total)
        
        # Try each consecutive pair
        for i in range(len(flowers) - 1):
            p1, q1 = flowers[i]
            p2, q2 = flowers[i + 1]
            
            if p2 == p1 + 1:
                # Case 1: Buy all q1 of type p1, then as many of type p2
                if q1 * p1 <= m:
                    remaining = m - q1 * p1
                    y = min(q2, remaining // p2)
                    total = q1 * p1 + y * p2
                    max_petals = max(max_petals, total)
                
                # Case 2: Buy all q2 of type p2, then as many of type p1
                if q2 * p2 <= m:
                    remaining = m - q2 * p2
                    x = min(q1, remaining // p1)
                    total = x * p1 + q2 * p2
                    max_petals = max(max_petals, total)
        
        results.append(str(max_petals))
    
    print('\n'.join(results))

solve()
