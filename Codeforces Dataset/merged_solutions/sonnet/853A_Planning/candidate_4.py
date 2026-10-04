# CLAUSE: setup_environment
import sys
import heapq

def choose_flight(queue):
    cost, flight = heapq.heappop(queue)
    return -cost, flight

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    k = int(data[1])
    costs = [int(x) for x in data[2:2 + n]]

    # CLAUSE: solve_logic
    queue = []
    answer = [0] * n
    total = 0

    for flight in range(1, min(n, k + 1) + 1):
        heapq.heappush(queue, (-costs[flight - 1], flight))

    next_ready = min(n, k + 1) + 1

    for offset in range(n):
        current_minute = k + 1 + offset
        while next_ready <= n and next_ready <= current_minute:
            heapq.heappush(queue, (-costs[next_ready - 1], next_ready))
            next_ready += 1
        price, flight = choose_flight(queue)
        answer[flight - 1] = current_minute
        total += price * (current_minute - flight)

    # CLAUSE: finish_program
    sys.stdout.write(f"{total}\n{' '.join(map(str, answer))}")

if __name__ == "__main__":
    main()
