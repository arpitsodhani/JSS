import sys

# CLAUSE: detect_uniform_cycle
def uniform_cost(n, s):
    same = True
    for ch in s:
        same = same and ch == s[0]
    if same:
        return (n + 2) // 3
    return None

# CLAUSE: choose_breakpoint_at_transition
def select_cut(n, s):
    cut = 0
    for i in range(n):
        if s[i - 1] != s[i]:
            cut = i
            break
    return cut

# CLAUSE: linearize_rotated_ring
def linear_string(n, s, cut):
    left = s[cut:]
    right = s[:cut]
    return left + right

# CLAUSE: scan_equal_direction_runs
def run_scan(linear):
    groups = []
    count = 1
    for previous, current in zip(linear, linear[1:]):
        if previous == current:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)
    return groups

# CLAUSE: accumulate_run_repair_cost
def add_group_cost(groups):
    answer = 0
    for group in groups:
        answer += group // 3
    return answer

# CLAUSE: handle_circular_edge_cases
def compute(n, s):
    special = uniform_cost(n, s)
    if special is not None:
        return special
    cut = select_cut(n, s)
    linear = linear_string(n, s, cut)
    groups = run_scan(linear)
    return add_group_cost(groups)

def main():
    raw = sys.stdin.read().split()
    t = int(raw[0])
    output = []
    index = 1
    for _ in range(t):
        n = int(raw[index])
        s = raw[index + 1]
        index += 2
        output.append(str(compute(n, s)))
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
