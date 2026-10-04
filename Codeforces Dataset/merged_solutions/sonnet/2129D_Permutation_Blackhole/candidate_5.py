# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def prepare_factorials(n):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact = [1] * (n + 1)
    if n >= 0:
        invfact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        invfact[i - 1] = invfact[i] * i % MOD
    return fact, invfact

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    at = 1
    cases = []
    max_n = 0
    for _ in range(t):
        n = data[at]
        at += 1
        seq = data[at:at + n]
        at += n
        cases.append((n, seq))
        max_n = max(max_n, n)

    fact, invfact = prepare_factorials(max_n)

    def choose(a, b):
        if b < 0 or b > a:
            return 0
        return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

    res = []
    for n, target in cases:
        base = n + 1
        both = [[{} for _ in range(n + 2)] for __ in range(n + 2)]
        left_open = [[{} for _ in range(n + 2)] for __ in range(n + 2)]
        right_open = [[{} for _ in range(n + 2)] for __ in range(n + 2)]

        for i in range(1, n + 1):
            left_open[i][i][0] = 1
            right_open[i][i][0] = 1
        for i in range(1, n):
            both[i][i + 1][0] = 1

        def good(pos, score):
            want = target[pos - 1]
            return want == -1 or want == score

        def add(dst, key, val):
            old = dst.get(key)
            if old is None:
                dst[key] = val % MOD
            else:
                dst[key] = (old + val) % MOD

        for size in range(1, n + 1):
            l = 1
            while l + size <= n:
                r = l + size
                dst = right_open[l][r]
                x = l + 1
                while x <= r:
                    mul = choose(size - 1, x - l - 1)
                    for left_key, left_count in both[l][x].items():
                        outer_l, x_from_left = divmod(left_key, base)
                        for x_from_right, right_count in right_open[x][r].items():
                            if good(x, x_from_left + x_from_right):
                                add(dst, outer_l + 1, left_count * right_count * mul)
                    x += 1
                l += 1

            l = 1
            while l + size <= n + 1:
                r = l + size
                dst = left_open[l][r]
                x = l
                while x < r:
                    mul = choose(size - 1, x - l)
                    for x_from_left, left_count in left_open[l][x].items():
                        for right_key, right_count in both[x][r].items():
                            x_from_right, outer_r = divmod(right_key, base)
                            if good(x, x_from_left + x_from_right):
                                add(dst, outer_r + 1, left_count * right_count * mul)
                    x += 1
                l += 1

            width = size + 1
            l = 1
            while l + width <= n + 1:
                r = l + width
                dst = both[l][r]
                x = l + 1
                while x < r:
                    left_free = x - l - 1
                    right_free = r - x - 1
                    mul = choose(left_free + right_free, left_free)
                    nearer_l = 1 if x - l <= r - x else 0
                    nearer_r = 1 - nearer_l
                    for left_key, left_count in both[l][x].items():
                        outer_l, x_from_left = divmod(left_key, base)
                        for right_key, right_count in both[x][r].items():
                            x_from_right, outer_r = divmod(right_key, base)
                            if good(x, x_from_left + x_from_right):
                                add(dst, (outer_l + nearer_l) * base + outer_r + nearer_r, left_count * right_count * mul)
                    x += 1
                l += 1

        ans = 0
        for root in range(1, n + 1):
            ways = choose(n - 1, root - 1)
            for left_score, left_count in left_open[1][root].items():
                for right_score, right_count in right_open[root][n].items():
                    if good(root, left_score + right_score):
                        ans = (ans + left_count * right_count * ways) % MOD
        res.append(str(ans))

    sys.stdout.write("\n".join(res))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
