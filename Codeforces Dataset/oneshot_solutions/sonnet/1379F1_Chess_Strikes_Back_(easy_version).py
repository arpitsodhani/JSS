import sys

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    q = int(input_data[idx + 2])
    idx += 3
    
    # Count missing cells from each pattern
    missing_odd = 0   # Pattern 1: (odd row, odd column)
    missing_even = 0  # Pattern 2: (even row, even column)
    
    for _ in range(q):
        r = int(input_data[idx])
        c = int(input_data[idx + 1])
        idx += 2
        
        if r % 2 == 1 and c % 2 == 1:
            missing_odd += 1
        elif r % 2 == 0 and c % 2 == 0:
            missing_even += 1
        
        # Answer YES if either pattern is complete
        if missing_odd == 0 or missing_even == 0:
            print("YES")
        else:
            print("NO")

solve()
