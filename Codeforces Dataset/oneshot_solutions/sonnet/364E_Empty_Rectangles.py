import sys

def solve():
    input_data = sys.stdin.buffer.read().decode()
    tokens = input_data.split()
    
    n = int(tokens[0])
    m = int(tokens[1])
    k = int(tokens[2])
    
    # Read the grid (join all remaining tokens)
    grid_str = ''.join(tokens[3:])
    
    # Precompute column prefix sums
    col_prefix = [[0] * m for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            val = int(grid_str[i * m + j])
            col_prefix[i + 1][j] = col_prefix[i][j] + val
    
    count = 0
    
    # For each pair of rows
    for r1 in range(n):
        for r2 in range(r1, n):
            # Count subarrays with sum k
            prefix_sum = 0
            prefix_count = {0: 1}
            
            for c in range(m):
                ones = col_prefix[r2 + 1][c] - col_prefix[r1][c]
                prefix_sum += ones
                target = prefix_sum - k
                if target in prefix_count:
                    count += prefix_count[target]
                if prefix_sum in prefix_count:
                    prefix_count[prefix_sum] += 1
                else:
                    prefix_count[prefix_sum] = 1
    
    print(count)

solve()
