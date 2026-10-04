# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        
        suffix_ones = []
        for _ in range(n):
            row = data[idx:idx + n]
            idx += n
            
            cnt = 0
            for x in reversed(row):
                if x == 1:
                    cnt += 1
                else:
                    break
            suffix_ones.append(cnt)
        
        suffix_ones.sort()
        
        need = 1
        for cnt in suffix_ones:
            if cnt >= need:
                need += 1
        
        answers.append(str(min(need, n)))
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
