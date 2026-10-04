import sys

# CLAUSE: compute_tree_capacity_bounds
def compute_tree_capacity_bounds(h):
    return (1 << h) - 1

# CLAUSE: simulate_growth_phase
def simulate_growth_phase(h, p, total):
    moments = 0
    level_width = 1
    remaining = total
    levels_left = h
    while levels_left > 0 and level_width < p:
        done = apply_processor_cap(level_width, p)
        remaining = account_remaining_nodes(remaining, done)
        moments += 1
        levels_left -= 1
        level_width = track_ready_backlog(done)
    return moments, remaining

# CLAUSE: track_ready_backlog
def track_ready_backlog(processed_internal_nodes):
    return processed_internal_nodes * 2

# CLAUSE: apply_processor_cap
def apply_processor_cap(ready_tasks, p):
    return min(ready_tasks, p)

# CLAUSE: switch_to_bulk_work_phase
def switch_to_bulk_work_phase(remaining, p):
    if remaining <= 0:
        return 0
    return (remaining + p - 1) // p

# CLAUSE: account_remaining_nodes
def account_remaining_nodes(remaining, completed):
    return remaining - completed

# CLAUSE: finalize_minimum_moments
def finalize_minimum_moments(h, p):
    total = compute_tree_capacity_bounds(h)
    early, remaining = simulate_growth_phase(h, p, total)
    return early + switch_to_bulk_work_phase(remaining, p)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    at = 1
    for _ in range(t):
        h, p = data[at], data[at + 1]
        at += 2
        out.append(str(finalize_minimum_moments(h, p)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
