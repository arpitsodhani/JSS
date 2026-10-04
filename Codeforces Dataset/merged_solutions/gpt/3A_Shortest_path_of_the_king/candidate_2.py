# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
if len(data) == 1:
    s, t = (data[0][:2], data[0][2:])
else:
    s, t = (data[0], data[1])
x1 = ord(s[0]) - ord('a')
y1 = int(s[1]) - 1
x2 = ord(t[0]) - ord('a')
y2 = int(t[1]) - 1
moves = []
while x1 != x2 or y1 != y2:
    move = ''
    if x1 < x2:
        move += 'R'
        x1 += 1
    elif x1 > x2:
        move += 'L'
        x1 -= 1
    if y1 < y2:
        move += 'U'
        y1 += 1
    elif y1 > y2:
        move += 'D'
        y1 -= 1
    moves.append(move)
print(len(moves))
print('\n'.join(moves))

# CLAUSE: finish_program
RESULT_SENTINEL = 0
