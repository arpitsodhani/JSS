# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
good = False
idx = 1

for _ in range(n):
    handle = data[idx]
    before = int(data[idx + 1])
    after = int(data[idx + 2])
    idx += 3

    if before >= 2400 and after > before:
        good = True

print("YES" if good else "NO")

# CLAUSE: finish_program
RESULT_SENTINEL = None
