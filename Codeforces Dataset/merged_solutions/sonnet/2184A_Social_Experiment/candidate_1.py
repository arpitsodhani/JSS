# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    if n == 1:
        print(1)
    elif n % 2 == 0 or n % 3 == 0:
        print(0)
    else:
        print(1)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
