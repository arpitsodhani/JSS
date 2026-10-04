import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    tasks = []
    unknown = -1
    used = set()
    
    for i in range(n):
        t = data[idx]
        s = data[idx + 1]
        p = data[idx + 2]
        idx += 3
        
        tasks.append([t, s, p])
        if p == -1:
            unknown = i
        else:
            used.add(p)
    
    target_finish = data[idx]
    
    target_time = tasks[unknown][0]
    target_pages = tasks[unknown][1]
    
    by_time = sorted((t, s, p) for i, (t, s, p) in enumerate(tasks) if i != unknown)
    
    def finish_time(priority):
        cur = target_time
        need = target_pages
        backlog = 0
        pos = 0
        
        for t, s, p in by_time:
            if p <= priority:
                continue
            
            if t < target_time:
                if pos == 0:
                    last = t
                if 'last' in locals():
                    backlog = max(0, backlog - (t - last))
                backlog += s
                last = t
                pos = 1
            else:
                if pos == 1:
                    backlog = max(0, backlog - (target_time - last))
                    pos = 2
                
                if cur < t:
                    if backlog > 0:
                        spend = min(backlog, t - cur)
                        backlog -= spend
                        cur += spend
                    
                    if backlog == 0 and cur < t:
                        free = t - cur
                        if need <= free:
                            return cur + need
                        need -= free
                        cur = t
                
                backlog += s
        
        if pos == 1:
            backlog = max(0, backlog - (target_time - last))
        
        return cur + backlog + need
    
    low = -10 ** 18
    high = 10 ** 18
    
    while low < high:
        mid = (low + high) // 2
        if finish_time(mid) <= target_finish:
            high = mid
        else:
            low = mid + 1
    
    priority = low
    while priority in used:
        priority += 1
    
    tasks[unknown][2] = priority
    
    events = sorted((tasks[i][0], i) for i in range(n))
    remaining = [tasks[i][1] for i in range(n)]
    done = [0] * n
    
    heap = []
    cur = 0
    i = 0
    
    while i < n or heap:
        if not heap and cur < events[i][0]:
            cur = events[i][0]
        
        while i < n and events[i][0] <= cur:
            task_id = events[i][1]
            heapq.heappush(heap, (-tasks[task_id][2], task_id))
            i += 1
        
        neg_p, task_id = heapq.heappop(heap)
        next_time = events[i][0] if i < n else 10 ** 30
        
        can_print = next_time - cur
        if remaining[task_id] <= can_print:
            cur += remaining[task_id]
            remaining[task_id] = 0
            done[task_id] = cur
        else:
            remaining[task_id] -= can_print
            cur = next_time
            heapq.heappush(heap, (neg_p, task_id))
    
    print(priority)
    print(' '.join(map(str, done)))

if __name__ == "__main__":
    main()
