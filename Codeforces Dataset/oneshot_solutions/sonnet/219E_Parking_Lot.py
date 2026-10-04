import sys
from bisect import insort

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    occupied = []  # sorted list of occupied positions
    car_to_space = {}  # track which space each car is in
    
    results = []
    
    for _ in range(m):
        op_type = int(input_data[idx])
        idx += 1
        param = int(input_data[idx])
        idx += 1
        
        if op_type == 1:
            # Car arrives
            car_id = param
            
            if not occupied:
                space = 1
            else:
                candidates = []
                
                # Check space before first occupied
                if occupied[0] > 1:
                    space = 1
                    dist = occupied[0] - 1
                    candidates.append((dist, space))
                
                # Check spaces between consecutive occupied positions
                for i in range(len(occupied) - 1):
                    a, b = occupied[i], occupied[i+1]
                    if b - a > 1:
                        space = (a + b) // 2
                        dist = min(space - a, b - space)
                        candidates.append((dist, space))
                
                # Check space after last occupied
                if occupied[-1] < n:
                    space = n
                    dist = n - occupied[-1]
                    candidates.append((dist, space))
                
                # Choose best: max distance, then min index
                candidates.sort(key=lambda x: (-x[0], x[1]))
                space = candidates[0][1]
            
            insort(occupied, space)
            car_to_space[car_id] = space
            results.append(space)
        
        else:  # op_type == 2
            # Car departs
            car_id = param
            space = car_to_space[car_id]
            occupied.remove(space)
            del car_to_space[car_id]
    
    for r in results:
        print(r)

solve()
