# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def feasible(n, arr, mex):
    delta = [0] * (n + 1)
    active = 0
    limit = n - mex
    i = 0
    while i < n:
        active -= delta[i]
        required = 0
        if i > limit:
            required = i - limit
        if active < required:
            return False
        active += 1
        border = i + arr[i] + active - required
        if border < n:
            delta[border] += 1
        i += 1
    return True

def solve_one(n, arr):
    left = 1
    right = n
    while left < right:
        mid = (left + right + 1) // 2
        if feasible(n, arr, mid):
            left = mid
        else:
            right = mid - 1
    return left

def main():
    values = iter(map(int, sys.stdin.buffer.read().split()))
    tests = next(values)
    results = []
    for _ in range(tests):
        n = next(values)
        arr = [next(values) for _ in range(n)]
        results.append(str(solve_one(n, arr)))
    print("\n".join(results))

# CLAUSE: finish_program
main()
