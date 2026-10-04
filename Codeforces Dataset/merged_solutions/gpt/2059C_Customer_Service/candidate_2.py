# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    p = 1
    ans = []
    for _ in range(t):
        n = data[p]
        p += 1
        caps = []
        for _ in range(n):
            row = data[p:p + n]
            p += n
            c = 0
            for x in reversed(row):
                if x == 1:
                    c += 1
                else:
                    break
            caps.append(c)
        caps.sort()
        mex = 0
        for c in caps:
            if c >= mex:
                mex += 1
        ans.append(str(mex))
    print('\n'.join(ans))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
