# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import gcd

def solve_case(data, idx):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    a = list(map(int, data[idx:idx + n]))
    idx += n
    
    g = 0
    for _ in range(m):
        g = gcd(g, int(data[idx]))
        idx += 1
    
    total_abs = sum(abs(x) for x in a)
    parity = [0] * g
    min_abs = [10 ** 30] * g
    
    for i, x in enumerate(a):
        r = i % g
        if x < 0:
            parity[r] ^= 1
        ax = abs(x)
        if ax < min_abs[r]:
            min_abs[r] = ax
    
    answer = 0
    for target in (0, 1):
        current = total_abs
        for r in range(g):
            if parity[r] != target:
                current -= 2 * min_abs[r]
        answer = max(answer, current)
    
    return answer, idx

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        answer, idx = solve_case(data, idx)
        results.append(str(answer))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
