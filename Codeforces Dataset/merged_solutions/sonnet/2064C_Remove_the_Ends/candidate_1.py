# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve():
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
        
        positive_prefix = [0] * (n + 1)
        for i in range(n):
            positive_prefix[i + 1] = positive_prefix[i]
            if a[i] > 0:
                positive_prefix[i + 1] += a[i]
        
        negative_suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            negative_suffix[i] = negative_suffix[i + 1]
            if a[i] < 0:
                negative_suffix[i] += -a[i]
        
        best = 0
        for i in range(n + 1):
            best = max(best, positive_prefix[i] + negative_suffix[i])
        
        answers.append(str(best))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
