import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    # Store positions for each value
    positions = defaultdict(list)
    for i in range(n):
        positions[a[i]].append(i)
    
    # Find valid values and their periods
    valid = []
    
    for value in sorted(positions.keys()):
        pos = positions[value]
        
        if len(pos) == 1:
            # Single occurrence, period is 0
            valid.append((value, 0))
        else:
            # Check if positions form arithmetic progression
            period = pos[1] - pos[0]
            is_valid = True
            for i in range(1, len(pos)):
                if pos[i] - pos[i-1] != period:
                    is_valid = False
                    break
            
            if is_valid:
                valid.append((value, period))
    
    # Output
    print(len(valid))
    for value, period in valid:
        print(value, period)

solve()
