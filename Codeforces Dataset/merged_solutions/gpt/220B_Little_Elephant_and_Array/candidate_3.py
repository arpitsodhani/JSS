# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from math import isqrt

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n, m = data[0], data[1]
    a = data[2:2 + n]
    pos = 2 + n

    queries = []
    for i in range(m):
        l = data[pos] - 1
        r = data[pos + 1] - 1
        pos += 2
        queries.append((l, r, i))

    block = max(1, isqrt(n))
    queries.sort(key=lambda q: (q[0] // block, q[1] if (q[0] // block) % 2 == 0 else -q[1]))

    freq = [0] * (n + 1)
    ans = [0] * m
    cur = 0
    left = 0
    right = -1

    def add(idx):
        global cur
        x = a[idx]
        if x > n:
            return
        if freq[x] == x:
            cur -= 1
        freq[x] += 1
        if freq[x] == x:
            cur += 1

    def remove(idx):
        global cur
        x = a[idx]
        if x > n:
            return
        if freq[x] == x:
            cur -= 1
        freq[x] -= 1
        if freq[x] == x:
            cur += 1

    for l, r, qi in queries:
        while right < r:
            right += 1
            add(right)
        while right > r:
            remove(right)
            right -= 1
        while left < l:
            remove(left)
            left += 1
        while left > l:
            left -= 1
            add(left)
        ans[qi] = cur

    sys.stdout.write("\n".join(map(str, ans)))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
