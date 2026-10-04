import heapq

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    if n == 1:
        if max(a) >= 1:
            for i in range(m):
                if a[i] >= 1:
                    print(i + 1)
                    return
        print(-1)
        return
    
    if n == 2:
        count = sum(1 for x in a if x >= 1)
        if count >= 2:
            result = []
            for i in range(m):
                if a[i] >= 1:
                    result.append(i + 1)
                    if len(result) == 2:
                        break
            print(' '.join(map(str, result)))
            return
        print(-1)
        return
    
    # Check if solution is possible
    total_usable = sum(min(a[i], n // 2) for i in range(m))
    if total_usable < n:
        print(-1)
        return
    
    # Greedy construction with max heap
    heap = [(-min(a[i], n // 2), i + 1) for i in range(m) if a[i] > 0]
    heapq.heapify(heap)
    
    result = []
    
    while len(result) < n:
        if not heap:
            print(-1)
            return
        
        first = heapq.heappop(heap)
        
        if result and first[1] == result[-1]:
            if not heap:
                print(-1)
                return
            second = heapq.heappop(heap)
            result.append(second[1])
            if second[0] + 1 < 0:
                heapq.heappush(heap, (second[0] + 1, second[1]))
            heapq.heappush(heap, first)
        else:
            result.append(first[1])
            if first[0] + 1 < 0:
                heapq.heappush(heap, (first[0] + 1, first[1]))
    
    # Fix circular constraint if needed
    if result[0] == result[-1]:
        for i in range(1, n - 1):
            if (result[i] != result[0] and result[i] != result[-1] and
                result[i-1] != result[-1] and result[i+1] != result[-1] and
                result[n-2] != result[i]):
                result[i], result[-1] = result[-1], result[i]
                break
        else:
            print(-1)
            return
    
    # Verify solution
    for i in range(n):
        if result[i] == result[(i+1) % n]:
            print(-1)
            return
    
    print(' '.join(map(str, result)))

solve()
