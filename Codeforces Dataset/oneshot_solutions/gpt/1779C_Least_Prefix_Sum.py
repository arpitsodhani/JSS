import sys
import heapq

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []

    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        res = 0

        s = 0
        heap = []
        for i in range(m - 1, 0, -1):
            s += a[i]
            if a[i] > 0:
                heapq.heappush(heap, -a[i])
            while s > 0:
                x = -heapq.heappop(heap)
                s -= 2 * x
                res += 1

        s = 0
        heap = []
        for i in range(m, n):
            s += a[i]
            if a[i] < 0:
                heapq.heappush(heap, a[i])
            while s < 0:
                x = heapq.heappop(heap)
                s -= 2 * x
                res += 1

        ans.append(str(res))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
