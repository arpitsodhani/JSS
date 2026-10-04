import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    cards = input_data[1]
    
    r = cards.count('R')
    g = cards.count('G')
    b = cards.count('B')
    
    visited = set()
    queue = deque([(r, g, b)])
    visited.add((r, g, b))
    
    final_colors = set()
    
    while queue:
        cr, cg, cb = queue.popleft()
        
        if cr + cg + cb == 1:
            if cr == 1:
                final_colors.add('R')
            elif cg == 1:
                final_colors.add('G')
            else:
                final_colors.add('B')
            continue
        
        # Same color operations
        if cr >= 2:
            state = (cr - 1, cg, cb)
            if state not in visited:
                visited.add(state)
                queue.append(state)
        
        if cg >= 2:
            state = (cr, cg - 1, cb)
            if state not in visited:
                visited.add(state)
                queue.append(state)
        
        if cb >= 2:
            state = (cr, cg, cb - 1)
            if state not in visited:
                visited.add(state)
                queue.append(state)
        
        # Different color operations
        if cr >= 1 and cg >= 1:
            state = (cr - 1, cg - 1, cb + 1)
            if state not in visited:
                visited.add(state)
                queue.append(state)
        
        if cr >= 1 and cb >= 1:
            state = (cr - 1, cg + 1, cb - 1)
            if state not in visited:
                visited.add(state)
                queue.append(state)
        
        if cg >= 1 and cb >= 1:
            state = (cr + 1, cg - 1, cb - 1)
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    print(''.join(sorted(final_colors)))

solve()
