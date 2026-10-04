import sys

# CLAUSE: identify_backward_marks
def collect_backward_positions(p):
    good = set()
    for pos, target in enumerate(p, 1):
        if target <= pos:
            good.add(pos)
    return good

# CLAUSE: classify_self_blocking_chairs
def collect_self_positions(p):
    return {pos for pos, target in enumerate(p, 1) if target == pos}

# CLAUSE: maintain_available_prefix
def stopped_before(pos, future_marks):
    return pos in future_marks

# CLAUSE: choose_sit_or_skip
def take_current(pos, backward_positions, self_positions):
    return pos in backward_positions or pos in self_positions

# CLAUSE: update_future_blockers
def add_future_mark(pos, target, future_marks):
    if target > pos:
        future_marks.add(target)

# CLAUSE: count_safe_sittings
def maximum_sits(p):
    backward_positions = collect_backward_positions(p)
    self_positions = collect_self_positions(p)
    future_marks = set()
    sat = 0
    for pos, target in enumerate(p, 1):
        if stopped_before(pos, future_marks):
            break
        if take_current(pos, backward_positions, self_positions):
            sat += 1
            add_future_mark(pos, target, future_marks)
    return sat

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    t = nums[0]
    idx = 1
    answers = []
    for _ in range(t):
        n = nums[idx]
        idx += 1
        perm = nums[idx:idx + n]
        idx += n
        answers.append(str(maximum_sits(perm)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
