# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    answers = []
    
    for _ in range(t):
        grid = data[idx:idx + 8]
        idx += 8
        
        answer = 'B'
        for row in grid:
            if row == 'R' * 8:
                answer = 'R'
                break
        
        answers.append(answer)
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
