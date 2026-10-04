# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    n, m = map(int, sys.stdin.read().split())
    
    if m % n != 0:
        print(-1)
        return
    
    ratio = m // n
    moves = 0
    
    while ratio % 3 == 0:
        ratio //= 3
        moves += 1
    
    while ratio % 2 == 0:
        ratio //= 2
        moves += 1
    
    print(moves if ratio == 1 else -1)

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
