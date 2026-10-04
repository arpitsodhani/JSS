# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = sys.stdin.readline().strip()
stack = []
for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)
sys.stdout.write(''.join(stack))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
