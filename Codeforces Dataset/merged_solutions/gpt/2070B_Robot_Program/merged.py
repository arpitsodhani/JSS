# Clause compute_prefix_displacements [Confidence: 0.60]
import sys

def solve_case(n, x, k, s):

    pref = [0]
    cur = 0
    for ch in s:
        cur += 1 if ch == 'R' else -1
        pref.append(cur)


# Clause locate_initial_zero_hit [Confidence: 0.40]
    initial_hit = seen.get(-x)


# Clause derive_cycle_zero_hit [Confidence: 0.40]
    cycle = None
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle = i
            break


# Clause account_first_execution [Confidence: 0.80]
    ans = 0
    remaining = 0
    active = first is not None and first <= k
    if active:
        ans = 1
        remaining = k - first


# Clause count_reset_cycles [Confidence: 0.80]
    if active and cycle is not None:
        ans += remaining // cycle


# Clause handle_stop_condition [Confidence: 1.00]
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


