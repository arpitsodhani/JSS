# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    n = int(sys.stdin.readline())

    if n % 2:
        print("black")
    else:
        print("white")
        print("1 2")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
