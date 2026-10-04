# CLAUSE: setup_environment
import sys
from heapq import heapify, heappush, heappop

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return
    n = data[0]
    k = data[1]
    pairs = [(data[2 + i], data[2 + n + i]) for i in range(n)]
    costs = []
    heapify(costs)
    for prepare_cost, print_cost in pairs:
        heappush(costs, prepare_cost)
        heappush(costs, heappop(costs) + print_cost)
    answer = 0
    remaining = k
    while remaining:
        answer += heappop(costs)
        remaining -= 1
    print(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
