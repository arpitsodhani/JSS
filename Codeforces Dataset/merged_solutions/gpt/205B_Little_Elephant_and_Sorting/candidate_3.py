# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    if not data:
        sys.exit()

    n = data[0]
    a = data[1:1 + n]

    ans = 0
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            ans += a[i] - a[i + 1]

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
