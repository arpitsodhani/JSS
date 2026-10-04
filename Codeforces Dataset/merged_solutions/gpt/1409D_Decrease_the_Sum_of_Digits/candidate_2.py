# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def digit_sum(x):
    return sum(map(int, str(x)))

def solve_case(n, s):
    if digit_sum(n) <= s:
        return 0
    add = 0
    place = 1
    while digit_sum(n + add) > s:
        digit = (n + add) // place % 10
        if digit:
            add += (10 - digit) * place
        place *= 10
    return add
data = sys.stdin.read().strip().split()
t = int(data[0])
ans = []
idx = 1
for _ in range(t):
    n = int(data[idx])
    s = int(data[idx + 1])
    idx += 2
    ans.append(str(solve_case(n, s)))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
