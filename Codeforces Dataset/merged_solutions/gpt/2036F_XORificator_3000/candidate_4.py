# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def pref_xor(n):
        if n < 0:
            return 0
        v = [n, 1, n + 1, 0]
        return v[n & 3]

    def range_xor(l, r):
        return pref_xor(r) ^ pref_xor(l - 1)

    def bad_xor(l, r, i, k):
        step = 1 << i
        k %= step

        if l <= k:
            a = 0
        else:
            a = (l - k + step - 1) // step

        if r < k:
            return 0
        b = (r - k) // step

        if a > b:
            return 0

        cnt = b - a + 1
        high = range_xor(a, b) << i
        low = k if cnt & 1 else 0
        return high ^ low

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        t = data[0]
        ans = []
        p = 1

        for _ in range(t):
            l, r, i, k = data[p:p + 4]
            p += 4
            ans.append(str(range_xor(l, r) ^ bad_xor(l, r, i, k)))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
