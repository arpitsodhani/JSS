import sys

def solve():
    input_data = sys.stdin.read().strip().split('\n')
    n, k = map(int, input_data[0].split())
    d = list(input_data[1])
    
    states = [''.join(d)]
    state_to_index = {''.join(d): 0}
    
    for iteration in range(k):
        # Find minimum x (1-indexed) where d[x] = '4' and d[x+1] = '7'
        x = -1
        for i in range(n - 1):
            if d[i] == '4' and d[i + 1] == '7':
                x = i + 1
                break
        
        if x == -1:
            # No more "47" patterns, state is stable
            print(''.join(d))
            return
        
        # Apply transformation based on whether x is odd or even
        if x % 2 == 1:
            d[x - 1] = '4'
            d[x] = '4'
        else:
            d[x - 1] = '7'
            d[x] = '7'
        
        state = ''.join(d)
        
        # Check for cycle
        if state in state_to_index:
            cycle_start = state_to_index[state]
            cycle_length = len(states) - cycle_start
            final_index = cycle_start + ((k - cycle_start) % cycle_length)
            print(states[final_index])
            return
        
        states.append(state)
        state_to_index[state] = len(states) - 1
    
    # Completed all k operations
    print(''.join(d))

solve()
