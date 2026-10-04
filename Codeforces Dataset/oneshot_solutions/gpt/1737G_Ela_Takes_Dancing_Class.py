import sys
from bisect import bisect_right

def main():
    input = sys.stdin.readline
    n, d, q = map(int, input().split())
    a = list(map(int, input().split()))
    s = input().strip()

    imm = [a[i] for i in range(n) if s[i] == '0']
    mov = [a[i] for i in range(n) if s[i] == '1']
    r = len(mov)

    def comp(x):
        return x - bisect_right(imm, x)

    b = [comp(x) for x in mov]
    b.sort()

    def expand(u):
        lo, hi = u, u + len(imm)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid - bisect_right(imm, mid) >= u:
                hi = mid
            else:
                lo = mid + 1
        return lo

    if r == 1:
        ans = []
        start = b[0]
        for _ in range(q):
            k, m = map(int, input().split())
            x = start + k * d
            y = expand(x)
            cnt_imm = bisect_right(imm, y)
            if m <= cnt_imm:
                ans.append(str(imm[m - 1]))
            else:
                ans.append(str(y))
        print("\n".join(ans))
        return

    h = [b[i] - (i + 1) for i in range(r)]
    mx = max(h)

    if d == 1:
        need = sum(mx - x for x in h)
        ans = []
        for _ in range(q):
            k, m = map(int, input().split())
            if k <= need:
                cur = h[:]
                rem = k
                while rem:
                    mn = min(cur)
                    nxt = min([x for x in cur if x > mn], default=10**30)
                    c = cur.count(mn)
                    step = min((nxt - mn + 0), rem)
                    if step == 0:
                        step = 1
                    add = min(step, rem)
                    for i in range(r):
                        if cur[i] == mn:
                            cur[i] += add
                    rem -= add
                vals = [cur[i] + i + 1 for i in range(r)]
            else:
                add = k - need
                vals = [mx + add + i + 1 for i in range(r)]
            merged = []
            i = j = 0
            mov_exp = [expand(x) for x in vals]
            while i < len(imm) or j < len(mov_exp):
                if j == len(mov_exp) or (i < len(imm) and imm[i] < mov_exp[j]):
                    merged.append(imm[i])
                    i += 1
                else:
                    merged.append(mov_exp[j])
                    j += 1
            ans.append(str(merged[m - 1]))
        print("\n".join(ans))
        return

    limit = min(max([0] + [int(line.split()[0]) for line in []]), 0)
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    maxk = max(k for k, _ in queries)

    pos = b[:]
    states = []
    seen_block_time = None
    t = 0

    while t <= maxk and t <= 200000:
        states.append(pos[:])
        x = pos.pop(0)
        y = x
        need = d
        idx = 0
        while need:
            y += need
            c = 0
            while idx < len(pos) and pos[idx] <= y:
                c += 1
                idx += 1
            need = c
        ins = bisect_right(pos, y)
        pos.insert(ins, y)
        t += 1
        ok = True
        for i in range(1, r):
            if pos[i] != pos[0] + i:
                ok = False
                break
        if ok:
            states.append(pos[:])
            seen_block_time = t
            break

    ans = []
    if seen_block_time is None:
        for k, m in queries:
            vals = states[min(k, len(states) - 1)]
            mov_exp = [expand(x) for x in vals]
            merged = []
            i = j = 0
            while i < len(imm) or j < len(mov_exp):
                if j == len(mov_exp) or (i < len(imm) and imm[i] < mov_exp[j]):
                    merged.append(imm[i])
                    i += 1
                else:
                    merged.append(mov_exp[j])
                    j += 1
            ans.append(str(merged[m - 1]))
    else:
        base = states[seen_block_time]
        cycle = r
        shift = d + r - 1
        cyc = [base[:]]
        cur = base[:]
        for _ in range(1, cycle):
            x = cur.pop(0)
            y = x
            need = d
            idx = 0
            while need:
                y += need
                c = 0
                while idx < len(cur) and cur[idx] <= y:
                    c += 1
                    idx += 1
                need = c
            ins = bisect_right(cur, y)
            cur.insert(ins, y)
            cyc.append(cur[:])

        for k, m in queries:
            if k <= seen_block_time:
                vals = states[k]
            else:
                rem = k - seen_block_time
                full, off = divmod(rem, cycle)
                vals = [x + full * shift for x in cyc[off]]
            mov_exp = [expand(x) for x in vals]
            merged = []
            i = j = 0
            while i < len(imm) or j < len(mov_exp):
                if j == len(mov_exp) or (i < len(imm) and imm[i] < mov_exp[j]):
                    merged.append(imm[i])
                    i += 1
                else:
                    merged.append(mov_exp[j])
                    j += 1
            ans.append(str(merged[m - 1]))

    print("\n".join(ans))

if __name__ == "__main__":
    main()
