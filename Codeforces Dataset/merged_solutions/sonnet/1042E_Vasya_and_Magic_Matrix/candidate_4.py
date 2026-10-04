# CLAUSE: setup_environment
import sys
from itertools import groupby

MOD = 998244353

# CLAUSE: solve_logic
def parse_input():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    m = int(raw[1])
    total = n * m
    items = []
    at = 2
    for index in range(total):
        items.append((int(raw[at]), index // m + 1, index % m + 1, index))
        at += 1
    target = (int(raw[at]) - 1) * m + int(raw[at + 1]) - 1
    return m, total, target, items

def contribution(count, inv_count, sums, x, y):
    sum_x, sum_y, sum_sq, sum_dp = sums
    sq = x * x + y * y
    value = sum_dp + count * sq - 2 * x * sum_x - 2 * y * sum_y + sum_sq
    return value % MOD * inv_count % MOD

def main():
    m, total, target, items = parse_input()
    items.sort()
    count = 0
    sums = [0, 0, 0, 0]
    answer = 0

    for value, group in groupby(items, key=lambda item: item[0]):
        batch = list(group)
        bx = 0
        by = 0
        bsq = 0
        bdp = 0
        inv_count = pow(count, MOD - 2, MOD) if count else 0

        for cell_value, x, y, index in batch:
            sq = x * x + y * y
            dp = contribution(count, inv_count, sums, x, y) if count else 0
            if index == target:
                answer = dp
            bx = (bx + x) % MOD
            by = (by + y) % MOD
            bsq = (bsq + sq) % MOD
            bdp = (bdp + dp) % MOD

        count += len(batch)
        sums[0] = (sums[0] + bx) % MOD
        sums[1] = (sums[1] + by) % MOD
        sums[2] = (sums[2] + bsq) % MOD
        sums[3] = (sums[3] + bdp) % MOD

    sys.stdout.write(str(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
