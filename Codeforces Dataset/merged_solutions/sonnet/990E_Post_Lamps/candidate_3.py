# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def lamps_needed(previous_open, n, power):
    current = 0
    count = 0
    while current < n:
        chosen = previous_open[current]
        if chosen == -1:
            return -1
        next_current = chosen + power
        if next_current <= current:
            return -1
        count += 1
        current = next_current
    return count

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    m = data[1]
    k = data[2]

    closed = [0] * n
    at = 3
    end = at + m
    for x in data[at:end]:
        closed[x] = 1

    costs = data[end:end + k]

    previous_open = []
    last_open = -1
    for index, flag in enumerate(closed):
        if flag == 0:
            last_open = index
        previous_open.append(last_open)

    if closed[0]:
        print(-1)
        return

    answer = -1
    for power, each_cost in enumerate(costs, 1):
        amount = lamps_needed(previous_open, n, power)
        if amount != -1:
            candidate = amount * each_cost
            if answer == -1 or candidate < answer:
                answer = candidate

    print(answer)

# CLAUSE: finish_program
main()
