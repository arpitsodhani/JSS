# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import heapq

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        heap = []
        total = 0

        for x in data[idx:idx + n]:
            if x == 0:
                if heap:
                    total -= heapq.heappop(heap)
            else:
                heapq.heappush(heap, -x)

        idx += n
        ans.append(str(total))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
