import sys
sys.setrecursionlimit(300000)

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    p = 0
    n = int(tokens[p]); p += 1
    d = int(tokens[p]); p += 1
    q = int(tokens[p]); p += 1
    a = list(map(int, tokens[p:p + n])); p += n
    s = tokens[p].decode(); p += 1
    jobs = []
    for i in range(q):
        jobs.append((int(tokens[p]), int(tokens[p + 1]), i))
        p += 2
    jobs.sort()
    target_time = jobs[-1][0] if jobs else 0

    # CLAUSE: separate_fixed_and_active_order
    y = [0]
    left = [0]
    right = [0]
    heap = [0]
    count = [0]
    tag = [0]
    fixed = [0]
    any_fixed = [0]
    state = 2463534242

    def next_priority():
        nonlocal state
        state = (state * 1103515245 + 12345) & 0x7fffffff
        return state

    def node(value, is_fixed):
        y.append(value)
        left.append(0)
        right.append(0)
        heap.append(next_priority())
        count.append(1)
        tag.append(0)
        fixed.append(is_fixed)
        any_fixed.append(is_fixed)
        return len(y) - 1

    # CLAUSE: initialize_lazy_order_tree
    def cnt(v):
        return count[v] if v else 0

    def add_all(v, delta):
        if v:
            y[v] += delta
            tag[v] += delta

    def down(v):
        if v and tag[v]:
            delta = tag[v]
            add_all(left[v], delta)
            add_all(right[v], delta)
            tag[v] = 0

    def up(v):
        count[v] = cnt(left[v]) + 1 + cnt(right[v])
        any_fixed[v] = fixed[v] or any_fixed[left[v]] or any_fixed[right[v]]

    def join(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if heap[a] >= heap[b]:
            down(a)
            right[a] = join(right[a], b)
            up(a)
            return a
        down(b)
        left[b] = join(a, left[b])
        up(b)
        return b

    def cut(v, need):
        if not v:
            return 0, 0
        down(v)
        got = cnt(left[v])
        if need <= got:
            first, second = cut(left[v], need)
            left[v] = second
            up(v)
            return first, v
        first, second = cut(right[v], need - got - 1)
        right[v] = first
        up(v)
        return v, second

    def value_at(v, k):
        while v:
            down(v)
            z = cnt(left[v])
            if k <= z:
                v = left[v]
            elif k == z + 1:
                return y[v]
            else:
                k -= z + 1
                v = right[v]

    def frozen_rank(v, before=0):
        down(v)
        if any_fixed[left[v]]:
            return frozen_rank(left[v], before)
        before += cnt(left[v])
        if fixed[v]:
            return before + 1
        return frozen_rank(right[v], before + 1)

    root = 0
    for value, ch in zip(a, s):
        root = join(root, node(value, ch == "0"))

    # CLAUSE: detect_perfect_prefix_size
    def find_block(v):
        start = value_at(v, 1)
        lo = 1
        hi = cnt(v)
        while lo + 1 <= hi:
            mid = (lo + hi + 1) >> 1
            if value_at(v, mid) <= start + d + mid - 2:
                lo = mid
            else:
                hi = mid - 1
        return lo

    # CLAUSE: project_perfect_block_position
    def projected(v, width, rank, elapsed):
        q, r = divmod(elapsed, width)
        period = d + width - 1
        border = width - r
        if rank <= border:
            return value_at(v, rank + r) + q * period
        return value_at(v, rank - border) + (q + 1) * period

    # CLAUSE: binary_search_phase_length
    def get_span(v, width, clock):
        rest = target_time - clock
        span = rest
        if width < cnt(v):
            outside = value_at(v, width + 1)
            if outside <= projected(v, width, 1, rest) + d + width - 1:
                low = 0
                high = rest
                while low < high:
                    mid = (low + high) >> 1
                    if outside <= projected(v, width, 1, mid) + d + width - 1:
                        high = mid
                    else:
                        low = mid + 1
                span = low
        if any_fixed[v]:
            pos = frozen_rank(v)
            if pos <= width:
                span = min(span, pos - 1)
        return span

    # CLAUSE: apply_cyclic_block_advance
    def rotate_phase(v, width, elapsed):
        front, back = cut(v, width)
        r = elapsed % width
        q = elapsed // width
        first, second = cut(front, r)
        period = d + width - 1
        add_all(second, q * period)
        add_all(first, (q + 1) * period)
        return join(join(second, first), back)

    # CLAUSE: answer_sorted_rank_queries
    answer = [0] * q
    peeled = []
    time = 0
    at = 0
    while at < q:
        while root:
            h, rest = cut(root, 1)
            if fixed[h]:
                peeled.append(y[h])
                root = rest
            else:
                root = join(h, rest)
                break
        if root == 0:
            while at < q:
                answer[jobs[at][2]] = peeled[jobs[at][1] - 1]
                at += 1
            break
        width = find_block(root)
        span = get_span(root, width, time)
        stop = time + span
        base_fixed = len(peeled)
        while at < q and jobs[at][0] <= stop:
            moment, order, idx = jobs[at]
            active_rank = order - base_fixed
            if active_rank <= 0:
                answer[idx] = peeled[order - 1]
            elif active_rank <= width:
                answer[idx] = projected(root, width, active_rank, moment - time)
            else:
                answer[idx] = value_at(root, active_rank)
            at += 1
        if at == q:
            break
        root = rotate_phase(root, width, span)
        time = stop
    sys.stdout.write("\n".join(str(x) for x in answer))

main()
