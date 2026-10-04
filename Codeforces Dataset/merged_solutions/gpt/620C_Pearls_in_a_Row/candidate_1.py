# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
a = data[1:]

segments = []
seen = set()
start = 1

for i, x in enumerate(a, 1):
    if x in seen:
        segments.append([start, i])
        start = i + 1
        seen.clear()
    else:
        seen.add(x)

if not segments:
    print(-1)
else:
    segments[-1][1] = n
    out = [str(len(segments))]
    out.extend(f"{l} {r}" for l, r in segments)
    print("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
