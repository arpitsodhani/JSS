import sys

# CLAUSE: classify_initial_pattern
def classify_initial_pattern(a):
    if all(x == '0' for x in a):
        return "zero", -1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return "pair", i
    return "alternating", -1

def flip(a, l, r):
    for i in range(l, r + 1):
        a[i] = '1' if a[i] == '0' else '0'

# CLAUSE: seed_uniform_block
def seed_uniform_block(a, ops):
    kind, pos = classify_initial_pattern(a)
    if kind == "zero":
        return None
    if kind == "pair":
        return pos, pos + 1
    ops.append((0, 2))
    flip(a, 0, 2)
    return 2, 3

# CLAUSE: expand_block_right
def expand_block_right(a, l, r, ops):
    while r + 1 < len(a):
        if a[r + 1] != a[l]:
            ops.append((l, r))
            flip(a, l, r)
        r += 1
    return l, r

# CLAUSE: expand_block_left
def expand_block_left(a, l, r, ops):
    while l > 0:
        if a[l - 1] != a[l]:
            ops.append((l, r))
            flip(a, l, r)
        l -= 1
    return l, r

# CLAUSE: finalize_zero_string
def finalize_zero_string(a, l, r, ops):
    if any(x == '1' for x in a):
        ops.append((l, r))
        flip(a, l, r)

def build_to_zero(text):
    a = list(text)
    ops = []
    block = seed_uniform_block(a, ops)
    if block is None:
        return ops
    l, r = block
    l, r = expand_block_right(a, l, r, ops)
    l, r = expand_block_left(a, l, r, ops)
    finalize_zero_string(a, l, r, ops)
    return ops

# CLAUSE: invert_target_sequence
def solve_case(n, s, t):
    first = build_to_zero(s)
    second = build_to_zero(t)
    return first + second[::-1]

# CLAUSE: validate_operation_budget
def validate_operation_budget(n, s, t, ops):
    a = list(s)
    assert len(ops) <= 2 * n
    for l, r in ops:
        assert 0 <= l < r < n
        part = a[l:r + 1]
        assert part == part[::-1]
        flip(a, l, r)
    assert ''.join(a) == t

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    q = int(data[0])
    p = 1
    out = []
    for _ in range(q):
        n = int(data[p])
        s = data[p + 1]
        t = data[p + 2]
        p += 3
        ans = solve_case(n, s, t)
        validate_operation_budget(n, s, t, ans)
        out.append(str(len(ans)))
        out.extend(f"{l + 1} {r + 1}" for l, r in ans)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
