import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n, k, b, c = data[:4]
    t = data[4:4 + n]
    
    blog_cost = min(b, 5 * c)
    answer = 10 ** 30
    
    for r in range(5):
        events = []
        
        for value in t:
            q, rem = divmod(value, 5)
            
            if r >= rem:
                start_q = q
                extra = (r - rem) * c
                base = -q * blog_cost + extra
            else:
                start_q = q + 1
                extra = (r - rem + 5) * c
                base = -(q + 1) * blog_cost + extra
            
            events.append((start_q, base))
        
        events.sort()
        
        chosen = []
        chosen_sum = 0
        i = 0
        
        while i < n:
            current_q = events[i][0]
            
            while i < n and events[i][0] == current_q:
                val = events[i][1]
                
                if len(chosen) < k:
                    heapq.heappush(chosen, -val)
                    chosen_sum += val
                elif val < -chosen[0]:
                    chosen_sum += val + heapq.heappop(chosen)
                    heapq.heappush(chosen, -val)
                
                i += 1
            
            if len(chosen) == k:
                answer = min(answer, k * current_q * blog_cost + chosen_sum)
    
    print(answer)

if __name__ == "__main__":
    main()
