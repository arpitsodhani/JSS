import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    starts = []
    ends = []
    
    for _ in range(n):
        a = int(data[idx])
        h = int(data[idx + 1])
        left = int(data[idx + 2])
        right = int(data[idx + 3])
        idx += 4
        
        if left < 100:
            q = (100 - left) / 100.0
            starts.append((a - h, q))
            ends.append((a, q))
        
        if right < 100:
            q = (100 - right) / 100.0
            starts.append((a + 1, q))
            ends.append((a + h + 1, q))
    
    mushrooms = []
    for _ in range(m):
        b = int(data[idx])
        z = int(data[idx + 1])
        idx += 2
        mushrooms.append((b, z))
    
    starts.sort()
    ends.sort()
    mushrooms.sort()
    
    start_idx = 0
    end_idx = 0
    current = 1.0
    answer = 0.0
    
    for x, power in mushrooms:
        while start_idx < len(starts) and starts[start_idx][0] <= x:
            current *= starts[start_idx][1]
            start_idx += 1
        
        while end_idx < len(ends) and ends[end_idx][0] <= x:
            current /= ends[end_idx][1]
            end_idx += 1
        
        answer += power * current
    
    print("{:.10f}".format(answer))

if __name__ == "__main__":
    main()
