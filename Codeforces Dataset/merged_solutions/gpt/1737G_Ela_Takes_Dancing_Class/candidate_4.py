import sys
sys.setrecursionlimit(300000)

def run():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    d = int(data[1])
    q = int(data[2])
    pos = list(map(int, data[3:3 + n]))
    mask = data[3 + n].decode()
    offset = 4 + n
    req = []
    for i in range(q):
        req.append((int(data[offset]), int(data[offset + 1]), i))
        offset += 2
    req.sort()
    max_t = req[-1][0] if q else 0

    # CLAUSE: separate_fixed_and_active_order
    coord = [0]
    ch0 = [0]
    ch1 = [0]
    prior = [0]
    length = [0]
    plus = [0]
    still = [0]
    inside = [0]
    salt = 987654321

    def gen():
        nonlocal salt
        salt = (salt * 48271) % 2147483647
        return salt

    def alloc(x, stay):
        coord.append(x)
        ch0.append(0)
        ch1.append(0)
        prior.append(gen())
        length.append(1)
        plus.append(0)
        still.append(stay)
        inside.append(stay)
        return len(coord) - 1

    # CLAUSE: initialize_lazy_order_tree
    def length_of(t):
        return length[t] if t else 0

    def mark(t, z):
        if t:
            coord[t] += z
            plus[t] += z

    def spread(t):
        if t and plus[t]:
            z = plus[t]
            mark(ch0[t], z)
            mark(ch1[t], z)
            plus[t] = 0

    def update(t):
        length[t] = 1 + length_of(ch0[t]) + length_of(ch1[t])
        inside[t] = still[t] or inside[ch0[t]] or inside[ch1[t]]

    def unite(a, b):
        if not a:
            return b
        if not b:
            return a
        if prior[a] > prior[b]:
            spread(a)
            ch1[a] = unite(ch1[a], b)
            update(a)
            return a
        spread(b)
        ch0[b] = unite(a, ch0[b])
        update(b)
        return b

    def separate(t, k):
        if not t:
            return 0, 0
        spread(t)
        lsz = length_of(ch0[t])
        if k <= lsz:
            a, b = separate(ch0[t], k)
            ch0[t] = b
            update(t)
            return a, t
        a, b = separate(ch1[t], k - lsz - 1)
        ch1[t] = a
        update(t)
        return t, b

    def kth_coord(t, k):
        while True:
            spread(t)
            lsz = length_of(ch0[t])
            if k <= lsz:
                t = ch0[t]
            elif k == lsz + 1:
                return coord[t]
            else:
                k -= lsz + 1
                t = ch1[t]

    def earliest_still(t, base):
        spread(t)
        if inside[ch0[t]]:
            return earliest_still(ch0[t], base)
        base += length_of(ch0[t])
        if still[t]:
            return base + 1
        return earliest_still(ch1[t], base + 1)

    root = 0
    for x, c in zip(pos, mask):
        root = unite(root, alloc(x, c == "0"))

    # CLAUSE: detect_perfect_prefix_size
    def prefix_len(root):
        start = kth_coord(root, 1)
        lo = 1
        hi = length_of(root)
        while lo != hi:
            mid = (lo + hi + 1) // 2
            if kth_coord(root, mid) <= start + d + mid - 2:
                lo = mid
            else:
                hi = mid - 1
        return lo

    # CLAUSE: project_perfect_block_position
    def locate(root, width, rank, elapsed):
        qv = elapsed // width
        rv = elapsed - qv * width
        span = d + width - 1
        if rank + rv <= width:
            return kth_coord(root, rank + rv) + qv * span
        return kth_coord(root, rank + rv - width) + (qv + 1) * span

    # CLAUSE: binary_search_phase_length
    def valid_span(root, width, now):
        rem = max_t - now
        best = rem
        if width < length_of(root):
            border = kth_coord(root, width + 1)
            if border <= locate(root, width, 1, rem) + d + width - 1:
                lo, hi = 0, rem
                while lo < hi:
                    mid = (lo + hi) // 2
                    if border <= locate(root, width, 1, mid) + d + width - 1:
                        hi = mid
                    else:
                        lo = mid + 1
                best = lo
        if inside[root]:
            pos_fixed = earliest_still(root, 0)
            if pos_fixed <= width and pos_fixed - 1 < best:
                best = pos_fixed - 1
        return best

    # CLAUSE: apply_cyclic_block_advance
    def enact(root, width, elapsed):
        chosen, rest = separate(root, width)
        rot = elapsed % width
        loops = elapsed // width
        a, b = separate(chosen, rot)
        dist = d + width - 1
        mark(b, loops * dist)
        mark(a, (loops + 1) * dist)
        return unite(unite(b, a), rest)

    # CLAUSE: answer_sorted_rank_queries
    answer = [0] * q
    prefix = []
    qi = 0
    now = 0
    while qi < q:
        while root:
            first, rest = separate(root, 1)
            if still[first]:
                prefix.append(coord[first])
                root = rest
            else:
                root = unite(first, rest)
                break
        if not root:
            while qi < q:
                answer[req[qi][2]] = prefix[req[qi][1] - 1]
                qi += 1
            break
        width = prefix_len(root)
        step = valid_span(root, width, now)
        bound = now + step
        kept = len(prefix)
        while qi < q and req[qi][0] <= bound:
            tm, m, idx = req[qi]
            r = m - kept
            if r <= 0:
                answer[idx] = prefix[m - 1]
            elif r <= width:
                answer[idx] = locate(root, width, r, tm - now)
            else:
                answer[idx] = kth_coord(root, r)
            qi += 1
        if qi >= q:
            break
        root = enact(root, width, step)
        now = bound
    sys.stdout.write("\n".join(map(str, answer)))

run()
