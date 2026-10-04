import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    a = [0] + data[2:]
    
    start = [0] * (n + 1)
    finish = [0] * (n + 1)
    heap = []
    
    next_id = 1
    for _ in range(min(k, n)):
        start[next_id] = 0
        finish[next_id] = a[next_id]
        heapq.heappush(heap, (finish[next_id], next_id))
        next_id += 1
    
    completions = {}
    max_time = 0
    
    while heap:
        time, idx = heapq.heappop(heap)
        completions[time] = completions.get(time, 0) + 1
        max_time = max(max_time, time)
        
        if next_id <= n:
            start[next_id] = time
            finish[next_id] = time + a[next_id]
            heapq.heappush(heap, (finish[next_id], next_id))
            next_id += 1
    
    done = [0] * (max_time + 1)
    current = 0
    for time in range(max_time + 1):
        current += completions.get(time, 0)
        done[time] = current
    
    answer = 0
    for i in range(1, n + 1):
        interesting = False
        for test in range(1, a[i] + 1):
            time = start[i] + test - 1
            completed = done[time]
            percent = (200 * completed + n) // (2 * n)
            
            if percent == test:
                interesting = True
                break
        
        if interesting:
            answer += 1
    
    print(answer)

if __name__ == "__main__":
    main()
