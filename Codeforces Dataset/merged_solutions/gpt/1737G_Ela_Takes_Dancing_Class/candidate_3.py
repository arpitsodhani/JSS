import sys
sys.setrecursionlimit(300000)

def solve():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    it = iter(raw)
    n, d, q = int(next(it)), int(next(it)), int(next(it))
    a = [int(next(it)) for _ in range(n)]
    s = next(it).decode()
    ask = []
    for idx in range(q):
        ask.append((int(next(it)), int(next(it)), idx))
    ask.sort()
    horizon = ask[-1][0] if ask else 0

    # CLAUSE: separate_fixed_and_active_order
    X = [0]
    L = [0]
    R = [0]
    P = [0]
    S = [0]
    A = [0]
    F = [0]
    G = [0]
    rng = 1234567

    def roll():
        nonlocal rng
        rng = (rng + 0x9e3779b97f4a7c15) & ((1 << 64) - 1)
        z = rng
        z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9 & ((1 << 64) - 1)
        z = (z ^ (z >> 27)) * 0x94d049bb133111eb & ((1 << 64) - 1)
        return z ^ (z >> 31)

    def create(x, immovable):
        X.append(x)
        L.append(0)
        R.append(0)
        P.append(roll())
        S.append(1)
        A.append(0)
        F.append(immovable)
        G.append(immovable)
        return len(X) - 1

    # CLAUSE: initialize_lazy_order_tree
    def sz(t):
        return S[t] if t else 0

    def lazy_add(t, z):
        if t:
            X[t] += z
            A[t] += z

    def prop(t):
        if t and A[t] != 0:
            z = A[t]
            lazy_add(L[t], z)
            lazy_add(R[t], z)
            A[t] = 0

    def recalc(t):
        S[t] = sz(L[t]) + sz(R[t]) + 1
        G[t] = F[t] or G[L[t]] or G[R[t]]

    def meld(a, b):
        if a == 0 or b == 0:
            return a + b
        if P[a] > P[b]:
            prop(a)
            R[a] = meld(R[a], b)
            recalc(a)
            return a
        prop(b)
        L[b] = meld(a, L[b])
        recalc(b)
        return b

    def divide(t, k):
        if t == 0:
            return 0, 0
        prop(t)
        ls = sz(L[t])
        if k < ls + 1:
            u, v = divide(L[t], k)
            L[t] = v
            recalc(t)
            return u, t
        u, v = divide(R[t], k - ls - 1)
        R[t] = u
        recalc(t)
        return t, v

    def get(t, k):
        while True:
            prop(t)
            ls = sz(L[t])
            if k < ls + 1:
                t = L[t]
            elif k == ls + 1:
                return X[t]
            else:
                k -= ls + 1
                t = R[t]

    def first_blocked(t, acc=0):
        prop(t)
        if G[L[t]]:
            return first_blocked(L[t], acc)
        acc += sz(L[t])
        if F[t]:
            return acc + 1
        return first_blocked(R[t], acc + 1)

    root = 0
    for x, ch in zip(a, s):
        root = meld(root, create(x, ch == "0"))

    # CLAUSE: detect_perfect_prefix_size
    def detect(root):
        origin = get(root, 1)
        low = 1
        high = sz(root)
        while low < high:
            mid = (low + high + 1) // 2
            ok = get(root, mid) - mid <= origin + d - 2
            if ok:
                low = mid
            else:
                high = mid - 1
        return low

    # CLAUSE: project_perfect_block_position
    def block_value(root, block_len, rank, passed):
        cycle = d + block_len - 1
        whole, off = divmod(passed, block_len)
        suffix_len = block_len - off
        if rank <= suffix_len:
            return get(root, off + rank) + whole * cycle
        return get(root, rank - suffix_len) + (whole + 1) * cycle

    # CLAUSE: binary_search_phase_length
    def skip_length(root, block_len, current_time):
        left = 0
        right = horizon - current_time
        ans = right
        total = sz(root)
        if block_len != total:
            next_coord = get(root, block_len + 1)
            if next_coord <= block_value(root, block_len, 1, right) + d + block_len - 1:
                while left < right:
                    mid = (left + right) // 2
                    if next_coord <= block_value(root, block_len, 1, mid) + d + block_len - 1:
                        right = mid
                    else:
                        left = mid + 1
                ans = left
        if G[root]:
            where = first_blocked(root)
            if where <= block_len:
                ans = min(ans, where - 1)
        return ans

    # CLAUSE: apply_cyclic_block_advance
    def materialize(root, block_len, passed):
        a, b = divide(root, block_len)
        off = passed % block_len
        whole = passed // block_len
        u, v = divide(a, off)
        gain = d + block_len - 1
        lazy_add(v, whole * gain)
        lazy_add(u, (whole + 1) * gain)
        return meld(meld(v, u), b)

    # CLAUSE: answer_sorted_rank_queries
    out = [0] * q
    immobile = []
    ptr = 0
    t = 0
    while ptr < q:
        while root:
            one, rest = divide(root, 1)
            if F[one]:
                immobile.append(X[one])
                root = rest
            else:
                root = meld(one, rest)
                break
        if root == 0:
            while ptr < q:
                out[ask[ptr][2]] = immobile[ask[ptr][1] - 1]
                ptr += 1
            break
        block_len = detect(root)
        passed = skip_length(root, block_len, t)
        end_time = t + passed
        fixed_count = len(immobile)
        while ptr < q and ask[ptr][0] <= end_time:
            qt, qm, qi = ask[ptr]
            rank = qm - fixed_count
            if rank < 1:
                out[qi] = immobile[qm - 1]
            elif rank <= block_len:
                out[qi] = block_value(root, block_len, rank, qt - t)
            else:
                out[qi] = get(root, rank)
            ptr += 1
        if ptr == q:
            break
        root = materialize(root, block_len, passed)
        t = end_time
    print("\n".join(map(str, out)))

solve()
