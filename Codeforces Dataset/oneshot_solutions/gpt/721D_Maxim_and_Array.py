import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, x = data[0], data[1], data[2]
    a = data[3:3 + n]

    neg = sum(1 for v in a if v < 0)

    if neg % 2 == 0:
        idx = min(range(n), key=lambda i: abs(a[i]))
        if a[idx] >= 0:
            need = a[idx] // x + 1
            use = min(k, need)
            a[idx] -= use * x
        else:
            need = (-a[idx]) // x + 1
            use = min(k, need)
            a[idx] += use * x
        k -= use

    heap = [(abs(a[i]), i) for i in range(n)]
    heapq.heapify(heap)

    while k > 0:
        _, i = heapq.heappop(heap)
        if a[i] < 0:
            a[i] -= x
        else:
            a[i] += x
        heapq.heappush(heap, (abs(a[i]), i))
        k -= 1

    print(*a)

if __name__ == "__main__":
    main()
