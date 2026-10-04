# CLAUSE: setup_environment
import sys
import math

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.read().split()))
    if len(data) < 8:
        return
    A = [[data[i], i] for i in range(4)]
    B = [[data[i + 4], i] for i in range(4)]
    C = [[data[i], i] for i in range(4)]
    A.sort()
    B.sort()
    ga = 0
    gb = 0
    for i in range(1, 4):
        ga = math.gcd(ga, A[i][0] - A[0][0])
        gb = math.gcd(gb, B[i][0] - B[0][0])
    if ga != gb or (ga != 0 and (A[0][0] - B[0][0]) % ga != 0):
        print(-1)
        return
    if ga == 0:
        print(0 if A[0][0] == B[0][0] else -1)
        return
    r = A[0][0] % ga
    cnt = [0, 0]
    for i in range(4):
        A[i][0] = (A[i][0] - r) // ga
        B[i][0] = (B[i][0] - r) // ga
        cnt[A[i][0] & 1] += 1
        cnt[B[i][0] & 1] -= 1
    if cnt[0] or cnt[1]:
        print(-1)
        return
    ra = []
    rb = []

    def chk(s):
        s.sort()

    def sym(s, ret, i, j, real=False):
        if real:
            ii = jj = -1
            for x in range(4):
                if s[x][1] == i:
                    ii = x
                if s[x][1] == j:
                    jj = x
            i, j = (ii, jj)
        s[i][0] = 2 * s[j][0] - s[i][0]
        ret.append((s[i][1], s[j][1]))

    def gather(s, ret):
        while True:
            chk(s)
            d = s[3][0] - s[0][0]
            if d == 1:
                break
            ok = False
            for j in (1, 2):
                if 4 * (s[j][0] - s[0][0]) >= d and 4 * (s[3][0] - s[j][0]) >= d:
                    if s[j][0] - s[0][0] <= s[3][0] - s[j][0]:
                        sym(s, ret, 0, j)
                    else:
                        sym(s, ret, 3, j)
                    ok = True
                    break
            if ok:
                continue
            dl = min(s[1][0] - s[0][0], s[3][0] - s[1][0])
            dr = min(s[2][0] - s[0][0], s[3][0] - s[2][0])
            if dl < dr:
                if s[1][0] - s[0][0] == dl:
                    if s[3][0] - s[2][0] == dr:
                        sym(s, ret, 1, 2)
                        sym(s, ret, 1, 3)
                    else:
                        sym(s, ret, 1, 0)
                        sym(s, ret, 1, 2)
                elif s[3][0] - s[2][0] == dr:
                    sym(s, ret, 1, 3)
                    sym(s, ret, 1, 2)
                else:
                    sym(s, ret, 1, 2)
                    sym(s, ret, 1, 0)
            elif s[3][0] - s[2][0] == dr:
                if s[1][0] - s[0][0] == dl:
                    sym(s, ret, 2, 1)
                    sym(s, ret, 2, 0)
                else:
                    sym(s, ret, 2, 3)
                    sym(s, ret, 2, 1)
            elif s[1][0] - s[0][0] == dl:
                sym(s, ret, 2, 0)
                sym(s, ret, 2, 1)
            else:
                sym(s, ret, 2, 1)
                sym(s, ret, 2, 3)
        chk(s)
        if s[0][0] & 1:
            for j in range(4):
                if s[j][0] != s[3][0]:
                    sym(s, ret, j, 3)
        chk(s)
    gather(A, ra)
    gather(B, rb)

    def slide():
        s = A[0][0]
        t = B[0][0]
        if s == t:
            return
        ex = []
        length = abs(t - s) // 2
        rollback = False
        while True:
            chk(A)
            d = A[3][0] - A[0][0]
            if length == 0 and d == 1:
                break
            while not rollback and d < length:
                chk(A)
                sym(A, ex, 2, 0)
                sym(A, ex, 1, 3)
                chk(A)
                d = A[3][0] - A[0][0]
                ra.append(ex[-2])
                ra.append(ex[-1])
            if rollback:
                rollback = False
            if d > length:
                rollback = True
                u = ex[-2]
                v = ex[-1]
                sym(A, ra, v[0], v[1], True)
                sym(A, ra, u[0], u[1], True)
                ex.pop()
                ex.pop()
                continue
            length -= d
            for _ in range(2):
                chk(A)
                if s < t:
                    for i in range(3):
                        sym(A, ra, i, 3)
                else:
                    for i in range(1, 4):
                        sym(A, ra, i, 0)
    slide()
    chk(A)
    chk(B)
    bid = [0] * 4
    for i in range(4):
        bid[B[i][1]] = A[i][1]
    while rb:
        x, y = rb.pop()
        ra.append((bid[x], bid[y]))
    ans = []
    for x, y in ra:
        if C[x][0] != C[y][0]:
            ans.append((C[x][0], C[y][0]))
        C[x][0] = 2 * C[y][0] - C[x][0]
    print(len(ans))
    for x, y in ans:
        print(x, y)
if __name__ == '__main__':
    main()

# CLAUSE: finish_program
RESULT_SENTINEL = 0
