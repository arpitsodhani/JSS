# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
def minimum_cost(n, k, first, second):
    waiting = []
    for prepare, print_cost in zip(first, second):
        heappush(waiting, prepare)
        current = heappop(waiting)
        heappush(waiting, current + print_cost)
    answer = sum(heappop(waiting) for _ in range(k))
    return answer

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    nums = [int(x) for x in tokens]
    n = nums[0]
    k = nums[1]
    split = 2 + n
    print(minimum_cost(n, k, nums[2:split], nums[split:split + n]))

# CLAUSE: finish_program
main()
