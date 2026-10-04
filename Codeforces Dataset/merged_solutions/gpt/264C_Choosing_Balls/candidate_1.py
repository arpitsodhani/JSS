# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
p = 0

n = data[p]
q = data[p + 1]
p += 2

v = data[p:p + n]
p += n

c = data[p:p + n]
p += n

INF = 10 ** 30
out = []

for _ in range(q):
    a = data[p]
    b = data[p + 1]
    p += 2

    dp = {}
    best1 = 0
    best2 = 0
    col1 = -1

    for val, col in zip(v, c):
        old = dp.get(col, -INF)
        other = best1 if col1 != col else best2

        cur = other + val * b
        if old != -INF:
            same = old + val * a
            if same > cur:
                cur = same

        if cur > old:
            dp[col] = cur
            if col == col1:
                best1 = cur
            elif cur > best1:
                best2 = best1
                best1 = cur
                col1 = col
            elif cur > best2:
                best2 = cur

    out.append(str(best1))

sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
RESULT_SENTINEL = None
