# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    if len(data) >= 2 and data[0] == len(data) - 1:
        tests = data[1:]
    else:
        tests = data
    out = []
    for n in tests:
        ans = 0
        l = 1
        while l <= n:
            q = n // l
            r = n // q
            ans += (r - l + 1) * q * q
            l = r + 1
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
