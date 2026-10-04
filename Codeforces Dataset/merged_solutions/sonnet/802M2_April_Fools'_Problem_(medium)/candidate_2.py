# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    n, k = values[0], values[1]
    a = values[2:2 + n]
    b = values[2 + n:2 + 2 * n]
    heap = []
    for i in range(n):
        heapq.heappush(heap, a[i])
        chosen = heapq.heappop(heap)
        heapq.heappush(heap, chosen + b[i])
    total = 0
    for _ in range(k):
        total += heapq.heappop(heap)
    sys.stdout.write(str(total))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
