# CLAUSE: setup_environment
import sys
from collections import defaultdict

# CLAUSE: solve_logic
def count_by_row_pairs(rows, width, need):
    result = 0
    for upper in range(len(rows)):
        col_sums = [0] * width
        for lower in range(upper, len(rows)):
            row = rows[lower]
            for c, value in enumerate(row):
                col_sums[c] += value
            pref = 0
            freq = defaultdict(int)
            freq[0] = 1
            for value in col_sums:
                pref += value
                result += freq[pref - need]
                freq[pref] += 1
    return result

def solve():
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n, m, k = map(int, raw[:3])
    stream = b"".join(raw[3:])
    matrix = []
    p = 0
    for _ in range(n):
        matrix.append([ch - 48 for ch in stream[p:p + m]])
        p += m

    if n <= m:
        answer = count_by_row_pairs(matrix, m, k)
    else:
        turned = [[matrix[r][c] for r in range(n)] for c in range(m)]
        answer = count_by_row_pairs(turned, n, k)

    sys.stdout.write(str(answer))

# CLAUSE: finish_program
solve()
