import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    d = int(next(it))
    q = int(next(it))
    coords = [int(next(it)) for _ in range(n)]
    bits = next(it).decode()
    queries = [(int(next(it)), int(next(it)), i) for i in range(q)]
    queries.sort()
    last_time = queries[-1][0] if queries else 0

    # CLAUSE: separate_fixed_and_active_order
    val = [0]
    lc = [0]
    rc = [0]
    pr = [0]
    sz = [0]
    lazy = [0]
    frozen = [0]
    has_frozen = [0]
    seed = 88172645463393265

    def rnd():
        nonlocal seed
        seed ^= (seed << 7) & ((1 << 64) - 1)
        seed ^= seed >> 9
        return seed

    def make_node(x, fixed):
        val.append(x)
        lc.append(0)
        rc.append(0)
        pr.append(rnd())
        sz.append(1)
        lazy.append(0)
        frozen.append(fixed)
        has_frozen.append(fixed)
        return len(val) - 1

    # CLAUSE: initialize_lazy_order_tree
    def size(t):
        return sz[t] if t else 0

    def put_add(t, z):
        if t:
            val[t] += z
            lazy[t] += z

    def push(t):
        z = lazy[t] if t else 0
        if z:
            put_add(lc[t], z)
            put_add(rc[t], z)
            lazy[t] = 0

    def pull(t):
        sz[t] = 1 + size(lc[t]) + size(rc[t])
        has_frozen[t] = frozen[t] or has_frozen[lc[t]] or has_frozen[rc[t]]

    def merge(a, b):
        if not a or not b:
            return a or b
        if pr[a] > pr[b]:
            push(a)
            rc[a] = merge(rc[a], b)
            pull(a)
            return a
        push(b)
        lc[b] = merge(a, lc[b])
        pull(b)
        return b

    def split(t, k):
        if not t:
            return 0, 0
        push(t)
        left_size = size(lc[t])
        if k <= left_size:
            a, b = split(lc[t], k)
            lc[t] = b
            pull(t)
            return a, t
        a, b = split(rc[t], k - left_size - 1)
        rc[t] = a
        pull(t)
        return t, b

    def kth(t, k):
        while True:
            push(t)
            left_size = size(lc[t])
            if k <= left_size:
                t = lc[t]
            elif k == left_size + 1:
                return val[t]
            else:
                k -= left_size + 1
                t = rc[t]

    def first_fixed(t, add_rank=0):
        push(t)
        if has_frozen[lc[t]]:
            return first_fixed(lc[t], add_rank)
        add_rank += size(lc[t])
        if frozen[t]:
            return add_rank + 1
        return first_fixed(rc[t], add_rank + 1)

    root = 0
    for x, c in zip(coords, bits):
        root = merge(root, make_node(x, 1 if c == "0" else 0))

    # CLAUSE: detect_perfect_prefix_size
    def perfect_prefix(root):
        total = size(root)
        base = kth(root, 1)
        lo, hi = 1, total
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if kth(root, mid) <= base + d + mid - 2:
                lo = mid
            else:
                hi = mid - 1
        return lo

    # CLAUSE: project_perfect_block_position
    def make_projector(root, x):
        jump = d + x - 1
        def project(rank, moves):
            turn = moves % x
            full = moves // x
            if rank <= x - turn:
                return kth(root, rank + turn) + full * jump
            return kth(root, rank - (x - turn)) + (full + 1) * jump
        return project

    # CLAUSE: binary_search_phase_length
    def phase_limit(root, x, current, project):
        remaining = last_time - current
        limit = remaining
        total = size(root)
        if x < total:
            nxt = kth(root, x + 1)
            if nxt <= project(1, remaining) + d + x - 1:
                lo, hi = 0, remaining
                while lo < hi:
                    mid = (lo + hi) // 2
                    if nxt <= project(1, mid) + d + x - 1:
                        hi = mid
                    else:
                        lo = mid + 1
                limit = lo
        if has_frozen[root]:
            p = first_fixed(root)
            if p <= x and p - 1 < limit:
                limit = p - 1
        return limit

    # CLAUSE: apply_cyclic_block_advance
    def advance(root, x, moves):
        block, tail = split(root, x)
        cut = moves % x
        whole = moves // x
        left_part, right_part = split(block, cut)
        step = d + x - 1
        put_add(right_part, whole * step)
        put_add(left_part, (whole + 1) * step)
        return merge(merge(right_part, left_part), tail)

    # CLAUSE: answer_sorted_rank_queries
    ans = [0] * q
    fixed_prefix = []
    now = 0
    qi = 0
    while qi < q:
        while root:
            head, rest = split(root, 1)
            if frozen[head]:
                fixed_prefix.append(val[head])
                root = rest
            else:
                root = merge(head, rest)
                break
        if not root:
            while qi < q:
                ans[queries[qi][2]] = fixed_prefix[queries[qi][1] - 1]
                qi += 1
            break
        x = perfect_prefix(root)
        project = make_projector(root, x)
        limit = phase_limit(root, x, now, project)
        until = now + limit
        while qi < q and queries[qi][0] <= until:
            t, m, idx = queries[qi]
            r = m - len(fixed_prefix)
            if r <= 0:
                ans[idx] = fixed_prefix[m - 1]
            elif r <= x:
                ans[idx] = project(r, t - now)
            else:
                ans[idx] = kth(root, r)
            qi += 1
        if qi == q:
            break
        root = advance(root, x, limit)
        now = until
    sys.stdout.write("\n".join(map(str, ans)))

solve()
