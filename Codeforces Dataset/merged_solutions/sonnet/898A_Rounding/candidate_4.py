# CLAUSE: setup_environment
import sys
n = int(sys.stdin.readline())

# CLAUSE: solve_logic
remainder = n % 10
adjustments = [0, -1, -2, -3, -4, -5, 4, 3, 2, 1]
answer = n + adjustments[remainder]

# CLAUSE: finish_program
sys.stdout.write(str(answer))
