import sys

# CLAUSE: compute_tree_capacity_bounds
def compute_tree_capacity_bounds(height):
    nodes = 1
    for _ in range(height):
        nodes <<= 1
    return nodes - 1

# CLAUSE: simulate_growth_phase
def simulate_growth_phase(height, processors):
    ready = 1
    spent = 0
    done_total = 0
    depth = 0
    while depth < height and ready < processors:
        used = apply_processor_cap(ready, processors)
        done_total += used
        spent += 1
        depth += 1
        ready = track_ready_backlog(used)
    return spent, done_total

# CLAUSE: track_ready_backlog
def track_ready_backlog(completed_here):
    return completed_here + completed_here

# CLAUSE: apply_processor_cap
def apply_processor_cap(waiting, processors):
    return waiting if waiting < processors else processors

# CLAUSE: switch_to_bulk_work_phase
def switch_to_bulk_work_phase(waiting, processors):
    return (waiting + processors - 1) // processors

# CLAUSE: account_remaining_nodes
def account_remaining_nodes(height, already_done):
    return compute_tree_capacity_bounds(height) - already_done

# CLAUSE: finalize_minimum_moments
def finalize_minimum_moments(height, processors):
    early_time, completed = simulate_growth_phase(height, processors)
    remaining = account_remaining_nodes(height, completed)
    return early_time + switch_to_bulk_work_phase(remaining, processors)

def main():
    nums = list(map(int, sys.stdin.buffer.read().split()))
    ans = []
    pos = 1
    for _ in range(nums[0]):
        h = nums[pos]
        p = nums[pos + 1]
        pos += 2
        ans.append(str(finalize_minimum_moments(h, p)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
