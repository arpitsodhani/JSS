# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ans = []
    idx = 1

    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2

        if x >= y or x > 3 or (x == 2 and y == 3):
            ans.append("YES")
        else:
            ans.append("NO")

    print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
