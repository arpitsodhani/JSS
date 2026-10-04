# Clause classify_initial_pattern [Confidence: 0.60]
import sys

def change(a, l, r):
    trans = {'0': '1', '1': '0'}
    for i in range(l, r + 1):
        a[i] = trans[a[i]]

def classify_initial_pattern(a):
    if '1' not in a:
        return "zero", -1
    previous = a[0]
    for i in range(1, len(a)):
        if a[i] == previous:
            return "pair", i - 1
        previous = a[i]
    return "alternating", -1


# Clause seed_uniform_block [Confidence: 0.80]
def seed_uniform_block(a, ops):
    kind, pos = classify_initial_pattern(a)
    if kind == "zero":
        return None
    if kind == "pair":
        return pos, pos + 1
    ops.append((0, 2))
    flip(a, 0, 2)
    return 2, 3


# Clause expand_block_right [Confidence: 0.80]
def expand_block_right(bits, left, right, answer):
    for nxt in range(right + 1, len(bits)):
        if bits[nxt] != bits[right]:
            answer.append((left, right))
            apply_range(bits, left, right)
        right = nxt
    return left, right


# Clause expand_block_left [Confidence: 0.80]
def expand_block_left(a, l, r, ops):
    positions = range(l - 1, -1, -1)
    for pos in positions:
        if a[pos] != a[r]:
            ops.append((l, r))
            change(a, l, r)
        l = pos
    return l, r


# Clause finalize_zero_string [Confidence: 1.00]
def finalize_zero_string(bits, left, right, answer):
    if bits[0] == '1':
        answer.append((left, right))
        apply_range(bits, left, right)

def normalize(source):
    bits = list(source)
    answer = []
    left, right, done = seed_uniform_block(bits, answer)
    if done:
        return answer
    left, right = expand_block_right(bits, left, right, answer)
    left, right = expand_block_left(bits, left, right, answer)
    finalize_zero_string(bits, left, right, answer)
    return answer


# Clause invert_target_sequence [Confidence: 0.80]
def compose(n, s, t):
    left_part = path_to_zero(s)
    right_part = path_to_zero(t)
    return left_part + tuple(reversed(right_part))


# Clause validate_operation_budget [Confidence: 1.00]
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


