# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
s = sys.stdin.readline().strip()

def prod_digits(t):
    p = 1
    for ch in t:
        p *= ord(ch) - 48
    return p

ans = prod_digits(s)

digits = list(s)
m = len(digits)

for i in range(m):
    if digits[i] == '0':
        continue
    candidate = digits[:]
    candidate[i] = str(int(candidate[i]) - 1)
    for j in range(i + 1, m):
        candidate[j] = '9'
    t = ''.join(candidate).lstrip('0')
    if t:
        ans = max(ans, prod_digits(t))

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
