# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import defaultdict

    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    a = data[2:2 + n]

    limit = 10 ** 15

    if k == 1:
        powers = [1]
    elif k == -1:
        powers = [1, -1]
    elif k == 0:
        powers = [1, 0]
    else:
        powers = []
        x = 1
        while abs(x) <= limit:
            powers.append(x)
            x *= k

    cnt = defaultdict(int)
    cnt[0] = 1
    pref = 0
    ans = 0

    for v in a:
        pref += v
        for p in powers:
            ans += cnt[pref - p]
        cnt[pref] += 1

    print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
