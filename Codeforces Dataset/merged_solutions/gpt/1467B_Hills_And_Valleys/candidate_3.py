# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def is_bad(a, i):
        if i <= 0 or i >= len(a) - 1:
            return 0
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            return 1
        if a[i] < a[i - 1] and a[i] < a[i + 1]:
            return 1
        return 0

    def solve_case(a):
        n = len(a)
        total = sum(is_bad(a, i) for i in range(1, n - 1))
        ans = total

        for i in range(n):
            before = 0
            for j in range(i - 1, i + 2):
                before += is_bad(a, j)

            old = a[i]
            candidates = []
            if i > 0:
                candidates.append(a[i - 1])
            if i + 1 < n:
                candidates.append(a[i + 1])

            for x in candidates:
                a[i] = x
                after = 0
                for j in range(i - 1, i + 2):
                    after += is_bad(a, j)
                ans = min(ans, total - before + after)

            a[i] = old

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
            out.append(str(solve_case(a)))

        print("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
