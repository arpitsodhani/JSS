# CLAUSE: pair_positions
import sys

def pair_positions(a, b):
    pairs = []
    for x, y in zip(a, b):
        pairs.append((x, y))
    return pairs

# CLAUSE: construct_target_order
def construct_target_order(pairs):
    order = sorted(range(len(pairs)), key=lambda i: (pairs[i][0], pairs[i][1]))
    return [pairs[i] for i in order]

# CLAUSE: validate_dual_monotonicity
def validate_dual_monotonicity(target):
    for before, after in zip(target, target[1:]):
        if before[1] > after[1]:
            return False
    return True

# CLAUSE: locate_next_target_pair
def locate_next_target_pair(cur_a, cur_b, start, needed):
    need_a, need_b = needed
    for j in range(start, len(cur_a)):
        if cur_a[j] == need_a and cur_b[j] == need_b:
            return j
    return -1

# CLAUSE: apply_synchronized_swap
def apply_synchronized_swap(cur_a, cur_b, ops, i, j):
    if i == j:
        return
    cur_a[i], cur_a[j] = cur_a[j], cur_a[i]
    cur_b[i], cur_b[j] = cur_b[j], cur_b[i]
    ops.append((i + 1, j + 1))

# CLAUSE: emit_operation_sequence
def handle_case(n, a, b):
    target = construct_target_order(pair_positions(a, b))
    if not validate_dual_monotonicity(target):
        return ["-1"]

    cur_a = a[:]
    cur_b = b[:]
    ops = []

    for i in range(n):
        j = locate_next_target_pair(cur_a, cur_b, i, target[i])
        if j == -1:
            return ["-1"]
        apply_synchronized_swap(cur_a, cur_b, ops, i, j)

    if any(cur_a[i] > cur_a[i + 1] for i in range(n - 1)):
        return ["-1"]
    if any(cur_b[i] > cur_b[i + 1] for i in range(n - 1)):
        return ["-1"]
    if len(ops) > 10000:
        return ["-1"]

    lines = [str(len(ops))]
    lines.extend("{} {}".format(i, j) for i, j in ops)
    return lines

def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(tokens)
    output = []
    for _ in range(t):
        n = next(tokens)
        a = [next(tokens) for _ in range(n)]
        b = [next(tokens) for _ in range(n)]
        output.extend(handle_case(n, a, b))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
