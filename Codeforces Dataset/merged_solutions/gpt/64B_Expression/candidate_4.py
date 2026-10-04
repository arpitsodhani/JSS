# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    s = input().strip()
    a = int(s[0])
    op = s[1]
    b = int(s[2])
    print(a + b if op == '+' else a - b)

# CLAUSE: finish_program
def main():
    _inner_main()

main()
