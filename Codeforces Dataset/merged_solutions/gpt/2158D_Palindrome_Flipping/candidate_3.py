import sys

def flip_segment(arr, l, r):
    for k in range(l, r + 1):
        arr[k] = chr(ord(arr[k]) ^ 1)

# CLAUSE: classify_initial_pattern
def classify_initial_pattern(arr):
    ones = 0
    pair_at = -1
    for i, c in enumerate(arr):
        ones += c == '1'
        if i and pair_at < 0 and arr[i] == arr[i - 1]:
            pair_at = i - 1
    if ones == 0:
        return 0, -1
    if pair_at >= 0:
        return 1, pair_at
    return 2, -1

# CLAUSE: seed_uniform_block
def seed_uniform_block(arr, res):
    typ, at = classify_initial_pattern(arr)
    if typ == 0:
        return None
    if typ == 1:
        return [at, at + 1]
    res.append([0, 2])
    flip_segment(arr, 0, 2)
    return [2, 3]

# CLAUSE: expand_block_right
def expand_block_right(arr, block, res):
    l, r = block
    while r != len(arr) - 1:
        if arr[r + 1] != arr[r]:
            res.append([l, r])
            flip_segment(arr, l, r)
        r += 1
    block[0], block[1] = l, r

# CLAUSE: expand_block_left
def expand_block_left(arr, block, res):
    l, r = block
    while l:
        if arr[l - 1] != arr[l]:
            res.append([l, r])
            flip_segment(arr, l, r)
        l -= 1
    block[0], block[1] = l, r

# CLAUSE: finalize_zero_string
def finalize_zero_string(arr, block, res):
    if arr[0] != '0':
        res.append([block[0], block[1]])
        flip_segment(arr, block[0], block[1])

def path_to_zero(s):
    arr = list(s)
    res = []
    block = seed_uniform_block(arr, res)
    if block is not None:
        expand_block_right(arr, block, res)
        expand_block_left(arr, block, res)
        finalize_zero_string(arr, block, res)
    return [tuple(x) for x in res]

# CLAUSE: invert_target_sequence
def compose(n, s, t):
    left_part = path_to_zero(s)
    right_part = path_to_zero(t)
    return left_part + tuple(reversed(right_part))

# CLAUSE: validate_operation_budget
def validate_operation_budget(n, s, t, ops):
    arr = list(s)
    assert len(ops) <= 2 * n
    for l, r in ops:
        assert l < r
        ok = True
        i, j = l, r
        while i < j:
            ok &= arr[i] == arr[j]
            i += 1
            j -= 1
        assert ok
        flip_segment(arr, l, r)
    assert ''.join(arr) == t

def main():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    at = 1
    ans = []
    for _ in range(q):
        n = int(raw[at])
        s = raw[at + 1].decode()
        t = raw[at + 2].decode()
        at += 3
        ops = compose(n, s, t)
        validate_operation_budget(n, s, t, ops)
        ans.append(str(len(ops)))
        ans += [f"{l + 1} {r + 1}" for l, r in ops]
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
