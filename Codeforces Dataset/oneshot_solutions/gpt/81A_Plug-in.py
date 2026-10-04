import sys

s = sys.stdin.readline().strip()
stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)

sys.stdout.write(''.join(stack))
