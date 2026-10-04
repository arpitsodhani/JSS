# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import defaultdict

def parse_cases(data):
    if not data:
        return []
    
    t = data[0]
    idx = 1
    cases = []
    ok = True
    
    for _ in range(t):
        if idx >= len(data):
            ok = False
            break
        n = data[idx]
        idx += 1
        need = 2 * n + 1
        if idx + need > len(data):
            ok = False
            break
        cases.append((n, data[idx:idx + need]))
        idx += need
    
    if ok and idx == len(data):
        return cases
    
    n = data[0]
    arr = data[1:1 + 2 * n + 1]
    return [(n, arr)] if len(arr) == 2 * n + 1 else []

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    cases = parse_cases(data)
    
    out = []
    for n, arr in cases:
        positions = defaultdict(list)
        for i, x in enumerate(arr, 1):
            positions[x].append(i)
        
        for pos in positions.values():
            if len(pos) == 3:
                out.append(' '.join(map(str, pos)))
                break
    
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
