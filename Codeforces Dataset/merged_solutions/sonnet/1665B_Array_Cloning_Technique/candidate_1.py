# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import Counter

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = []
        for _ in range(n):
            a.append(int(data[idx]))
            idx += 1
        
        have = max(Counter(a).values())
        ops = 0
        
        while have < n:
            add = min(have, n - have)
            ops += 1 + add
            have += add
        
        answers.append(str(ops))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
