import sys

def main():
    input_data = sys.stdin.buffer.read().decode('utf-8').split()
    idx = 0
    
    n = int(input_data[idx])
    idx += 1
    q = int(input_data[idx])
    idx += 1
    m = int(input_data[idx])
    idx += 1
    
    a = [0] * (n + 1)  # 1-indexed
    for i in range(1, n + 1):
        a[i] = int(input_data[idx])
        idx += 1
    
    # Process queries
    for _ in range(q):
        query_type = int(input_data[idx])
        idx += 1
        l = int(input_data[idx])
        idx += 1
        r = int(input_data[idx])
        idx += 1
        
        if query_type == 1:
            # Cyclic shift right
            temp = a[r]
            for i in range(r, l, -1):
                a[i] = a[i - 1]
            a[l] = temp
        else:
            # Reverse
            i, j = l, r
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
    
    # Output important indices
    result = []
    for _ in range(m):
        b = int(input_data[idx])
        idx += 1
        result.append(str(a[b]))
    
    print(' '.join(result))

if __name__ == "__main__":
    main()
