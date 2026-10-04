# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = data[1:]

bits = set()
for x in a:
    while x in bits:
        bits.remove(x)
        x += 1
    bits.add(x)

if not bits:
    print(0)
else:
    print(max(bits) + 1 - len(bits))

# CLAUSE: finish_program
RESULT_SENTINEL = None
