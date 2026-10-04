# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def c2(v):
    return v * (v - 1) // 2

def c3(v):
    return v * (v - 1) * (v - 2) // 6

def enough(n, p, k):
    remaining = n - k
    twice_good = 0
    twice_good += 2 * c3(k)
    twice_good += 2 * c2(k) * remaining
    twice_good += k * c2(remaining)
    return twice_good / (2 * c3(n)) >= p - 1e-9

def minimum_maps(n, p):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if enough(n, p, mid):
            right = mid
        else:
            left = mid + 1
    return left

# CLAUSE: finish_program
tokens = sys.stdin.readline().split()
n = int(tokens[0])
p = float(tokens[1])
print(minimum_maps(n, p))
