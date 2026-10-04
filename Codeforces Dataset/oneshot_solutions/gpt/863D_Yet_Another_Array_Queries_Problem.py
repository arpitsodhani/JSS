import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    q = next(it)
    m = next(it)

    a = [0] + [next(it) for _ in range(n)]

    queries = []
    for _ in range(q):
        t = next(it)
        l = next(it)
        r = next(it)
        queries.append((t, l, r))

    pos = [next(it) for _ in range(m)]

    for t, l, r in reversed(queries):
        for i, p in enumerate(pos):
            if l <= p <= r:
                if t == 1:
                    pos[i] = r if p == l else p - 1
                else:
                    pos[i] = l + r - p

    print(*[a[p] for p in pos])

if __name__ == "__main__":
    main()
