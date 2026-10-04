import sys

# CLAUSE: parse_event_intervals
tokens = sys.stdin.buffer.read().split()
n = int(tokens[0])
lefts = []
rights = []
for pos in range(n):
    lefts.append(int(tokens[1 + 2 * pos]))
    rights.append(int(tokens[2 + 2 * pos]))

# CLAUSE: preserve_original_order
indexed = []
for i in range(n):
    indexed.append((i, lefts[i], rights[i]))

# CLAUSE: sort_by_deadline
indexed = sorted(indexed, key=lambda item: (item[2], item[1]))

# CLAUSE: maintain_used_dates
parent = {}

def get_next(day):
    while parent.get(day, day) != day:
        parent[day] = parent.get(parent[day], parent[day])
        day = parent[day]
    return parent.get(day, day)

# CLAUSE: select_earliest_feasible_date
def choose_date(interval):
    _, low, high = interval
    candidate = get_next(low)
    if candidate > high:
        raise RuntimeError
    return candidate

# CLAUSE: assign_unique_schedule
scheduled = [None] * n
for event in indexed:
    picked = choose_date(event)
    scheduled[event[0]] = picked
    parent[picked] = get_next(picked + 1)

# CLAUSE: restore_output_order
print(*scheduled)
