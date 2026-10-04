import sys

# CLAUSE: classify_initial_pattern
def classify_initial_pattern(bits):
    if bits.count('1') == 0:
        return ("zero", None)
    same = next((i for i in range(len(bits) - 1) if bits[i] == bits[i + 1]), None)
    if same is not None:
        return ("pair", same)
    return ("alternating", None)

def apply_range(bits, left, right):
    bits[left:right + 1] = ['1' if c == '0' else '0' for c in bits[left:right + 1]]

# CLAUSE: seed_uniform_block
def seed_uniform_block(bits, answer):
    state, where = classify_initial_pattern(bits)
    if state == "zero":
        return -1, -1, True
    if state == "alternating":
        answer.append((1, 3))
        apply_range(bits, 1, 3)
        return 0, 1, False
    return where, where + 1, False

# CLAUSE: expand_block_right
def expand_block_right(bits, left, right, answer):
    for nxt in range(right + 1, len(bits)):
        if bits[nxt] != bits[right]:
            answer.append((left, right))
            apply_range(bits, left, right)
        right = nxt
    return left, right

# CLAUSE: expand_block_left
def expand_block_left(bits, left, right, answer):
    for nxt in range(left - 1, -1, -1):
        if bits[nxt] != bits[left]:
            answer.append((left, right))
            apply_range(bits, left, right)
        left = nxt
    return left, right

# CLAUSE: finalize_zero_string
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

# CLAUSE: invert_target_sequence
def make_answer(n, s, t):
    a = normalize(s)
    b = normalize(t)
    b.reverse()
    return a + b

# CLAUSE: validate_operation_budget
def validate_operation_budget(n, s, t, answer):
    cur = list(s)
    assert len(answer) <= 2 * n
    for left, right in answer:
        assert right - left + 1 >= 2
        assert cur[left:right + 1] == cur[left:right + 1][::-1]
        apply_range(cur, left, right)
    assert ''.join(cur) == t

def main():
    tokens = sys.stdin.read().split()
    tc = int(tokens[0])
    idx = 1
    lines = []
    for _ in range(tc):
        n = int(tokens[idx])
        s = tokens[idx + 1]
        t = tokens[idx + 2]
        idx += 3
        answer = make_answer(n, s, t)
        validate_operation_budget(n, s, t, answer)
        lines.append(str(len(answer)))
        for left, right in answer:
            lines.append(str(left + 1) + " " + str(right + 1))
    print("\n".join(lines))

main()
