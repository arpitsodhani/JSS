import sys

# CLAUSE: parse_event_intervals
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
raw_intervals = [(data[i], data[i + 1]) for i in range(1, 2 * n, 2)]

# CLAUSE: preserve_original_order
events = [(r, l, idx) for idx, (l, r) in enumerate(raw_intervals)]

# CLAUSE: sort_by_deadline
events.sort()

# CLAUSE: maintain_used_dates
next_free = {}

def find_day(x):
    path = []
    while x in next_free:
        path.append(x)
        x = next_free[x]
    for y in path:
        next_free[y] = x
    return x

# CLAUSE: select_earliest_feasible_date
def earliest_available(left, right):
    day = find_day(left)
    if day > right:
        raise RuntimeError
    return day

# CLAUSE: assign_unique_schedule
answer = [0] * n
for r, l, idx in events:
    chosen = earliest_available(l, r)
    answer[idx] = chosen
    next_free[chosen] = find_day(chosen + 1)

# CLAUSE: restore_output_order
sys.stdout.write(" ".join(map(str, answer)))
