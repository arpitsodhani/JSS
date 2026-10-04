# CLAUSE: setup_environment
import sys
from collections import defaultdict

MOD = 998244353

# CLAUSE: solve_logic
def build_combinations(n):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = table[i][i] = 1
        for j in range(1, i):
            table[i][j] = (table[i - 1][j - 1] + table[i - 1][j]) % MOD
    return table

def solve_case(n, s, comb):
    base = n + 1

    def allowed(i, v):
        fixed = s[i - 1]
        return fixed < 0 or fixed == v

    inner = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
    open_l = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
    open_r = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]

    for i in range(1, n + 1):
        open_l[i][i][0] = 1
        open_r[i][i][0] = 1
    for i in range(1, n):
        inner[i][i + 1][0] = 1

    def extend_right(l, r, span):
        dst = open_r[l][r]
        for mid in range(l + 1, r + 1):
            choose = comb[span - 1][mid - l - 1]
            for a, wa in inner[l][mid].items():
                score_l, mid_left = divmod(a, base)
                for mid_right, wb in open_r[mid][r].items():
                    if allowed(mid, mid_left + mid_right):
                        key = score_l + 1
                        dst[key] = (dst[key] + wa * wb * choose) % MOD

    def extend_left(l, r, span):
        dst = open_l[l][r]
        for mid in range(l, r):
            choose = comb[span - 1][mid - l]
            for mid_left, wa in open_l[l][mid].items():
                for b, wb in inner[mid][r].items():
                    mid_right, score_r = divmod(b, base)
                    if allowed(mid, mid_left + mid_right):
                        key = score_r + 1
                        dst[key] = (dst[key] + wa * wb * choose) % MOD

    def close_interval(l, r):
        dst = inner[l][r]
        for mid in range(l + 1, r):
            left_gap = mid - l - 1
            right_gap = r - mid - 1
            choose = comb[left_gap + right_gap][left_gap]
            give_l = 1 if mid - l <= r - mid else 0
            give_r = 1 - give_l
            for a, wa in inner[l][mid].items():
                score_l, mid_left = divmod(a, base)
                for b, wb in inner[mid][r].items():
                    mid_right, score_r = divmod(b, base)
                    if allowed(mid, mid_left + mid_right):
                        key = (score_l + give_l) * base + score_r + give_r
                        dst[key] = (dst[key] + wa * wb * choose) % MOD

    for span in range(1, n + 1):
        for l in range(1, n - span + 1):
            extend_right(l, l + span, span)
        for l in range(1, n - span + 2):
            extend_left(l, l + span, span)
        for l in range(1, n - span):
            close_interval(l, l + span + 1)

    ans = 0
    for root in range(1, n + 1):
        split = comb[n - 1][root - 1]
        for ls, wl in open_l[1][root].items():
            for rs, wr in open_r[root][n].items():
                if allowed(root, ls + rs):
                    ans = (ans + wl * wr * split) % MOD
    return ans

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    pos = 1
    cases = []
    mx = 0
    for _ in range(t):
        n = data[pos]
        pos += 1
        s = data[pos:pos + n]
        pos += n
        cases.append((n, s))
        mx = max(mx, n)
    comb = build_combinations(mx)
    sys.stdout.write("\n".join(str(solve_case(n, s, comb)) for n, s in cases))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
