# CLAUSE: setup_environment
import sys
from math import isqrt

# CLAUSE: solve_logic
def losing_pair(a, b):
    if a > b:
        a, b = b, a
    gap = b - a
    if gap == 0:
        return a == 0
    return a == (gap + isqrt(5 * gap * gap)) // 2

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    if not nums:
        return
    n = nums[0]
    arr = nums[1:1 + n]
    if n == 1:
        winner = "BitLGM" if arr[0] else "BitAryo"
    elif n == 2:
        winner = "BitAryo" if losing_pair(arr[0], arr[1]) else "BitLGM"
    else:
        value = 0
        for item in arr:
            value ^= item
        winner = "BitLGM" if value else "BitAryo"
    sys.stdout.write(winner)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
