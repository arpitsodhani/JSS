# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    t = data[pos]
    pos += 1
    out = []

# CLAUSE: solve_logic
    for _ in range(t):
        n = data[pos]
        m = data[pos + 1]
        pos += 2
        a = data[pos:pos + m]
        pos += m
        a.sort()
        total = 0
        for left in range(1, n):
            right = n - left
            c1 = m - bisect_left(a, left)
            c2 = m - bisect_left(a, right)
            both = m - bisect_left(a, left if left > right else right)
            total += c1 * c2 - both
        out.append(str(total))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
