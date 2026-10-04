# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read()
    if not raw.strip():
        return
    data = tuple(map(int, raw.split()))
    n = data[0]
    k = data[1]
    starts = data[2:2 + n]
    finishes = data[2 + n:2 + n + n]
    queue = []
    index = 0
    while index < n:
        heapq.heappush(queue, starts[index])
        least = heapq.heappop(queue)
        heapq.heappush(queue, least + finishes[index])
        index += 1
    picked = []
    for _ in range(k):
        picked.append(heapq.heappop(queue))
    sys.stdout.write(str(sum(picked)))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
