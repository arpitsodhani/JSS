import sys
from heapq import heappush, heappop

def solve():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    x = int(input_data[idx])
    idx += 1
    y = int(input_data[idx])
    idx += 1
    
    shows = []
    for i in range(n):
        l = int(input_data[idx])
        idx += 1
        r = int(input_data[idx])
        idx += 1
        shows.append((l, r))
    
    # Sort by start time
    shows.sort()
    
    MOD = 10**9 + 7
    
    # Two heaps:
    # - active_tvs: min-heap of (end_time, start_time) for TVs currently in use
    # - available_tvs: max-heap of (-end_time, start_time) for TVs available for reuse
    active_tvs = []
    available_tvs = []
    
    for l, r in shows:
        # Move TVs that ended before l to available_tvs
        while active_tvs and active_tvs[0][0] < l:
            end_time, start_time = heappop(active_tvs)
            heappush(available_tvs, (-end_time, start_time))
        
        reused = False
        if available_tvs:
            # Get the TV with the latest end_time
            neg_end_time, start_time = heappop(available_tvs)
            end_time = -neg_end_time
            
            # Check if it's cheaper to reuse
            if y * (l - end_time) < x:
                # Reuse this TV
                heappush(active_tvs, (r, start_time))
                reused = True
            else:
                # Put it back
                heappush(available_tvs, (neg_end_time, start_time))
        
        if not reused:
            # Rent a new TV
            heappush(active_tvs, (r, l))
    
    # Calculate total cost
    total_cost = 0
    for end_time, start_time in active_tvs:
        cost = (x + y * (end_time - start_time)) % MOD
        total_cost = (total_cost + cost) % MOD
    
    for neg_end_time, start_time in available_tvs:
        end_time = -neg_end_time
        cost = (x + y * (end_time - start_time)) % MOD
        total_cost = (total_cost + cost) % MOD
    
    print(total_cost)

solve()
