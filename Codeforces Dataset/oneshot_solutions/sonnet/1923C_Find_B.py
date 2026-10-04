import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        q = int(data[idx + 1])
        idx += 2
        
        c = [0] + [int(data[idx + i]) for i in range(n)]
        idx += n
        
        # Prefix sums for efficient range queries
        prefix_sum = [0] * (n + 1)
        prefix_count_ones = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + c[i]
            prefix_count_ones[i] = prefix_count_ones[i - 1] + (1 if c[i] == 1 else 0)
        
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            
            length = r - l + 1
            subarray_sum = prefix_sum[r] - prefix_sum[l - 1]
            count_ones = prefix_count_ones[r] - prefix_count_ones[l - 1]
            
            if length >= 2 and subarray_sum > 2 * count_ones:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    main()
