# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
import math

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    ans = []
    for i in range(1, t + 1):
        n = int(data[i])
        side = 1.0 / math.tan(math.pi / (2 * n))
        ans.append(f"{side:.9f}")
    
    print("\n".join(ans))

main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
