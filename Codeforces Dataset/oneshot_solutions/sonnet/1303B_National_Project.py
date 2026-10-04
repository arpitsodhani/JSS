import sys

def solve(n, g, b):
    high_needed = (n + 1) // 2
    
    full_cycles = high_needed // g
    remaining = high_needed % g
    
    if remaining == 0:
        d_good = full_cycles * (g + b) - b
    else:
        d_good = full_cycles * (g + b) + remaining
    
    return max(d_good, n)

input_data = sys.stdin.read().split()
idx = 0
t = int(input_data[idx])
idx += 1

for _ in range(t):
    n = int(input_data[idx])
    g = int(input_data[idx + 1])
    b = int(input_data[idx + 2])
    idx += 3
    print(solve(n, g, b))
