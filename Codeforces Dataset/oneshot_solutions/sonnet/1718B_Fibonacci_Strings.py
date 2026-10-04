import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    t = data[idx]
    idx += 1
    
    tests = []
    max_total = 0
    
    for _ in range(t):
        k = data[idx]
        idx += 1
        counts = data[idx:idx + k]
        idx += k
        total = sum(counts)
        tests.append(counts)
        max_total = max(max_total, total)
    
    fib = [1, 1]
    prefix = [1, 2]
    while prefix[-1] < max_total:
        fib.append(fib[-1] + fib[-2])
        prefix.append(prefix[-1] + fib[-1])
    
    last_by_total = {value: i for i, value in enumerate(prefix)}
    answers = []
    
    for counts in tests:
        total = sum(counts)
        if total not in last_by_total:
            answers.append("NO")
            continue
        
        last = last_by_total[total]
        heap = [(-count, i) for i, count in enumerate(counts)]
        heapq.heapify(heap)
        
        previous = -1
        ok = True
        
        for i in range(last, -1, -1):
            if not heap:
                ok = False
                break
            
            first = heapq.heappop(heap)
            
            if first[1] == previous:
                if not heap:
                    ok = False
                    break
                second = heapq.heappop(heap)
                heapq.heappush(heap, first)
                value, letter = -second[0], second[1]
            else:
                value, letter = -first[0], first[1]
            
            if value < fib[i]:
                ok = False
                break
            
            value -= fib[i]
            if value > 0:
                heapq.heappush(heap, (-value, letter))
            
            previous = letter
        
        answers.append("YES" if ok else "NO")
    
    print('\n'.join(answers))

if __name__ == "__main__":
    main()
