import sys

def solve_case(n, x, k, s):
    # CLAUSE: compute_prefix_displacements
    pref = []
    balance = 0
    for ch in s:
        if ch == "L":
            balance -= 1
        else:
            balance += 1
        pref.append(balance)

    # CLAUSE: locate_initial_zero_hit
    first_time = n + 1
    need = -x
    for idx, value in enumerate(pref):
        if value == need:
            first_time = idx + 1
            break

    # CLAUSE: derive_cycle_zero_hit
    restart_time = n + 1
    for idx, value in enumerate(pref):
        if value == 0:
            restart_time = idx + 1
            break

    # CLAUSE: account_first_execution
    answer = 0
    remaining_time = 0
    if first_time <= n and first_time <= k:
        answer = 1
        remaining_time = k - first_time

    # CLAUSE: count_reset_cycles
    if answer and restart_time <= n:
        answer += remaining_time // restart_time

    # CLAUSE: handle_stop_condition
    return answer

def main():
    it = iter(sys.stdin.read().split())
    t = int(next(it))
    res = []
    for _ in range(t):
        n = int(next(it))
        x = int(next(it))
        k = int(next(it))
        s = next(it)
        res.append(str(solve_case(n, x, k, s)))
    print("\n".join(res))

if __name__ == "__main__":
    main()
