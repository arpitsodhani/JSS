# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        first = s[:n]
        second = s[n:]
        
        correct_first = first.count('W')
        wrong_first = n - correct_first
        
        if correct_first % 2 == 1:
            answers.append("NO")
            continue
        
        need = correct_first // 2
        ok = True
        
        if wrong_first > 0:
            first_bad = first.find('R')
            if first[:first_bad].count('W') < need:
                ok = False
            
            last_bad = second.rfind('W')
            if second[last_bad + 1:].count('R') < need:
                ok = False
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
