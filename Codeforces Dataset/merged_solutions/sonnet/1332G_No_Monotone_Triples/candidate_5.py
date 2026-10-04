# CLAUSE: setup_environment
import sys

def upper_count_by_value(st, top, arr, x, kind):
    l = 1
    r = top
    ans = 0
    while l <= r:
        m = (l + r) // 2
        good = arr[st[m]] < x if kind == 0 else arr[st[m]] > x
        if good:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans

def lower_count_by_index(st, top, x):
    l = 1
    r = top
    ans = top + 1
    while l <= r:
        m = (l + r) // 2
        if st[m] <= x:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

def mark(tree, n, p):
    while p <= n:
        tree[p] += 1
        p += p & -p

def prefix(tree, p):
    s = 0
    while p:
        s += tree[p]
        p -= p & -p
    return s

def kth(tree, k):
    p = 0
    bit = 1 << (len(tree).bit_length())
    while bit:
        nxt = p + bit
        if nxt < len(tree) and tree[nxt] < k:
            k -= tree[nxt]
            p = nxt
        bit >>= 1
    return p + 1

# CLAUSE: solve_logic
def prepare(arr):
    n = len(arr) - 1
    lim3 = [n + 1] * (n + 2)
    lim4 = [n + 1] * (n + 2)
    res3 = [None] * (n + 2)
    res4 = [None] * (n + 2)
    state = [0] * (n + 2)
    smin = [0] * (n + 2)
    smax = [0] * (n + 2)
    amin = amax = len_min = len_max = 0
    tree = [0] * (n + 3)
    mark(tree, n + 1, n + 1)
    for i in range(n, 0, -1):
        x = arr[i]
        while amin and arr[smin[amin]] > x:
            v = smin[amin]
            state[v] -= 1
            if state[v] == 0:
                mark(tree, n + 1, v)
            amin -= 1
            len_min = 0
        while amax and arr[smax[amax]] < x:
            v = smax[amax]
            state[v] -= 1
            if state[v] == 0:
                mark(tree, n + 1, v)
            amax -= 1
            len_max = 0
        lo = upper_count_by_value(smin, amin, arr, x, 0)
        hi = upper_count_by_value(smax, amax, arr, x, 1)
        lim3[i] = i + max(len_min, len_max) + 1
        res3[i] = (i, lim3[i] - 1, lim3[i])
        if lo and hi:
            start = smin[lo]
            if smax[hi] > start:
                start = smax[hi]
            want = prefix(tree, start - 1) + 1
            if prefix(tree, n + 1) >= want:
                lim4[i] = kth(tree, want)
                if lim4[i] <= n:
                    p = lower_count_by_index(smin, amin, lim4[i])
                    q = lower_count_by_index(smax, amax, lim4[i])
                    m = smin[p]
                    z = smax[q]
                    if m > z:
                        m, z = z, m
                    res4[i] = (i, m, z, lim4[i])
        amin += 1
        smin[amin] = i
        amax += 1
        smax[amax] = i
        len_min += 1
        len_max += 1
        state[i] = 2
        if i + 1 <= n and lim3[i + 1] < lim3[i]:
            lim3[i] = lim3[i + 1]
            res3[i] = res3[i + 1]
        if i + 1 <= n and lim4[i + 1] < lim4[i]:
            lim4[i] = lim4[i + 1]
            res4[i] = res4[i + 1]
    return lim3, lim4, res3, res4

def answer(data):
    n, q = data[0], data[1]
    arr = [0] + data[2:2 + n]
    lim3, lim4, res3, res4 = prepare(arr)
    lines = []
    p = n + 2
    for _ in range(q):
        l = data[p]
        r = data[p + 1]
        p += 2
        if lim4[l] <= r:
            lines.append("4")
            lines.append("{} {} {} {}".format(*res4[l]))
        elif lim3[l] <= r:
            lines.append("3")
            lines.append("{} {} {}".format(*res3[l]))
        else:
            lines.append("0")
    return "\n".join(lines)

# CLAUSE: finish_program
def main():
    data = [int(x) for x in sys.stdin.buffer.read().split()]
    sys.stdout.write(answer(data))

if __name__ == "__main__":
    main()
