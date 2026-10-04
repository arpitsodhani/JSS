# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
t = int(data[0])
pos = 1
ans = []
for _ in range(t):
    n = int(data[pos])
    s = data[pos + 1]
    pos += 2
    ones = [i + 1 for i, c in enumerate(s) if c == '1']
    zeros = [i + 1 for i, c in enumerate(s) if c == '0']
    if len(ones) % 2 == 0:
        ans.append(str(len(ones)))
        if ones:
            ans.append(' '.join(map(str, ones)))
    elif len(zeros) % 2 == 1:
        ans.append(str(len(zeros)))
        ans.append(' '.join(map(str, zeros)))
    else:
        ans.append('-1')
print('\n'.join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
