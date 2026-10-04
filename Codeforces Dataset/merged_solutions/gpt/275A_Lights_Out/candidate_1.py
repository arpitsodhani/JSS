# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
nums = list(map(int, sys.stdin.read().split()))
presses = [nums[i * 3:(i + 1) * 3] for i in range(3)]

lights = [[1] * 3 for _ in range(3)]
dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(3):
    for j in range(3):
        if presses[i][j] % 2:
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < 3 and 0 <= nj < 3:
                    lights[ni][nj] ^= 1

for row in lights:
    print(''.join(map(str, row)))

# CLAUSE: finish_program
RESULT_SENTINEL = None
