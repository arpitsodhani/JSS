# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = sys.stdin.read().split()
s = data[0]
n = len(s)
q = int(data[1])
pal = [[False] * n for _ in range(n)]
for i in range(n):
    pal[i][i] = True
for i in range(n - 1):
    pal[i][i + 1] = s[i] == s[i + 1]
for length in range(3, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        pal[left][right] = s[left] == s[right] and pal[left + 1][right - 1]

ans = [[0] * n for _ in range(n)]
for i in range(n):
    ans[i][i] = 1
for length in range(2, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        ans[left][right] = ans[left + 1][right] + ans[left][right - 1] - ans[left + 1][right - 1] + int(pal[left][right])

out = []
pos = 2
for _ in range(q):
    l = int(data[pos]) - 1
    r = int(data[pos + 1]) - 1
    pos += 2
    out.append(str(ans[l][r]))

# CLAUSE: finish_program
sys.stdout.write("\n".join(out))
