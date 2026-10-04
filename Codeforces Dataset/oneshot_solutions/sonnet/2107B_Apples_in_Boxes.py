import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        a = list(map(int, input_data[idx:idx + n]))
        idx += n
        
        @lru_cache(maxsize=None)
        def can_win(state):
            # Try all possible moves
            for i in range(len(state)):
                if state[i] > 0:
                    new_list = list(state)
                    new_list[i] -= 1
                    new_list.sort()
                    new_state = tuple(new_list)
                    
                    # Check if this move violates the constraint
                    if new_state[-1] - new_state[0] > k:
                        continue
                    
                    # Check if opponent loses from new state
                    if not can_win(new_state):
                        return True
            
            return False
        
        initial_state = tuple(sorted(a))
        if can_win(initial_state):
            results.append("Tom")
        else:
            results.append("Jerry")
    
    print('\n'.join(results))

solve()
