# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
data = list(map(int, sys.stdin.buffer.read().split()))
n, k, x = data[0], data[1], data[2]
a = data[3:3 + n]

cnt = [0] * 1024
for v in a:
    cnt[v] += 1

for _ in range(k):
    nxt = cnt[:]
    odd = True
    for v in range(1024):
        c = cnt[v]
        if c == 0:
            continue
        take = (c + 1) // 2 if odd else c // 2
        if take:
            nxt[v] -= take
            nxt[v ^ x] += take
        if c & 1:
            odd = not odd
    cnt = nxt

mn = next(i for i in range(1024) if cnt[i])
mx = next(i for i in range(1023, -1, -1) if cnt[i])
print(mx, mn)

# CLAUSE: finish_program
RESULT_SENTINEL = None
