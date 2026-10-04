import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    rows = set()
    cols = set()
    result = []
    
    for _ in range(m):
        r = int(input_data[idx])
        idx += 1
        c = int(input_data[idx])
        idx += 1
        
        rows.add(r)
        cols.add(c)
        
        not_under_attack = (n - len(rows)) * (n - len(cols))
        result.append(not_under_attack)
    
    print(' '.join(map(str, result)))

solve()
