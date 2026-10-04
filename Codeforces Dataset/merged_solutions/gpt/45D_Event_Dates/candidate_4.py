import sys

# CLAUSE: parse_event_intervals
stream = iter(map(int, sys.stdin.buffer.read().split()))
n = next(stream)
intervals = []
for _ in range(n):
    intervals.append([next(stream), next(stream)])

# CLAUSE: preserve_original_order
events = []
for index, bounds in enumerate(intervals):
    bounds.append(index)
    events.append(bounds)

# CLAUSE: sort_by_deadline
events.sort(key=lambda bounds: (bounds[1], bounds[0]))

# CLAUSE: maintain_used_dates
representative = {}

def first_free(start):
    stack = []
    while start in representative:
        stack.append(start)
        start = representative[start]
    for item in stack:
        representative[item] = start
    return start

# CLAUSE: select_earliest_feasible_date
def select(bounds):
    day = first_free(bounds[0])
    if day > bounds[1]:
        raise RuntimeError
    return day

# CLAUSE: assign_unique_schedule
result = [0] * n
for bounds in events:
    day = select(bounds)
    result[bounds[2]] = day
    representative[day] = first_free(day + 1)

# CLAUSE: restore_output_order
sys.stdout.write(*[" ".join(map(str, result))])
