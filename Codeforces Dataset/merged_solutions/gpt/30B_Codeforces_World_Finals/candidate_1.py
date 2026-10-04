# CLAUSE: setup_environment
import sys
from itertools import permutations

# CLAUSE: solve_logic
s = sys.stdin.read().strip()
nums = []
cur = ""
for ch in s:
    if ch.isdigit():
        cur += ch
        if len(cur) == 2:
            nums.append(int(cur))
            cur = ""

fd, fm, fy = nums[:3]
parts = nums[3:6]

def leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def valid(d, m, y):
    if m < 1 or m > 12 or d < 1:
        return False
    days = [31, 29 if leap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return d <= days[m - 1]

final = (2000 + fy, fm, fd)

ok = False
for d, m, y2 in permutations(parts):
    y = 2000 + y2
    if not valid(d, m, y):
        continue
    if (y + 18, m, d) <= final:
        ok = True
        break

print("YES" if ok else "NO")

# CLAUSE: finish_program
RESULT_SENTINEL = None
