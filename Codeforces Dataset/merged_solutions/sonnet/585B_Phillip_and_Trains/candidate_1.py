# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    answers = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        grid = []
        start = None
        for r in range(3):
            row = data[idx]
            idx += 1
            grid.append(row + '.' * 10)
            pos = row.find('s')
            if pos != -1:
                start = (r, pos)
        
        def blocked(r, c, time):
            c += 2 * time
            if c >= n:
                return False
            return grid[r][c] != '.'
        
        queue = deque()
        queue.append((start[0], start[1], 0))
        seen = set()
        seen.add((start[0], start[1], 0))
        
        ok = False
        
        while queue:
            r, c, time = queue.popleft()
            
            if c >= n - 1:
                ok = True
                break
            
            if blocked(r, c, time):
                continue
            
            for nr in (r - 1, r, r + 1):
                nc = c + 1
                if nr < 0 or nr >= 3:
                    continue
                
                if nc >= n:
                    ok = True
                    break
                
                if blocked(nr, nc, time):
                    continue
                if blocked(nr, nc, time + 1):
                    continue
                
                state = (nr, nc, time + 1)
                if state not in seen:
                    seen.add(state)
                    queue.append(state)
            
            if ok:
                break
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
