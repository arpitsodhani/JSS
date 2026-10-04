import sys

# CLAUSE: identify_backward_marks
def mark_backward_kind(p):
    kind = bytearray(len(p))
    for idx, val in enumerate(p):
        if val <= idx + 1:
            kind[idx] = 1
    return kind

# CLAUSE: classify_self_blocking_chairs
def mark_self_kind(p):
    kind = bytearray(len(p))
    for idx, val in enumerate(p):
        if val == idx + 1:
            kind[idx] = 1
    return kind

# CLAUSE: maintain_available_prefix
def available(index, blocked):
    return blocked[index] == 0

# CLAUSE: choose_sit_or_skip
def sit_decision(index, backward_kind, self_kind):
    return backward_kind[index] == 1 or self_kind[index] == 1

# CLAUSE: update_future_blockers
def update_blocked(index, target, blocked):
    target -= 1
    if target > index:
        blocked[target] = 1

# CLAUSE: count_safe_sittings
def compute(p):
    backward_kind = mark_backward_kind(p)
    self_kind = mark_self_kind(p)
    blocked = bytearray(len(p))
    ans = 0
    for index, target in enumerate(p):
        if not available(index, blocked):
            return ans
        if sit_decision(index, backward_kind, self_kind):
            ans += 1
            update_blocked(index, target, blocked)
    return ans

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    lines = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        lines.append(str(compute(tokens[pos:pos + n])))
        pos += n
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
