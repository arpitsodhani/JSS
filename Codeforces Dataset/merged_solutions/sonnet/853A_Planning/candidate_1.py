# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    costs = [0] + data[2:2 + n]
    
    heap = []
    answer = [0] * (n + 1)
    total_cost = 0
    next_flight = 1
    
    for minute in range(k + 1, k + n + 1):
        while next_flight <= n and next_flight <= minute:
            heapq.heappush(heap, (-costs[next_flight], next_flight))
            next_flight += 1
        
        neg_cost, flight = heapq.heappop(heap)
        answer[flight] = minute
        total_cost += (-neg_cost) * (minute - flight)
    
    print(total_cost)
    print(' '.join(map(str, answer[1:])))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
