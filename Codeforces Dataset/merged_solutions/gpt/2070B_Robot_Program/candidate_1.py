import sys

def solve_case(n, x, k, s):
    # CLAUSE: compute_prefix_displacements
    pref = [0]
    cur = 0
    for ch in s:
        cur += 1 if ch == 'R' else -1
        pref.append(cur)

    # CLAUSE: locate_initial_zero_hit
    first = None
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first = i
            break

    # CLAUSE: derive_cycle_zero_hit
    cycle = None
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle = i
            break

    # CLAUSE: account_first_execution
    ans = 0
    remaining = 0
    active = first is not None and first <= k
    if active:
        ans = 1
        remaining = k - first

    # CLAUSE: count_reset_cycles
    if active and cycle is not None:
        ans += remaining // cycle

    # CLAUSE: handle_stop_condition
    return ans

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    p = 1
    for _ in range(t):
        n = int(data[p])
        x = int(data[p + 1])
        k = int(data[p + 2])
        s = data[p + 3]
        p += 4
        out.append(str(solve_case(n, x, k, s)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
