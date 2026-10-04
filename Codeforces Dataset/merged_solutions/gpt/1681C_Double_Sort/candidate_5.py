# CLAUSE: pair_positions
import sys

def pair_positions(a, b):
    return tuple((a[i], b[i]) for i in range(len(a)))

# CLAUSE: construct_target_order
def construct_target_order(pairs):
    return tuple(sorted(pairs, key=lambda pair: pair))

# CLAUSE: validate_dual_monotonicity
def validate_dual_monotonicity(target):
    index = 0
    while index + 1 < len(target):
        if target[index][1] > target[index + 1][1]:
            return False
        index += 1
    return True

# CLAUSE: locate_next_target_pair
def locate_next_target_pair(current, start, needed):
    try:
        return current.index(needed, start)
    except ValueError:
        return -1

# CLAUSE: apply_synchronized_swap
def apply_synchronized_swap(current, ops, i, j):
    if i != j:
        current[i], current[j] = current[j], current[i]
        ops.append((i + 1, j + 1))

# CLAUSE: emit_operation_sequence
def build_answer(n, a, b):
    original = pair_positions(a, b)
    target = construct_target_order(original)
    if not validate_dual_monotonicity(target):
        return ["-1"]

    current = list(original)
    operations = []

    i = 0
    while i < n:
        if current[i] != target[i]:
            j = locate_next_target_pair(current, i + 1, target[i])
            if j == -1:
                return ["-1"]
            apply_synchronized_swap(current, operations, i, j)
        i += 1

    if tuple(current) != target or len(operations) > 10000:
        return ["-1"]

    response = [str(len(operations))]
    for first, second in operations:
        response.append(f"{first} {second}")
    return response

def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    all_lines = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        a = list(map(int, data[pos:pos + n]))
        pos += n
        b = list(map(int, data[pos:pos + n]))
        pos += n
        all_lines.extend(build_answer(n, a, b))
    sys.stdout.write("\n".join(all_lines))

main()
