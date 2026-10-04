# CLAUSE: setup_environment
import sys
from functools import lru_cache

sys.setrecursionlimit(300000)

def two_largest_total(a, b, c):
    if a < b:
        a, b = b, a
    if c > a:
        return c + a
    if c > b:
        return a + c
    return a + b

# CLAUSE: solve_logic
def solve_case(n, p):
    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i >> 1] + 1

    table = [list(range(1, n + 1))]
    k = 1
    while (1 << k) <= n:
        prev = table[-1]
        step = 1 << (k - 1)
        row = []
        limit = n - (1 << k) + 1
        for i in range(limit):
            x = prev[i]
            y = prev[i + step]
            row.append(x if p[x - 1] > p[y - 1] else y)
        table.append(row)
        k += 1

    def range_peak(l, r):
        length = r - l + 1
        k = logs[length]
        x = table[k][l - 1]
        y = table[k][r - (1 << k)]
        if p[x - 1] > p[y - 1]:
            return x
        return y

    def compact(seq):
        seq = list(set(seq))
        kept = []
        for item in seq:
            dominated = False
            a, b, c, d = item
            for other in seq:
                if other == item:
                    continue
                if other[0] >= a and other[1] >= b and other[2] >= c and other[3] >= d:
                    dominated = True
                    break
            if not dominated:
                kept.append(item)
        return tuple(kept)

    @lru_cache(None)
    def dfs(l, r, left_allowed, right_allowed):
        if l > r:
            return ((0, 0, 0, 0),)
        m = range_peak(l, r)
        left_states = dfs(l, m - 1, left_allowed, 1)
        right_states = dfs(m + 1, r, 1, right_allowed)
        made = []
        for lh, ld, ch_l, cd_l in left_states:
            for ch_r, cd_r, rh, rd in right_states:
                if left_allowed:
                    nh = max(lh, ch_l + 1, ch_r + 1)
                    nd = max(ld, cd_l, cd_r, two_largest_total(lh + 1, ch_l, ch_r))
                    made.append((nh, nd, rh, rd))
                if right_allowed:
                    nh = max(rh, ch_l + 1, ch_r + 1)
                    nd = max(rd, cd_l, cd_r, two_largest_total(ch_l, ch_r, rh + 1))
                    made.append((lh, ld, nh, nd))
        return compact(made)

    root = p.index(n) + 1
    before = dfs(1, root - 1, 0, 1)
    after = dfs(root + 1, n, 1, 0)
    answer = 0
    for left in before:
        for right in after:
            answer = max(answer, left[3], right[1], left[2] + right[0])
    return answer

# CLAUSE: finish_program
def main():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    pos = 1
    answers = []
    for _ in range(t):
        n = int(tokens[pos])
        pos += 1
        p = [int(x) for x in tokens[pos:pos + n]]
        pos += n
        pos += 1
        answers.append(str(solve_case(n, p)))
    print("\n".join(answers))

if __name__ == "__main__":
    main()
