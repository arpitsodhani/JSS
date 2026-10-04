import sys

def solve(a):
    n = len(a)
    if n <= 1:
        return 0
    
    sorted_a = sorted(a)
    max_keep = 0
    
    # Try all contiguous segments in sorted array
    for start in range(n):
        for end in range(start, n):
            target_len = end - start + 1
            
            # Find if we can match sorted_a[start:end+1] as a subsequence in a
            j = 0
            for i in range(n):
                if j < target_len and a[i] == sorted_a[start + j]:
                    j += 1
            
            # If we matched the entire target segment
            if j == target_len:
                max_keep = max(max_keep, target_len)
    
    return n - max_keep

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        print(solve(a))

if __name__ == "__main__":
    main()
