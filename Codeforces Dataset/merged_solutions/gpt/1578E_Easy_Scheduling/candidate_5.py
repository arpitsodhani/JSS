import sys

# CLAUSE: compute_tree_capacity_bounds
def compute_tree_capacity_bounds(h):
    top_power = 1 << h
    return top_power - 1

# CLAUSE: simulate_growth_phase
def simulate_growth_phase(h, p):
    moments = 0
    processed = 0
    frontier = 1
    remaining_height = h
    while remaining_height and not switch_to_bulk_work_phase(frontier, p):
        capacity_used = apply_processor_cap(frontier, p)
        processed = account_remaining_nodes(processed, capacity_used)
        moments += 1
        remaining_height -= 1
        frontier = track_ready_backlog(capacity_used)
    return moments, processed

# CLAUSE: track_ready_backlog
def track_ready_backlog(internal_done):
    return internal_done << 1

# CLAUSE: apply_processor_cap
def apply_processor_cap(frontier, p):
    return frontier if frontier < p else p

# CLAUSE: switch_to_bulk_work_phase
def switch_to_bulk_work_phase(ready, p):
    return ready >= p

# CLAUSE: account_remaining_nodes
def account_remaining_nodes(done_so_far, done_now):
    return done_so_far + done_now

# CLAUSE: finalize_minimum_moments
def finalize_minimum_moments(h, p):
    early, completed = simulate_growth_phase(h, p)
    remaining = compute_tree_capacity_bounds(h) - completed
    return early + ((remaining + p - 1) // p)

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    answers = []
    for i in range(1, len(values), 2):
        answers.append(str(finalize_minimum_moments(values[i], values[i + 1])))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
