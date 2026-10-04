# CLAUSE: setup_environment
import sys
from collections import defaultdict

MOD = 998244353

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    ptr = 0
    t = data[ptr]
    ptr += 1
    tests = []
    max_n = 0
    for _ in range(t):
        n = data[ptr]
        ptr += 1
        s = data[ptr:ptr + n]
        ptr += n
        tests.append((n, s))
        if n > max_n:
            max_n = n

    comb = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    for i in range(max_n + 1):
        comb[i][0] = 1
        comb[i][i] = 1
        for j in range(1, i):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

    out = []
    for n, s in tests:
        base = n + 1

        def ok(pos, val):
            need = s[pos - 1]
            return need == -1 or need == val

        both = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
        ropen = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]
        lopen = [[defaultdict(int) for _ in range(n + 2)] for __ in range(n + 2)]

        for i in range(1, n + 1):
            ropen[i][i][0] = 1
            lopen[i][i][0] = 1
        for i in range(1, n):
            both[i][i + 1][0] = 1

        for length in range(1, n + 1):
            for l in range(1, n - length + 1):
                r = l + length
                cur = ropen[l][r]
                for x in range(l + 1, r + 1):
                    choose = comb[length - 1][x - l - 1]
                    for kl, wl in both[l][x].items():
                        add_l, add_x_l = divmod(kl, base)
                        for add_x_r, wr in ropen[x][r].items():
                            if ok(x, add_x_l + add_x_r):
                                key = add_l + 1
                                cur[key] = (cur[key] + wl * wr * choose) % MOD

            for l in range(1, n - length + 2):
                r = l + length
                cur = lopen[l][r]
                for x in range(l, r):
                    choose = comb[length - 1][x - l]
                    for add_x_l, wl in lopen[l][x].items():
                        for kr, wr in both[x][r].items():
                            add_x_r, add_r = divmod(kr, base)
                            if ok(x, add_x_l + add_x_r):
                                key = add_r + 1
                                cur[key] = (cur[key] + wl * wr * choose) % MOD

            gap = length + 1
            for l in range(1, n - gap + 2):
                r = l + gap
                cur = both[l][r]
                for x in range(l + 1, r):
                    choose = comb[r - l - 2][x - l - 1]
                    add_left = 1 if x - l <= r - x else 0
                    add_right = 1 - add_left
                    for kl, wl in both[l][x].items():
                        left_end, mid_l = divmod(kl, base)
                        for kr, wr in both[x][r].items():
                            mid_r, right_end = divmod(kr, base)
                            if ok(x, mid_l + mid_r):
                                key = (left_end + add_left) * base + right_end + add_right
                                cur[key] = (cur[key] + wl * wr * choose) % MOD

        ans = 0
        for root in range(1, n + 1):
            choose = comb[n - 1][root - 1]
            for left_score, wl in lopen[1][root].items():
                for right_score, wr in ropen[root][n].items():
                    if ok(root, left_score + right_score):
                        ans = (ans + wl * wr * choose) % MOD
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
