# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
sys.setrecursionlimit(10**6)

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    shortcuts = set()
    for _ in range(n):
        x = int(input_data[idx])
        idx += 1
        y = int(input_data[idx])
        idx += 1
        shortcuts.add((x, y))
    
    memo = {}
    
    def is_losing(x, y):
        if (x, y) in shortcuts:
            return True
        if x == 0 and y == 0:
            return True
        if (x, y) in memo:
            return memo[(x, y)]
        
        # Check if we can reach a losing position
        for new_x in range(x):
            if is_losing(new_x, y):
                memo[(x, y)] = False
                return False
        
        for new_y in range(y):
            if is_losing(x, new_y):
                memo[(x, y)] = False
                return False
        
        memo[(x, y)] = True
        return True
    
    for _ in range(m):
        x = int(input_data[idx])
        idx += 1
        y = int(input_data[idx])
        idx += 1
        if is_losing(x, y):
            print("LOSE")
        else:
            print("WIN")

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
