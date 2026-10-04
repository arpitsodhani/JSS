# CLAUSE: setup_environment
import sys
from array import array

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    x = int(data[1])
    inf = n + 1

    first = array("i", [inf]) * (x + 4)
    last = array("i", [0]) * (x + 4)

    for i, token in enumerate(data[2:], 1):
        v = int(token)
        if first[v] == inf:
            first[v] = i
        last[v] = i

    prefix_good = bytearray(x + 4)
    suffix_good = bytearray(x + 5)
    prefix_good[0] = 1
    suffix_good[x + 1] = 1

    prefix_end = array("i", [0]) * (x + 4)
    suffix_start = array("i", [inf]) * (x + 5)

    max_seen = 0
    for v in range(1, x + 1):
        if prefix_good[v - 1] and max_seen <= first[v]:
            prefix_good[v] = 1
        if last[v] > max_seen:
            max_seen = last[v]
        prefix_end[v] = max_seen

    min_seen = inf
    for v in range(x, 0, -1):
        if suffix_good[v + 1] and last[v] <= min_seen:
            suffix_good[v] = 1
        if first[v] < min_seen:
            min_seen = first[v]
        suffix_start[v] = min_seen

    ans = 0
    r = 1
    for l in range(1, x + 1):
        before = l - 1
        if not prefix_good[before]:
            break
        if r < l:
            r = l
        needed = prefix_end[before]
        while r <= x and (not suffix_good[r + 1] or needed > suffix_start[r + 1]):
            r += 1
        if r <= x:
            ans += x - r + 1

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
