# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
t = int(data[0])
words = data[1:]
ans = []
for s in words[:t]:
    a = ord(s[0]) - ord('a')
    b = ord(s[1]) - ord('a')
    index = a * 25 + b + 1
    if b > a:
        index -= 1
    ans.append(str(index))
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
