# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import defaultdict, deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    a = data[1:]
    
    if len(a) != n:
        return
    
    groups = [defaultdict(deque) for _ in range(3)]
    for i, x in enumerate(a, 1):
        groups[x % 3][x].append(i)
    
    values = [sorted(groups[r].keys()) for r in range(3)]
    ptr = [0, 0, 0]
    
    result = []
    current = 0
    
    for pos in range(n):
        need_residue = pos % 3
        
        if current < 0:
            print("Impossible")
            return
        
        keys = values[need_residue]
        p = ptr[need_residue]
        
        while p < len(keys) and not groups[need_residue][keys[p]]:
            p += 1
        
        ptr[need_residue] = p
        
        if p == len(keys) or keys[p] > current:
            print("Impossible")
            return
        
        x = keys[p]
        result.append(groups[need_residue][x].popleft())
        current = x + 1
    
    print("Possible")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
