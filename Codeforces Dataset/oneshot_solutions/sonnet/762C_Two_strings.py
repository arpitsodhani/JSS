def solve(a, b):
    n = len(a)
    m = len(b)
    
    if m == 0:
        return ""
    
    # left[i] = max number of chars from start of b that match in a[0:i]
    left = [0] * (n + 1)
    j = 0
    for i in range(n):
        left[i] = j
        if j < m and a[i] == b[j]:
            j += 1
    left[n] = j
    
    # right[i] = max number of chars from end of b that match in a[i:]
    right = [0] * (n + 1)
    count = 0
    j = m - 1
    for i in range(n - 1, -1, -1):
        right[i + 1] = count
        if j >= 0 and a[i] == b[j]:
            count += 1
            j -= 1
    right[0] = count
    
    # Find the best split
    max_len = 0
    best_left = 0
    best_right = 0
    
    for i in range(n + 1):
        l = left[i]
        r = right[i]
        
        # Make sure they don't overlap
        if l + r <= m:
            total = l + r
            if total > max_len:
                max_len = total
                best_left = l
                best_right = r
    
    if max_len == 0:
        return "-"
    
    # Reconstruct the answer
    return b[:best_left] + b[m - best_right:]

# Read input
a = input().strip()
b = input().strip()

# Solve and print result
print(solve(a, b))
