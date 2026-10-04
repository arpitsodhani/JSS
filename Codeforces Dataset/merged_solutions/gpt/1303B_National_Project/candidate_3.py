# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def solve():
        data = list(map(int, sys.stdin.buffer.read().split()))
        t = data[0]
        ans = []
        idx = 1

        for _ in range(t):
            n, g, b = data[idx], data[idx + 1], data[idx + 2]
            idx += 3

            need_good = (n + 1) // 2
            full_good_blocks = (need_good - 1) // g
            days = full_good_blocks * (g + b) + (need_good - full_good_blocks * g)
            ans.append(str(max(n, days)))

        sys.stdout.write("\n".join(ans))

    if __name__ == "__main__":
        solve()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
