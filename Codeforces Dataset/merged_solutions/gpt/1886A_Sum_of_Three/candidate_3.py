# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    ans = []

    for n in data[1:1 + t]:
        if n < 7 or n == 9:
            ans.append("NO")
        else:
            ans.append("YES")
            if n % 3 == 0:
                ans.append(f"1 4 {n - 5}")
            elif n % 3 == 1:
                ans.append(f"1 2 {n - 3}")
            else:
                ans.append(f"1 2 {n - 3}")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
