# Clause setup_environment [Confidence: 1.00]
import sys


# Clause solve_logic [Confidence: 0.80]
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


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


