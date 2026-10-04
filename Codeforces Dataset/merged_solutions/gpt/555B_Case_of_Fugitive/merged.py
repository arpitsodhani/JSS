# CLAUSE: setup_environment
import sys
import heapq

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    p = 2

    islands = []
    for _ in range(n):
        l, r = data[p], data[p + 1]
        p += 2
        islands.append((l, r))

    bridges = []
    for i in range(m):
        bridges.append((data[p], i + 1))
        p += 1

    if m < n - 1:
        print("No")
        return

    gaps = []
    for i in range(n - 1):
        l1, r1 = islands[i]
        l2, r2 = islands[i + 1]
        gaps.append((l2 - r1, r2 - l1, i))

    gaps.sort()
    bridges.sort()

    ans = [0] * (n - 1)
    heap = []
    j = 0

    for length, bridge_id in bridges:
        while j < n - 1 and gaps[j][0] <= length:
            heapq.heappush(heap, (gaps[j][1], gaps[j][2]))
            j += 1

        while heap and heap[0][0] < length:
            print("No")
            return

        if heap:
            _, gap_id = heapq.heappop(heap)
            ans[gap_id] = bridge_id

    if any(x == 0 for x in ans):
        print("No")
        return

    print("Yes")
    print(*ans)

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
