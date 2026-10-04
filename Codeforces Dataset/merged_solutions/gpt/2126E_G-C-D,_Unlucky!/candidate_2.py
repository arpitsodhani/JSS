# CLAUSE: setup_environment
import sys
from math import gcd

# CLAUSE: solve_logic
def lcm(a, b):
    return a // gcd(a, b) * b

def possible(n, p, s):
    a = [lcm(p[i], s[i]) for i in range(n)]
    g = 0
    for i in range(n):
        g = gcd(g, a[i])
        if g != p[i]:
            return False
    g = 0
    for i in range(n - 1, -1, -1):
        g = gcd(g, a[i])
        if g != s[i]:
            return False
    return True

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        p = data[idx:idx + n]
        idx += n
        s = data[idx:idx + n]
        idx += n
        ans.append('YES' if possible(n, p, s) else 'NO')
    sys.stdout.write('\n'.join(ans))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
