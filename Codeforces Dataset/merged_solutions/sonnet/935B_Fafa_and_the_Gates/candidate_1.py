# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    
    if len(data) == 1:
        token = data[0]
        s = ''.join(c for c in token if c in 'UR')
    else:
        s = data[1]
    
    diff = 0
    last_side = 0
    coins = 0
    
    for move in s:
        if move == 'R':
            diff += 1
        else:
            diff -= 1
        
        if diff > 0:
            side = 1
        elif diff < 0:
            side = -1
        else:
            continue
        
        if last_side != 0 and side != last_side:
            coins += 1
        
        last_side = side
    
    print(coins)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
