# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, q = data[0], data[1]
a = data[2:2 + n]
queries = data[2 + n:]

pos = [0] * 51

for i, color in enumerate(a, 1):
    if pos[color] == 0:
        pos[color] = i

ans = []

for color in queries:
    p = pos[color]
    ans.append(str(p))
    for c in range(1, 51):
        if pos[c] and pos[c] < p:
            pos[c] += 1
    pos[color] = 1

print(" ".join(ans))

# CLAUSE: finish_program
RESULT_SENTINEL = None
