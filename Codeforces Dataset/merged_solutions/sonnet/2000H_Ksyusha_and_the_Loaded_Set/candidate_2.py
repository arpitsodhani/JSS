# CLAUSE: setup_environment
import sys
from heapq import heappush, heappop

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    t = int(data[p])
    p += 1
    ans = []
    huge = 10 ** 30

    for _ in range(t):
        n = int(data[p])
        m = int(data[p + 1])
        p += 2

        initial = []
        pool = [0]
        for _ in range(n):
            x = int(data[p])
            p += 1
            initial.append(x)
            pool.append(x)

        ops = []
        for _ in range(m):
            typ = data[p]
            x = int(data[p + 1])
            p += 2
            ops.append((typ, x))
            if typ != b'?':
                pool.append(x)

        values = sorted(set(pool))
        where = {v: i for i, v in enumerate(values)}
        sz = len(values)

        left = [-1] * sz
        right = [-1] * sz
        live = [False] * sz
        heap = []

        def push_gap(a, b):
            if b == -1:
                length = huge
            else:
                length = values[b] - values[a] - 1
            if length > 0:
                heappush(heap, (-length, a, b))

        order = [0] + sorted(set(initial))
        last = -1
        for v in order:
            c = where[v]
            live[c] = True
            if last != -1:
                left[c] = last
                right[last] = c
            last = c

        for v in order:
            c = where[v]
            push_gap(c, right[c])

        def add(x):
            c = where[x]
            if live[c]:
                return
            a = c - 1
            while not live[a]:
                a -= 1
            b = right[a]
            live[c] = True
            left[c] = a
            right[c] = b
            right[a] = c
            if b != -1:
                left[b] = c
            push_gap(a, c)
            push_gap(c, b)

        def erase(x):
            c = where[x]
            if not live[c]:
                return
            a = left[c]
            b = right[c]
            live[c] = False
            right[a] = b
            if b != -1:
                left[b] = a
            push_gap(a, b)

        def ask(k):
            while heap:
                neg, a, b = heap[0]
                if not live[a] or right[a] != b:
                    heappop(heap)
                    continue
                real = huge if b == -1 else values[b] - values[a] - 1
                if real != -neg:
                    heappop(heap)
                    continue
                if real >= k:
                    return values[a] + 1
                return values[0] + 1
            return values[0] + 1

        for typ, x in ops:
            if typ == b'+':
                add(x)
            elif typ == b'-':
                erase(x)
            else:
                ans.append(str(ask(x)))

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
