import sys

# CLAUSE: identify_backward_marks
def backward_flags(p):
    return [value <= index + 1 for index, value in enumerate(p)]

# CLAUSE: classify_self_blocking_chairs
def self_flags(p):
    return [value == index + 1 for index, value in enumerate(p)]

# CLAUSE: maintain_available_prefix
def chair_is_open(i, marked):
    return not marked[i]

# CLAUSE: choose_sit_or_skip
def should_sit(i, p, backward, same_place):
    return backward[i] or same_place[i]

# CLAUSE: update_future_blockers
def mark_after_sitting(i, p, marked):
    target = p[i] - 1
    if target > i:
        marked[target] = True

# CLAUSE: count_safe_sittings
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
