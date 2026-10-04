# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    n = len(a)

    obs = []
    for i in range(n):
        m = 0
        if a[i] == 'X':
            m |= 1
        if b[i] == 'X':
            m |= 2
        obs.append(m)

    pieces = [
        (3, 1),
        (3, 2),
        (1, 3),
        (2, 3),
    ]

    neg = -10**9
    dp = [neg] * 4
    dp[0] = 0

    for i in range(n):
        ndp = [neg] * 4
        next_obs = obs[i + 1] if i + 1 < n else 3

        for carry in range(4):
            if dp[carry] < 0:
                continue
            cur_blocked = obs[i] | carry

            ndp[0] = max(ndp[0], dp[carry])

            for cur_mask, next_mask in pieces:
                if (cur_mask & cur_blocked) == 0 and (next_mask & next_obs) == 0:
                    ndp[next_mask] = max(ndp[next_mask], dp[carry] + 1)

        dp = ndp

    print(max(dp))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
