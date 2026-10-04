# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from array import array

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        n = data[0]
        a = array('b')
        b = array('b')
        p = 1
        for _ in range(n):
            a.append(data[p] - 1)
            b.append(data[p + 1] - 1)
            p += 2

        pow5 = [1]
        for _ in range(9):
            pow5.append(pow5[-1] * 5)
        base = pow5[9]

        code_to_id = array('h', [-1]) * base
        codes = []
        occs = []

        def gen(pos, rem, code, occ):
            if pos == 9:
                code_to_id[code] = len(codes)
                codes.append(code)
                occs.append(occ)
                return
            step = pow5[pos]
            for c in range(rem + 1):
                gen(pos + 1, rem - c, code + c * step, occ + c)

        gen(0, 4, 0, 0)

        s = len(codes)
        occ = array('b', occs)
        cnt = array('b', [0]) * (s * 9)
        rem_id = array('H', [0]) * (s * 9)
        add_id = array('h', [-1]) * (s * 9)

        for i, code in enumerate(codes):
            off = i * 9
            for f in range(9):
                c = (code // pow5[f]) % 5
                cnt[off + f] = c
                rem_id[off + f] = code_to_id[code - c * pow5[f]]
                if occ[i] < 4:
                    add_id[off + f] = code_to_id[code + pow5[f]]

        empty = code_to_id[0]

        def normalize(cid, k, f):
            c = cnt[cid * 9 + f]
            if c:
                cid = rem_id[cid * 9 + f]
            cap = 4 - occ[cid]
            while cap and k < n and a[k] == f:
                cid = add_id[cid * 9 + b[k]]
                k += 1
                cap -= 1
            return cid, k

        start_cid, start_k = normalize(empty, 0, 0)
        total = (n + 1) * 9 * s
        inf = 65535
        dist = array('H', [inf]) * total

        start = (start_k * 9) * s + start_cid
        dist[start] = 0
        q = array('I', [start])
        head = 0

        while head < len(q):
            idx = q[head]
            head += 1
            d = dist[idx]

            cid = idx % s
            t = idx // s
            f = t % 9
            k = t // 9

            if k == n and cid == empty:
                print(d + 2 * n)
                return

            if f:
                ncid, nk = normalize(cid, k, f - 1)
                ni = (nk * 9 + f - 1) * s + ncid
                if dist[ni] == inf:
                    dist[ni] = d + 1
                    q.append(ni)

            if f < 8:
                ncid, nk = normalize(cid, k, f + 1)
                ni = (nk * 9 + f + 1) * s + ncid
                if dist[ni] == inf:
                    dist[ni] = d + 1
                    q.append(ni)

    main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
