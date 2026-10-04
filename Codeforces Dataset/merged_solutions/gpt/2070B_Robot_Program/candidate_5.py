import sys

def solve_case(n, x, k, s):
    # CLAUSE: compute_prefix_displacements
    prefix = [0] * n
    pos = 0
    for i, ch in enumerate(s):
        pos += 1 if ch == "R" else -1
        prefix[i] = pos

    # CLAUSE: locate_initial_zero_hit
    first_hit = None
    target = -x
    index = 0
    while index < n:
        if prefix[index] == target:
            first_hit = index + 1
            break
        index += 1

    # CLAUSE: derive_cycle_zero_hit
    cycle_hit = None
    index = 0
    while index < n:
        if prefix[index] == 0:
            cycle_hit = index + 1
            break
        index += 1

    # CLAUSE: account_first_execution
    count = 0
    available = 0
    if first_hit is not None:
        if first_hit <= k:
            count = 1
            available = k - first_hit

    # CLAUSE: count_reset_cycles
    if count == 1 and cycle_hit is not None:
        count += available // cycle_hit

    # CLAUSE: handle_stop_condition
    return count

def main():
    items = sys.stdin.read().split()
    t = int(items[0])
    ans = []
    cursor = 1
    for _ in range(t):
        n = int(items[cursor])
        x = int(items[cursor + 1])
        k = int(items[cursor + 2])
        s = items[cursor + 3]
        cursor += 4
        ans.append(str(solve_case(n, x, k, s)))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
