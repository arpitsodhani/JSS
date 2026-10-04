# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []

    idx = 1
    for _ in range(t):
        x, y = data[idx], data[idx + 1]
        idx += 2
        if x > y:
            x, y = y, x
        ans.append(f"{x} {y}")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
