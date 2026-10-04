import sys
import heapq

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        q = data[idx:idx + n]
        idx += n

        present = set(q)
        min_heap = [x for x in range(1, n + 1) if x not in present]
        heapq.heapify(min_heap)

        mn = []
        for i, x in enumerate(q):
            if i == 0 or x != q[i - 1]:
                mn.append(x)
            else:
                mn.append(heapq.heappop(min_heap))

        mx = []
        max_heap = []
        prev = 0

        for i, x in enumerate(q):
            if i == 0 or x != q[i - 1]:
                for v in range(prev + 1, x):
                    heapq.heappush(max_heap, -v)
                mx.append(x)
                prev = x
            else:
                mx.append(-heapq.heappop(max_heap))

        out.append(" ".join(map(str, mn)))
        out.append(" ".join(map(str, mx)))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
