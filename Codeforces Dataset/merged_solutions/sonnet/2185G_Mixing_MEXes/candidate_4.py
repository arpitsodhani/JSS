# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    case_count = values[pos]
    pos += 1
    result = []

    for _ in range(case_count):
        n = values[pos]
        pos += 1
        total_count = defaultdict(int)
        all_arrays = []
        total_items = 0

        for _ in range(n):
            size = values[pos]
            pos += 1
            current = values[pos:pos + size]
            pos += size
            all_arrays.append(current)
            total_items += size
            for x in current:
                total_count[x] += 1

        base_sum = 0
        remove_delta = 0
        add_targets = []

        for current in all_arrays:
            present = set(current)
            count = defaultdict(int)
            for x in current:
                count[x] += 1

            mex = 0
            while mex in present:
                mex += 1

            second_gap = mex + 1
            while second_gap in present:
                second_gap += 1

            base_sum += mex
            add_targets.append((mex, second_gap - mex))

            x = 0
            while x < mex:
                if count[x] == 1:
                    remove_delta += x - mex
                x += 1

        add_delta = sum(total_count[mex] * jump for mex, jump in add_targets)
        result.append(str(total_items * (n - 1) * base_sum + (n - 1) * remove_delta + add_delta))

    print("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
