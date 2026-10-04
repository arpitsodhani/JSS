# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    buttons = data[1:1 + n]

    if (n == 1 and buttons[0] == 1) or (n > 1 and buttons.count(0) == 1):
        print("YES")
    else:
        print("NO")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
