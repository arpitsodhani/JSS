# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def capped_power_two(exp, cap):
        if exp >= cap.bit_length():
            return cap + 1
        return 1 << exp

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            return

        t = data[0]
        pairs = []
        idx = 1
        max_k = 1
        for _ in range(t):
            n = data[idx]
            k = data[idx + 1]
            idx += 2
            pairs.append((n, k))
            if k > max_k:
                max_k = k

        out = []
        for n, k in pairs:
            total = capped_power_two(n - 1, max_k)
            if k > total:
                out.append("-1")
                continue

            ans = [0] * n
            l, r = 0, n - 1

            for x in range(1, n):
                block = capped_power_two(n - x - 1, max_k)
                if k <= block:
                    ans[l] = x
                    l += 1
                else:
                    ans[r] = x
                    r -= 1
                    k -= block

            ans[l] = n
            out.append(" ".join(map(str, ans)))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
