import sys

def solve(s):
    if len(set(s)) == 1:
        return 0
    
    min_ops = float('inf')
    
    for target in set(s):
        max_len = 0
        current_len = 0
        
        for ch in s:
            if ch != target:
                current_len += 1
            else:
                if current_len > 0:
                    max_len = max(max_len, current_len)
                current_len = 0
        
        if current_len > 0:
            max_len = max(max_len, current_len)
        
        min_ops = min(min_ops, max_len.bit_length())
    
    return min_ops

input_lines = sys.stdin.read().strip().split('\n')
t = int(input_lines[0])
for i in range(1, t + 1):
    print(solve(input_lines[i]))
