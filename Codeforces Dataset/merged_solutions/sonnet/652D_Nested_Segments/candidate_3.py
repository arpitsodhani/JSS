# CLAUSE: setup_environment
import sys
from bisect import bisect_left

def update(bit, pos):
    size = len(bit)
    while pos < size:
        bit[pos] += 1
        pos += pos & -pos

def prefix(bit, pos):
    total = 0
    while pos:
        total += bit[pos]
        pos -= pos & -pos
    return total

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    n = values[0]
    intervals = [(values[i], values[i + 1], (i - 1) // 2) for i in range(1, 2 * n, 2)]
    compressed = sorted(values[i + 1] for i in range(1, 2 * n, 2))
    intervals.sort(reverse=True)

    bit = [0] * (n + 1)
    result = [0] * n
    for left, right, index in intervals:
        place = bisect_left(compressed, right) + 1
        result[index] = prefix(bit, place - 1)
        update(bit, place)

    sys.stdout.write("\n".join(str(x) for x in result))

# CLAUSE: finish_program
main()
