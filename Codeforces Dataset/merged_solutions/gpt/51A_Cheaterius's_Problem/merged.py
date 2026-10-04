# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()

if not data:
    sys.exit()

n = int(data[0])
tokens = data[1:]

amulets = []

if len(tokens) >= 2 * n:
    for i in range(n):
        s = tokens[2 * i] + tokens[2 * i + 1]
        amulets.append(s)
else:
    s = ''.join(tokens)
    for i in range(n):
        amulets.append(s[4 * i:4 * i + 4])

seen = set()

for s in amulets:
    a, b, c, d = s[0], s[1], s[2], s[3]
    rotations = [
        a + b + c + d,
        c + a + d + b,
        d + c + b + a,
        b + d + a + c,
    ]
    seen.add(min(rotations))

print(len(seen))

# CLAUSE: finish_program
RESULT_SENTINEL = None
