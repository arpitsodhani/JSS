import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    w = int(input_data[idx])
    h = int(input_data[idx + 1])
    n = int(input_data[idx + 2])
    idx += 3
    
    groups = defaultdict(lambda: {'V': [], 'H': []})
    
    for i in range(n):
        g = int(input_data[idx])
        p = int(input_data[idx + 1])
        t = int(input_data[idx + 2])
        idx += 3
        
        param = t - p
        if g == 1:  # vertical
            groups[param]['V'].append((p, i))
        else:  # horizontal
            groups[param]['H'].append((p, i))
    
    result = [None] * n
    
    for param, group in groups.items():
        verticals = sorted(group['V'])
        horizontals = sorted(group['H'])
        
        k = len(verticals)
        m = len(horizontals)
        
        for i in range(min(k, m)):
            x_i, v_id = verticals[i]
            y_i, h_id = horizontals[i]
            
            result[v_id] = (w, y_i)
            result[h_id] = (x_i, h)
        
        for i in range(m, k):
            x_i, v_id = verticals[i]
            result[v_id] = (x_i, h)
        
        for i in range(k, m):
            y_i, h_id = horizontals[i]
            result[h_id] = (w, y_i)
    
    for x, y in result:
        print(x, y)

solve()
