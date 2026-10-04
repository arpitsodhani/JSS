# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def can_split(text, target):
    current = 0
    groups = 1
    for ch in text:
        current += int(ch)
        if current == target:
            groups += 1
            current = 0
        if current > target:
            return False
    return current == 0 and groups >= 2

def solve(data):
    if not data:
        return ""
    s = data[0] if len(data) == 1 else data[1]
    first_sum = 0
    for index, ch in enumerate(s[:-1]):
        first_sum += int(ch)
        if can_split(s[index + 1:], first_sum):
            return "YES"
    return "NO"

# CLAUSE: finish_program
result = solve(sys.stdin.read().split())
if result:
    print(result)
