import sys

def solve_case(A, B, C, k):
    la = 10 ** (A - 1)
    ra = 10 ** A - 1
    lb0 = 10 ** (B - 1)
    rb0 = 10 ** B - 1
    lc = 10 ** (C - 1)
    rc = 10 ** C - 1

    for a in range(la, ra + 1):
        lb = max(lb0, lc - a)
        rb = min(rb0, rc - a)
        if lb <= rb:
            cnt = rb - lb + 1
            if k > cnt:
                k -= cnt
            else:
                b = lb + k - 1
                return f"{a} + {b} = {a + b}"
    return "-1"

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

t = data[0]
idx = 1
ans = []
for _ in range(t):
    A, B, C, k = data[idx], data[idx + 1], data[idx + 2], data[idx + 3]
    idx += 4
    ans.append(solve_case(A, B, C, k))

print("\n".join(ans))
