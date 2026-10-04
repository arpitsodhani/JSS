# CLAUSE: setup_environment
import sys

n, pos, l, r = map(int, sys.stdin.buffer.readline().split())

# CLAUSE: solve_logic
need_left = int(l > 1)
need_right = int(r < n)

answers = {
    (0, 0): 0,
    (1, 0): abs(pos - l) + 1,
    (0, 1): abs(pos - r) + 1,
}

if (need_left, need_right) in answers:
    answer = answers[(need_left, need_right)]
else:
    answer = r - l + 2 + min(abs(pos - l), abs(pos - r))

# CLAUSE: finish_program
print(answer)
