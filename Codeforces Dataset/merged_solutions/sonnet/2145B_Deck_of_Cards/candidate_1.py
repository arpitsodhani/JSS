# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        left = s.count('0')
        right = s.count('1')
        both = s.count('2')
        
        result = []
        for i in range(1, n + 1):
            can_be_removed = i <= left + both or i > n - right - both
            must_be_removed = i <= left or i > n - right
            
            if must_be_removed:
                result.append('-')
            elif can_be_removed:
                result.append('?')
            else:
                result.append('+')
        
        answers.append(''.join(result))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
