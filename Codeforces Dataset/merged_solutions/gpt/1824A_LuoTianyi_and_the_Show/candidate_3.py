# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        idx = 1
        out = []

        for _ in range(t):
            n = data[idx]
            m = data[idx + 1]
            idx += 2

            left = 0
            right = 0
            fixed = set()

            for _ in range(n):
                x = data[idx]
                idx += 1
                if x == -1:
                    left += 1
                elif x == -2:
                    right += 1
                else:
                    fixed.add(x)

            seats = sorted(fixed)
            k = len(seats)

            ans = max(min(m, k + left), min(m, k + right))

            for i, x in enumerate(seats):
                free_left = x - 1 - i
                free_right = m - x - (k - i - 1)
                ans = max(ans, k + min(left, free_left) + min(right, free_right))

            out.append(str(ans))

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
