# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def solve():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    if len(raw) - 1 != n:
        return

    heaps = [[], [], []]
    for i in range(n):
        value = int(raw[i + 1])
        heapq.heappush(heaps[value % 3], (value, i + 1))

    order = []
    available = 0

    for step in range(n):
        heap = heaps[step % 3]
        if not heap:
            print("Impossible")
            return

        value, original_index = heapq.heappop(heap)
        if value > available:
            print("Impossible")
            return

        order.append(original_index)
        available = value + 1

    print("Possible")
    print(*order)

# CLAUSE: finish_program
if __name__ == "__main__":
    solve()
