import sys

memo = {}

def dp(rows, cols, target):
    if target == 0 or target == rows * cols:
        return 0
    
    if target > rows * cols or target < 0:
        return float('inf')
    
    if (rows, cols, target) in memo:
        return memo[(rows, cols, target)]
    
    ans = float('inf')
    
    # Try horizontal breaks
    for i in range(1, rows):
        cost = cols * cols
        for j in range(target + 1):
            ans = min(ans, cost + dp(i, cols, j) + dp(rows - i, cols, target - j))
    
    # Try vertical breaks
    for i in range(1, cols):
        cost = rows * rows
        for j in range(target + 1):
            ans = min(ans, cost + dp(rows, i, j) + dp(rows, cols - i, target - j))
    
    memo[(rows, cols, target)] = ans
    return ans

def main():
    input_data = sys.stdin.read().strip().split()
    idx = 0
    q = int(input_data[idx])
    idx += 1
    
    results = []
    for _ in range(q):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        k = int(input_data[idx + 2])
        idx += 3
        
        results.append(str(dp(n, m, k)))
    
    print('\n'.join(results))

if __name__ == '__main__':
    main()
