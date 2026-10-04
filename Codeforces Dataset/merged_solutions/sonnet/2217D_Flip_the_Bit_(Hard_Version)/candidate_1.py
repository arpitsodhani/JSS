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
        k = data[idx + 1]
        idx += 2
        
        a = data[idx:idx + n]
        idx += n
        
        special = data[idx:idx + k]
        idx += k
        special.sort()
        
        x = a[special[0] - 1]
        counts = [0] * (k + 1)
        
        prev = 0
        total = 0
        
        for i in range(1, n + 2):
            cur = 0 if i == n + 1 else (a[i - 1] ^ x)
            
            if cur ^ prev:
                part = bisect_left(special, i)
                counts[part] += 1
                total += 1
            
            prev = cur
        
        answers.append(str(max(total // 2, max(counts))))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
