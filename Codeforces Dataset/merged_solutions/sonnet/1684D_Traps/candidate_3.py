# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def best_damage(n, k, arr):
    chosen = heapq.nlargest(k, (value + pos for pos, value in enumerate(arr, 1)))
    return sum(arr) + k * n - k * (k - 1) // 2 - sum(chosen)

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(nums)
    t = next(it)
    res = []
    for _ in range(t):
        n = next(it)
        k = next(it)
        arr = [next(it) for _ in range(n)]
        res.append(str(best_damage(n, k, arr)))
    print("\n".join(res))

# CLAUSE: finish_program
main()
