# CLAUSE: setup_environment
import sys
import bisect
import heapq

# CLAUSE: solve_logic
def rounded_percent(m, n):
    return (200 * m + n) // (2 * n)

def main():
    data = list(map(int, sys.stdin.read().split()))
    n, k = (data[0], data[1])
    a = data[2:2 + n]
    heap = [0] * k
    heapq.heapify(heap)
    starts = [0] * n
    ends = [0] * n
    for i in range(n):
        t = heapq.heappop(heap)
        starts[i] = t
        ends[i] = t + a[i]
        heapq.heappush(heap, ends[i])
    sorted_ends = sorted(ends)
    ans = 0
    for i in range(n):
        s = starts[i]
        for q in range(1, a[i] + 1):
            m = bisect.bisect_right(sorted_ends, s + q - 1)
            if rounded_percent(m, n) == q:
                ans += 1
                break
    print(ans)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
