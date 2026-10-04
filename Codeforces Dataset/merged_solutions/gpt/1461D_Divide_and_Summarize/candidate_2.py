# CLAUSE: setup_environment
import sys
from bisect import bisect_right

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    for _ in range(t):
        n = data[p]
        q = data[p + 1]
        p += 2
        a = data[p:p + n]
        p += n
        a.sort()
        pref = [0] * (n + 1)
        for i, x in enumerate(a, 1):
            pref[i] = pref[i - 1] + x
        possible = set()
        stack = [(0, n - 1)]
        while stack:
            l, r = stack.pop()
            total = pref[r + 1] - pref[l]
            possible.add(total)
            if a[l] == a[r]:
                continue
            mid = (a[l] + a[r]) // 2
            m = bisect_right(a, mid, l, r + 1)
            if m == l or m == r + 1:
                continue
            stack.append((l, m - 1))
            stack.append((m, r))
        for _ in range(q):
            s = data[p]
            p += 1
            out.append('Yes' if s in possible else 'No')
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
