# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

if len(data) >= 4 and len(data) == 1 + 3 * data[0]:
    data = data[1:]

ans = []
for i in range(0, len(data), 3):
    x, y, z = data[i], data[i + 1], data[i + 2]
    ans.append("YES" if (x | y | z) == (x ^ y ^ z) else "NO")

print("\n".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
