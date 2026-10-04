# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    out = []
    inf = 10 ** 18

    for _ in range(t):
        n = data[p]
        p += 1
        a = data[p:p + n]
        p += n
        x = data[p]
        p += 1

        b = [v - x for v in a]
        ans = n

        for i in range(n):
            bad = False
            if i >= 1 and b[i - 1] + b[i] < 0:
                bad = True
            if i >= 2 and b[i - 2] + b[i - 1] + b[i] < 0:
                bad = True
            if bad:
                ans -= 1
                b[i] = inf

        out.append(str(ans))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
