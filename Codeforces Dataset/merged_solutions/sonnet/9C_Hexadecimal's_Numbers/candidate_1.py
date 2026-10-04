# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    n = int(sys.stdin.readline())
    
    count = 0
    
    def generate(x):
        nonlocal count
        if x > n:
            return
        if x > 0:
            count += 1
        generate(x * 10)
        generate(x * 10 + 1)
    
    generate(1)
    print(count)

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
