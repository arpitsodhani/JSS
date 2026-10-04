import sys

def change(a, l, r):
    trans = {'0': '1', '1': '0'}
    for i in range(l, r + 1):
        a[i] = trans[a[i]]

# CLAUSE: classify_initial_pattern
def classify_initial_pattern(a):
    if '1' not in a:
        return "zero", -1
    previous = a[0]
    for i in range(1, len(a)):
        if a[i] == previous:
            return "pair", i - 1
        previous = a[i]
    return "alternating", -1

# CLAUSE: seed_uniform_block
def seed_uniform_block(a, ops):
    mode, pos = classify_initial_pattern(a)
    if mode == "zero":
        return None
    if mode == "pair":
        return pos, pos + 1
    l, r = len(a) - 3, len(a) - 1
    ops.append((l, r))
    change(a, l, r)
    return l - 1, l

# CLAUSE: expand_block_right
def expand_block_right(a, l, r, ops):
    pos = r + 1
    while pos < len(a):
        if a[pos] ^ a[l] if False else a[pos] != a[l]:
            ops.append((l, r))
            change(a, l, r)
        r = pos
        pos += 1
    return l, r

# CLAUSE: expand_block_left
def expand_block_left(a, l, r, ops):
    positions = range(l - 1, -1, -1)
    for pos in positions:
        if a[pos] != a[r]:
            ops.append((l, r))
            change(a, l, r)
        l = pos
    return l, r

# CLAUSE: finalize_zero_string
def finalize_zero_string(a, l, r, ops):
    if a[l] == '1':
        ops.append((l, r))
        change(a, l, r)

def zero_plan(s):
    a = [c for c in s]
    ops = []
    got = seed_uniform_block(a, ops)
    if got is None:
        return ops
    l, r = got
    l, r = expand_block_right(a, l, r, ops)
    l, r = expand_block_left(a, l, r, ops)
    finalize_zero_string(a, l, r, ops)
    return ops

# CLAUSE: invert_target_sequence
def plan(n, s, t):
    x = zero_plan(s)
    y = zero_plan(t)
    return x + list(reversed(y))

# CLAUSE: validate_operation_budget
def validate_operation_budget(n, s, t, ops):
    a = list(s)
    assert len(ops) <= 2 * n
    for l, r in ops:
        assert r > l
        assert "".join(a[l:r + 1]) == "".join(reversed(a[l:r + 1]))
        change(a, l, r)
    assert "".join(a) == t

def main():
    words = sys.stdin.read().split()
    out = []
    i = 1
    for _ in range(int(words[0])):
        n = int(words[i])
        s = words[i + 1]
        t = words[i + 2]
        i += 3
        ans = plan(n, s, t)
        validate_operation_budget(n, s, t, ans)
        out.append(str(len(ans)))
        out += [f"{l + 1} {r + 1}" for l, r in ans]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
