import sys
import heapq

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    idx += 1
    
    events = []
    
    for layer in range(n):
        k = data[idx]
        left_wall = data[idx + 1]
        right_wall = data[idx + 2]
        idx += 3
        
        lengths = data[idx:idx + k]
        idx += k
        
        total_doors = sum(lengths)
        free_space = right_wall - left_wall - total_doors
        
        prefix = 0
        events.append((left_wall, layer, left_wall + free_space))
        for length in lengths:
            prefix += length
            start = left_wall + prefix
            events.append((start, layer, start + free_space))
    
    events.sort()
    
    current = [-1] * n
    active = 0
    heap = []
    answer = 0
    
    i = 0
    while i < len(events):
        x = events[i][0]
        
        while i < len(events) and events[i][0] == x:
            _, layer, right = events[i]
            if current[layer] == -1:
                active += 1
            current[layer] = right
            heapq.heappush(heap, (right, layer))
            i += 1
        
        while heap and current[heap[0][1]] != heap[0][0]:
            heapq.heappop(heap)
        
        if active == n:
            best_right = heap[0][0]
            if best_right > x:
                answer = max(answer, best_right - x)
    
    print(answer)

if __name__ == "__main__":
    main()
