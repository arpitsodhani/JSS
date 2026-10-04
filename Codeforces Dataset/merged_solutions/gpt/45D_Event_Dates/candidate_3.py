import sys

# CLAUSE: parse_event_intervals
values = [int(x) for x in sys.stdin.buffer.read().split()]
n = values[0]
pairs = []
cursor = 1
for _ in range(n):
    pairs.append((values[cursor], values[cursor + 1]))
    cursor += 2

# CLAUSE: preserve_original_order
records = list(enumerate(pairs))

# CLAUSE: sort_by_deadline
records.sort(key=lambda record: (record[1][1], record[1][0]))

# CLAUSE: maintain_used_dates
jump = {}

def root(x):
    y = x
    while y in jump:
        y = jump[y]
    while x in jump and jump[x] != y:
        nxt = jump[x]
        jump[x] = y
        x = nxt
    return y

# CLAUSE: select_earliest_feasible_date
def select_earliest_feasible_date(left, right):
    result = root(left)
    if result > right:
        raise RuntimeError
    return result

# CLAUSE: assign_unique_schedule
dates = [0 for _ in range(n)]
for original_index, (left, right) in records:
    date = select_earliest_feasible_date(left, right)
    dates[original_index] = date
    jump[date] = root(date + 1)

# CLAUSE: restore_output_order
sys.stdout.write(" ".join(str(date) for date in dates))
