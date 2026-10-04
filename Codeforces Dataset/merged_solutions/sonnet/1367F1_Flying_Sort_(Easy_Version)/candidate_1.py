# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def solve_case(n, a):
    values = sorted(a)
    rank = {values[i]: i for i in range(n)}
    
    pos = [0] * n
    for i, x in enumerate(a):
        pos[rank[x]] = i
    
    best = 1
    current = 1
    
    for i in range(1, n):
        if pos[i - 1] < pos[i]:
            current += 1
        else:
            current = 1
        best = max(best, current)
    
    return n - best

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        answers.append(str(solve_case(n, a)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
