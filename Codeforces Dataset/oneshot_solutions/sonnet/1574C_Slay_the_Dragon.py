import sys
from bisect import bisect_left

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    
    heroes = []
    for i in range(n):
        heroes.append(int(input_data[idx]))
        idx += 1
    
    heroes.sort()
    total_sum = sum(heroes)
    
    m = int(input_data[idx])
    idx += 1
    
    for _ in range(m):
        x = int(input_data[idx])
        y = int(input_data[idx + 1])
        idx += 2
        
        pos = bisect_left(heroes, x)
        
        min_cost = float('inf')
        
        # Try the smallest hero >= x
        if pos < n:
            h = heroes[pos]
            cost = max(0, x - h) + max(0, y - (total_sum - h))
            min_cost = min(min_cost, cost)
        
        # Try the largest hero < x
        if pos > 0:
            h = heroes[pos - 1]
            cost = max(0, x - h) + max(0, y - (total_sum - h))
            min_cost = min(min_cost, cost)
        
        print(min_cost)

main()
