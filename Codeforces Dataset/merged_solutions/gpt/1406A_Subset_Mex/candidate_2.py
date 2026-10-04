# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        cnt = [0] * (n + 2)
        for _ in range(n):
            x = data[idx]
            idx += 1
            if x <= n + 1:
                cnt[x] += 1
        ans = 0
        for _ in range(2):
            mex = 0
            while cnt[mex] > 0:
                cnt[mex] -= 1
                mex += 1
            ans += mex
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
