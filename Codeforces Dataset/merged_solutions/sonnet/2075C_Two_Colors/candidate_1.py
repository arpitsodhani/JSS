# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        
        paints = data[idx:idx + m]
        idx += m
        paints.sort()
        
        def count_at_least(x):
            return m - bisect_left(paints, x)
        
        result = 0
        for left_len in range(1, n):
            right_len = n - left_len
            
            left_choices = count_at_least(left_len)
            right_choices = count_at_least(right_len)
            same_color = count_at_least(max(left_len, right_len))
            
            result += left_choices * right_choices - same_color
        
        answers.append(str(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
