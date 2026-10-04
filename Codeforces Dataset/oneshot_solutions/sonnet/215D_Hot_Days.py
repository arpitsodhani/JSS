import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    
    n = data[0]
    m = data[1]
    idx = 2
    
    answer = 0
    
    for _ in range(n):
        temp = data[idx]
        limit = data[idx + 1]
        fine = data[idx + 2]
        bus_cost = data[idx + 3]
        idx += 4
        
        comfortable = limit - temp
        
        if comfortable <= 0:
            answer += bus_cost + m * fine
            continue
        
        best = bus_cost + m * fine
        
        max_clean_buses = (m + comfortable - 1) // comfortable
        border = min(m, max_clean_buses + 2)
        
        for buses in range(1, border + 1):
            if buses * comfortable >= m:
                bad = 0
            else:
                bad = m - (buses - 1) * comfortable
            cost = buses * bus_cost + bad * fine
            if cost < best:
                best = cost
        
        answer += best
    
    print(answer)

if __name__ == "__main__":
    main()
