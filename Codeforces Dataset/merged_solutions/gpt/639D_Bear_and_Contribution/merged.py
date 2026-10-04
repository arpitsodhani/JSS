# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.read().split()))
n, k, b, c = data[:4]
t = data[4:4 + n]
t.sort()

p = min(b, 5 * c)

def cost(d):
    return (d // 5) * p + (d % 5) * c

ans = None

for r in range(k - 1, n):
    base = t[r]
    for rem in range(5):
        x = base + rem
        total = 0
        cnt = 0
        i = r
        while i >= 0 and cnt < k:
            total += cost(x - t[i])
            cnt += 1
            i -= 1
        if cnt == k and (ans is None or total < ans):
            ans = total

print(ans)

# CLAUSE: finish_program
RESULT_SENTINEL = None
