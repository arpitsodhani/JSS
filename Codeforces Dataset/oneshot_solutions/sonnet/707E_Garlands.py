import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    k = int(input_data[idx + 2])
    idx += 3
    
    # Build 2D prefix sum for each garland
    garland_prefix = []
    
    for _ in range(k):
        num_bulbs = int(input_data[idx])
        idx += 1
        
        # Create grid for this garland (1-indexed)
        grid = [[0] * (m + 1) for _ in range(n + 1)]
        
        for _ in range(num_bulbs):
            r = int(input_data[idx])
            c = int(input_data[idx + 1])
            v = int(input_data[idx + 2])
            idx += 3
            grid[r][c] = v
        
        # Compute 2D prefix sum
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = grid[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        garland_prefix.append(prefix)
    
    # All garlands initially on
    garland_state = [True] * k
    
    q = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(q):
        query_type = input_data[idx]
        if query_type == "ASK":
            r1 = int(input_data[idx + 1])
            c1 = int(input_data[idx + 2])
            r2 = int(input_data[idx + 3])
            c2 = int(input_data[idx + 4])
            idx += 5
            
            total = 0
            for g_idx in range(k):
                if garland_state[g_idx]:
                    # Rectangle sum using 2D prefix sum
                    total += garland_prefix[g_idx][r2][c2] - garland_prefix[g_idx][r1-1][c2] - garland_prefix[g_idx][r2][c1-1] + garland_prefix[g_idx][r1-1][c1-1]
            results.append(total)
        else:  # SWITCH
            g = int(input_data[idx + 1]) - 1  # 1-indexed to 0-indexed
            idx += 2
            garland_state[g] = not garland_state[g]
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
