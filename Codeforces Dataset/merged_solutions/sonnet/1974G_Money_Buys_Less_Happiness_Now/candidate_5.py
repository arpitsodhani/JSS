# CLAUSE: setup_environment
import sys
from heapq import heappush, heapreplace

# CLAUSE: solve_logic
def solve_case(months, income, source, start):
    chosen_total = 0
    max_heap = []
    stop = start + months
    month = 0

    for index in range(start, stop):
        cost = source[index]
        earned = month * income

        can_buy = chosen_total + cost <= earned
        can_swap = max_heap and -max_heap[0] > cost

        if can_buy:
            chosen_total += cost
            heappush(max_heap, -cost)
        elif can_swap:
            removed = -max_heap[0]
            chosen_total += cost - removed
            heapreplace(max_heap, -cost)

        month += 1

    return len(max_heap), stop

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    outputs = []

    for _ in range(tokens[0]):
        m = tokens[at]
        x = tokens[at + 1]
        at += 2
        result, at = solve_case(m, x, tokens, at)
        outputs.append(str(result))

    sys.stdout.write("\n".join(outputs))

# CLAUSE: finish_program
main()
