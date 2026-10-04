import sys

# CLAUSE: detect_uniform_cycle
def direct_if_uniform(n, s):
    for i in range(1, n):
        if s[i] != s[0]:
            return -1
    return (n + 2) // 3

# CLAUSE: choose_breakpoint_at_transition
def cut_position(n, s):
    pairs = zip(range(n), range(1, n + 1))
    for a, b in pairs:
        if s[a] != s[b % n]:
            return b % n
    return 0

# CLAUSE: linearize_rotated_ring
def rotated_view(n, start):
    for offset in range(n):
        yield (start + offset) % n

# CLAUSE: scan_equal_direction_runs
def runs_from_view(n, s, start):
    lengths = []
    last = None
    count = 0
    for idx in rotated_view(n, start):
        if last is None or s[idx] == last:
            count += 1
        else:
            lengths.append(count)
            count = 1
        last = s[idx]
    lengths.append(count)
    return lengths

# CLAUSE: accumulate_run_repair_cost
def changes_needed(lengths):
    total = 0
    for value in lengths:
        total = total + value // 3
    return total

# CLAUSE: handle_circular_edge_cases
def solve(n, s):
    direct = direct_if_uniform(n, s)
    if direct >= 0:
        return direct
    start = cut_position(n, s)
    return changes_needed(runs_from_view(n, s, start))

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    ans = []
    p = 1
    for _ in range(t):
        n = int(data[p])
        s = data[p + 1].decode()
        p += 2
        ans.append(str(solve(n, s)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
