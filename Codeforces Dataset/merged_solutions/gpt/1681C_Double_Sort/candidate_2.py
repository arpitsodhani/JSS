# CLAUSE: pair_positions
import sys

def pair_positions(a, b):
    pairs = []
    for i in range(len(a)):
        pairs.append([a[i], b[i]])
    return pairs

# CLAUSE: construct_target_order
def construct_target_order(pairs):
    target = pairs[:]
    target.sort(key=lambda item: (item[0], item[1]))
    return target

# CLAUSE: validate_dual_monotonicity
def validate_dual_monotonicity(target):
    last_b = -10**30
    for _, b_value in target:
        if b_value < last_b:
            return False
        last_b = b_value
    return True

# CLAUSE: locate_next_target_pair
def locate_next_target_pair(current, left, needed):
    pos = left
    while pos < len(current):
        if current[pos][0] == needed[0] and current[pos][1] == needed[1]:
            return pos
        pos += 1
    return -1

# CLAUSE: apply_synchronized_swap
def apply_synchronized_swap(current, ops, i, j):
    if i == j:
        return
    temp = current[i]
    current[i] = current[j]
    current[j] = temp
    ops.append((i + 1, j + 1))

# CLAUSE: emit_operation_sequence
def process(n, a, b):
    current = pair_positions(a, b)
    target = construct_target_order(current)
    if not validate_dual_monotonicity(target):
        return ["-1"]

    ops = []
    for i, needed in enumerate(target):
        j = locate_next_target_pair(current, i, needed)
        if j < 0:
            return ["-1"]
        apply_synchronized_swap(current, ops, i, j)

    if len(ops) > 10000:
        return ["-1"]
    lines = [str(len(ops))]
    for op in ops:
        lines.append(str(op[0]) + " " + str(op[1]))
    return lines

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    t = values[0]
    p = 1
    output = []
    for _ in range(t):
        n = values[p]
        p += 1
        a = values[p:p + n]
        p += n
        b = values[p:p + n]
        p += n
        output += process(n, a, b)
    print("\n".join(output))

main()
