# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    heights = data[1:]

    positions = defaultdict(list)
    for i, h in enumerate(heights):
        positions[h].append(i)

    active = [False] * n
    left = list(range(n))
    right = list(range(n))
    odd = 0

    def remove_interval_size(size):
        return size & 1

    def add_point(pos):
        nonlocal odd
        active[pos] = True
        l = pos
        r = pos
        odd += 1

        if pos > 0 and active[pos - 1]:
            old_l = left[pos - 1]
            old_size = pos - old_l
            odd -= remove_interval_size(old_size)
            odd -= 1
            l = old_l
            new_size = r - l + 1
            odd += new_size & 1

        if pos + 1 < n and active[pos + 1]:
            old_r = right[pos + 1]
            current_size = r - l + 1
            old_size = old_r - pos
            odd -= current_size & 1
            odd -= old_size & 1
            r = old_r
            odd += (r - l + 1) & 1

        left[r] = l
        right[l] = r
        left[pos] = l
        right[pos] = r

    ordered = sorted(positions.keys())
    possible = True
    for h in ordered[:-1]:
        for p in positions[h]:
            add_point(p)
        if odd != 0:
            possible = False
            break

    sys.stdout.write("YES\n" if possible else "NO\n")

# CLAUSE: finish_program
main()
