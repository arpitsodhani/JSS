import sys

def toggle(buf, lo, hi):
    k = lo
    while k <= hi:
        buf[k] = '0' if buf[k] == '1' else '1'
        k += 1

# CLAUSE: classify_initial_pattern
def classify_initial_pattern(buf):
    zero = True
    same = -1
    for i in range(len(buf)):
        if buf[i] == '1':
            zero = False
        if i + 1 < len(buf) and same == -1 and buf[i] == buf[i + 1]:
            same = i
    if zero:
        return {"kind": "zero", "index": -1}
    if same != -1:
        return {"kind": "pair", "index": same}
    return {"kind": "alternating", "index": -1}

# CLAUSE: seed_uniform_block
def seed_uniform_block(buf, ops):
    info = classify_initial_pattern(buf)
    if info["kind"] == "zero":
        return ()
    if info["kind"] == "pair":
        i = info["index"]
        return (i, i + 1)
    ops.append((0, 2))
    toggle(buf, 0, 2)
    return (2, 3)

# CLAUSE: expand_block_right
def expand_block_right(buf, segment, ops):
    lo, hi = segment
    for i in range(hi + 1, len(buf)):
        if buf[i] != buf[lo]:
            ops.append((lo, hi))
            toggle(buf, lo, hi)
        hi = i
    return lo, hi

# CLAUSE: expand_block_left
def expand_block_left(buf, segment, ops):
    lo, hi = segment
    i = lo - 1
    while i >= 0:
        if buf[i] != buf[hi]:
            ops.append((lo, hi))
            toggle(buf, lo, hi)
        lo = i
        i -= 1
    return lo, hi

# CLAUSE: finalize_zero_string
def finalize_zero_string(buf, segment, ops):
    lo, hi = segment
    if ''.join(buf) != '0' * len(buf):
        ops.append((lo, hi))
        toggle(buf, lo, hi)

def reduce_to_zero(s):
    buf = list(s)
    ops = []
    segment = seed_uniform_block(buf, ops)
    if segment:
        segment = expand_block_right(buf, segment, ops)
        segment = expand_block_left(buf, segment, ops)
        finalize_zero_string(buf, segment, ops)
    return ops

# CLAUSE: invert_target_sequence
def operations_for(n, s, t):
    ops = []
    ops.extend(reduce_to_zero(s))
    tail = reduce_to_zero(t)
    for op in tail[::-1]:
        ops.append(op)
    return ops

# CLAUSE: validate_operation_budget
def validate_operation_budget(n, s, t, ops):
    buf = list(s)
    assert len(ops) <= 2 * n
    for lo, hi in ops:
        assert 0 <= lo < hi < n
        assert all(buf[lo + d] == buf[hi - d] for d in range((hi - lo + 1) // 2))
        toggle(buf, lo, hi)
    assert ''.join(buf) == t

def main():
    data = sys.stdin.readline().split()
    tests = int(data[0]) if data else 0
    out = []
    for _ in range(tests):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        t = sys.stdin.readline().strip()
        ans = operations_for(n, s, t)
        validate_operation_budget(n, s, t, ans)
        out.append(str(len(ans)))
        out.extend("%d %d" % (l + 1, r + 1) for l, r in ans)
    sys.stdout.write("\n".join(out))

main()
