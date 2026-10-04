import sys

def solve_case(n, x, k, s):
    # CLAUSE: compute_prefix_displacements
    running = 0
    seen = {}
    for second, ch in enumerate(s, 1):
        running += (ch == "R") - (ch == "L")
        if running not in seen:
            seen[running] = second

    # CLAUSE: locate_initial_zero_hit
    initial_hit = seen.get(-x)

    # CLAUSE: derive_cycle_zero_hit
    loop_hit = seen.get(0)

    # CLAUSE: account_first_execution
    visits = 0
    rest = 0
    counted_first = initial_hit is not None and initial_hit <= k
    if counted_first:
        visits = 1
        rest = k - initial_hit

    # CLAUSE: count_reset_cycles
    if counted_first and loop_hit is not None:
        visits += rest // loop_hit

    # CLAUSE: handle_stop_condition
    return visits

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    out = []
    i = 1
    for _ in range(t):
        n = int(raw[i])
        x = int(raw[i + 1])
        k = int(raw[i + 2])
        s = raw[i + 3].decode()
        i += 4
        out.append(str(solve_case(n, x, k, s)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
