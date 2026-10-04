# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    n = int(input())
    fib = {1}
    a, b = 1, 1
    while b <= n:
        fib.add(b)
        a, b = b, a + b

    print(''.join('O' if i in fib else 'o' for i in range(1, n + 1)))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
