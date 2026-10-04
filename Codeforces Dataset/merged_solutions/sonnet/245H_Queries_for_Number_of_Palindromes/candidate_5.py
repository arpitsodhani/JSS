# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
raw = sys.stdin.buffer.read().split()
s = raw[0]
n = len(s)
q = int(raw[1])
pal = [[False] * n for _ in range(n)]
count = [[0] * n for _ in range(n)]

length = 1
while length <= n:
    start = 0
    while start + length <= n:
        end = start + length - 1
        if length == 1:
            pal[start][end] = True
        elif length == 2:
            pal[start][end] = s[start] == s[end]
        else:
            pal[start][end] = s[start] == s[end] and pal[start + 1][end - 1]
        start += 1
    length += 1

left = n - 1
while left >= 0:
    right = left
    while right < n:
        value = 1 if pal[left][right] else 0
        if left + 1 < n:
            value += count[left + 1][right]
        if right - 1 >= 0:
            value += count[left][right - 1]
        if left + 1 < n and right - 1 >= 0:
            value -= count[left + 1][right - 1]
        count[left][right] = value
        right += 1
    left -= 1

res = []
p = 2
for _ in range(q):
    l = int(raw[p]) - 1
    r = int(raw[p + 1]) - 1
    p += 2
    res.append(str(count[l][r]))

# CLAUSE: finish_program
sys.stdout.write("\n".join(res))
