# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

def read_case():
    items = list(map(int, sys.stdin.buffer.read().split()))
    return items[0], items[1], items[2:]

def main():
    n, k, costs = read_case()
    scheduled = [(i + 1, cost) for i, cost in enumerate(costs)]

    # CLAUSE: solve_logic
    heap = []
    assigned = [0] * n
    total_cost = 0
    index = 0
    minute = k + 1

    while minute <= k + n:
        limit = min(n, minute)
        while index < limit:
            flight, cost = scheduled[index]
            heappush(heap, (-cost, flight))
            index += 1
        neg, flight = heappop(heap)
        assigned[flight - 1] = minute
        total_cost += (-neg) * (minute - flight)
        minute += 1

    # CLAUSE: finish_program
    output = [str(total_cost), " ".join(str(x) for x in assigned)]
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
