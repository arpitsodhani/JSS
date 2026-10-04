# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import gcd

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
        
        total = sum(a)
        prefix = 0
        best = 0
        
        for i in range(n - 1):
            prefix += a[i]
            best = max(best, gcd(prefix, total - prefix))
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
