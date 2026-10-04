import sys

def handle(n, k, b, s):
    # CLAUSE: derive_beauty_bounds
    target_core = k * b
    limit = target_core + n * (k - 1)

    # CLAUSE: validate_sum_feasibility
    outside = s < target_core or limit < s
    if outside:
        return "-1"

    # CLAUSE: reserve_beauty_core
    arr = [0] * n
    arr[0:1] = [target_core]

    # CLAUSE: allocate_remainder_budget
    surplus = s - target_core

    # CLAUSE: distribute_surplus_across_slots
    for pos, current in enumerate(arr):
        if surplus <= 0:
            break
        gained = min(surplus, k - 1)
        arr[pos] = current + gained
        surplus -= gained

    # CLAUSE: preserve_floor_contributions
    total_beauty = sum(item // k for item in arr)
    if total_beauty != b:
        return "-1"

    # CLAUSE: emit_constructed_array
    return " ".join(map(str, arr))

def main():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    pos = 1
    res = []
    for _ in range(t):
        n = int(tokens[pos])
        k = int(tokens[pos + 1])
        b = int(tokens[pos + 2])
        s = int(tokens[pos + 3])
        pos += 4
        res.append(handle(n, k, b, s))
    sys.stdout.write("\n".join(res))

main()
