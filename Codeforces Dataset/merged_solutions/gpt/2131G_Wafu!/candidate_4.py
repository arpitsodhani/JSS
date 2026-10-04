# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 10**9 + 7

    def solve_case(n, k, arr):
        exps = [x - 1 for x in arr]
        small_set = {e for e in exps if e <= 30}

        pref = [0] * 32
        for r in range(1, 32):
            pref[r] = pref[r - 1]
            if r - 1 in small_set:
                pref[r] += 1 << (r - 1)

        div = [0] * 32
        for r in range(32):
            d = 1 << r
            a = pref[r] % d
            div[r] = (((a - k) % d) + k) // d

        ans = 1
        for r in range(31):
            cnt = div[r] - div[r + 1]
            if cnt:
                ans = ans * pow(r + 1, cnt, MOD) % MOD

        small = [e for e in exps if e < 30]
        large = [e for e in exps if e >= 30]
        min_large = min(large) if large else 10**30
        max_exp = max(exps)

        def ok(t):
            total = 0
            for e in small:
                if e < t:
                    total += 1 << e
                    if total >= k:
                        return False
            if min_large < t:
                return False
            return total < k

        lo, hi = 0, max_exp + 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid

        if lo > 30:
            ans = ans * (lo + 1) % MOD

        return ans

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []
        for _ in range(t):
            n = data[idx]
            k = data[idx + 1]
            idx += 2
            arr = data[idx:idx + n]
            idx += n
            out.append(str(solve_case(n, k, arr)))
        print("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
