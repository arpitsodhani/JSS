# CLAUSE: setup_environment
import sys
import random

# CLAUSE: solve_logic
def ask(x):
    if x >= 0:
        print('+', x, flush=True)
    else:
        print('-', -x, flush=True)
    return int(sys.stdin.readline())

def answer(x):
    print('!', x, flush=True)
    sys.exit()
first = int(sys.stdin.readline())
mx = first
pos = 0
random.seed(1840)
for _ in range(500):
    step = random.randint(1, 10 ** 6)
    pos += step
    v = ask(step)
    if v > mx:
        mx = v
v = ask(-pos)
B = 320
seen = {v: 0}
for i in range(1, B):
    v = ask(1)
    seen[v] = i
cur = B - 1
jump = mx - cur
v = ask(jump)
cur = mx
best = None
if v in seen:
    cand = cur - seen[v]
    if cand >= mx:
        best = cand
for _ in range(1, 220):
    v = ask(B)
    cur += B
    if v in seen:
        cand = cur - seen[v]
        if cand >= mx and (best is None or cand < best):
            best = cand
    if best is not None:
        answer(best)
answer(best if best is not None else mx)

# CLAUSE: finish_program
RESULT_SENTINEL = 0
