import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    
    n = data[idx]
    k = data[idx + 1]
    s = data[idx + 2]
    t = data[idx + 3]
    idx += 4
    
    cars = []
    max_capacity = 0
    for _ in range(n):
        c = data[idx]
        v = data[idx + 1]
        idx += 2
        cars.append((c, v))
        max_capacity = max(max_capacity, v)
    
    stations = data[idx:idx + k]
    stations.sort()
    
    points = [0] + stations + [s]
    segments = []
    max_segment = 0
    for i in range(len(points) - 1):
        d = points[i + 1] - points[i]
        segments.append(d)
        max_segment = max(max_segment, d)
    
    def can(capacity):
        if capacity < max_segment:
            return False
        
        total_time = 0
        for d in segments:
            if capacity >= 2 * d:
                total_time += d
            else:
                total_time += 3 * d - capacity
            
            if total_time > t:
                return False
        
        return total_time <= t
    
    if not can(max_capacity):
        print(-1)
        return
    
    left = max_segment
    right = max_capacity
    while left < right:
        mid = (left + right) // 2
        if can(mid):
            right = mid
        else:
            left = mid + 1
    
    need = left
    answer = min(c for c, v in cars if v >= need)
    print(answer)

if __name__ == "__main__":
    main()
