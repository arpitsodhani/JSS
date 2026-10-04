# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def solve():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n, m = map(int, input().split())
        a = [input().strip() for _ in range(n)]
        ans = [list(row) for row in a]
        ok = True
        for i in range(n):
            cnt = sum((1 for j in range(m) if a[i][j] in 'UD'))
            if cnt % 2:
                ok = False
        for j in range(m):
            cnt = sum((1 for i in range(n) if a[i][j] in 'LR'))
            if cnt % 2:
                ok = False
        if not ok:
            out.append('-1')
            continue
        for i in range(n):
            k = 0
            for j in range(m):
                if a[i][j] == 'U':
                    if k % 2 == 0:
                        ans[i][j] = 'W'
                        ans[i + 1][j] = 'B'
                    else:
                        ans[i][j] = 'B'
                        ans[i + 1][j] = 'W'
                    k += 1
        for j in range(m):
            k = 0
            for i in range(n):
                if a[i][j] == 'L':
                    if k % 2 == 0:
                        ans[i][j] = 'W'
                        ans[i][j + 1] = 'B'
                    else:
                        ans[i][j] = 'B'
                        ans[i][j + 1] = 'W'
                    k += 1
        out.extend((''.join(row) for row in ans))
    print('\n'.join(out))
if __name__ == '__main__':
    solve()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
