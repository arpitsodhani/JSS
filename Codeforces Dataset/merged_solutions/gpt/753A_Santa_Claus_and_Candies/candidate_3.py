# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    n = int(sys.stdin.readline())

    ans = []
    cur = 1
    while n >= cur:
        ans.append(cur)
        n -= cur
        cur += 1

    if n:
        ans[-1] += n

    print(len(ans))
    print(*ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
