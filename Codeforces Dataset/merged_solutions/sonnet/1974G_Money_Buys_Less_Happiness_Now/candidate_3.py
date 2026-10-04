# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
def best_count(costs, monthly_income):
    total = 0
    selected = []

    for month_index, price in enumerate(costs):
        limit = month_index * monthly_income
        if total + price <= limit:
            total += price
            heappush(selected, -price)
            continue

        if selected:
            largest = -selected[0]
            if largest > price:
                total -= largest
                total += price
                heappop(selected)
                heappush(selected, -price)

    return len(selected)

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    cursor = 1
    results = []

    for _ in range(values[0]):
        months = values[cursor]
        income = values[cursor + 1]
        cursor += 2
        segment = values[cursor:cursor + months]
        cursor += months
        results.append(str(best_count(segment, income)))

    print("\n".join(results))

# CLAUSE: finish_program
main()
