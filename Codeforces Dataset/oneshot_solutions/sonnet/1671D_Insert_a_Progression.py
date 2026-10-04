import sys

def solve(n, x, a):
    if n == 0:
        return x - 1
    
    if x == 0:
        return sum(abs(a[i] - a[i+1]) for i in range(n-1))
    
    # Initial score from existing array
    initial = sum(abs(a[i] - a[i+1]) for i in range(n-1))
    
    # Cost within the block [1, 2, ..., x]
    block_cost = x - 1
    
    # Find minimum connection cost
    min_conn = float('inf')
    
    # Insert at beginning (increasing)
    min_conn = min(min_conn, abs(x - a[0]))
    
    # Insert at beginning (decreasing)
    min_conn = min(min_conn, abs(1 - a[0]))
    
    # Insert at end (increasing)
    min_conn = min(min_conn, abs(a[n-1] - 1))
    
    # Insert at end (decreasing)
    min_conn = min(min_conn, abs(a[n-1] - x))
    
    # Insert between elements
    for i in range(n-1):
        edge_cost = abs(a[i] - a[i+1])
        
        # Increasing: a[i] - 1 - 2 - ... - x - a[i+1]
        new_cost_inc = abs(a[i] - 1) + abs(x - a[i+1])
        additional_inc = new_cost_inc - edge_cost
        min_conn = min(min_conn, additional_inc)
        
        # Decreasing: a[i] - x - (x-1) - ... - 1 - a[i+1]
        new_cost_dec = abs(a[i] - x) + abs(1 - a[i+1])
        additional_dec = new_cost_dec - edge_cost
        min_conn = min(min_conn, additional_dec)
    
    return initial + block_cost + min_conn

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n, x = map(int, [input_data[idx], input_data[idx+1]])
        idx += 2
        
        if n > 0:
            a = list(map(int, input_data[idx:idx+n]))
            idx += n
        else:
            a = []
        
        print(solve(n, x, a))

if __name__ == "__main__":
    main()
