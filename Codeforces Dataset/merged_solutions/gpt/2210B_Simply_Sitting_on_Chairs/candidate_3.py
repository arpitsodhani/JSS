import sys

# CLAUSE: identify_backward_marks
def is_backward_or_current(pos, target):
    return target <= pos

# CLAUSE: classify_self_blocking_chairs
def is_self_mark(pos, target):
    return target == pos

# CLAUSE: maintain_available_prefix
def reached_marked_chair(pos, first_block):
    return pos == first_block

# CLAUSE: choose_sit_or_skip
def greedy_choice(pos, target):
    return is_backward_or_current(pos, target) or is_self_mark(pos, target)

# CLAUSE: update_future_blockers
def next_block_after_sit(pos, target, first_block):
    if target > pos and target < first_block:
        return target
    return first_block

# CLAUSE: count_safe_sittings
def run_game(p):
    stop = len(p) + 1
    total = 0
    for pos in range(1, len(p) + 1):
        if reached_marked_chair(pos, stop):
            break
        target = p[pos - 1]
        if greedy_choice(pos, target):
            total += 1
            stop = next_block_after_sit(pos, target, stop)
    return total

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    tests = values[0]
    k = 1
    res = []
    for _ in range(tests):
        n = values[k]
        k += 1
        res.append(str(run_game(values[k:k + n])))
        k += n
    sys.stdout.write("\n".join(res))

if __name__ == "__main__":
    main()
