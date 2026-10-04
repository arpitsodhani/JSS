# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    MOD = 998244353

    def inversion_count(a):
        def rec(l, r):
            if r - l == 1:
                return [a[l]], 0
            m = (l + r) // 2
            left, c1 = rec(l, m)
            right, c2 = rec(m, r)
            i = j = 0
            nl = len(left)
            nr = len(right)
            cur = c1 + c2
            merged = []
            append = merged.append
            while i < nl and j < nr:
                if left[i] <= right[j]:
                    cur += j
                    append(left[i])
                    i += 1
                else:
                    append(right[j])
                    j += 1
            while i < nl:
                cur += j
                append(left[i])
                i += 1
            if j < nr:
                merged.extend(right[j:])
            return merged, cur

        if len(a) <= 1:
            return 0
        return rec(0, len(a))[1]

    def solve_case(a, b):
        n = len(a)
        if n == 1:
            return 0

        b.sort()

        def rec(l, r):
            if r - l == 1:
                x = a[l]
                return [x * y for y in b], 0

            m = (l + r) // 2
            left, c1 = rec(l, m)
            right, c2 = rec(m, r)

            i = j = 0
            nl = len(left)
            nr = len(right)
            cur = c1 + c2
            merged = []
            append = merged.append

            while i < nl and j < nr:
                if left[i] <= right[j]:
                    cur += j
                    append(left[i])
                    i += 1
                else:
                    append(right[j])
                    j += 1

            while i < nl:
                cur += j
                append(left[i])
                i += 1

            if j < nr:
                merged.extend(right[j:])

            return merged, cur

        _, cross = rec(0, n)
        num = (cross - n * inversion_count(a)) % MOD
        den = n * (n - 1) % MOD
        return num * pow(den, MOD - 2, MOD) % MOD

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        p = 1
        ans = []
        for _ in range(t):
            n = data[p]
            p += 1
            a = data[p:p + n]
            p += n
            b = data[p:p + n]
            p += n
            ans.append(str(solve_case(a, b)))
        print("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
