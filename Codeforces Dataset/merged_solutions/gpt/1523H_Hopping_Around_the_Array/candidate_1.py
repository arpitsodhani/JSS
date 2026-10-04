# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    it = iter(data)
    n = next(it)
    q = next(it)
    a = [0] + [next(it) for _ in range(n)]

    L = array('I')
    R = array('I')
    QK = array('I')
    max_k = 0
    for _ in range(q):
        l = next(it)
        r = next(it)
        k = next(it)
        L.append(l)
        R.append(r)
        QK.append(k)
        if k > max_k:
            max_k = k

    K = max_k

    lg = array('B', [0]) * (n + 2)
    for i in range(2, n + 2):
        lg[i] = lg[i >> 1] + 1

    def build_sparse(arr):
        st = [arr]
        length = 2
        half = 1
        while length <= n:
            prev = st[-1]
            row = array('I', [0]) * (n + 1)
            lim = n - length + 2
            for i in range(1, lim):
                x = prev[i]
                y = prev[i + half]
                row[i] = x if x >= y else y
            st.append(row)
            half = length
            length <<= 1
        return st

    levels = []

    base = []
    for d in range(K + 1):
        row = array('I', [0]) * (n + 1)
        for i in range(1, n + 1):
            v = i + a[i] + d
            row[i] = n if v > n else v
        base.append(row)
    levels.append(base)

    P = 1
    while (1 << P) <= n:
        P += 1

    for p in range(P - 1):
        prev_level = levels[p]
        nxt = [array('I', [0]) * (n + 1) for _ in range(K + 1)]

        for rem in range(K + 1):
            st = build_sparse(prev_level[rem])
            for used in range(K - rem + 1):
                out = nxt[rem + used]
                rarr = prev_level[used]
                for i in range(1, n + 1):
                    rr = rarr[i]
                    ln = rr - i + 1
                    j = lg[ln]
                    span = 1 << j
                    x = st[j][i]
                    y = st[j][rr - span + 1]
                    v = x if x >= y else y
                    if v > out[i]:
                        out[i] = v

        levels.append(nxt)

    ans = array('I', [0]) * q
    pos = [array('I', L) for _ in range(K + 1)]

    for p in range(P - 1, -1, -1):
        tmp = [array('I', [0]) * q for _ in range(K + 1)]
        level = levels[p]

        for rem in range(K + 1):
            st = build_sparse(level[rem])
            for used in range(K - rem + 1):
                d = rem + used
                td = tmp[d]
                pc = pos[used]
                for idx in range(q):
                    if d <= QK[idx]:
                        left = L[idx]
                        rr = pc[idx]
                        ln = rr - left + 1
                        j = lg[ln]
                        span = 1 << j
                        x = st[j][left]
                        y = st[j][rr - span + 1]
                        v = x if x >= y else y
                        if v > td[idx]:
                            td[idx] = v

        add = 1 << p
        for idx in range(q):
            k = QK[idx]
            if L[idx] != R[idx] and tmp[k][idx] < R[idx]:
                ans[idx] += add
                for d in range(k + 1):
                    pos[d][idx] = tmp[d][idx]

    out = []
    for idx in range(q):
        if L[idx] == R[idx]:
            out.append("0")
        else:
            out.append(str(ans[idx] + 1))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = None
