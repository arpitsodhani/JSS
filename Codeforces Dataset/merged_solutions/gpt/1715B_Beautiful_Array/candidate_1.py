import sys

def solve_case(n, k, b, s):
    # CLAUSE: derive_beauty_bounds
    low = b * k
    high = low + n * (k - 1)

    # CLAUSE: validate_sum_feasibility
    if s < low or s > high:
        return None

    # CLAUSE: reserve_beauty_core
    ans = [0] * n
    ans[0] = low

    # CLAUSE: allocate_remainder_budget
    rem = s - low

    # CLAUSE: distribute_surplus_across_slots
    for i in range(n):
        add = min(rem, k - 1)
        ans[i] += add
        rem -= add

    # CLAUSE: preserve_floor_contributions
    if sum(x // k for x in ans) != b:
        return None

    # CLAUSE: emit_constructed_array
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    p = 1
    for _ in range(t):
        n, k, b, s = data[p:p + 4]
        p += 4
        ans = solve_case(n, k, b, s)
        if ans is None:
            out.append("-1")
        else:
            out.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(out))

main()
