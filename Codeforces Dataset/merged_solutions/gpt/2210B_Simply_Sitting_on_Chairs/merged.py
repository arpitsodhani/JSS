# Clause identify_backward_marks [Confidence: 0.60]
import sys

def mark_backward_kind(p):
    kind = bytearray(len(p))
    for idx, val in enumerate(p):
        if val <= idx + 1:
            kind[idx] = 1
    return kind


# Clause classify_self_blocking_chairs [Confidence: 0.40]
def collect_self_positions(p):
    return {pos for pos, target in enumerate(p, 1) if target == pos}


# Clause maintain_available_prefix [Confidence: 1.00]
def available(index, blocked):
    return blocked[index] == 0


# Clause choose_sit_or_skip [Confidence: 0.60]
def sit_decision(index, backward_kind, self_kind):
    return backward_kind[index] == 1 or self_kind[index] == 1


# Clause update_future_blockers [Confidence: 0.60]
def apply_selection(i, perm, blocked):
    j = perm[i - 1]
    if j > i:
        blocked[j] = 1


# Clause count_safe_sittings [Confidence: 1.00]
def solve_case(p):
    n = len(p)
    backward = backward_flags(p)
    same_place = self_flags(p)
    marked = [False] * n
    ans = 0
    for i in range(n):
        if not chair_is_open(i, marked):
            break
        if should_sit(i, p, backward, same_place):
            ans += 1
            mark_after_sitting(i, p, marked)
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    at = 1
    out = []
    for _ in range(t):
        n = data[at]
        at += 1
        p = data[at:at + n]
        at += n
        out.append(str(solve_case(p)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()


