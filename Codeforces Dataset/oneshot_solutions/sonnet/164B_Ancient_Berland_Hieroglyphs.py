import sys

def max_substring_as_subsequence(a, b):
    n = len(a)
    m = len(b)
    max_len = 0
    
    for l in range(n):
        b_idx = 0
        for r in range(l, n):
            found = False
            while b_idx < m:
                if b[b_idx] == a[r]:
                    b_idx += 1
                    found = True
                    break
                b_idx += 1
            
            if found:
                max_len = max(max_len, r - l + 1)
            else:
                break
    
    return max_len

def solve(circle_a, circle_b):
    n = len(circle_a)
    m = len(circle_b)
    max_result = 0
    
    for break_a in range(n):
        a = circle_a[break_a:] + circle_a[:break_a]
        for break_b in range(m):
            b = circle_b[break_b:] + circle_b[:break_b]
            result = max_substring_as_subsequence(a, b)
            max_result = max(max_result, result)
    
    return max_result

lines = sys.stdin.read().strip().split('\n')
n, m = map(int, lines[0].split())
circle_a = list(map(int, lines[1].split()))
circle_b = list(map(int, lines[2].split()))

print(solve(circle_a, circle_b))
