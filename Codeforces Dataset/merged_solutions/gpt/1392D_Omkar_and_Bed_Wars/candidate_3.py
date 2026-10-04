import sys

# CLAUSE: detect_uniform_cycle
def all_same(n, s):
    return len(set(s)) == 1

# CLAUSE: choose_breakpoint_at_transition
def boundary_after_change(n, s):
    for right in range(n):
        left = (right - 1) % n
        if s[left] != s[right]:
            return right
    return 0

# CLAUSE: linearize_rotated_ring
def segment_order(n, start):
    return [(start + offset) % n for offset in range(n)]

# CLAUSE: scan_equal_direction_runs
def scan_by_indices(s, order):
    runs = []
    previous = s[order[0]]
    size = 0
    for idx in order:
        current = s[idx]
        if current == previous:
            size += 1
        else:
            runs.append(size)
            previous = current
            size = 1
    runs.append(size)
    return runs

# CLAUSE: accumulate_run_repair_cost
def sum_repairs(runs):
    changes = 0
    for run in runs:
        changes += run // 3
    return changes

# CLAUSE: handle_circular_edge_cases
def process(n, s):
    if all_same(n, s):
        return (n + 2) // 3
    start = boundary_after_change(n, s)
    order = segment_order(n, start)
    runs = scan_by_indices(s, order)
    return sum_repairs(runs)

def main():
    it = iter(sys.stdin.read().split())
    t = int(next(it))
    answers = []
    for _ in range(t):
        n = int(next(it))
        s = next(it)
        answers.append(str(process(n, s)))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    main()
