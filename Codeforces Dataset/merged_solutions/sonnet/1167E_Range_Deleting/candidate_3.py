# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def positions(values, limit, size):
    inf = size + 1
    left = [inf] * (limit + 4)
    right = [0] * (limit + 4)
    for i in range(size):
        v = values[i]
        if left[v] == inf:
            left[v] = i + 1
        right[v] = i + 1
    return left, right, inf

def valid_prefix(left, right, limit):
    ok = [True] * (limit + 4)
    border = [0] * (limit + 4)
    mx = 0
    for v in range(1, limit + 1):
        ok[v] = ok[v - 1] and mx <= left[v]
        if right[v] > mx:
            mx = right[v]
        border[v] = mx
    return ok, border

def valid_suffix(left, right, limit, inf):
    ok = [True] * (limit + 5)
    border = [inf] * (limit + 5)
    mn = inf
    for v in range(limit, 0, -1):
        ok[v] = ok[v + 1] and right[v] <= mn
        if left[v] < mn:
            mn = left[v]
        border[v] = mn
    return ok, border

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    a = [int(v) for v in data[2:]]

    first, last, inf = positions(a, x, n)
    pref_ok, pref_last = valid_prefix(first, last, x)
    suff_ok, suff_first = valid_suffix(first, last, x, inf)

    total = 0
    r = 1
    l = 1
    while l <= x and pref_ok[l - 1]:
        r = max(r, l)
        while r <= x:
            if suff_ok[r + 1] and pref_last[l - 1] <= suff_first[r + 1]:
                break
            r += 1
        total += max(0, x - r + 1)
        l += 1

    print(total)

# CLAUSE: finish_program
main()
