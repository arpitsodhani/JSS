# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from math import isqrt

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    t = data[0]
    queries = []
    max_n = 0
    idx = 1
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        queries.append((n, k))
        max_n = max(max_n, n)
    
    phi = list(range(max_n + 1))
    for i in range(2, max_n + 1):
        if phi[i] == i:
            for j in range(i, max_n + 1, i):
                phi[j] -= phi[j] // i
    
    coprime_pairs = [0] * (max_n + 1)
    if max_n >= 1:
        coprime_pairs[1] = 1
    for i in range(2, max_n + 1):
        coprime_pairs[i] = coprime_pairs[i - 1] + phi[i]
    
    cost = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    for r in range(1, max_n + 1):
        for l in range(r, 0, -1):
            cost[l][r] = cost[l + 1][r] + coprime_pairs[r // l]
    
    answers = []
    
    for n, k in queries:
        k = min(k, n)
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            prev[i] = cost[1][i]
        
        for parts in range(2, k + 1):
            cur = [0] * (n + 1)
            
            def compute(left, right, opt_left, opt_right):
                if left > right:
                    return
                
                mid = (left + right) // 2
                best_value = 10 ** 30
                best_pos = opt_left
                
                upper = min(opt_right, mid - 1)
                for cut in range(opt_left, upper + 1):
                    value = prev[cut] + cost[cut + 1][mid]
                    if value < best_value:
                        best_value = value
                        best_pos = cut
                
                cur[mid] = best_value
                compute(left, mid - 1, opt_left, best_pos)
                compute(mid + 1, right, best_pos, opt_right)
            
            compute(parts, n, parts - 1, n - 1)
            prev = cur
        
        answers.append(str(prev[n]))
    
    sys.stdout.write('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
