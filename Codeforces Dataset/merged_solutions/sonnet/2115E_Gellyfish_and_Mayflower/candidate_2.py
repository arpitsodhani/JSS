# CLAUSE: setup_environment
import sys
from math import gcd

NEG = -10**30

def close_mod(values, mod, base_w, cost, power):
    d = gcd(mod, cost)
    result = [NEG] * mod
    for start in range(d):
        seq = []
        x = start
        while True:
            seq.append(x)
            x = (x + cost) % mod
            if x == start:
                break
        length = len(seq)
        gains = [power - ((seq[i] + cost) // mod) * base_w for i in range(length)]
        pref = [0] * (2 * length)
        for i in range(1, 2 * length):
            pref[i] = pref[i - 1] + gains[(i - 1) % length]
        dq = []
        head = 0
        for k in range(2 * length - 1):
            pos = seq[k % length]
            val = values[pos]
            cur = val - pref[k] if val > NEG // 2 else NEG
            while len(dq) > head:
                last = dq[-1]
                last_pos = seq[last % length]
                last_val = values[last_pos]
                last_cur = last_val - pref[last] if last_val > NEG // 2 else NEG
                if last_cur >= cur:
                    break
                dq.pop()
            dq.append(k)
            border = k - length + 1
            while len(dq) > head and dq[head] < border:
                head += 1
            if k >= length - 1:
                best = dq[head]
                best_pos = seq[best % length]
                best_val = values[best_pos]
                if best_val > NEG // 2:
                    result[pos] = best_val - pref[best] + pref[k]
    return result

def merge_into(dst, src):
    if src is None:
        return dst
    if dst is None:
        return src[:]
    for i, val in enumerate(src):
        if val > dst[i]:
            dst[i] = val
    return dst

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    idx = 0
    n = data[idx]
    m = data[idx + 1]
    idx += 2
    cost = [0] * (n + 1)
    power = [0] * (n + 1)
    for i in range(1, n + 1):
        cost[i] = data[idx]
        power[i] = data[idx + 1]
        idx += 2
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        edges[u].append(v)
    q = data[idx]
    idx += 1
    queries = []
    limit = max(cost) * max(cost)
    need = 0
    large = False
    for _ in range(q):
        p = data[idx]
        r = data[idx + 1]
        idx += 2
        queries.append((p, r))
        if r <= limit:
            if r > need:
                need = r
        else:
            large = True
    small = None
    if need:
        small = [[NEG] * (need + 1) for _ in range(n + 1)]
        small[1] = [0] * (need + 1)
        for u in range(1, n + 1):
            arr = small[u]
            c = cost[u]
            w = power[u]
            for x in range(c, need + 1):
                val = arr[x - c] + w
                if val > arr[x]:
                    arr[x] = val
            for v in edges[u]:
                dst = small[v]
                for x, val in enumerate(arr):
                    if val > dst[x]:
                        dst[x] = val
    big = None
    if large:
        big = [None] * (n + 1)
        for best in range(1, n + 1):
            cb = cost[best]
            wb = power[best]
            before = [None] * (n + 1)
            after = [None] * (n + 1)
            if power[1] * cb <= wb * cost[1]:
                base = [NEG] * cb
                base[0] = 0
                if best == 1:
                    after[1] = base
                else:
                    before[1] = base
            for u in range(1, n + 1):
                if power[u] * cb > wb * cost[u]:
                    continue
                if u == best:
                    after[u] = merge_into(after[u], before[u])
                    before[u] = None
                else:
                    if before[u] is not None:
                        before[u] = close_mod(before[u], cb, wb, cost[u], power[u])
                    if after[u] is not None:
                        after[u] = close_mod(after[u], cb, wb, cost[u], power[u])
                for v in edges[u]:
                    if power[v] * cb <= wb * cost[v]:
                        before[v] = merge_into(before[v], before[u])
                        after[v] = merge_into(after[v], after[u])
            by_p = [None] * (n + 1)
            for p in range(1, n + 1):
                arr = after[p]
                if arr is None:
                    by_p[p] = [NEG] * cb
                    continue
                pref = [NEG] * cb
                suff = [NEG] * (cb + 1)
                cur = NEG
                for i in range(cb):
                    if arr[i] > cur:
                        cur = arr[i]
                    pref[i] = cur
                cur = NEG
                for i in range(cb - 1, -1, -1):
                    if arr[i] > cur:
                        cur = arr[i]
                    suff[i] = cur
                offs = [NEG] * cb
                for r in range(cb):
                    val = pref[r]
                    if suff[r + 1] > NEG // 2:
                        other = suff[r + 1] - wb
                        if other > val:
                            val = other
                    offs[r] = val
                by_p[p] = offs
            big[best] = by_p
    ans = []
    for p, r in queries:
        if r <= limit:
            ans.append(str(small[p][r]))
        else:
            best_ans = NEG
            for b in range(1, n + 1):
                cb = cost[b]
                add = big[b][p][r % cb]
                if add > NEG // 2:
                    val = (r // cb) * power[b] + add
                    if val > best_ans:
                        best_ans = val
            ans.append(str(best_ans))
    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
