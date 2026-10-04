import sys

# CLAUSE: detect_uniform_cycle
def uniform_answer(n, s):
    if s.count(s[0]) == n:
        return (n + 2) // 3
    return None

# CLAUSE: choose_breakpoint_at_transition
def find_break(n, s):
    for i in range(n):
        if s[i] != s[(i + 1) % n]:
            return i + 1
    return 0

# CLAUSE: linearize_rotated_ring
def rotate_from(s, start):
    return s[start:] + s[:start]

# CLAUSE: scan_equal_direction_runs
def run_lengths(line):
    runs = []
    cur = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            cur += 1
        else:
            runs.append(cur)
            cur = 1
    runs.append(cur)
    return runs

# CLAUSE: accumulate_run_repair_cost
def repair_cost(runs):
    total = 0
    for length in runs:
        total += length // 3
    return total

# CLAUSE: handle_circular_edge_cases
def solve_case(n, s):
    direct = uniform_answer(n, s)
    if direct is not None:
        return direct
    start = find_break(n, s)
    linear = rotate_from(s, start)
    return repair_cost(run_lengths(linear))

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out = []
    pos = 1
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        out.append(str(solve_case(n, s)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
