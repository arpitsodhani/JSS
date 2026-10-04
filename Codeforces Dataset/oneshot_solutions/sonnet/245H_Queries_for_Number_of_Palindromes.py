import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    s = input_data[idx]
    idx += 1
    n = len(s)
    
    q = int(input_data[idx])
    idx += 1
    
    # DP to check if s[i:j+1] is palindrome
    is_pal = [[False] * n for _ in range(n)]
    
    # Base case: single characters
    for i in range(n):
        is_pal[i][i] = True
    
    # Base case: two characters
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_pal[i][i + 1] = True
    
    # Fill for lengths 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i + 1][j - 1]:
                is_pal[i][j] = True
    
    # Precompute count of palindromes for each range [l, r]
    cnt = [[0] * n for _ in range(n)]
    
    # Base case: single characters
    for i in range(n):
        cnt[i][i] = 1
    
    # Fill using DP with inclusion-exclusion principle
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            cnt[l][r] = cnt[l + 1][r] + cnt[l][r - 1] - cnt[l + 1][r - 1]
            if is_pal[l][r]:
                cnt[l][r] += 1
    
    # Answer queries
    results = []
    for _ in range(q):
        l = int(input_data[idx]) - 1  # Convert to 0-indexed
        idx += 1
        r = int(input_data[idx]) - 1  # Convert to 0-indexed
        idx += 1
        results.append(cnt[l][r])
    
    print('\n'.join(map(str, results)))

solve()
