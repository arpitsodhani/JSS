# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    n, k = map(int, input().split())
    s = input().strip()
    t = input().strip()

    x = 1
    ans = 0

    for i in range(n):
        if s[i] == t[i]:
            x *= 2
            if s[i] == 'a':
                x -= 1
            else:
                x -= 1
        else:
            x *= 2
        if x > k:
            x = k
        ans += x

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
