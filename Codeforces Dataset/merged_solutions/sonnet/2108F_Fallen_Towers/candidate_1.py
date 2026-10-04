# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from itertools import permutations

def solve(n, a):
    max_mex = 0
    
    for perm in permutations(range(n)):
        current = a[:]
        for idx in perm:
            val = current[idx]
            for j in range(idx + 1, min(idx + 1 + val, n)):
                current[j] += 1
            current[idx] = 0
        
        # Check if non-decreasing
        valid = True
        for i in range(n - 1):
            if current[i] > current[i + 1]:
                valid = False
                break
        
        if valid:
            # Compute MEX
            s = set(current)
            mex = 0
            while mex in s:
                mex += 1
            max_mex = max(max_mex, mex)
    
    return max_mex

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = list(map(int, input_data[idx:idx + n]))
        idx += n
        print(solve(n, a))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
