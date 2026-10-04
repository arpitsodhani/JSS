import sys
sys.setrecursionlimit(300000)

def solve():
    buf = sys.stdin.buffer.read().split()
    if not buf:
        return
    n = int(buf[0])
    d = int(buf[1])
    q = int(buf[2])
    arr = [int(x) for x in buf[3:3 + n]]
    flags = buf[3 + n].decode()
    queries = []
    at = 4 + n
    for idx in range(q):
        queries.append((int(buf[at]), int(buf[at + 1]), idx))
        at += 2
    queries.sort(key=lambda x: x[0])
    finish = queries[-1][0] if queries else 0

    # CLAUSE: separate_fixed_and_active_order
    v = [0]
    loch = [0]
    hich = [0]
    w = [0]
    sub = [0]
    inc = [0]
    stop = [0]
    stop_sub = [0]
    cur_rand = 13579

    def random_weight():
        nonlocal cur_rand
        cur_rand = (cur_rand ^ (cur_rand << 13)) & 0xffffffff
        cur_rand ^= cur_rand >> 17
        cur_rand = (cur_rand ^ (cur_rand << 5)) & 0xffffffff
        return cur_rand

    def new_item(x, imm):
        v.append(x)
        loch.append(0)
        hich.append(0)
        w.append(random_weight())
        sub.append(1)
        inc.append(0)
        stop.append(imm)
        stop_sub.append(imm)
        return len(v) - 1

    # CLAUSE: initialize_lazy_order_tree
    def nodes(t):
        return sub[t] if t else 0

    def bump(t, delta):
        if t:
            v[t] += delta
            inc[t] += delta

    def push(t):
        if t == 0 or inc[t] == 0:
            return
        delta = inc[t]
        bump(loch[t], delta)
        bump(hich[t], delta)
        inc[t] = 0

    def pull(t):
        sub[t] = nodes(loch[t]) + 1 + nodes(hich[t])
        stop_sub[t] = stop[t] or stop_sub[loch[t]] or stop_sub[hich[t]]

    def merge(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if w[a] > w[b]:
            push(a)
            hich[a] = merge(hich[a], b)
            pull(a)
            return a
        push(b)
        loch[b] = merge(a, loch[b])
        pull(b)
        return b

    def split(t, k):
        if t == 0:
            return 0, 0
        push(t)
        left_count = nodes(loch[t])
        if k <= left_count:
            a, b = split(loch[t], k)
            loch[t] = b
            pull(t)
            return a, t
        a, b = split(hich[t], k - left_count - 1)
        hich[t] = a
        pull(t)
        return t, b

    def kth(t, k):
        while True:
            push(t)
            left_count = nodes(loch[t])
            if k <= left_count:
                t = loch[t]
                continue
            if k == left_count + 1:
                return v[t]
            k -= left_count + 1
            t = hich[t]

    def first_stopper(t):
        ans = 0
        while True:
            push(t)
            if stop_sub[loch[t]]:
                t = loch[t]
            else:
                ans += nodes(loch[t])
                if stop[t]:
                    return ans + 1
                ans += 1
                t = hich[t]

    root = 0
    for x, ch in zip(arr, flags):
        root = merge(root, new_item(x, ch == "0"))

    # CLAUSE: detect_perfect_prefix_size
    def detect(root):
        first = kth(root, 1)
        l = 1
        r = nodes(root)
        while l < r:
            m = (l + r + 1) // 2
            if kth(root, m) <= first + d + m - 2:
                l = m
            else:
                r = m - 1
        return l

    # CLAUSE: project_perfect_block_position
    def future_value(root, width, rank, passed):
        each = d + width - 1
        qv, rem = divmod(passed, width)
        shifted = rank + rem
        if shifted <= width:
            return kth(root, shifted) + qv * each
        return kth(root, shifted - width) + (qv + 1) * each

    # CLAUSE: binary_search_phase_length
    def phase(root, width, now):
        rem = finish - now
        limit = rem
        if width < nodes(root):
            after = kth(root, width + 1)
            threshold = lambda t: future_value(root, width, 1, t) + d + width - 1
            if after <= threshold(rem):
                a = 0
                b = rem
                while a < b:
                    c = (a + b) // 2
                    if after <= threshold(c):
                        b = c
                    else:
                        a = c + 1
                limit = a
        if stop_sub[root]:
            pos = first_stopper(root)
            if pos <= width:
                limit = min(limit, pos - 1)
        return limit

    # CLAUSE: apply_cyclic_block_advance
    def apply(root, width, passed):
        front, tail = split(root, width)
        rem = passed % width
        whole = passed // width
        a, b = split(front, rem)
        add = d + width - 1
        bump(b, whole * add)
        bump(a, (whole + 1) * add)
        return merge(merge(b, a), tail)

    # CLAUSE: answer_sorted_rank_queries
    out = [0] * q
    fixed = []
    qi = 0
    now = 0
    while qi < q:
        while root:
            one, rest = split(root, 1)
            if stop[one]:
                fixed.append(v[one])
                root = rest
            else:
                root = merge(one, rest)
                break
        if root == 0:
            while qi < q:
                out[queries[qi][2]] = fixed[queries[qi][1] - 1]
                qi += 1
            break
        width = detect(root)
        length = phase(root, width, now)
        end = now + length
        fixed_len = len(fixed)
        while qi < q and queries[qi][0] <= end:
            t, m, idx = queries[qi]
            rank = m - fixed_len
            if rank <= 0:
                out[idx] = fixed[m - 1]
            elif rank <= width:
                out[idx] = future_value(root, width, rank, t - now)
            else:
                out[idx] = kth(root, rank)
            qi += 1
        if qi == q:
            break
        root = apply(root, width, length)
        now = end
    sys.stdout.write("\n".join(str(x) for x in out))

solve()
