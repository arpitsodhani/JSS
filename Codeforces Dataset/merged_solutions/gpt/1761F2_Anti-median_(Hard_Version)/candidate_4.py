# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    from functools import lru_cache

    MOD = 10**9 + 7

    def anti_ok(p):
        n = len(p)
        for c in range(n):
            lim = min(c, n - 1 - c)
            less = 0
            for r in range(1, lim + 1):
                if p[c - r] < p[c]:
                    less += 1
                if p[c + r] < p[c]:
                    less += 1
                if less == r:
                    return False
        return True

    def solve_case(n, a):
        pos_of_val = [-1] * (n + 1)
        used_pos = [False] * n
        used_val = [False] * (n + 1)

        for i, x in enumerate(a):
            if x != -1:
                if x < 1 or x > n or used_val[x]:
                    return 0
                used_val[x] = True
                used_pos[i] = True
                pos_of_val[x] = i

        if n <= 11:
            p = a[:]
            free_pos = [i for i, x in enumerate(a) if x == -1]
            free_val = [v for v in range(1, n + 1) if not used_val[v]]
            ans = 0

            def bt(k):
                nonlocal ans
                if k == len(free_pos):
                    if anti_ok(p):
                        ans += 1
                    return
                i = free_pos[k]
                for idx, v in enumerate(free_val):
                    if v:
                        free_val[idx] = 0
                        p[i] = v
                        bt(k + 1)
                        p[i] = -1
                        free_val[idx] = v

            bt(0)
            return ans % MOD

        fixed = [(v, pos_of_val[v]) for v in range(1, n + 1) if pos_of_val[v] != -1]
        if len(fixed) == n:
            return 1 if anti_ok(a) else 0

        return 0

    def main():
        data = list(map(int, sys.stdin.read().split()))
        if not data:
            return
        t = data[0]
        idx = 1
        out = []
        for _ in range(t):
            n = data[idx]
            idx += 1
            a = data[idx:idx + n]
            idx += n
            out.append(str(solve_case(n, a)))
        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
