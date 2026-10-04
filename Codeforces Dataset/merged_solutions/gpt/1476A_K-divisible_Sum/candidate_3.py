# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []

    idx = 1
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2

        s = ((n + k - 1) // k) * k
        ans.append(str((s + n - 1) // n))

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
