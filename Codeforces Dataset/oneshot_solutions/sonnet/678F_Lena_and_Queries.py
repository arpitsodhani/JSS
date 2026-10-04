import sys

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    
    pairs = {}  # query_id -> (a, b)
    results = []
    
    for query_num in range(1, n + 1):
        query_type = int(input_data[idx])
        idx += 1
        
        if query_type == 1:
            # Add pair (a, b)
            a = int(input_data[idx])
            idx += 1
            b = int(input_data[idx])
            idx += 1
            pairs[query_num] = (a, b)
        
        elif query_type == 2:
            # Remove pair from query i
            remove_idx = int(input_data[idx])
            idx += 1
            if remove_idx in pairs:
                del pairs[remove_idx]
        
        else:  # query_type == 3
            # Find max(x*q + y) for all pairs (x, y)
            q = int(input_data[idx])
            idx += 1
            
            if not pairs:
                results.append("EMPTY SET")
            else:
                max_val = max(a * q + b for a, b in pairs.values())
                results.append(str(max_val))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
