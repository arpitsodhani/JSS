import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, x = data[0], data[1], data[2]
    a = data[3:3 + n]
    
    neg = sum(1 for v in a if v < 0)
    
    if neg % 2 == 0:
        pos = min(range(n), key=lambda i: abs(a[i]))
        
        need = abs(a[pos]) // x + 1
        if need > k:
            if a[pos] < 0:
                a[pos] += k * x
            else:
                a[pos] -= k * x
            print(' '.join(map(str, a)))
            return
        
        if a[pos] < 0:
            a[pos] += need * x
        else:
            a[pos] -= need * x
        k -= need
    
    heap = []
    for i, v in enumerate(a):
        heapq.heappush(heap, (abs(v), i))
    
    for _ in range(k):
        _, i = heapq.heappop(heap)
        if a[i] < 0:
            a[i] -= x
        else:
            a[i] += x
        heapq.heappush(heap, (abs(a[i]), i))
    
    print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()
