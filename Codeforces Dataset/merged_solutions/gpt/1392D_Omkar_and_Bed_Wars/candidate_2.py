import sys

# CLAUSE: detect_uniform_cycle
def is_single_cycle(s):
    first = s[0]
    for ch in s:
        if ch != first:
            return False
    return True

# CLAUSE: choose_breakpoint_at_transition
def transition_start(s, n):
    idx = 0
    while s[idx] == s[(idx + 1) % n]:
        idx += 1
    return (idx + 1) % n

# CLAUSE: linearize_rotated_ring
def make_linear(s, start, n):
    chars = []
    for step in range(n):
        chars.append(s[(start + step) % n])
    return chars

# CLAUSE: scan_equal_direction_runs
def collect_runs(chars):
    result = []
    i = 0
    n = len(chars)
    while i < n:
        j = i + 1
        while j < n and chars[j] == chars[i]:
            j += 1
        result.append(j - i)
        i = j
    return result

# CLAUSE: accumulate_run_repair_cost
def count_changes(lengths):
    return sum(length // 3 for length in lengths)

# CLAUSE: handle_circular_edge_cases
def answer(n, s):
    if is_single_cycle(s):
        return (n + 2) // 3
    start = transition_start(s, n)
    chars = make_linear(s, start, n)
    lengths = collect_runs(chars)
    return count_changes(lengths)

def main():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    res = []
    k = 1
    for _ in range(t):
        n = int(tokens[k])
        s = tokens[k + 1].decode()
        k += 2
        res.append(str(answer(n, s)))
    print("\n".join(res))

if __name__ == "__main__":
    main()
