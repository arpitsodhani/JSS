import sys

# CLAUSE: compute_tree_capacity_bounds
def compute_tree_capacity_bounds(h):
    return pow(2, h) - 1

# CLAUSE: simulate_growth_phase
def simulate_growth_phase(h, p):
    state = {"time": 0, "ready": 1, "left": compute_tree_capacity_bounds(h), "level": 0}
    while state["level"] < h and state["ready"] < p:
        processed = apply_processor_cap(state["ready"], p)
        state["left"] = account_remaining_nodes(state["left"], processed)
        state["time"] += 1
        state["level"] += 1
        state["ready"] = track_ready_backlog(processed)
    return state

# CLAUSE: track_ready_backlog
def track_ready_backlog(processed):
    return processed << 1

# CLAUSE: apply_processor_cap
def apply_processor_cap(ready, p):
    return min(ready, p)

# CLAUSE: switch_to_bulk_work_phase
def switch_to_bulk_work_phase(state, p):
    if state["left"] == 0:
        return 0
    return -(-state["left"] // p)

# CLAUSE: account_remaining_nodes
def account_remaining_nodes(left, processed):
    left -= processed
    return left

# CLAUSE: finalize_minimum_moments
def finalize_minimum_moments(h, p):
    state = simulate_growth_phase(h, p)
    return state["time"] + switch_to_bulk_work_phase(state, p)

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(it)
    res = []
    for _ in range(t):
        res.append(str(finalize_minimum_moments(next(it), next(it))))
    print("\n".join(res))

if __name__ == "__main__":
    main()
