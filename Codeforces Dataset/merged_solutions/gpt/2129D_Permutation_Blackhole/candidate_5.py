# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        MOD = 998244353
        DI = 12
        D = DI + 1
        MAXN = 105

        C = [[0] * MAXN for _ in range(MAXN)]
        for i in range(MAXN):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        def solve_case(n, a):
            dp = [[None] * n for _ in range(n)]
            left = [[0] * D for _ in range(n)]
            right = [[0] * D for _ in range(n)]

            left[0][0] = 1
            right[n - 1][0] = 1

            ok_pairs = []
            for v in a:
                cur = []
                for x in range(D):
                    for y in range(D):
                        if x + y <= DI and (v == -1 or v == x + y):
                            cur.append((x, y))
                ok_pairs.append(cur)

            for length in range(2, n + 1):
                if length == 2:
                    for l in range(n - 1):
                        m = [0] * (D * D)
                        m[0] = 1
                        dp[l][l + 1] = m
                else:
                    for l in range(0, n - length + 1):
                        r = l + length - 1
                        m = [0] * (D * D)
                        for ln in range(1, D):
                            base_req = 1 << (ln - 1)
                            for rn in range(D):
                                req = base_req + ((1 << (rn - 1)) if rn else 0)
                                if req > r - l:
                                    continue
                                total = 0
                                for i in range(l + 1, r):
                                    if base_req > i - l + 1:
                                        continue
                                    if rn and (1 << (rn - 1)) > r - i + 1:
                                        continue
                                    li = dp[l][i]
                                    ir = dp[i][r]
                                    if li is None or ir is None:
                                        continue
                                    pat = 0
                                    if i - l <= r - i:
                                        lrow = (ln - 1) * D
                                        for x, y in ok_pairs[i]:
                                            if x and (1 << (x - 1)) > i - l + 1:
                                                continue
                                            if y and (1 << (y - 1)) > r - i + 1:
                                                continue
                                            pat += li[lrow + x] * ir[y * D + rn]
                                    elif rn:
                                        lrow = ln * D
                                        rr = rn - 1
                                        for x, y in ok_pairs[i]:
                                            if x and (1 << (x - 1)) > i - l + 1:
                                                continue
                                            if y and (1 << (y - 1)) > r - i + 1:
                                                continue
                                            pat += li[lrow + x] * ir[y * D + rr]
                                    total += (pat % MOD) * C[r - l - 2][r - i - 1]
                                m[ln * D + rn] = total % MOD
                        dp[l][r] = m

                cur = length - 1
                for num in range(1, 8):
                    total = 0
                    for i in range(cur):
                        mat = dp[i][cur]
                        if mat is None:
                            continue
                        pat = 0
                        for x, y in ok_pairs[i]:
                            pat += left[i][x] * mat[y * D + num - 1]
                        total += (pat % MOD) * C[cur - 1][i]
                    left[cur][num] = total % MOD

                cur = n - length
                for num in range(1, 8):
                    total = 0
                    for i in range(cur + 1, n):
                        mat = dp[cur][i]
                        if mat is None:
                            continue
                        pat = 0
                        row = (num - 1) * D
                        for x, y in ok_pairs[i]:
                            pat += right[i][x] * mat[row + y]
                        total += (pat % MOD) * C[n - cur - 2][n - 1 - i]
                    right[cur][num] = total % MOD

            ans = 0
            for i in range(n):
                for x, y in ok_pairs[i]:
                    ans = (ans + left[i][x] * right[i][y] % MOD * C[n - 1][i]) % MOD
            return ans

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            t = data[0]
            idx = 1
            out = []
            for _ in range(t):
                n = data[idx]
                idx += 1
                a = data[idx:idx + n]
                idx += n
                out.append(str(solve_case(n, a)))
            print("\n".join(out))

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
