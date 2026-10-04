# CLAUSE: setup_environment
import sys
import heapq

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    k = values[1]
    costs = [0] + values[2:2 + n]

    # CLAUSE: solve_logic
    available = []
    departure = [0] * (n + 1)
    total = 0
    incoming = 1

    for minute in range(k + 1, k + n + 1):
        while incoming <= n and incoming <= minute:
            heapq.heappush(available, (-costs[incoming], incoming))
            incoming += 1
        negative_cost, flight = heapq.heappop(available)
        departure[flight] = minute
        total += -negative_cost * (minute - flight)

    # CLAUSE: finish_program
    sys.stdout.write(str(total) + "\n")
    sys.stdout.write(" ".join(map(str, departure[1:])))

if __name__ == "__main__":
    main()
