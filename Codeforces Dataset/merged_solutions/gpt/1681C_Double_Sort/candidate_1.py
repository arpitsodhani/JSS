# CLAUSE: pair_positions
import sys

def pair_positions(a, b):
    return list(zip(a, b))

# CLAUSE: construct_target_order
def construct_target_order(pairs):
    return sorted(pairs)

# CLAUSE: validate_dual_monotonicity
def validate_dual_monotonicity(target):
    for i in range(1, len(target)):
        if target[i - 1][1] > target[i][1]:
            return False
    return True

# CLAUSE: locate_next_target_pair
def locate_next_target_pair(current, start, needed):
    for pos in range(start, len(current)):
        if current[pos] == needed:
            return pos
    return -1

# CLAUSE: apply_synchronized_swap
def apply_synchronized_swap(current, ops, i, j):
    if i != j:
        current[i], current[j] = current[j], current[i]
        ops.append((i + 1, j + 1))

# CLAUSE: emit_operation_sequence
def solve_case(n, a, b):
    current = pair_positions(a, b)
    target = construct_target_order(current)
    if not validate_dual_monotonicity(target):
        return ["-1"]

    ops = []
    for i in range(n):
        j = locate_next_target_pair(current, i, target[i])
        if j == -1:
            return ["-1"]
        apply_synchronized_swap(current, ops, i, j)

    if len(ops) > 10000:
        return ["-1"]
    out = [str(len(ops))]
    out.extend(f"{x} {y}" for x, y in ops)
    return out

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        b = data[idx:idx + n]
        idx += n
        ans.extend(solve_case(n, a, b))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
