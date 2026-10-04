# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    volumes = data[idx:idx + n]
    idx += n
    
    prefix = []
    total = 0
    for v in volumes:
        total += v
        prefix.append(total)
    
    q = data[idx]
    idx += 1
    
    answers = []
    for _ in range(q):
        t = data[idx]
        idx += 1
        
        pipes = 0
        possible = True
        
        for i, need in enumerate(prefix, 1):
            required = (need + t - 1) // t
            if required > i:
                possible = False
                break
            if required > pipes:
                pipes = required
        
        answers.append(str(pipes if possible else -1))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
