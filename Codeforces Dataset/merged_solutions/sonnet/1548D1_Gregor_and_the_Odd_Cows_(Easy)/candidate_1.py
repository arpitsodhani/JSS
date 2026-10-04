# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import comb

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    counts = [0] * 4
    
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        
        x //= 2
        y //= 2
        mask = (x & 1) * 2 + (y & 1)
        counts[mask] += 1
    
    total = comb(n, 3)
    
    bad = 0
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                bad += counts[i] * counts[j] * counts[k]
    
    print(total - bad)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
