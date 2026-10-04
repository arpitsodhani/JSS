# CLAUSE: setup_environment
import sys

def add(bit, i, v):
    n = len(bit) - 1
    while i <= n:
        bit[i] += v
        i += i & -i

def pref(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

def first_at_least(bit, pos):
    total = pref(bit, len(bit) - 1)
    target = pref(bit, pos - 1) + 1
    if total < target:
        return len(bit) - 1
    idx = 0
    step = 1 << (len(bit).bit_length())
    while step:
        nxt = idx + step
        if nxt < len(bit) and bit[nxt] < target:
            target -= bit[nxt]
            idx = nxt
        step >>= 1
    return idx + 1

def left_value_less(stack, top, arr, value):
    lo, hi = 1, top + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if arr[stack[mid]] < value:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

def left_value_greater(stack, top, arr, value):
    lo, hi = 1, top + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if arr[stack[mid]] > value:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1

def first_index_not_after(stack, top, value):
    lo, hi = 1, top + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if stack[mid] > value:
            lo = mid + 1
        else:
            hi = mid
    return lo

# CLAUSE: solve_logic
def build_answers(a, n):
    b = [n + 1] * (n + 2)
    c = [n + 1] * (n + 2)
    cnt = [0] * (n + 2)
    triple = [[0, 0, 0] for _ in range(n + 2)]
    quad = [[0, 0, 0, 0] for _ in range(n + 2)]
    low = [0] * (n + 2)
    high = [0] * (n + 2)
    p_low = p_high = run_low = run_high = 0
    bit = [0] * (n + 3)
    add(bit, n + 1, 1)
    for i in range(n, 0, -1):
        while p_low and a[low[p_low]] > a[i]:
            u = low[p_low]
            cnt[u] -= 1
            if cnt[u] == 0:
                add(bit, u, 1)
            p_low -= 1
            run_low = 0
        while p_high and a[high[p_high]] < a[i]:
            u = high[p_high]
            cnt[u] -= 1
            if cnt[u] == 0:
                add(bit, u, 1)
            p_high -= 1
            run_high = 0
        s1 = left_value_less(low, p_low, a, a[i])
        s2 = left_value_greater(high, p_high, a, a[i])
        b[i] = i + max(run_low, run_high) + 1
        triple[i] = [i, b[i] - 1, b[i]]
        if s1 and s2:
            c[i] = first_at_least(bit, max(low[s1], high[s2]))
            if c[i] <= n:
                u = first_index_not_after(low, p_low, c[i])
                v = first_index_not_after(high, p_high, c[i])
                x, y = low[u], high[v]
                if x > y:
                    x, y = y, x
                quad[i] = [i, x, y, c[i]]
        p_low += 1
        low[p_low] = i
        p_high += 1
        high[p_high] = i
        run_low += 1
        run_high += 1
        cnt[i] += 2
        if i < n and b[i] > b[i + 1]:
            b[i] = b[i + 1]
            triple[i] = triple[i + 1]
        if i < n and c[i] > c[i + 1]:
            c[i] = c[i + 1]
            quad[i] = quad[i + 1]
    return b, c, triple, quad

# CLAUSE: finish_program
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    arr = [0] + data[2:2 + n]
    b, c, triple, quad = build_answers(arr, n)
    out = []
    at = 2 + n
    for _ in range(q):
        l, r = data[at], data[at + 1]
        at += 2
        if r >= c[l]:
            out.append("4")
            out.append(" ".join(map(str, quad[l])))
        elif r >= b[l]:
            out.append("3")
            out.append(" ".join(map(str, triple[l])))
        else:
            out.append("0")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
