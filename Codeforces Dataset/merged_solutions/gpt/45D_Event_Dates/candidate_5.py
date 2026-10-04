import sys

# CLAUSE: parse_event_intervals
items = list(map(int, sys.stdin.buffer.read().split()))
n = items[0]
intervals = [(items[k], items[k + 1]) for k in range(1, len(items), 2)]

# CLAUSE: preserve_original_order
by_event = []
for original, interval in enumerate(intervals):
    left, right = interval
    by_event.append({"l": left, "r": right, "i": original})

# CLAUSE: sort_by_deadline
by_event.sort(key=lambda event: (event["r"], event["l"]))

# CLAUSE: maintain_used_dates
link = {}

def locate(day):
    if day not in link:
        return day
    trail = []
    while day in link:
        trail.append(day)
        day = link[day]
    for old in trail:
        link[old] = day
    return day

# CLAUSE: select_earliest_feasible_date
def take(event):
    day = locate(event["l"])
    if day > event["r"]:
        raise RuntimeError
    return day

# CLAUSE: assign_unique_schedule
chosen_dates = [0] * n
for event in by_event:
    assigned = take(event)
    chosen_dates[event["i"]] = assigned
    link[assigned] = locate(assigned + 1)

# CLAUSE: restore_output_order
sys.stdout.write(" ".join(map(str, chosen_dates)))
