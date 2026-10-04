import sys

def solve():
    t = sys.stdin.read().strip()
    n_t = len(t)
    
    # Try each possible length of original message s
    for n in range(n_t // 2 + 1, n_t):
        s = t[:n]
        k = 2 * n - n_t
        
        # Check if t is formed by overlapping two copies of s
        if s[-k:] == s[:k] and t == s + s[k:]:
            print("YES")
            print(s)
            return
    
    print("NO")

solve()
