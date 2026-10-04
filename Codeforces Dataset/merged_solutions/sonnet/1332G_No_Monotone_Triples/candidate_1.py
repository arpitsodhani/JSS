# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from itertools import combinations

def is_valid_subsequence(values):
    """Check if a sequence has NO monotone triple."""
    n = len(values)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                a, b, c = values[i], values[j], values[k]
                if (a <= b <= c) or (a >= b >= c):
                    return False
    return True

def solve_query(arr, L, R):
    """Find the maximum subsequence with no monotone triples."""
    subarray = arr[L:R+1]
    n = len(subarray)
    
    if n < 3:
        return 0, []
    
    max_size = min(n, 5)
    
    for size in range(max_size, 2, -1):
        for indices in combinations(range(n), size):
            values = [subarray[i] for i in indices]
            if is_valid_subsequence(values):
                original_indices = [L + i + 1 for i in indices]
                return size, original_indices
    
    return 0, []

def main():
    data = sys.stdin.read().split()
    n, q = int(data[0]), int(data[1])
    arr = [int(data[2 + i]) for i in range(n)]
    
    idx = 2 + n
    for _ in range(q):
        L, R = int(data[idx]), int(data[idx + 1])
        idx += 2
        
        size, indices = solve_query(arr, L - 1, R - 1)
        print(size)
        if size > 0:
            print(' '.join(map(str, indices)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
