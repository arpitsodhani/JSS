# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    t = int(input())
    for _ in range(t):
        x = list(map(int, input().split()))
        print(max(x) - min(x))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
