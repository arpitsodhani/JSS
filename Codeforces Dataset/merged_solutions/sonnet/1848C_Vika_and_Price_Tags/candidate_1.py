# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def residue(a, b):
    if a == 0 and b == 0:
        return -1
    if a == 0:
        return 0
    if b == 0:
        return 1
    
    steps = 0
    while a != b:
        if a < b:
            a, b = b, a
        
        q = a // b
        r = a % b
        
        if r == 0:
            steps += q - 1
            break
        
        steps += q
        a, b = b, r
    
    return (steps + 2) % 3

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
        b = data[idx:idx + n]
        idx += n
        
        need = -1
        ok = True
        
        for x, y in zip(a, b):
            r = residue(x, y)
            if r == -1:
                continue
            if need == -1:
                need = r
            elif need != r:
                ok = False
                break
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
