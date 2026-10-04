import sys

# CLAUSE: identify_backward_marks
def build_backward_table(perm):
    table = [0] * (len(perm) + 1)
    for i in range(1, len(perm) + 1):
        if perm[i - 1] <= i:
            table[i] = 1
    return table

# CLAUSE: classify_self_blocking_chairs
def build_self_table(perm):
    table = [0] * (len(perm) + 1)
    for i in range(1, len(perm) + 1):
        if perm[i - 1] == i:
            table[i] = 1
    return table

# CLAUSE: maintain_available_prefix
def still_reachable(i, blocked):
    return blocked[i] == 0

# CLAUSE: choose_sit_or_skip
def selected_by_greedy(i, backward, self_mark):
    if self_mark[i]:
        return True
    return backward[i] == 1

# CLAUSE: update_future_blockers
def apply_selection(i, perm, blocked):
    j = perm[i - 1]
    if j > i:
        blocked[j] = 1

# CLAUSE: count_safe_sittings
def answer_for(perm):
    n = len(perm)
    backward = build_backward_table(perm)
    self_mark = build_self_table(perm)
    blocked = [0] * (n + 1)
    count = 0
    i = 1
    while i <= n:
        if not still_reachable(i, blocked):
            break
        if selected_by_greedy(i, backward, self_mark):
            count += 1
            apply_selection(i, perm, blocked)
        i += 1
    return count

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ptr = 1
    out = []
    for _ in range(t):
        n = data[ptr]
        ptr += 1
        out.append(str(answer_for(data[ptr:ptr + n])))
        ptr += n
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
