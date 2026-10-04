# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def is_lucky(s):
    digits = [ord(ch) - 48 for ch in s]
    n = len(digits)
    for end in range(n - 1):
        target = sum(digits[:end + 1])
        current = 0
        pieces = 1
        possible = True
        for i in range(end + 1, n):
            current += digits[i]
            if current == target:
                pieces += 1
                current = 0
            elif current > target:
                possible = False
                break
        if possible and current == 0 and pieces > 1:
            return True
    return False

# CLAUSE: finish_program
tokens = sys.stdin.read().split()
if tokens:
    ticket = tokens[0] if len(tokens) == 1 else tokens[1]
    print("YES" if is_lucky(ticket) else "NO")
