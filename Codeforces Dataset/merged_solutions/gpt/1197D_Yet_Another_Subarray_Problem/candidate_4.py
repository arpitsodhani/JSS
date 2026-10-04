# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        n, m, k = data[0], data[1], data[2]
        a = data[3:]

        neg = -10**30
        dp = [neg] * m
        ans = 0

        for x in a:
            ndp = [neg] * m
            ndp[1 % m] = x - k
            for r in range(m):
                if dp[r] == neg:
                    continue
                nr = (r + 1) % m
                val = dp[r] + x
                if r == 0:
                    val -= k
                if val > ndp[nr]:
                    ndp[nr] = val
            dp = ndp
            best = max(dp)
            if best > ans:
                ans = best

        print(ans)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
