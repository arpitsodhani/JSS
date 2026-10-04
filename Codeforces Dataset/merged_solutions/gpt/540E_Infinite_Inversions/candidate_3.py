# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from bisect import bisect_left
    from array import array

    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    mp = {}

    idx = 1
    for _ in range(n):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        va = mp.get(a, a)
        vb = mp.get(b, b)
        mp[a] = vb
        mp[b] = va

    items = [(k, v) for k, v in mp.items() if k != v]
    items.sort()

    pos = [x for x, _ in items]
    vals = [v for _, v in items]

    ans = 0
    m = len(items)

    for x, y in items:
        if x < y:
            ans += y - x - 1 - (bisect_left(pos, y) - bisect_left(pos, x + 1))
        else:
            ans += x - y - 1 - (bisect_left(pos, x) - bisect_left(pos, y + 1))

    comp = {v: i + 1 for i, v in enumerate(sorted(vals))}
    bit = array('i', [0]) * (m + 2)

    def add(i):
        while i <= m:
            bit[i] += 1
            i += i & -i

    def sum_pref(i):
        s = 0
        while i:
            s += bit[i]
            i -= i & -i
        return s

    seen = 0
    for v in vals:
        c = comp[v]
        ans += seen - sum_pref(c)
        add(c)
        seen += 1

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
