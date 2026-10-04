# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    s = list(data[2])
    
    steps = []
    
    while True:
        current = []
        i = 0
        while i < n - 1:
            if s[i] == 'R' and s[i + 1] == 'L':
                current.append(i + 1)
                s[i], s[i + 1] = s[i + 1], s[i]
                i += 2
            else:
                i += 1
        
        if not current:
            break
        
        steps.append(current)
    
    min_seconds = len(steps)
    total_moves = sum(len(step) for step in steps)
    
    if k < min_seconds or k > total_moves:
        print(-1)
        return
    
    extra = k - min_seconds
    answer = []
    
    for step in steps:
        while extra > 0 and len(step) > 1:
            answer.append([step.pop(0)])
            extra -= 1
        answer.append(step)
    
    out = []
    for move in answer:
        out.append(str(len(move)) + " " + " ".join(map(str, move)))
    
    print("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
