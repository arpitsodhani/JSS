import sys

# CLAUSE: compute_tree_capacity_bounds
def compute_tree_capacity_bounds(h):
    total = 0
    width = 1
    for _ in range(h):
        total += width
        width *= 2
    return total

# CLAUSE: simulate_growth_phase
def simulate_growth_phase(h, p, total):
    ready_by_level = [1]
    moments = 0
    remaining = total
    current_level = 0
    while current_level < h and ready_by_level[-1] < p:
        completed = apply_processor_cap(ready_by_level[-1], p)
        remaining = account_remaining_nodes(remaining, completed)
        moments += 1
        current_level += 1
        ready_by_level.append(track_ready_backlog(completed))
    return moments, remaining

# CLAUSE: track_ready_backlog
def track_ready_backlog(done_internal):
    return 2 * done_internal

# CLAUSE: apply_processor_cap
def apply_processor_cap(ready_tasks, processors):
    if ready_tasks <= processors:
        return ready_tasks
    return processors

# CLAUSE: switch_to_bulk_work_phase
def switch_to_bulk_work_phase(unfinished, processors):
    q, r = divmod(unfinished, processors)
    return q + (1 if r else 0)

# CLAUSE: account_remaining_nodes
def account_remaining_nodes(unfinished, just_completed):
    return unfinished - just_completed

# CLAUSE: finalize_minimum_moments
def finalize_minimum_moments(h, p):
    total = compute_tree_capacity_bounds(h)
    prefix_time, unfinished = simulate_growth_phase(h, p, total)
    return prefix_time + switch_to_bulk_work_phase(unfinished, p)

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    out = []
    idx = 1
    for _ in range(t):
        h = int(raw[idx])
        p = int(raw[idx + 1])
        idx += 2
        out.append(str(finalize_minimum_moments(h, p)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
