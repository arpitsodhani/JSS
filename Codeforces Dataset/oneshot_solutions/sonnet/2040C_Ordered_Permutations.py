import sys

def solve(n, k):
    max_k = 1 << (n - 1)  # 2^(n-1)
    if k > max_k:
        return "-1"
    
    def helper(start, length, k):
        if length == 1:
            return [start]
        
        mid = 1 << (length - 2)  # 2^(length - 2)
        
        if k <= mid:
            return [start] + helper(start + 1, length - 1, k)
        else:
            return helper(start + 1, length - 1, k - mid) + [start]
    
    result = helper(1, n, k)
    return ' '.join(map(str, result))

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2
        
        result = solve(n, k)
        print(result)

if __name__ == "__main__":
    main()
