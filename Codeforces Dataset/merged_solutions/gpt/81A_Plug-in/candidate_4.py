# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    s = sys.stdin.readline().strip()
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    sys.stdout.write(''.join(stack))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
