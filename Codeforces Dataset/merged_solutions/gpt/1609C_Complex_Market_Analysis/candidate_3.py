# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    import math

    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        r = int(math.isqrt(x))
        for d in range(3, r + 1, 2):
            if x % d == 0:
                return False
        return True

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        e = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n

        ans = 0

        for start in range(e):
            chain = []
            for j in range(start, n, e):
                chain.append(a[j])

            m = len(chain)
            ones_left = [0] * m
            cnt = 0

            for i in range(m):
                if chain[i] == 1:
                    cnt += 1
                else:
                    ones_left[i] = cnt
                    cnt = 0

            cnt = 0
            for i in range(m - 1, -1, -1):
                if chain[i] == 1:
                    cnt += 1
                else:
                    if is_prime(chain[i]):
                        ans += (ones_left[i] + 1) * (cnt + 1) - 1
                    cnt = 0

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
