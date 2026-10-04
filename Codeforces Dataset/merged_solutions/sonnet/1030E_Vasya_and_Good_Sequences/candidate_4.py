# CLAUSE: setup_environment
import sys
from itertools import accumulate

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return

    n = int(raw[0])
    bit_counts = [int(item).bit_count() for item in raw[1:n + 1]]

    prefix_ones = list(accumulate((count & 1 for count in bit_counts), initial=0))
    zeros = 0
    ones = 0
    for value in prefix_ones:
        if value & 1:
            ones += 1
        else:
            zeros += 1

    answer = zeros * (zeros - 1) // 2 + ones * (ones - 1) // 2

    bad = 0
    for left, first in enumerate(bit_counts):
        total = first
        largest = first
        if (total & 1) == 0 and largest * 2 > total:
            bad += 1
        for right in range(left + 1, min(n, left + 130)):
            item = bit_counts[right]
            total += item
            if item > largest:
                largest = item
            if (total & 1) == 0 and largest * 2 > total:
                bad += 1

    sys.stdout.write(f"{answer - bad}\n")

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
