import sys

def solve_case(n, h):
    results = []
    for i in range(n):
        chain_length = n - 1
        
        from_left = [0] * chain_length
        from_left[0] = h[i]
        for j in range(1, chain_length):
            prev_vessel = (i + j) % n
            from_left[j] = max(from_left[j - 1], h[prev_vessel])
        
        from_right = [0] * chain_length
        from_right[chain_length - 1] = h[(i - 1) % n]
        for j in range(chain_length - 2, -1, -1):
            curr_vessel = (i + 1 + j) % n
            from_right[j] = max(from_right[j + 1], h[curr_vessel])
        
        total_water = 0
        for j in range(chain_length):
            water_level = min(from_left[j], from_right[j])
            total_water += water_level
        
        results.append(total_water)
    
    return results

def main():
    data = sys.stdin.buffer.read().decode().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        h = list(map(int, data[idx:idx+n]))
        idx += n
        
        results = solve_case(n, h)
        print(' '.join(map(str, results)))

if __name__ == '__main__':
    main()
