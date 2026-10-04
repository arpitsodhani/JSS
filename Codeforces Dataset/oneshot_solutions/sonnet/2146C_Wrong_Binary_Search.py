def solve(n, s):
    # Check for impossible configurations
    for i in range(n):
        if s[i] == '0':
            left_stable = (i == 0 or s[i - 1] == '1')
            right_stable = (i == n - 1 or s[i + 1] == '1')
            if left_stable and right_stable:
                return None
    
    # Build permutation
    perm = [0] * n
    
    # Place stable values at their natural positions
    for i in range(n):
        if s[i] == '1':
            perm[i] = i + 1
    
    # Handle unstable segments
    i = 0
    while i < n:
        if s[i] == '0':
            # Find the end of this unstable segment
            j = i
            while j < n and s[j] == '0':
                j += 1
            
            # Rotate the segment: [v1, v2, ..., vk] -> [v2, v3, ..., vk, v1]
            values = list(range(i + 1, j + 1))
            rotated = values[1:] + [values[0]]
            
            for k in range(i, j):
                perm[k] = rotated[k - i]
            
            i = j
        else:
            i += 1
    
    return perm

# Main execution
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    result = solve(n, s)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))
