# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def position_after(x, n):
    r = n % 4
    if x % 2 == 0:
        if r == 0:
            return x
        if r == 1:
            return x - n
        if r == 2:
            return x + 1
        return x + n + 1
    else:
        if r == 0:
            return x
        if r == 1:
            return x + n
        if r == 2:
            return x - 1
        return x - n - 1

data = sys.stdin.buffer.read().split()
if not data:
    sys.exit()

t = int(data[0])
out = []
idx = 1
for _ in range(t):
    x = int(data[idx])
    n = int(data[idx + 1])
    idx += 2
    out.append(str(position_after(x, n)))

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
