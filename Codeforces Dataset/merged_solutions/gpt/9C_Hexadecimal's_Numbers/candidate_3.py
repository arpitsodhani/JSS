# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())

    ans = 0

    def dfs(x):
        global ans
        if x > n:
            return
        if x > 0:
            ans += 1
        dfs(x * 10)
        dfs(x * 10 + 1)

    dfs(1)
    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
