import sys

def main():
    input_data = sys.stdin.buffer.read().decode().split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    q = int(input_data[idx])
    idx += 1
    v = int(input_data[idx])
    idx += 1
    
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    
    for i in range(1, n + 1):
        a[i] = int(input_data[idx])
        idx += 1
    
    for i in range(1, n + 1):
        b[i] = int(input_data[idx])
        idx += 1
    
    results = []
    
    for _ in range(q):
        query_type = int(input_data[idx])
        idx += 1
        
        if query_type == 1:
            i = int(input_data[idx])
            idx += 1
            x = int(input_data[idx])
            idx += 1
            b[i] = x
        else:
            l = int(input_data[idx])
            idx += 1
            r = int(input_data[idx])
            idx += 1
            
            min_beauty = float('inf')
            
            for l0 in range(l, r + 1):
                or_val = 0
                max_val = 0
                for r0 in range(l0, r + 1):
                    or_val |= b[r0]
                    max_val = max(max_val, a[r0])
                    if or_val >= v:
                        min_beauty = min(min_beauty, max_val)
                        break
            
            if min_beauty == float('inf'):
                results.append(-1)
            else:
                results.append(min_beauty)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
